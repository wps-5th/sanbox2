from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    comment = forms.CharField()

    class Meta:
        model = Post
        fields = {
            'photo',
            'comment'
        }

    widgets = {
        'comment': forms.TextInput(
            attrs={
                'placeholder': '입력하세요',
                'size': '20',
            }
        ),
    }
