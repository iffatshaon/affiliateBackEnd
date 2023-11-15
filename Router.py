from fastapi import APIRouter
from functions.User import welcome,register
from functions.Captcha import getCaptcha

router = APIRouter()

router.get("/", response_model=dict)(welcome)
router.post("/register_user", response_model=dict)(register)
router.get("/get_captcha")(getCaptcha)