import email
from multiprocessing import context
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from app.form import SubscribeForm

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First job description",
    "Second job description"
]

# Create your views here.
# def hello(request):
#     return HttpResponse("<h3>Hello World<h3>")

def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty=""
    if request.POST:
        email = request.POST['email']
        print(email)
        if email=="":
            email_error_empty = "No email entered";
    context={"form":subscribe_form,"email_error_empty":email_error_empty}
    return render(request,"app/subscribe.html",context)


class TempClass:
  x = 5

def hello(request):
    list = ["alpha","beta"]
    temp = TempClass()
    is_authenticated = True
    context={"name" : "Django", "age" : 10, "first_list":list, "temp_object":temp, "is_authenticated":is_authenticated}
    return render(request, 'app/hello.html', context)
    

def job_list(request):
    # list_of_jobs="<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('job_detail',args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'><h1>{j}</h1></a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    context={"job_title_list":job_title}
    return render(request,"app/index.html",context)

def job_detail(request, id):
    print(type(id))
    if id == 0:
        return redirect(reverse('jobs_home'))
    try:
        # return_html = f"<h1>{job_title[id]}</h1><h3>{job_description[id]}<h3>"
        # return HttpResponse(return_html)
        context={"job_title":job_title[id], "job_description":job_description[id]}
        return render(request,"app/job_detail.html",context)
    except:
        return HttpResponseNotFound("Not Found")

def job_detail_string(request, id):
    return_html = f"<h1>String<h3>"
    return HttpResponse(return_html)
