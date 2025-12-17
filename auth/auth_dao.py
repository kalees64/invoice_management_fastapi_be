from config.db import connection
from . import auth_model
from utils.expection_catcher import CatchException

db = connection


def login(data: auth_model.Login):
    try:
        if not db.is_connected():
            raise CatchException(message="Database connection is not active", status_code=500, response=None)
        sql = "SELECT id, name, email FROM users WHERE email = %s AND password = %s"
        values = (data.email, data.password)
        cursor = db.cursor(dictionary=True)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is None:
            raise CatchException(message="Invalid email or password", status_code=401, response=None)
        return result
    except CatchException:
        raise
    except Exception as e:
        raise CatchException(message=str(e), status_code=500, response=None)
    finally:
        if cursor:
            cursor.close()



