from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        password=request.POST['pwd']
        print(name)
        print(password)
        return HttpResponse('Data submitted successfully')
    return render(request,'hai.html')
