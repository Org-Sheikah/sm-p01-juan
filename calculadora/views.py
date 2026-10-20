from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

# 1. Importamos tus modelos relacionales de PostgreSQL / Django
from .models import OperacionCalculadora, RutaGuardada, EtiquetaRuta

# 2. Importamos las funciones con relaciones de Firebase
from .firebase_service import (
    guardar_operacion_firebase, 
    guardar_ruta_con_etiquetas_firebase
)

# 3. Importamos PyMongo para MongoDB
from pymongo import MongoClient


def index(request):
    return render(request, 'calculadora/index.html')


# =====================================================================
# API 1: CALCULADORA (Relaciones 1 a 1 y 1 a Muchos)
# =====================================================================
@csrf_exempt
def guardar_operacion_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expresion = data.get('expresion', '')
            resultado = data.get('resultado', '')
            usuario_input = data.get('usuario', '').strip()

            nombre_usuario = usuario_input if usuario_input else (
                request.user.username if request.user.is_authenticated else "anonimo"
            )

            # --- POSTGRESQL (1:N Usuario -> OperacionCalculadora) ---
            user_obj, _ = User.objects.get_or_create(username=nombre_usuario)
            operacion_postgres = OperacionCalculadora.objects.create(
                usuario=user_obj,
                expresion=expresion,
                resultado=str(resultado)
            )

            # --- MONGODB ---
            try:
                mongo_client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
                db = mongo_client["sm_p01_mongodb"]
                coleccion_mongo = db["operaciones_calculadora"]

                coleccion_mongo.insert_one({
                    "usuario": nombre_usuario,
                    "expresion": expresion,
                    "resultado": str(resultado)
                })
            except Exception as mongo_err:
                print(f"Error en MongoDB: {mongo_err}")

            # --- FIREBASE (1:1 Perfil, 1:N Operación por Referencia) ---
            doc_id_firebase = guardar_operacion_firebase(nombre_usuario, expresion, str(resultado))

            return JsonResponse({
                'status': 'ok',
                'mensaje': 'Operación guardada en PostgreSQL, MongoDB y Firebase',
                'postgres_id': operacion_postgres.id,
                'firebase_id': doc_id_firebase
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'invalid method'}, status=405)


# =====================================================================
# API 2: RUTAS Y ETIQUETAS (Relación Muchos a Muchos - N:M)
# =====================================================================
@csrf_exempt
def guardar_ruta_api(request):
    """
    Endpoint para guardar una ruta con múltiples etiquetas (Relación N:M)
    en PostgreSQL, MongoDB y Firebase.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            origen = data.get('origen', '')
            destino = data.get('destino', '')
            etiquetas_list = data.get('etiquetas', [])  # Ej: ["Trabajo", "Frecuente", "Turismo"]

            # -------------------------------------------------------------
            # 1. POSTGRESQL (Muchos a Muchos mediante ManyToManyField)
            # -------------------------------------------------------------
            ruta_pg = RutaGuardada.objects.create(origen=origen, destino=destino)
            for nombre_etiqueta in etiquetas_list:
                etiqueta_obj, _ = EtiquetaRuta.objects.get_or_create(nombre=nombre_etiqueta)
                ruta_pg.etiquetas.add(etiqueta_obj)

            # -------------------------------------------------------------
            # 2. MONGODB (Muchos a Muchos guardando array de etiquetas)
            # -------------------------------------------------------------
            try:
                mongo_client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
                db = mongo_client["sm_p01_mongodb"]
                coleccion_rutas = db["rutas_guardadas"]

                coleccion_rutas.insert_one({
                    "origen": origen,
                    "destino": destino,
                    "etiquetas": etiquetas_list
                })
            except Exception as mongo_err:
                print(f"Error en MongoDB (Rutas): {mongo_err}")

            # -------------------------------------------------------------
            # 3. FIREBASE FIRESTORE (Muchos a Muchos con Array de Referencias)
            # -------------------------------------------------------------
            doc_id_firebase = guardar_ruta_con_etiquetas_firebase(origen, destino, etiquetas_list)

            return JsonResponse({
                'status': 'ok',
                'mensaje': 'Ruta con relación N:M guardada en las 3 bases de datos',
                'postgres_id': ruta_pg.id,
                'firebase_id': doc_id_firebase
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'invalid method'}, status=405)