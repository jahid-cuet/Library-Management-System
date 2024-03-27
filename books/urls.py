from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [

    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
    path('cars/<int:book_id>/buy/', views.borrow_book, name='borrow_book'),
    # path('widthdraw/', WithdrawMoneyView.as_view, name='buy_car'),
]