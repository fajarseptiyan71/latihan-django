from django.urls import path, re_path
from perpustakaan.views import (
    IndexView, 
    RegisterView, 
    EditPeminjamView, 
    DetailPeminjamView,
    DeletePeminjamView,
)

app_name = 'perpustakaan'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pinjam/', RegisterView.as_view(), name='register'),
    re_path('edit/(?P<pk>\d+)/$', EditPeminjamView.as_view(), name='edit'),
    re_path('detail/(?P<slug>[\w-]+)/$', DetailPeminjamView.as_view(), name='detail'),
    re_path('kembalikan/(?P<pk>\d+)/$', DeletePeminjamView.as_view(), name='kembalikan'),
]