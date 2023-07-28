from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from rest_framework import mixins
from .permissions import IsOwner
from rest_framework import permissions
from django.contrib.auth.models import User


# @csrf_exempt
# def post_view(request):
#     # GET
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return JsonResponse(data=serializer.data, safe=False)


# class PostView(APIView):
#     # GET
#     def get(self, request, *args, **kwargs):
#         if 'pk' in kwargs:
#             post = Post.objects.get(id=kwargs['pk'])
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         else:
#             queryset = Post.objects.all()
#             serializer = PostSerializer(queryset, many=True)
#             return Response(serializer.data)

#     # POST
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.errors)
    
#     # delete
#     def delete(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id=pk)
#         post.delete()
#         return Response(status=204)

#     # update
#     def put(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.errors)

# class PostListView( mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostDetailView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
