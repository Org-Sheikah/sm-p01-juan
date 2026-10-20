import firebase_admin
from firebase_admin import credentials, firestore
import os

# Inicializar Firebase de manera segura buscando el archivo en la carpeta actual o en la raíz
if not firebase_admin._apps:
    try:
        # Opción 1: Buscar en la misma carpeta (calculadora/)
        cred_path = os.path.join(os.path.dirname(__file__), 'firebase-key.json')
        
        # Opción 2: Si no está ahí, buscar en la raíz del proyecto (sm-p01-juan/)
        if not os.path.exists(cred_path):
            cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase-key.json')

        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print(f"Firebase inicializado correctamente con: {cred_path}")
        else:
            print(f"ADVERTENCIA: No se encontró el archivo firebase-key.json. Modo offline/test activado.")
    except Exception as e:
        print(f"Error al inicializar Firebase: {e}")

# Función segura para obtener el cliente de Firestore
def get_firestore_client():
    try:
        # Si no hay aplicaciones de Firebase inicializadas (como en GitHub Actions), retorna None sin romper la app
        if not firebase_admin._apps:
            return None
        return firestore.client()
    except Exception:
        return None

# ---------------------------------------------------------------------
# 1. RELACIÓN 1 A 1: Usuario -> Perfil
# ---------------------------------------------------------------------
def crear_perfil_usuario_firebase(usuario, telefono=""):
    db = get_firestore_client()
    if not db:
        return None
    try:
        user_ref = db.collection('perfiles_usuario').document(usuario)
        user_ref.set({
            'usuario': usuario,
            'telefono': telefono,
            'actualizado': firestore.SERVER_TIMESTAMP
        }, merge=True)
        return user_ref.id
    except Exception as e:
        print(f"Error en relación 1:1 Firebase: {e}")
        return None

# ---------------------------------------------------------------------
# 2. RELACIÓN 1 A MUCHOS: Usuario -> Operaciones de Calculadora
# ---------------------------------------------------------------------
def guardar_operacion_firebase(usuario, expresion, resultado):
    db = get_firestore_client()
    if not db:
        return None
    try:
        # Aseguramos el perfil (1 a 1)
        crear_perfil_usuario_firebase(usuario)

        # Creamos la referencia al documento del usuario (llave foránea en NoSQL)
        usuario_ref = db.collection('perfiles_usuario').document(usuario)

        doc_ref = db.collection('operaciones_calculadora').document()
        doc_ref.set({
            'id_operacion': doc_ref.id,
            'usuario_ref': usuario_ref,       
            'usuario': usuario,               
            'expresion': expresion,
            'resultado': str(resultado),
            'fecha': firestore.SERVER_TIMESTAMP
        })
        return doc_ref.id
    except Exception as e:
        print(f"Error en relación 1:N Firebase: {e}")
        return None

# ---------------------------------------------------------------------
# 3. RELACIÓN MUCHOS A MUCHOS: Rutas <-> Etiquetas
# ---------------------------------------------------------------------
def guardar_ruta_con_etiquetas_firebase(origen, destino, lista_etiquetas):
    db = get_firestore_client()
    if not db:
        return None
    try:
        etiquetas_refs = []

        for etiq in lista_etiquetas:
            etiq_ref = db.collection('etiquetas_ruta').document(etiq)
            etiq_ref.set({'nombre': etiq}, merge=True)
            etiquetas_refs.append(etiq_ref)

        ruta_ref = db.collection('rutas_guardadas').document()
        ruta_ref.set({
            'origen': origen,
            'destino': destino,
            'etiquetas': etiquetas_refs,  
            'etiquetas_nombres': lista_etiquetas,
            'fecha': firestore.SERVER_TIMESTAMP
        })

        for etiq_ref in etiquetas_refs:
            etiq_ref.update({
                'rutas': firestore.ArrayUnion([ruta_ref])
            })

        return ruta_ref.id
    except Exception as e:
        print(f"Error en relación N:M Firebase: {e}")
        return None