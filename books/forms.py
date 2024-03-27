from django import forms
from .models import Category,Book,Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=Review
#         fields = ['review_text']
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']