# Copyright (c) 2009, Carlos Daniel Ruvalcaba Valenzuela
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice, 
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, 
#      this list of conditions and the following disclaimer in the documentation 
#      and/or other materials provided with the distribution.
#    * Neither the name of the Blackchair Software nor the names of its contributors 
#      may be used to endorse or promote products derived from this software without 
#      specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

