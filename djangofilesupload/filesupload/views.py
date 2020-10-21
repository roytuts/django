from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
            return render(request, "single.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'single.html', {'form': form})

@ensure_csrf_cookie
def upload_multiple_files(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
            context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
            return render(request, "multiple.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'multiple.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)