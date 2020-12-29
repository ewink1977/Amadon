from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/', views.checkout, name="checkout"),
    path('thanks/', views.thanks, name="thanks"),
]
