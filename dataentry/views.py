from django.shortcuts import render, redirect
from uploads.models import Upload
from dataentry.utils import get_all_custom_models
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages

# Create your views here.

def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        full_file_path = str(upload.file.path) 
        
        try:
            call_command('importcsvdata', full_file_path, model_name)
            messages.success(request, 'Data imported Successfully')
        except Exception as e:
            messages.error(request, str(e))
        
        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models':custom_models,
        }
        return render(request, "importdata.html", context)