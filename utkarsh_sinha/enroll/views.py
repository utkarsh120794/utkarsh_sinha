from django.shortcuts import render
from .forms import EmployeeRegistration

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
    else: 
        fm =EmployeeRegistration()
    return render(request, 'addandshow.html', {'form':fm})

