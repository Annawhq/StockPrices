from django import forms
#from analytic import predict

class UserForms(forms.Form):
    ticker=forms.CharField()
