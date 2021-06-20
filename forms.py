from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from tinymce.widgets import TinyMCE
from embed_video.fields import EmbedVideoField

class ChangeProfileUser(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('FOI', 'Mail', 'Phone', 'Group', 'Country',
                  'GraduatedPlace', 'Status', 'Avatar')
        # labels = {
        #     'FOI': 'ФИО: ',
        #     'Mail': 'Почта: ',
        #     'Phone': 'Тел.: ',
        #     'Group': 'Группа: ',
        #     'Country': 'Страна: ',
        #     'Positon': 'Должность: ',
        #     'GraduatedPlace': 'ВУЗ: ',
        #     'Status': 'Статус',
        #     'Avatar': 'Фото',
        # }
        widgets = {
            'FOI': forms.TextInput(attrs={'class': 'form-control', 'id': 'FIO'}),
            'Mail': forms.EmailInput(attrs={'class': 'form-control', 'id': 'mail'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            'Group': forms.TextInput(attrs={'class': 'form-control', 'id': 'group'}),
            'Country': forms.TextInput(attrs={'class': 'form-control', 'id': 'user_country'}),
            'GraduatedPlace': forms.TextInput(attrs={'class': 'form-control', 'id': 'GraduatedPlace'}),
            'Status': forms.TextInput(attrs={'class': 'form-control', 'id': 'status'}),
            'Avatar': forms.FileInput(attrs={'class': 'form-control', 'id': 'Avatar'}),
        }

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('Name','Description', 'Photo','Level')
        widgets = {
        'Name': forms.TextInput(attrs={'class': 'form-control', 'id': 'Name'}),
        'Description': forms.TextInput(attrs={'class': 'form-control', 'id': 'Description'}),
        'Photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'Photo'}),
        'Level': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Level'}, ),
                    }



class CourseElementTextForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget, label='')
    Name = forms.CharField(max_length=300, label='Название')
    widgets = {
        'Name': forms.TextInput(attrs={'class': 'form-control', 'id': 'Name'}),
    }

class CourseElementVideoForm(forms.Form):
    Video = forms.URLField()
    Name = forms.CharField(max_length=300, label='Название')
    widgets = {
        'Name': forms.TextInput(attrs={'class': 'form-control', 'id': 'Name'}),
        'Video':forms.URLInput(attrs={'class': 'form-control', 'id': 'Video'})
    }

class CourseElementQuizForm(forms.ModelForm):
    class Meta:
        model = CourseElementQuiz
        fields = (
            'QuizText','option1', 'option2','option3','option4',
            'option1_answer', 'option2_answer', 'option3_answer', 'option4_answer',
                  )
    # QuizText = models.CharField(max_length=500)
    # option1 = models.CharField(max_length=500)
    # option2 = models.CharField(max_length=500)
    # option3 = models.CharField(max_length=500, blank=True, null=True)
    # option4 = models.CharField(max_length=500, blank=True, null=True)
    # option1_answer = models.BooleanField(default=False)
    # option2_answer = models.BooleanField(default=False)
    # option3_answer = models.BooleanField(default=False)
    # option4_answer = models.BooleanField(default=False)
        widgets = {
            'QuizText': forms.TextInput(attrs={'class': 'form-control', 'id': 'QuizText'}),
            'option1': forms.TextInput(attrs={'class': 'form-control', 'id': 'option1'}),
            'option2': forms.TextInput(attrs={'class': 'form-control', 'id': 'option2'}),
            'option3': forms.TextInput(attrs={'class': 'form-control', 'id': 'option3'}),
            'option4': forms.TextInput(attrs={'class': 'form-control', 'id': 'option4'}),
            'option1_answer': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'option1_answer'}),
            'option2_answer': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'option2_answer'}),
            'option3_answer': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'option3_answer'}),
            'option4_answer': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'option4_answer'}),
        }