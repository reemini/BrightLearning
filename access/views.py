from django.shortcuts import render
from . models import Note

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='noaccess')
def note (request):
    post = Note.objects.all()
    return render(request,'access/note.html', {'post':post})

def noaccess (request):
    return render(request,'access/noaccess.html')