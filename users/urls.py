from django.urls import path
from .views import UserRegistrationView, UserLoginView,user_logout,UserBankAccountUpdateView,book_detail
 
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='register'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('Logout/', user_logout, name='logout'),
   path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
   path('book_detail/<int:book_id>/',book_detail, name='book_detail' ),

 ]