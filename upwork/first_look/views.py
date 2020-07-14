from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

import random

# import models 

from . import utils

from .models import Designer, Manager, Accountant, Other, SoftwareEngineer, WebDesigner

# Create your views here.

def home_page(request):
    context = {}
    return render(request, 'first_look/index.html', context)
 
def login_page(request):

    if request.method == "POST":
        print("[*]form is submitted")
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        print(user_email)
        print(user_password)
        u =  authenticate(username = user_email, password = user_password)
        if u is not None:
            context = {}
            context['first_name'] = u.first_name.title()
            return render(request, 'dashboard/employee.html', context)
        else:
            context = {}
            context['alert_message'] = "Your Email address and password is not recognized."
            return render(request, 'registration/login.html', context)
    else:
        context = {}
        return render(request, 'registration/login.html', context)

def signup_page(request):

    if request.method == "POST":
        try:
            print("[*]form is submitted")
            user_fullname = request.POST.get('user_fullname')
            user_email = request.POST.get('user_email')
            user_phone = request.POST.get('user_phone')
            user_profile = request.POST.get('user_profile')
            user_password = request.POST.get('user_password')
            print(user_fullname)
            print(user_email)
            print(user_phone)
            print(user_profile)
            print(user_password)
            # u = User.objects.create_user(first_name = fname, last_name = lname, email = eadd, password = pass_, username = uname)
            user = User.objects.create_user(user_email, user_email, user_password)
            user_fullname = user_fullname.split(" ")
            user.first_name = user_fullname[0]
            user.last_name = " ".join(user_fullname[1:])
            user.save()
            context = {}
            context['alert_message'] = "Your account has been created please go to login page."
            print("sucess full insertion in databaes.")
            return render(request, "registration/signup_form.html", context)
        except:
            context = {}
            context['alert_message'] = "This email address already exits or Please fill all the information."
            return render(request, "registration/signup_form.html", context)
    else:
        context = {}
        context['alert_message'] = ""
        return render(request, 'registration/signup_form.html', context)



def file_job(request):
    if request.method == "POST":
        try:
            c_name = request.POST.get("company_name")
            income_ = request.POST.get("income")
            location = request.POST.get("location")
            user_profile = request.POST.get("user_profile")
            job_services = request.POST.get("services")
            job_description = request.POST.get("des")
            
            if c_name == "" or location == "" or user_profile == "" or job_services == "" or job_description == "":
                raise ValueError()
            
            print(c_name)
            print(location)
            print(user_profile)
            print(job_services)
            print(job_description)
            print(income_)
            j_id = random.randint(1, 10000)        
            if user_profile == "Manager":
                print("Manger")
                man = Manager(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location, email_address = job_description)
                print(man)
                print("==========")
                man.save()
            elif user_profile == "Designer":
                des_ = Designer(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location, email_address = job_description)
                des_.save()
            elif user_profile == "Accounting":
                acc = Accountant(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location ,email_address = job_description)
                acc.save()
            elif user_profile == "Web Designer":
                web = WebDesigner(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location, email_address = job_description)
                web.save()
            elif user_profile == "Software Engineer":
                se = SoftwareEngineer(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location, email_address = job_description)
                se.save() 
            elif user_profile == "Other":
                to = Other(job_id = j_id, income = income_, company_name = c_name, services = job_services, location = location, description = job_services,email_address = job_description)
                to.save()
                
            context = {}
            context['alert_message'] = "Jobs had been potsted."
            return render(request, 'jobs_posting/job_post.html', context)

            
        except:
            context = {}
            context['alert_message'] = "Please fill all the field."
            return render(request, 'jobs_posting/job_post.html', context) 
            
    else:
        context = {}
        context['alert_message'] = ""
        return render(request, 'jobs_posting/job_post.html', context)


def job_seeker_man_view(request):
    context = {}
    context['jobs'] = get_manger_jobs()  
    context['job_type'] = "Manager"
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)



def job_seeker_accountant_view(request):
    context = {}
    context['job_type'] = "Accountant"
    context['jobs'] = get_accountant_jobs()  
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)


def job_seeker_se_view(request):
    context = {}
    context['job_type'] = "Software Engineer"
    context['jobs'] = get_software_engineer_jobs()  
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)



def job_seeker_des_view(request):
    context = {}
    context['job_type'] = "Designer"
    context['jobs'] = get_designer_jobs()  
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)



def job_seeker_web_view(request):
    context = {}
    context['job_type'] = "Web developer"
    context['jobs'] = get_web_designer_jobs()  
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)



def job_seeker_other_view(request):
    context = {}
    context['job_type'] = "Other"
    context['jobs'] = get_other_jobs()  
    print(context['jobs'])
    return render(request, 'dashboard/seeker.html', context)

def get_manger_jobs():
    jobs = []
    for p in Manager.objects.raw('select * from first_look_manager'):
        jobs.append(p)
    return jobs


def get_accountant_jobs():
    jobs = []
    for p in Accountant.objects.raw('select * from first_look_accountant'):
        jobs.append(p)
    return jobs

def get_desiner_jobs():
    jobs = []
    for p in Designer.objects.raw('select * from first_look_designer'):
        jobs.append(p)
    return jobs

def get_software_engineer_jobs():
    jobs = []
    for p in SoftwareEngineer.objects.raw('select * from first_look_softwareengineer'):
        jobs.append(p)
    return jobs


def get_web_designer_jobs():
    jobs = []
    for p in WebDesigner.objects.raw('select * from first_look_webdesigner'):
        jobs.append(p)
    return jobs


def get_other_jobs():
    jobs = []
    for p in Other.objects.raw('select * from first_look_other'):
        jobs.append(p)
    return jobs