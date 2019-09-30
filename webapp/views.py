from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    emp = EmployeeForm()
    return render(request,"index.html",{'form':emp})  