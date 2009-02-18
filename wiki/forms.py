from django import forms
from django.utils.translation import ugettext_lazy as _

class NewPageForm(forms.Form):
    name = forms.CharField(label=_("Page Title"), max_length=120)
    
class EditPageForm(forms.Form):
    title = forms.CharField(label=_("Title"), max_length=120)
    contents = forms.CharField(label="", widget=forms.Textarea(attrs={'cols':'80', 'rows': '24'}))