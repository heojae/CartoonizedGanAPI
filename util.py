from io import BytesIO

import PIL.Image
from flask import send_file


def serve_pil_image(pil_img: PIL.Image.Image):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
