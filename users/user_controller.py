from fastapi import APIRouter, Depends
from . import user_service
from config.guard import verify_jwt_cookie

user_controller = APIRouter(tags=["Users"], prefix="/api/v1/users", )

@user_controller.get("/")
def get_all_users():
    try:
        return user_service.getAllUsers()
    except Exception as e:
        raise e
