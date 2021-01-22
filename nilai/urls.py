from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('',login_required(dashboard,login_url='login'),name='dashboard'),
    path('tambah-data-karyawan/',login_required(tambah_data_karyawan,login_url='login'),name='tambah-data-karyawan'),
    path('edit-data-karyawan/<str:id>/', edit_data_karyawan,name='edit-data-karyawan'),
    path('hapus-data-karyawan/<str:id>/', hapus_data_karyawan, name='hapus-data-karyawan'),
    path('kriteria/',KriteriaView,name='kriteria'),
    path('hapus-kriteria/<str:id>/',login_required(HapusKriteria,login_url='login'),name='hapus-kriteria'),
    path('penilaian/',login_required(Penilaian,login_url='login'),name='penilaian'),
    path('rincian-nilai/<str:id>/',login_required(rincian_nilai,login_url='login'), name='rincian-nilai'),

]