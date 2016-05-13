from django import forms

from .models import Post

#sfsdfsdfsdfsdfsdfsdf
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)