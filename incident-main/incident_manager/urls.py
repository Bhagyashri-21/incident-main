from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from incident_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('add-company/', views.add_company_view, name='add_company'),
    path('report-incident/', views.report_incident_view, name='report_incident'),
    path('company-form-success/', views.company_form_success_view, name='company_form_success'),
    path('incident-form-success/', views.incident_form_success_view, name='incident_form_success'),
    path('company-details/', views.company_details_view, name='company_details'),
    path('incident-details/', views.incident_details_view, name='incident_details'),
    path('incident-detail/<int:pk>/', views.incident_detail_view, name='incident_detail'),
    path('company-detail/<int:pk>/', views.company_detail_view, name='company_detail'),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirect root URL to login page
]
