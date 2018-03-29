from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Note
from django.template import loader
from django.contrib.auth.decorators import login_required
def index(request):
    latest_note_list = Note.objects.order_by('-pub_date')[:5]
    context = {'latest_note_list': latest_note_list}
    return render(request, 'notes/index.html', context)

def notes_list_view(request):
    notes = Note.all.all()
    return render(request, 'notes/note/list.html',{'notes':notes})
def note_detail_view(request,note_id):
   # note = get_object_or_404(Note,pub_date__year=year, pub_date__month=month, pub_date__day=day,slug=note )
    #return render(request, 'notes/note/detail.html',{'notes':note})
  note = get_object_or_404(Note,pk = note_id)
   #return HttpResponse('You are reading at note %s.'% note_id)
  return render(request, 'notes/note/detail.html',{'note':note})
# Create your views here