
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response



class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username , user not found'
                raise Exception('invalid username not found')

            user_obj = authenticate(username=data.get('username'),
                                    password=data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')


        except Exception as e:
            print(e)

        return Response(response)
    
LoginView = LoginView.as_view()

class RegisterView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Username not found'
                raise Exception('Please enter the username')

            if data.get('password') is None:
                response['message'] = 'Password not found'
                raise Exception('please enter the password')
            
            if data.get('cnfPassword') is None:
                response['message'] = 'Confirm password not found'
                raise Exception('Please re-enter the password')
            print(data.get('username'))
            print(data.get('password'))
            print(data.get('cnfPassword'))
            if data.get('password') != data.get('cnfPassword'):
                raise Exception('Password not matched')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'User already exist!'
                raise Exception('User already exist!')

            user_obj = User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User created!'
            response['status'] = 200
            
        except Exception as e:
            print(e)

        return Response(response)
    

RegisterView = RegisterView.as_view()
