from django.shortcuts import render,redirect
from  .import forms
from  .import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Book,BorrowingHistory
from django.contrib import messages

class DetailPostView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.user.account.balance >= book.borrowing_price:
        # Deduct borrowing price from user's account balance
        request.user.account.balance -= book.borrowing_price
        request.user.account.save()
        book.save()
        # Create borrowing record
        
        BorrowingHistory.objects.create(user=request.user, book=book)


        return redirect('profile')
    else:
        return render(request, 'post_details.html', {'book': book})
