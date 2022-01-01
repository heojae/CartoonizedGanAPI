import PIL.ImageFile
from PIL import Image
from flask import Flask, request

from config.exception import InvalidParameterException, apply_custom_error_handler
from config.cache_policy import apply_cache_policy
from config.swagger import apply_swagger
from model import JitCycleGANModel
from serve import FileSender

app = Flask(__name__)
apply_swagger(app)
apply_custom_error_handler(app)
apply_cache_policy(app)

# --------------------------------------------------------------------------------------------

cg_model = JitCycleGANModel()


@app.route('/cartoonize', methods=['POST'])
def cartoonize_api():
    global cg_model

    image = request.files.get('image', None)
    if not image:
        raise InvalidParameterException
    try:
        pil_image = Image.open(image)
    except PIL.ImageFile.ERRORS:
        raise InvalidParameterException

    output_pil_image = cg_model.inference(pil_image)

    return FileSender.send_pil_image(output_pil_image)


# start flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, use_reloader=False, port=8080)
