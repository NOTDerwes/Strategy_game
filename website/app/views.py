from django.shortcuts import render, redirect
from .forms import FileUploadForm

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can add code here for file verification
            return redirect('file_upload')
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})
