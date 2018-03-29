from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Array


class ArrayForm(forms.ModelForm):

    class Meta:
        model = Array
        fields = ['title', 'cr']
        labels = {'title': _('Array: '),
                  'cr': _('Challenge Rating: ')}
