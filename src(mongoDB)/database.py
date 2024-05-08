from pymongo import MongoClient
import certifi


MONGO_URL = "mongodb+srv://alex:1234567890@cluster0.ag2uptb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def dbConnection():
    try:
        client = MongoClient(MONGO_URL)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db
