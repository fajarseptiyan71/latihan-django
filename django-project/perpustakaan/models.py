from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
# Create your models here.

class Perpustakaan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    no_hp = models.CharField(max_length=13)
    kelas = models.CharField(max_length=10)
    judul = models.CharField(max_length=30)
    penulis = models.CharField(max_length=20)
    penerbit = models.CharField(max_length=20)
    jumlah_buku = models.IntegerField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super(Perpustakaan, self).save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse_lazy('perpustakaan:index')

    def __str__(self):
        return "{} .{} - {}".format(self.id, self.nama, self.judul)