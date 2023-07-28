import json
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_all(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        serialized_data = serializer.data
        return JsonResponse(serialized_data, safe=False)
    
@csrf_exempt
def book_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Book created successfully.'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt     
def book_update(request, pk):
    book = Book.objects.filter(pk=pk).first()
    if not book:
        return JsonResponse({'error': 'Book matching query does not exist.'}, status=400)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Book updated successfully.'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).first()
    if not book:
        return JsonResponse({'error': 'Book matching query does not exist.'}, status=400)
    if request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully.'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    

def shop(request):
    return render(request, 'booksapp/index.html')