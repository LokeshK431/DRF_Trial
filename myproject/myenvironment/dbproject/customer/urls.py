from django import views
from . import views
from django.urls import include, path
from . views import CustomerCreate, CustomerUpdate, CustomerDetail, CustomerDelete, CustomerList


urlpatterns = [
    path('create/', CustomerCreate.as_view(), name='create-customer'), #POST
    path('register/', views.register, name='register'), #POST
    path('login/', views.login, name = 'login'),
    path('', CustomerList.as_view()), #READ
    path('<int:pk>/', CustomerDetail.as_view(), name='retreive_customer'), #READ
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'), #UPDATE
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer'), #DELETE
]