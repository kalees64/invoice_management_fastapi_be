from . import auth_model, auth_dao
from utils import mail_util
import datetime
from config import guard
from utils.expection_catcher import CatchException


def login(data: auth_model.Login):
    try:
        result = auth_dao.login(data)

        token = guard.create_jwt_token(
            user=result["email"],
            expires_delta=datetime.timedelta(minutes=15)
        )

        return {
            "message": "Login successful",
            "token": token
        }

    except CatchException:
        raise

    except Exception as e:
        raise CatchException(
            message="Error while login",
            status_code=500,
            response=str(e)
        )

