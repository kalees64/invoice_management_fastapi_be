from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.user_controller import user_controller
from auth.auth_controller import auth_controller
from utils.expection_catcher import CatchException
from fastapi.responses import JSONResponse

app = FastAPI(title="Invoice Management API", description="Invoice Management API", version="0.0.1")

origins = [ "http://localhost:5173", "http://127.0.0.1:5173",]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.exception_handler(CatchException)
async def catch_exception_handler(request, exc: CatchException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "statusCode": exc.status_code,
            "message": exc.message,
            "response": exc.response
        }
    )


app.include_router(auth_controller)
# app.include_router(user_controller)


