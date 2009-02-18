from django import forms
from django.utils.translation import ugettext_lazy as _

class NewIssueForm(forms.Form):
    title = forms.CharField(label=_("Title"), max_length=255)
    issuetype = forms.CharField(label=_("Type"), max_length=255)
    priority = forms.IntegerField(label=_("Priority"))
    status = forms.IntegerField(label=_("Status"))
    contents = forms.CharField(label="", widget=forms.Textarea(attrs={'cols':'80', 'rows': '24'}))