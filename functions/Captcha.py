from captcha.image import ImageCaptcha
from io import BytesIO
from fastapi.responses import StreamingResponse

def getCaptcha():
    image = ImageCaptcha(width = 250, height = 90, fonts=['assets/fonts/grafity.ttf','assets/fonts/aachen.ttf'])
    captcha_text = 'abcde' 
    data = image.generate(captcha_text)
    captcha_image = BytesIO(data.read())
    captcha_image.seek(0)
    return StreamingResponse(captcha_image, media_type="image/png")

def checkCaptcha():
    pass