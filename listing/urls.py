from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('tambah', views.tambah),
    path('hapus', views.hapus),
    path('ubah/<int:ida>', views.ubah),
    path('ubah/', views.hapus),
]