from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CompanyForm, IncidentForm
from .models import Company, Incident

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def add_company_view(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_form_success')
    else:
        company_form = CompanyForm()
    
    return render(request, 'add_company.html', {'company_form': company_form})

@login_required
def report_incident_view(request):
    if request.method == 'POST':
        incident_form = IncidentForm(request.POST, request.FILES)
        if incident_form.is_valid():
            incident_form.save()
            return redirect('incident_form_success')
    else:
        incident_form = IncidentForm()
    
    return render(request, 'report_incident.html', {'incident_form': incident_form})

@login_required
def company_form_success_view(request):
    return render(request, 'company_form_success.html')

@login_required
def incident_form_success_view(request):
    return render(request, 'incident_form_success.html')

@login_required
def company_details_view(request):
    companies = Company.objects.all()
    return render(request, 'company_details.html', {'companies': companies})

@login_required
def incident_details_view(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_details.html', {'incidents': incidents})

@login_required
def incident_detail_view(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'incident_detail.html', {'incident': incident})

@login_required
def company_detail_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})

