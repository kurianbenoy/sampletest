from django.shortcuts import render

# Create your views here.
def NssForms(request):
	context={}
	return render(request,'nss/nssupload.html',context)
