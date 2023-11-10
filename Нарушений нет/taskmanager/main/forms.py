from .models import Statementes
from django.forms import ModelForm, TextInput, Textarea,Select


class StatementsForm(ModelForm):
    class Meta:
        model = Statementes
        fields = ["number", "comment","status"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер машины'
            }),
            "status": Select(attrs={
                'class': 'form-control',
            }, choices=[('новое', 'новое'),
                        ('подтверждено ', 'подтверждено '),
                        ('отклонено', 'отклонено')]),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите нарушение'
            })
        }