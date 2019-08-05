from django.urls import path

from bank import views

urlpatterns = [
    path('bank_details/', views.BankDetails.as_view(), name='bank_details'),
]
