from django.urls import path
from . import views

app_name='payment'
urlpatterns = [
    path('', views.index, name='pay'),
    path('paid/', views.paid, name='paid'),
    path('charge/', views.paid, name='charge'),
    path('verify/<int:id>/', views.verify, name='verify')
]
