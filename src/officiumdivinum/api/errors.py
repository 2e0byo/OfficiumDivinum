from flask_restful import APIException


class InvalidInput(APIException):
    status_code = 204
    detail = "Invalid input supplied"
