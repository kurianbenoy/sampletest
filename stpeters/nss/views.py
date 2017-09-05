from django.shortcuts import render
from django.http import HttpResponse

from .forms import NssUploadForm
from .models import NssUpload

# Create your views here.
def NssForms(request):
    form = NssUploadForm()
    print (form)
    if request.method == 'POST':
        form = NssUploadForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form,}
    return render(request,'nss/nssupload.html',context)

def nss_feed(request):
    data = NssUpload.objects.all()
    context ={'data':data}
    return render(request,'nss/nssfeed.html',context)
