from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def upload_files(request):
    if request.method == "GET":
        return render(request, 'files_upload.html', )
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        #print(files)
        for f in files:
            handle_uploaded_file(f)
        return JsonResponse({'msg':'<span style="color: green;">File successfully uploaded</span>'})
    else:
        return render(request, 'files_upload.html', )

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)