from django import forms
from .models import SuperRubric, SubRubric

class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperRubric.object.all(),
        empty_label=None, label='Надрубрика',
        required=True
    )

    class Meta:
        model = SubRubric
        fields = '__all__'

class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')

from django.forms import inlineformset_factory
from .models import Bb, AdditionalImage

class BbForm(forms.ModelForm):

    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}

AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__')

from captcha.fields import CaptchaField
from .models import Comment

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = {'is_active'}
        widgets = {'bb': forms.HiddenInput}

class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})

    class Meta:
        model = Comment
        exclude = {'is_active'}
        widgets = {'bb': forms.HiddenInput}



