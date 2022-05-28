from main.models import DoneWorks
from django.forms import ModelForm, TextInput, NumberInput

class GradesForm(ModelForm):
    class Meta:
        model = DoneWorks
        fields = ['grade']

        widgets = {
            'grade': NumberInput(attrs ={
                'class': 'grade',
                'placeholder': 'Оценка'
            }),
            #'comment_from_teacher': TextInput(attrs ={
            #    'class': 'review-label',
            #    'placeholder': 'Комментарий'
            #}),
        }
