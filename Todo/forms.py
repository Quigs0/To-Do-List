from django import forms
from .models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add tasks"
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': "switch"
            })
        }