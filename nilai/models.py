from django.db import models

# Create your models here.
from django.db.models import Max, Min


class Data_Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    no_induk = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=100)
    pendidikan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=100)
    skor = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return self.nama

class  Data_Kriteria(models.Model):
    list_attr = (
        ('cost','cost'),
        ('benefit','benefit')
    )
    kode_kriteria = models.CharField(max_length=2)
    nama_kriteria = models.CharField(max_length=100)
    attribut = models.CharField(max_length=100,choices=list_attr)
    bobot = models.IntegerField()

    def __str__(self):
        return self.nama_kriteria

class Data_Krips(models.Model):
    kriteria = models.ManyToManyField(Data_Kriteria)
    nama_krips = models.CharField(max_length=200,null=True,blank=True)
    nilai = models.IntegerField()

    class Meta:
        ordering = ['nilai']
    def __str__(self):
        return f'{self.nama_krips} {self.nilai}'

class Data_Nilai_Karyawan(models.Model):
    karyawan = models.ForeignKey(Data_Karyawan, on_delete=models.CASCADE,related_name='karyawan')
    kriteria = models.ForeignKey(Data_Kriteria, on_delete=models.CASCADE,null=True)
    nilai = models.IntegerField(null=True)

    def nilai_max(self):
        mv = Data_Nilai_Karyawan.objects.filter(kriteria=self.kriteria).aggregate(Max('nilai'))['nilai__max']
        return mv
    def normalisasi1(self):
        if self.kriteria.attribut == 'benefit':
            return (self.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=self.kriteria).aggregate(Max('nilai'))['nilai__max']))
        return (self.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=self.kriteria).aggregate(Min('nilai'))['nilai__min']))

    def normalisasi2(self):
        if self.kriteria.attribut == 'benefit':
            return (self.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=self.kriteria).aggregate(Max('nilai'))['nilai__max'])) * self.kriteria.bobot
        return (self.nilai / int(Data_Nilai_Karyawan.objects.filter(kriteria=self.kriteria).aggregate(Min('nilai'))['nilai__min'])) * self.kriteria.bobot

    def __str__(self):
        return f'{self.karyawan} : {self.kriteria} : {self.nilai}'


