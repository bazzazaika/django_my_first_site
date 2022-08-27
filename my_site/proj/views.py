from django.shortcuts import render, get_object_or_404
from .forms import DocumentForm
from django.shortcuts import redirect
from .models import Document
from django.views import generic

# Create your views here.


def index(request):
    return render(request, 'proj/project.html',context={},)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DocumentForm()
    return render(request, 'proj/model_form_upload.html', {
        'form': form
    })

def post_list(request):
    post = Document.objects.all()
    return render(request, "proj/project.html", {"posts":post})

def post_single(request, pk):
    post = get_object_or_404(Document, pk=pk)
    return render(request, "proj/one_post.html", {"post": post})


class DocumentListView(generic.ListView): # представление в виде списка
    model = Document

class DocumentDetailView(generic.DetailView):
    model = Document