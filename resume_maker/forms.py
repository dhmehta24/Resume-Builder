from django import forms
from django.forms import ModelForm,modelformset_factory,DateField
from django.conf import settings
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        """widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'},format=('%d-%m-%y')),
        }
        input_format = ('%d-%m-%y')"""


class EducationForm(ModelForm):
    class Meta:
        model = Education
        #fields = "__all__"
        exclude = ('person',)

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('person',)
        widgets = {
            'join_dt': forms.DateInput(attrs={'class': 'datepicker'},format=('%d-%m-%y')),
            'left_dt': forms.DateInput(attrs={'class': 'datepicker'},format=('%d-%m-%y')),
        }


class SkillsForm(ModelForm):
    class Meta:
        model = SkillSet
        exclude = ('person',)

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        exclude = ('person',)
        widgets = {
            'start_dt': forms.DateInput(attrs={'class': 'datepicker'},format=('%d-%m-%y')),
            'end_dt': forms.DateInput(attrs={'class': 'datepicker'},format=('%d-%m-%y')),
        }

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