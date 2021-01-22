from django.db.models import Max, Min, Value, F, FloatField
from django.forms import model_to_dict
from django.shortcuts import render,redirect
from .forms import *


def dashboard(r):
    kriteria = Data_Karyawan.objects.all()
    for x in Data_Karyawan.objects.all():
        d = x.karyawan.all()
        b = sum([(c.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=c.kriteria).aggregate(Max('nilai'))['nilai__max'])) * c.kriteria.bobot if c.kriteria.attribut == 'benefit' else (c.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=c.kriteria).aggregate(Min('nilai'))['nilai__min'])) * c.kriteria.bobot for c in d])
        print(b)
        x.skor = b
        x.save()

    if r.method =='POST':
        nilai_key = list(r.POST.dict())[2:]
        karyawan = Data_Karyawan.objects.get(id=r.POST.get('karyawan_id'))
        kriteria = Data_Kriteria.objects.filter(nama_kriteria__in=nilai_key)
        for i in kriteria:
            Data_Nilai_Karyawan.objects.create(karyawan = karyawan,kriteria=i,nilai=r.POST.get(i.nama_kriteria))


        return redirect('dashboard')
    data = Data_Karyawan.objects.all()
    kriteria = Data_Kriteria.objects.all()
    context = {
        'a':data,
        'kriteria':kriteria
    }
    return render(r,'dashboard.html',context)

def  tambah_data_karyawan(r):
    form =  KaryawanForm()
    if r.method =='POST':
        form = KaryawanForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(r,'tambah_data_karyawan.html',context)

def edit_data_karyawan(r,id):
    kar = Data_Karyawan.objects.get(id=id)
    form = KaryawanForm()
    if r.method == 'POST':
        form = KaryawanForm(r.POST, instance=kar)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'x':kar
    }
    return render(r, 'edit_data_karyawan.html', context)

def hapus_data_karyawan(r,id):
    kar = Data_Karyawan.objects.get(id=id)
    kar.delete()
    return redirect('dashboard')

def KriteriaView(r):
    form = NamaKriteriaForm()
    data = Data_Kriteria.objects.all()
    if r.method == 'POST':
        form = NamaKriteriaForm(r.POST)
        print(form.errors)
        if form.is_valid():
            data = form.save()
            for x in Data_Krips.objects.all():
                x.kriteria.add(data)
            return redirect('kriteria')
    context = {
        'a':data,
        'form':form
    }
    return render(r,'kriteria.html',context)

def HapusKriteria(r,id):
    Data_Kriteria.objects.get(id=id).delete()
    return redirect('kriteria')

def Penilaian(r):
    data = Data_Kriteria.objects.all()
    all_data_nilai = Data_Nilai_Karyawan.objects.all()
    all_user = Data_Karyawan.objects.filter(id__in=all_data_nilai.values_list('karyawan',flat=True))
    context = {
        'a':data,
        'b':all_user,
        'c':all_data_nilai
    }

    return render(r,'penilaian.html',context)

def rincian_nilai(r,id):
    karyawan = Data_Karyawan.objects.get(id=id)
    data_nilai =Data_Nilai_Karyawan.objects.filter(karyawan=karyawan)
    # for x in data_nilai:
        # x.nilai_max(x.kriteria)
        # print(x.nilai_max(x.kriteria))
    data_kriteria = Data_Kriteria.objects.all()
    context = {
        'karyawan':karyawan,
        'a': data_kriteria,
        'c': data_nilai
    }
    return render(r,'rincian_nilai.html',context)




