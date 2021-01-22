from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class KaryawanForm(forms.ModelForm):
    tanggal_lahir = forms.DateTimeField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = Data_Karyawan
        fields='__all__'

class NamaKriteriaForm(forms.ModelForm):
    class Meta:
        model = Data_Kriteria
        exclude = ['krips']
