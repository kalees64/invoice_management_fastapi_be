from config.db import connection
from . import user_models

db = connection

def getAllUsers():
    try:
        if not db.is_connected():
            raise Exception("Database connection failed")
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users")
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise e
    finally:
        db.close()

