from django.shortcuts import render
from .forms import *
# Create your views here.
def render_page(request):
    return render(request,"index.html",{ "person":PersonForm,
                                         "edu": EducationForm,
                                         "exp": ExperienceForm,
                                         "skills": SkillsForm,
                                         "projects": ProjectsForm,
                                         "lang": LanguageForm,
                                         "ach": AchievementsForm,
                                         "hobby": HobbiesForm })

def submit_data(request):
    if request.method == "POST":
        person = PersonForm()
