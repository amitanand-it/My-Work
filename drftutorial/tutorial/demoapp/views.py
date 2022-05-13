from django.shortcuts import render
from demoapp.serializers import DemoSerializer
from demoapp.models import Demo
from demoapp.forms import DemoForm
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def demo_list(request):

    form = DemoForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()

    context = {}
    context['form']= form
    return render(request, "demoapp/list.html", context)

    if request.method == 'GET':
        qs = Demo.objects.all()
        serializer = DemoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DemoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

        

def demo_detail(request, pk):

    try:
        obj = Demo.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DemoSerializer(obj)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DemoSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)


    if request.method == 'DELETE':
        obj.delete() 
        return HttpResponse(status=204)





