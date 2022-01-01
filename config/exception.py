from http import HTTPStatus

from flask import jsonify


class CustomException(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message


class InvalidParameterException(CustomException):
    status_code = HTTPStatus.BAD_REQUEST
    error_message = "잘못된 Request Format 입니다."


class InvalidImageModeException(CustomException):
    status_code = HTTPStatus.BAD_REQUEST
    error_message = "RGB, L, RGBA 의 이미지가 아닙니다."


def error_response(message, status_code):
    return jsonify({'message': message}), status_code


def apply_custom_error_handler(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        return error_response("서버 상에서 오류가 발생했습니다.", HTTPStatus.INTERNAL_SERVER_ERROR)

    @app.errorhandler(InvalidParameterException)
    def handle_error(e: InvalidParameterException):
        return error_response(e.error_message, e.status_code)
