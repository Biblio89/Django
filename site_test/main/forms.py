from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskFrom(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
                    'title' : TextInput(attrs={
                        'class' : 'form-control',
                        'placeholder': 'title'
                    }),
                        'task': Textarea(attrs={
                            'class': 'form-control',
                            'placeholder': 'task'
                        })
                    }