from django import forms
from .models import Candidate


class CandidateForm(forms.Form):
    
    name =  forms.CharField(widget=forms.TextInput(
            attrs={
                "placeholder": "ecrire votre Nom..",
                "class": "form-control",
            })
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                "placeholder": "ecrire votre prenom..",
                "class": "form-control",
            })
    )
    study_level = forms.CharField(widget=forms.TextInput(
            attrs={
                "placeholder": "ecrire votre niveau d'etude..",
                "class": "form-control",
            })
    )
    section = forms.CharField(widget=forms.TextInput(attrs={
                "placeholder": "ecrire votre section..",
                "class": "form-control",
            })
    )   
    diploma = forms.CharField(widget=forms.TextInput(
            attrs={
                "placeholder": "ecrire votre diplome..",
                "class": "form-control",
            })
    )
    
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        for fieldname in ['name', 'last_name', 'study_level','section','diploma']:
            self.fields[fieldname].help_text = None
    def save(self, commit=True):
        candidate = Candidate(
            name = self.cleaned_data['name'],
            last_name = self.cleaned_data['last_name'],
            study_level = self.cleaned_data['study_level'],
            section = self.cleaned_data['section'],
            diploma = self.cleaned_data['diploma'],
        )
        if commit:
            candidate.save()
        return candidate
    class Meta:
        model = Candidate
        fields = ('name','last_name', 'study_level','section','diploma')
    