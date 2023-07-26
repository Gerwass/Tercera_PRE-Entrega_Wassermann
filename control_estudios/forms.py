from django import forms

class CursoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   comision = forms.IntegerField(required=True, max_value=50000)



class EstudianteFormulario(forms.Form):
   apellido=forms.CharField(required=True,max_length=256)
   nombre=forms.CharField(required=True, max_length=256)
   email=forms.EmailField(required=True)
   #telefono=forms.CharField(max_length=20,null=True)
   dni=forms.CharField(max_length=32)
   #fecha_nacimiento=forms.DateField(required=True, null=True)


class ProfesorFormulario(forms.Form):
    apellido=forms.CharField(required=True, max_length=256)
    nombre=forms.CharField(required=True, max_length=256)
'''
    email=forms.EmailField(null=True)
    telefono=forms.CharField(max_length=20,null=True)
    dni=forms.CharField(max_length=32)
    fecha_nacimiento=forms.DateField(required=True, null=True)
    profesion=forms.CharField(max_length=128)
'''