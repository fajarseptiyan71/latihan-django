from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    UpdateView, 
    DetailView, 
    TemplateView, 
    DeleteView,
)
from perpustakaan.models import  Perpustakaan
from perpustakaan.forms import FormPeminjam
# Create your views here.

class IndexView(TemplateView):
    template_name = None
    model = Perpustakaan
    extra_context = {
        'title' : 'Home',
    }

    def get_template_names(self):
        if self.template_name is None:
            self.template_name = 'perpustakaan/index.html'
            return self.template_name
        else:
            return self.template_name

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        context = super(IndexView, self).get_context_data()
        context['datas'] = self.model.objects.all()
        return context

class RegisterView(CreateView):
    form_class = None
    model = Perpustakaan
    extra_context = {
        'title' : 'Registrasi',
    }
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())

    def get_form_class(self):
        self.form_class = FormPeminjam
        return self.form_class

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(RegisterView, self).get_context_data()

class EditPeminjamView(UpdateView):
    form_class = FormPeminjam
    model = Perpustakaan
    extra_context = {
        'title' : 'Edit',
    }
   
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(EditPeminjamView, self).get_context_data()
        return context

class DetailPeminjamView(DetailView):
    model = Perpustakaan
    extra_context = {
        'title' : 'Detail',
     }

class DeletePeminjamView(DeleteView):
    model = Perpustakaan
    success_url = reverse_lazy('perpustakaan:index')