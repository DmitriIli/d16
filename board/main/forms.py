from django import forms
from django.forms import ModelForm
from .models import Ads, Reply


class CreateForm(ModelForm):
    title = forms.CharField(max_length=64, help_text='Заголовок статьи')
    text = forms.CharField(widget=forms.Textarea,
                           max_length=512, help_text='Текст статьи')

    class Meta:
        model = Ads
        fields = ['title', 'text', 'category', 'upload']


class CreateReplyForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea,
                           max_length=512, help_text='Текст ответа')

    class Meta:
        model = Reply
        fields = ['text',]