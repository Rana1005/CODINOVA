import email
import io
from django.shortcuts import render
from itsdangerous import Serializer
from .models import Patient
from .serailizers import PatientSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def register_patient(request):
    if request.method == 'POST':
        # return HttpResponse("thanks")
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        # name=pythondata['name']
        # email=pythondata['email']
        # dob=pythondata['dob']
        # gender=pythondata['gender']
        # imgcheck=pythondata['imgcheck']
        # Patient.objects.create(name=name,email=email,dob=dob,gender=gender,imgcheck=imgcheck)
        # res = {'msg':'data created'}
        # json_data = JSONRenderer().render(res)
        serializer = PatientSerializer(data=pythondata)
        # print(pythondata['name'])
        if serializer.is_valid():
            # print("line22")
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        Patient.objects.create(serializer)
        res = {'msg':'data created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        
