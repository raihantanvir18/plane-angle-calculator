# from django import forms
# from .models import Equation

# class EquationForm(forms.ModelForm):
#     class Meta:
#         model = Equation
#         fields = ['equation1', 'equation2']



from django import forms
from .models import Equation

class EquationForm(forms.ModelForm):
    class Meta:
        model = Equation
        fields = ['equation1', 'equation2']
        widgets = {
            'equation1': forms.TextInput(attrs={'class': 'equation-input'}),
            'equation2': forms.TextInput(attrs={'class': 'equation-input'}),
        }
