from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from .utils import render_to_pdf
#from weasyprint import HTML
from django.template.loader import render_to_string

try:
    personId = Person.objects.last().id
except AttributeError:
    personId = 1

forms = {
              "person":PersonForm,
              "edu": EducationForm,
              "exp": ExperienceForm,
              "skills": SkillsForm,
              "projects": ProjectsForm,
              "lang": LanguageForm,
              "ach": AchievementsForm,
              "hobby": HobbiesForm
}

# Create your views here.
def render_page(request):
    person = Person.objects.last()
    education = Education.objects.filter(person_id=personId)
    exp = Experience.objects.filter(person_id=personId)
    skill = SkillSet.objects.filter(person_id=personId)
    prjct = Projects.objects.filter(person_id=personId)
    ach = Achievements.objects.filter(person_id=personId)

    context = {
        "person": person,
        "education": education,
        "exp": exp,
        "skill": skill,
        "prjct": prjct,
        "lang": Languages,
        "ach": ach,
        "hobb": Hobbies,
    }

    return render(request,"site.html",context)


def personal_det(request):
    return render(request,"getinput.html", { "person":PersonForm})

def get_input(request):
    show = False
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            #edu(request)
            show = True
            return render(request,"getinput.html",{ "form":form,"person":person,"show":show})
    else:
        form = PersonForm()

    """if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phno = request.POST.get("phone")
        addre = request.POST.get("address")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        website = request.POST.get("website")

        data = Person(first_name = name.split()[0], middle_name = name.split()[1], last_name = name.split()[-1], email = email, mobile_no = phno, age = age, address = addre, github = github, linkedin = linkedin, website = website)
        data.save()

        return render(request,"Education.html", { "edu" : EducationForm})

    else:"""
    return render(request, "getinput.html",{ "form" : form,"show":show})

def edu(request):
    if request.method == "POST":
        form = EducationForm(request.POST or None)
        """data = get_object_or_404(Person, pk=educ.id)
        #print(data)
        form = EducationForm(request.POST, instance=data)
        if form.is_valid():
            Education(person_id = educ.id).save()
            form.save()
            print("Data Saved")"""
        if form.is_valid():
            cd = form.cleaned_data
            degree = cd.get('degree')
            qualification = cd.get('qualification')
            institution = cd.get('institution')
            board = cd.get('board')
            start_yr = cd.get('start_yr')
            end_yr = cd.get('end_yr')
            cgpa = cd.get('cgpa')
            percent = cd.get('percent')

            data = Education(qualification = qualification, institution = institution, board = board, start_yr = start_yr, end_yr = end_yr, cgpa = cgpa, percent = percent,person_id=personId)
            data.save()
            print("Data Saved")
    else:
        form = EducationForm()




    """if request.method == "POST":
        qual = request.POST.get("qual")
        yr = request.POST.get("year")
        inst = request.POST.get("inst")
        score = request.POST.get("score")
        rem = request.POST.get("remarks")"""
    return render(request,"Education.html",{"edu":form})

def wor(request):
    print(personId)
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            company = cd.get('company')
            role = cd.get('role')
            join_dt = cd.get('join_dt')
            left_dt = cd.get('left_dt')
            details = cd.get('details')

            data = Experience(company = company,role = role, join_dt = join_dt, left_dt = left_dt, details = details, person_id = personId)
            data.save()
    else:
        form = ExperienceForm()
    return render(request,"work.html",{ "exp" : form})

def skill(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            skill = cd.get('skill')

            data = SkillSet(skill = skill,person_id = personId)
            data.save()
    else:
        form = SkillsForm()
    return render(request,"skillset.html", { "skill": form})

def pro(request):
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project = cd.get('project')
            start_dt = cd.get('start_dt')
            end_dt = cd.get('end_dt')
            project_link = cd.get('project_link')

            data = Projects(project = project, start_dt = start_dt, end_dt = end_dt, project_link = project_link, person_id = personId)
            data.save()
    else:
        form = ProjectsForm()
    return render(request,"project.html", {"prjct": form})

def lang(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LanguageForm()
    return render(request,"languages.html", { "lang": form })

def ext(request):
    if request.method == "POST":
        form = AchievementsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            achievement= cd.get('achievement')

            data = Achievements(achievement = achievement,person_id = personId)
            data.save()
    else:
        form = AchievementsForm()
    return render(request,"extra.html", { "ach" : form})

def get_pdf(request):
    pass

    """content = Person.objects.last()

    pdf = render_to_pdf("site.html")

    return HttpResponse(pdf, content_type = "application/pdf")

    return render_to_pdf(
            "site.html",
            {
                "pagesize":"A4",
                "data": content,
            })"""

    """html_string = render_to_string('site.html')
    
    html = HTML(string = html_string)

    html.write_pdf(target = 'resume.pdf')"""





