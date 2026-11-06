from django import forms

from .models import Application


class AllowForm(forms.Form):
    allow = forms.BooleanField(required=False)
    redirect_uri = forms.CharField(widget=forms.HiddenInput())
    scope = forms.CharField(required=False, widget=forms.HiddenInput())
    client_id = forms.CharField(widget=forms.HiddenInput())
    state = forms.CharField(required=False, widget=forms.HiddenInput())
    response_type = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        data = kwargs.get('data')
        # backwards compatible support for plural `scopes` query parameter
        if data and 'scopes' in data:
            # request.POST is an immutable QueryDict, so the form sets scope on a copy.
            data = data.copy()
            data['scope'] = data['scopes']
            kwargs['data'] = data
        return super(AllowForm, self).__init__(*args, **kwargs)


class RegistrationForm(forms.ModelForm):
    """
    TODO: add docstring
    """
    class Meta:
        model = Application
        fields = ('name', 'client_id', 'client_secret', 'client_type', 'authorization_grant_type', 'redirect_uris')
