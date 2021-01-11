from django import forms
from org.models import Session

sessionsObjs = Session.objects.all()
sessions = ((i.id,i.session) for i in sessionsObjs)


class PaymentForm(forms.Form):
    session = forms.ChoiceField(choices=sessions)


    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['session'].label = ''
