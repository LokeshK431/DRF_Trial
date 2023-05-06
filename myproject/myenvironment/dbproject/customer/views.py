from os import name
from .models import Customer

from rest_framework import generics
from .serializers import CustomerSerializer
from rest_framework.response import Response

from customer.models import Customer

from django.http import HttpResponse, HttpResponseRedirect

from django.core.exceptions import ValidationError
from django.db import models

from django.shortcuts import render, redirect
from customer.models import Customer

from rest_framework import status

from django.contrib.auth import login, authenticate

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('/success/')
        else:
            return render(request, 'login.html', {'error':'Invalid username & password.'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # customer = Customer.objects.create(
        # name = name,
        # phone = phone,
        # email = email,

        response = new_customer(name, email, phone, username, password)
        return response
    

    
    return render(request, 'register.html')

def validate_phone(value):
    if value[0] not in ['6','7','8','9']:
        raise ValidationError('Phone number must start with 6,7,8, or 9')
    
    

def new_customer(name, email, phone, username, password):
        new_customer = Customer(name=name, email=email, phone=phone, username=username, password=password)
        new_customer.save()
        return HttpResponse('Registration Successful!')

class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

        # queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many = True)
        # return Response(serializer.data)
        
    
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def detail(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)
    
class CustomerUpdate(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def update(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)
    
class CustomerDelete(generics.RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)