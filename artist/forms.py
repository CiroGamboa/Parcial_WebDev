from django import forms
from artist.models import *


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Obra
#         fields = [
#             'idtipoobra',
#             'idestilo',
#             'idautor',
#             'nombreobra',
#             'imgobra',
#             'fechaobra'
#         ]
#         labels = {
#             'idtipoobra': 'idtipoobra',
#             'idestilo': 'idestilo',
#             'idautor': 'idautor',
#             'nombreobra': 'Titulo',
#             'imgobra': 'Imagen',
#             'fechaobra': 'Fecha'
#         }
#         widgets = {
#             'idtipoobra': forms.HiddenInput(attrs={'value': TipoObra.objects.get(idtipoobra=1).idtipoobra}),
#             'idestilo': forms.HiddenInput(attrs={'value': Estilo.objects.get(idestilo=1).idestilo}),
#             'idautor': forms.HiddenInput(attrs={'value': Autor.objects.get(nombreart='Gsus').idautor}),
#             #'idtipoobra': forms.format_value(TipoObra.objects.get(idtipoobra=1)),
#             #'idestilo': forms.format_value(Estilo.objects.get(idestilo=1)),
#             #'idautor': forms.format_value(Autor.objects.get(nombreart='Gsus')),
#             'nombreobra': forms.TextInput(),
#             'imgobra': forms.FileInput(),
#             'fechaobra': forms.DateInput(attrs={'type':'date'})
#         }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ('imgobra','fechaobra')
