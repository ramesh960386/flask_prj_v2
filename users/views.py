from flask import Response
from flask_restful import Resource
from flask import request, make_response
from users.service import (
    create_user, reset_password_email_send, login_user, reset_password,
    create_task, get_task_list, get_task, update_task, delete_task
)


class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for login user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for forgot password email send user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password_email_send(request, input_data)
        return make_response(response, status)


class ResetPassword(Resource):
    @staticmethod
    def post(token) -> Response:
        """
        POST response method for save new password.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)

class TasksApi(Resource):
    def get(self) -> Response:
        response, status = get_task_list(request)
        return make_response(response, status)
    
    def post(self) -> Response:
        input_data = request.get_json()
        response, status = create_task(request, input_data)
        return make_response(response, status)


class TaskApi(Resource):
    def get(self, id):
        response, status = get_task(request, id)
        return make_response(response, status)
    
    def put(self, id) -> Response:
        input_data = request.get_json()
        response, status = update_task(request, input_data, id)
        return make_response(response, status)
    
    def delete(self, id):
        response, status = get_task(request, id)
        return make_response(response, status)