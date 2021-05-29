from django import forms
from django.forms import TextInput, EmailInput
from perpustakaan.models import Perpustakaan

class FormPeminjam(forms.ModelForm):
    class Meta:
        model = Perpustakaan
        fields = [
            'nama',
            'email',
            'no_hp',
            'kelas',
            'judul',
            'penulis',
            'penerbit',
            'jumlah_buku',
        ]
        labels = {
            'nama' : ('Nama'),
            'email' : ('Email'),
            'no_hp' : ('No Hp'),
            'kelas' : ('Kelas')
        }
        widgets = {
            'nama' : TextInput(attrs={
                'name' : 'nama',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput',
                'autocomplete' : 'off',
            }),
            'email' : EmailInput(attrs={
                'name' : 'email',
                'type' : 'email',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput2',
                'autocomplete' : 'off',
            }),
            'no_hp' : TextInput(attrs={
                'name' : 'no_hp',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput3',
                'autocomplete' : 'off',
            }),
            'kelas' : TextInput(attrs={
                'name' : 'kelas',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput4',
                'autocomplete' : 'off',
            }),
            'judul' : TextInput(attrs={
                'name' : 'judul',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput',
                'autocomplete' : 'off',
            }),
            'penulis' : TextInput(attrs={
                'name' : 'penulis',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput2',
                'autocomplete' : 'off',
            }),
            'penerbit' : TextInput(attrs={
                'name' : 'penerbit',
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput3',
                'autocomplete' : 'off',
            }),
            'jumlah_buku' : TextInput(attrs={
                'name' : 'jumlah_buku',
                'type' : 'nomber',
                'class' : 'form-control',
                'id' : 'formGroupExampleInput4',
                'autocomplete' : 'off',
            })
        }