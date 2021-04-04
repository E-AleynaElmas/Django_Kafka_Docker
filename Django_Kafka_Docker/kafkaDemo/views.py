from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import KafkaDemo
from .serializer import KafkaDemoSerializer
from rest_framework.decorators import api_view
import json
import time

#çalışıyor
@api_view(['GET'])
def eventList(request):
    start_time = time.time()
    time.sleep(0.01)

    events = KafkaDemo.objects.all()
    serializer = KafkaDemoSerializer(events, many=True)

    total = (time.time() - start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    with open(str("log.log"), "a") as dosya:
        dosya.write(sent+"\n")
        
    return Response(serializer.data)

#çalışıyor o id yoksa kontrolü
@api_view(['GET'])
def eventDetail(request, pk):
    start_time = time.time()
    time.sleep(0.01)

    events = KafkaDemo.objects.get(id=pk)
    serializer = KafkaDemoSerializer(events)

    total = (time.time() - start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    with open(str("log.log"), "a") as dosya:
        dosya.write(sent+"\n")
    return Response(serializer.data)

#çalışıyor aynı id varsa kontrolü
@api_view(['POST'])
def eventCreate(request):
    start_time = time.time()
    time.sleep(0.01)
    serializer = KafkaDemoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    total = (time.time() - start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    with open(str("log.log"), "a") as dosya:
        dosya.write(sent+"\n")
    return Response(serializer.data)

#çalışıyor o id yoksa hata dönmüyor düzelt
@api_view(['PUT'])
def eventUpdate(request, pk):
    start_time = time.time()
    time.sleep(0.01)

    event = KafkaDemo.objects.get(id=pk)
    serializer = KafkaDemoSerializer(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    total = (time.time() - start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    with open(str("log.log"), "a") as dosya:
        dosya.write(sent+"\n")

    return Response(serializer.data)

#çalışıyor o id yoksa hata dönmüyor düzelt
@api_view(['DELETE'])
def eventDelete(request, pk):
    start_time = time.time()
    time.sleep(0.01)
    
    event = KafkaDemo.objects.get(id=pk)
    event.delete()

    total = (time.time() - start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    with open(str("log.log"), "a") as dosya:
        dosya.write(sent+"\n")

    return Response('Deleted')

