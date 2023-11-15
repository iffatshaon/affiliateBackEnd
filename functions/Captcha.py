from captcha.image import ImageCaptcha
from io import BytesIO
from fastapi.responses import StreamingResponse

def getCaptcha():
    image = ImageCaptcha(width = 200, height = 90)
    captcha_text = 'abcde' 
    data = image.generate(captcha_text)
    captcha_image = BytesIO(data.read())
    captcha_image.seek(0)
    return StreamingResponse(captcha_image, media_type="image/png")

def checkCaptcha():
    pass