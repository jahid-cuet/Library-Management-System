from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import redirect

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self,form):
        # print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')
def user_logout(request):
    logout(request)
    return redirect('home')

class UserBankAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    


# views.py


# from books.models import Book, Comment
# from books.forms import CommentForm


# def book_detail(request):

#     if request.method=='POST':
#         author_form= CommentForm(request.POST)
#         if author_form.is_valid():
#             # author_form.save()
#             return render(request,'book_detail.html',{"form":author_form})
#     else:
#         author_form= CommentForm()
#     return render(request,'book_detail.html',{"form":author_form})


from books.models import Book, Comment
from books.forms import CommentForm

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = book.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            print(form.cleaned_data)
            return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form})
    else:
        form = CommentForm()
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form})
