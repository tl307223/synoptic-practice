from django import forms
from django.db.models import fields
from django.forms import ModelForm

from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import modelform_factory, inlineformset_factory
from django.forms.widgets import CheckboxInput

from .models import Question, Quiz, Choice

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in ('username', 'password'):
            self.fields[field].widget.attrs = {'class' : 'form-control'}


class QuestionModelForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class QuizModelForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

QuestionChoiceFormset = inlineformset_factory(Question, Choice, fields=('choice_text', 'correct'), max_num=4, extra=4)