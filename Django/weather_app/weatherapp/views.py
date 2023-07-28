from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import mixins

from .models import Report, Forecaster
from .serializers import ReportSerializer, ForecasterSerializer
from .permissions import IsForecaster
from rest_framework import permissions

# class ReportView(APIView):
#     # GET
#     def get(self, request, *args, **kwargs):
#         if 'pk' in kwargs:
#             report = Report.objects.get(id=kwargs['pk'])
#             serializer = ReportSerializer(report)
#             return Response(serializer.data)
#         else:
#             queryset = Report.objects.all()
#             serializer = ReportSerializer(queryset, many=True)
#             return Response(serializer.data)

#     # POST
#     def post(self, request, *args, **kwargs):
#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     # PUT
#     def put(self, request, pk, *args, **kwargs):
#         report = Report.objects.get(id=pk)
#         serializer = ReportSerializer(report, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     # DELETE
#     def delete(self, request, pk, *args, **kwargs):
#         report = Report.objects.get(id=pk)
#         report.delete()
#         return Response("Deleted successfully")
    
# class ReportMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReportMixinView(generics.ListCreateAPIView):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer

class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ForecasterListView(generics.ListCreateAPIView):
    queryset = Forecaster.objects.all()
    serializer_class = ForecasterSerializer

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsForecaster,)

class ReportDeleteView(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    

