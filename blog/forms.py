from django import forms
from .models import Post

class PostForm(forms.ModelForm):


    # �� ���� ����� ���� � model�� ������ �ϴ���
    class Meta:
        model = Post

        # �̹� �������� title�� text�� �������� ��
        fields = ('title', 'text',)