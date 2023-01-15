from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics, viewsets

from .serializers import BookingSerializer, MenuSerializer
from .models import Menu, Booking

# Create your views here.

# def sayHello(request):
#   return HttpResponse('Hello World')

def index(request):
  return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
