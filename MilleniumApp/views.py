from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from MilleniumApp.form import BuyerForm

#Displays HTML page
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#Displays Form
def index(request):
    buy =  BuyerForm()
    return render(request,"index.html",{'form':buy})

#Form Validation.
def valbuy(request):
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
        else:
            form = BuyerForm()
        return render(request,'index.html',{'form':form})

# Create your views here.
