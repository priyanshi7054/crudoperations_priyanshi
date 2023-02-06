from django.shortcuts import render
from django.http import HttpResponse
from REST_API2.models import employees
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from REST_API2.serializers import employeesSerializer


# Create your views here.
class employeesViews(APIView):
    def post(self, request):
        serializer = employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = employees.objects.get(id=id)
            serializer = employeesSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = employees.objects.all()
        serializer = employeesSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
