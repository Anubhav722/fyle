from django.urls import path

from bank import views

urlpatterns = [
    path('', views.BankDetails.as_view(), name='banks'),
    path('bank_detail/<str:ifsc>',
         views.get_bank_detail, name='bank_detail'),
]
