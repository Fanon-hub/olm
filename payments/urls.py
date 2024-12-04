from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('<int:pk>/', views.payment_detail, name='payment_detail'),
    path('create/', views.payment_create, name='payment_create'),
    path('<int:pk>/update/', views.payment_update, name='payment_update'),
    path('<int:pk>/delete/', views.payment_delete, name='payment_delete'),
]