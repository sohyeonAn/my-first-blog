from django import forms
from .models import Post

class PostForm(forms.ModelForm):


    # 이 폼을 만들기 위해 어떤 model이 쓰여야 하는지
    class Meta:
        model = Post

        # 이번 폼에서는 title과 text만 보여지게 함
        fields = ('title', 'text',)