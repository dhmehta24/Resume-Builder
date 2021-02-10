from django.forms import ModelForm
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ('person',)

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('person',)

class SkillsForm(ModelForm):
    class Meta:
        model = SkillSet
        exclude = ('person',)

class ProjectsForm(ModelForm):
    class Meta:
        model = SkillSet
        exclude = ('person',)

class LanguageForm(ModelForm):
    class Meta:
        model = Languages
        exclude = ('person',)


class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        exclude = ('person',)


class HobbiesForm(ModelForm):
    class Meta:
        model = Hobbies
        exclude = ('person',)