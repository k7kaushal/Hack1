from django.shortcuts import render
import joblib
from django.http import JsonResponse
from .models import Prediction
from .serializers import PredictSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
import sklearn

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def prediction(request, format=None):
    if request.method == 'GET':
        Predict = Prediction.objects.all()
        model = joblib.load(r'C:\Users\ASUS\Desktop\cloudify\cloudify\Predict\model\Hack.pkl')
        print(model.predict([[266,291,2,1,1,32,1,20999,0,1,19817]]))
        serializer = PredictSerializer(Predict, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)