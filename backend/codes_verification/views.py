from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Code
from .serializers import CodeSerializer
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from energyapp import settings
# Create your views here.
import random 

def create_code():
    list_num = [0,1,2,3,4,5,6,7,8,9]
    code_list = []
    for x in range(5):
        num = random.choice(list_num)
        code_list.append(num)
    code_string = "".join(str(item) for item in code_list)
    return code_string
def send_email(code, email):
    subject = "CORREO DE VERIFICACION (NO RESPONDER):"
    message = "Tu codigo de verificacion es: " + str(code)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

@api_view(['POST'])
def generate_code(request):

    email = request.data.email
    password = request.data.password
    user = authenticate(request, email = email, password = password)
    print(request.data)
    print(email)
    print(password)
    print(user)
    if user is not None:
        code = create_code()
        data = { 'code': code, 'user':user}
        serializer = CodeSerializer(data=data)
        if serializer.is_valid():
            send_email(code, email)
            serializer.save()
            return Response(
                {'message': 'Code saved', 'status':'1'}
            )
        else:
            return Response({'errors':serializer.errors, 'status':'0'})
    else:
        raise ValueError('Invalid Credentials')
