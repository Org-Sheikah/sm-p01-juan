import mongoengine

class OperacionMongo(mongoengine.Document):
    usuario = mongoengine.StringField(required=True)
    expresion = mongoengine.StringField(required=True)
    resultado = mongoengine.StringField(required=True)
    fecha = mongoengine.DateTimeField()

    meta = {'collection': 'operaciones_calculadora'}