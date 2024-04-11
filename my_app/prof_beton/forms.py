from django import forms
from .models import Beton

class BetonForm(forms.ModelForm):
    class Meta:
        model = Beton
        fields = ['name', 'frost_resistance', 'water_resistance', 'mobility', 'price']
        labels = {'name': 'Марка', 'frost_resistance': 'Морозостойкость',
                  'water_resistance': 'Влагозащита', 'mobility': 'Подвижность', 'price': 'Цена'}

