from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/API_document.yaml'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "CARTOONIZE API"})


def apply_swagger(app):
    app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
