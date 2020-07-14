from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name = "Home"),
    path('login/', views.login_page, name = "Login"),
    path('signup/', views.signup_page, name = "Signup"),
    path('file_a_job/', views.file_job, name = "FileJob"),
    path('get_manager_jobs/', views.job_seeker_man_view, name = "ManagerJobs"),
    path('get_se_jobs/', views.job_seeker_se_view, name = "SeJobs"),
    path('get_des_jobs/', views.job_seeker_des_view, name = "DesJobs"),
    path('get_web_jobs/', views.job_seeker_web_view, name = "webjobs"),
    path('get_account_jobs/', views.job_seeker_accountant_view, name = "AccountJobs"),
    path('get_other_jobs/', views.job_seeker_other_view, name = "OtherJobs"),  
]
