from django import forms
from django.utils.translation import ugettext_lazy as _


issue_status = ((1, _("New")),
                (2, _("Accepted")),
                (3, _("Started")),
                (4, _("Fixed")),
                (5, _("Verified")),
                (6, _("Invalid")),
                (7, _("Duplicated")),
                (8, _("WontFix")),
                )

issue_priority = ((1, _("Low")),
                  (2, _("Medium")),
                  (3, _("High")),
                  (4, _("Critical")),
                  (5, _("Blocker")),
                  )

issue_type = (("defect", _("Defect")),
              ("enhancement", _("Enhancement")),
              ("task", _("Task")),
              )

di_type = dict(issue_type)
di_priority = dict(issue_priority)
di_status = dict(issue_status)

bugreport = _("""
<p>
Description of the problem
</p>
<br/><br/>

What steps will reproduce the problem?
<ol>
<li> </li>
<li> </li>
<li> </li>
</ol>

<p>
What is the expected output?
</p>

""")


class NewIssueForm(forms.Form):
    title = forms.CharField(label=_("Title"), max_length=255)
    issuetype = forms.ChoiceField(label=_("Type"), choices=issue_type)
    priority = forms.ChoiceField(label=_("Priority"), choices=issue_priority)
    status = forms.ChoiceField(label=_("Status"), choices=issue_status)
    contents = forms.CharField(label="", widget=forms.Textarea(attrs={'cols':'80', 'rows': '24'}), initial=bugreport)
    
class EditIssueForm(forms.Form):
    issuetype = forms.ChoiceField(label=_("Type"), choices=issue_type)
    priority = forms.ChoiceField(label=_("Priority"), choices=issue_priority)
    status = forms.ChoiceField(label=_("Status"), choices=issue_status)
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'cols':'80', 'rows': '24'}))

