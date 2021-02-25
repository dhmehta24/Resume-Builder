from django.shortcuts import render
from .forms import *
# Create your views here.


def get_input(request):

    if request.method == "POST":
        new_name = request.POST.get("name")
        new_email = request.POST.get("email")
        new_phone = request.POST.get("phone")
        new_github = request.POST.get("github")
        new_linked= request.POST.get("linkedin")
        new_dob = request.POST.get("dob")
        new_address = request.POST.get("address")


        show=True
    else:
        new_name=None
        show=False
        new_email = None
        new_phone = None
        new_github = None
        new_linked = None
        new_dob = None
        new_address = None

    context={
        "name":new_name,
        "email": new_email,
        "phone": new_phone,
        "github": new_github,
        "linked": new_linked,
        "dob": new_dob,
        "address_": new_address,
        "show":show,

    }

    print('//////////')
    print(request.POST)
    return render(request,"resume_maker/getinput.html",context)

def render_page(request):



    context={

        "person":PersonForm,
              "edu": EducationForm,
              "exp": ExperienceForm,
              "skills": SkillsForm,
              "projects": ProjectsForm,
              "lang": LanguageForm,
              "ach": AchievementsForm,
              "hobby": HobbiesForm}

    return render(request,"resume_maker/site.html",)
def edu(request):

    if request.method == "POST":
        new_degree=request.POST.get('Degree')
        new_year = request.POST.get('year')
        new_score = request.POST.get('score')
        new_institute = request.POST.get('institute')
        show = True

        # print(new_degree)
        # print(new_year)

    else:
        new_degree=None
        new_year = None
        new_score = None
        new_institute = None
        show = False

    context={
        'degree':new_degree,
        'score': new_score,
        'year': new_year,
     'institute': new_institute,
        "show": show,

    }
    return render(request,"resume_maker/Education.html",context)
def wor(request):
    if request.method == "POST":
        save='Next'
    else:
        save='Skip'
    # print('#####')
    # print(save)
    context={
        'Save':save
    }
    return render(request,"resume_maker/work.html",context)
def pos(request):
    if request.method == "POST":
        save='Next'
    else:
        save='Skip'
    # print('#####')
    # print(save)
    context={
        'pos_save':save
    }
    return render(request,"resume_maker/position.html",context)

def pro(request):
    if request.method == "POST":
        save='Next'
    else:
        save='Skip'
    # print('#####')
    # print(save)
    context={
        'pro_save':save
    }
    return render(request,"resume_maker/project.html",context)

def aca(request):
    if request.method == "POST":
        save='Next'
    else:
        save='Skip'
    # print('#####')
    # print(save)
    context={
        'aca_save':save
    }
    return render(request,"resume_maker/academic.html",context)
def ext(request):
    if request.method == "POST":
        save='Show My Resume'
    else:
        save='Skip and Show my Resume'
    # print('#####')
    # print(save)
    context={
        'show_resume':save
    }
    return render(request,"resume_maker/extra.html",context)
