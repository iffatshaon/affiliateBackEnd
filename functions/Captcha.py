from fastapi.responses import StreamingResponse
from io import BytesIO
from captcha.image import ImageCaptcha
import random
import string

def generate_text_and_hash():
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(5))
    hash_value = random.getrandbits(128)
    return captcha_text, hash_value

def generate_captcha_image(text):
    image = ImageCaptcha(width=250, height=90, fonts=['assets/fonts/roman.ttf'])
    data = image.generate(text)
    captcha_image = BytesIO(data.read())
    captcha_image.seek(0)
    return captcha_image

def getCaptcha():
    captcha_text, hash_value = generate_text_and_hash()
    captcha_image = generate_captcha_image(captcha_text)
    response_data = {"hash_value": hash_value}
    captcha_image.seek(0)
    return StreamingResponse(captcha_image, media_type="image/png", headers={"data": str(response_data)})
