from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Array, Creature


class ArrayForm(forms.ModelForm):

    class Meta:
        model = Array
        fields = ['title', 'cr']
        labels = {'title': _('Array: '),
                  'cr': _('Challenge Rating: ')}


class NameForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ['name']
        labels = {'name': _('')}
