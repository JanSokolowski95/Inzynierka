from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadImageForm
from .functions import handle_uploaded_file

def upload_file(request):
    form = 'Dummy String'
    form = UploadImageForm(data = request.POST, files = request.FILES)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            print('succes uploading file')
            results = handle_uploaded_file(request.FILES['image'])
            return render(request, 'NeuralApp/results.html', {'results': results})
        else:
            print('error uploading file')
            form = UploadImageForm()
    return render(request, 'NeuralApp/home.html', {'form': form})

def results(request):
    results = 'Upload your image first'
    return render(request, 'NeuralApp/results.html', {'results': results})
# Create your views here.
