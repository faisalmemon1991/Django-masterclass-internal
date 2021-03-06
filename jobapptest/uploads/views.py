from django.shortcuts import render

from uploads.forms import UploadFileForm, UploadForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':  
        form = UploadForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            saved_object = form.instance  
              
            return render(request, 'uploads/add_image.html', {'form': form, 'saved_object': saved_object})  
    else:  
        form = UploadForm()  
  
    return render(request, 'uploads/add_image.html', {'form': form})  

def upload_file(request):
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            saved_object = form.instance  
              
            return render(request, 'uploads/add_file.html', {'form': form, 'saved_object': saved_object})  
    else:  
        form = UploadFileForm()  
  
    return render(request, 'uploads/add_file.html', {'form': form})  
