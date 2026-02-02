from django import forms

class CreateProductForm(forms.Form):
     name = forms.CharField(max_length=300)
     desc = forms.CharField()
     price = forms.DecimalField()
     category = forms.ChoiceField()
     sub_category = forms.ChoiceField()

     widgets = {
          'name': forms.TextInput(attrs={
               'class': 'form-control',
          }),
          'name': forms.TextInput(attrs={
               'class': 'form-control',
          }),
          'name': forms.TextInput(attrs={
               'class': 'form-control',
          }),
          "category": forms.Select(attrs={
               "class": "form-select"
          }),
          "sub_category": forms.Select(attrs={
                "class": "form-select"
          }),
     }

     