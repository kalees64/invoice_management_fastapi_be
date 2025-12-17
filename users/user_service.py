from . import user_dao


def getAllUsers():
    try:
        result = user_dao.getAllUsers()
        return {"success": True, "data": result}
    except Exception as e:
        raise e