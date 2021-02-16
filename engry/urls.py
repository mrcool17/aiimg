from django.urls import include, path
from rest_framework import routers
from engry import views

urlpatterns = [
  # path('welcome', views.welcome),
 
  # path ('que/', views.serchCreateAPIView.as_view(), name='que-create'),
  path ('imgeng/', views.uimgCreateAPIView.as_view(), name='imgeng-create1'),
]

