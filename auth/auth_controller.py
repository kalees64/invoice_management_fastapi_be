from fastapi import APIRouter, Response
from . import auth_model, auth_service
from utils.expection_catcher import CatchException
from utils.send_response import SendResponse

auth_controller = APIRouter(tags=["Auth"], prefix="/api/v1/auth")

@auth_controller.post("/login")
def login(data: auth_model.Login, response: Response):
    try:
        result = auth_service.login(data)

        response.set_cookie(
            key="access_token",
            value=result["token"],
            httponly=True,
            secure=False,
            max_age=15 * 60,
            expires=15 * 60,
            path="/api/v1/auth/login",
            samesite="lax"
        )

        return SendResponse(message="Login Success", status_code=200, response=result)

    except CatchException:
        raise


