from main.models import Grades
from django.forms import ModelForm, TextInput, NumberInput

class GradesForm(ModelForm):
    class Meta:
        model = Grades
        fields = ['grade', 'comment_from_teacher']

        widgets = {
            'grade': NumberInput(attrs ={
                'class': 'grade',
                'placeholder': 'Оценка'
            }),
            'comment_from_teacher': TextInput(attrs ={
                'class': 'review-label',
                'placeholder': 'Комментарий'
            }),
        }
