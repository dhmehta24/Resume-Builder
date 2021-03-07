from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    age = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null= True)
    website = models.URLField(blank=True,null = True)

    def full_name(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])

    def __str__(self):
        return self.first_name

class Education(models.Model):
    Degrees = (
        ('PhD','PhD'),
        ('Masters','Masters'),
        ('Bachelors','Bachelors'),
        ('High School','High School')
    )
    Status = (
        ('Pursuing','Pursuing'),
        ('Completed','Completed')
    )
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    qualification = models.CharField(choices=Degrees,max_length=25)
    status = models.CharField(choices = Status, max_length = 25)
    institution = models.CharField(max_length=75)
    board = models.CharField(max_length=75)
    start_yr = models.DateField()
    end_yr = models.DateField()
    cgpa = models.FloatField(blank=True,null=True)
    percent = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.qualification

class Experience(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    role = models.CharField(max_length = 270)
    join_dt = models.DateField()
    left_dt = models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.company

class SkillSet(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    skill = models.CharField(max_length=25)

    def __str__(self):
        return self.skill

class Projects(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    project = models.CharField(max_length=150)
    start_dt = models.DateField()
    end_dt = models.DateField()
    project_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.project

class Languages(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    language = models.CharField(max_length=25)

    def __str__(self):
        return self.language

class Achievements(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    achievement = models.TextField()

    def __str__(self):
        return self.achievement

class Hobbies(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    hobby = models.CharField(max_length=150)

    def __str__(self):
        return self.hobby

