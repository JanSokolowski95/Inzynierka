from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadImageForm
from .functions import handle_uploaded_file

def format_results(results):
    return map((lambda t: '{0} - {1:g}%'.format(t[0], t[1]*100)), results)
    

def upload_file(request):
    
    if request.method == 'POST':
        form = UploadImageForm(data = request.POST, files = request.FILES)
        print(form.errors)
        if form.is_valid():
            print('succes uploading file')
            results = handle_uploaded_file(request.FILES['image'])
            results = format_results(results)
            return render(request, 'NeuralApp/results.html', {'results': results})
    else:
        form = UploadImageForm()
    return render(request, 'NeuralApp/home.html', {'form': form})

def results(request):
    results = 'Upload your image first'
    return render(request, 'NeuralApp/results.html', {'results': results})
# Create your views here.
