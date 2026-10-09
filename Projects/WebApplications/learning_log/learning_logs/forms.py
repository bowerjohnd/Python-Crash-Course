from django import forms

from .models import Topic

class TopicForm(forms.Modelform):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}