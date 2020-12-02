from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Daftar
# Create your views here.

def home(request):
    ambil = Daftar.objects.all()
    return render(request, 'home.html',{'data':ambil})

def tambah(request):
    if request.method == "POST":
        lis = request.POST["lis"]
        a = Daftar(lis = lis)
        a.save()
        return redirect(home)
    else:
        return redirect(home)

def hapus(request):
    if request.method == "POST":
        id = request.POST["id"]
        Daftar.objects.filter(id=id).delete()
        return redirect(home)
    else:
        return redirect(home)

def ubah(request,ida):
    if request.method == "POST":
        id = ida
        lala = Daftar.objects.get(id=id)
        lala.lis = request.POST["lis"]
        lala.save()
        return redirect(home)
    else:
        ambil = Daftar.objects.filter(id=ida).first
        return render(request,'ubah.html',{'data':ambil})