from .models import *
from django import forms

# class PlatForm(forms.ModelForm):
#     nom = forms.CharField(label="Nom")
#     description = forms.CharField(label="Description", widget=forms.Textarea)
#     prix = forms.DecimalField(label="Prix")
#     categorie = forms.CharField(label="Categorie", widget=forms.Select)

#     class Meta:
#         model = Plat
#         fields = ['nom', 'description', 'prix', 'categorie']



# class PlatForm(forms.ModelForm):
#     class Meta:
#         model = Plat
#         fields = ['nom', 'description', 'prix', 'categorie']
#         labels = {
#             'nom': 'Nom',
#             'description': 'Description',
#             'prix': 'Prix',
#             'categorie': 'Catégorie',
#         }
#         widgets = {
#             'description': forms.Textarea,
#         }


class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['nom', 'description', 'prix', 'categorie', 'image']
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'prix': 'Prix',
            'categorie': 'Catégorie',
            'image': 'Photo'
        }
        widgets = {
            'description': forms.Textarea,
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PlatForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].queryset = CategoriePlat.objects.all()