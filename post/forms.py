from django import forms

from .models import Comment


class PostForm(forms.ModelForm):
    pass


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Leave a reply...",
        'id': "usercomment",
        'rows': '5'
    }))

    class Meta:
        model=Comment
        fields=('content',)
