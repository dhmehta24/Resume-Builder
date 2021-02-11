from django.shortcuts import render
from .forms import *
# Create your views here.
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

    return render(request,"resume_maker/site.html",context)

def submit_data(request):
    if request.method == "POST":
        person = PersonForm()
def get_input(request):
    new_name = request.POST.get("name")
    context={
        "name":new_name
    }
    return render(request,"resume_maker/getinput.html",context)
