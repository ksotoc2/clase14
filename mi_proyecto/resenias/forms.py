from django import forms
from .models import Resenia, Libro

class ReseniaForm(forms.ModelForm):
    class Meta:
        model = Resenia
        fields = ['contenido', 'puntuacion']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),
            'puntuacion': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion']
