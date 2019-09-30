# DJango Forms

What is DJango
------
> It is "a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source".

What is DJango Forms
------
> Django Forms. Django provides a Form class which is used to create HTML forms.

> Each field of the form class map to the HTML form <input> elements and each one is a class itself, it manages form data and performs validation while submitting the form.

Steps for creating django forms
------
> In this example, we are implementing sample django forms using basic django model object.

##### Install DJango RestFramework / prerequisites
> install django (if django is not installed on your machine)
`pip install django`
> **OR**
> use this command for user specific installation 
`pip install django --user`

##### Project setupProject setupProject setupProject setup

> Create new django project called **employee_form**

```python
mkdir django_employee_form
cd django_employee_form
django-admin create employee_form
```
 > Create django app 

```python 
django-admin startapp webapp
```

##### Modify your django application settings.py
> Add 'webapp' into INSTALLED_APPS.

```python
INSTALLED_APPS = [
    ....
    'webapp',
]
```
##### Implement DJango forms

> Define sample URLS on webapp/urls.py

```python
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
]
```
> Now sync your database for the first time & Create superuser for the first time

```python
python manage.py migrate
python manage.py createsuperuser
```

> Create a model for Employee on webapp/models.py

```python
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.BigIntegerField()
    def __str__(self):
        return self.name
```
> sync DB with changes

```python
python manage.py makemigrations
python manage.py migrate
```

> Add your **Employee** model into admin console. We can navigate and check the entries on db http://localhost:8000/admin

```python
from django.contrib import admin
from .models import Employee
admin.site.register(Employee)
```

> Create a file form.py and define ModelForm on it.
```python
from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ('id', 'name')
```

> Create index.html file on webapp/templates/index.html
 
 ```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
</head>  
<body>  
<form method="POST" class="post-form">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit" class="save btn btn-default">Save</button>  
    </form>  
</body>  
</html>  
```
![alt text](https://github.com/prabhakar2020/django_forms/blob/master/preview.PNG)
> Update views as per the ModelForms on webapp/views.py
 
 ```python
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import EmployeeForm
def index(request):
    emp = EmployeeForm()
    return render(request,"index.html",{'form':emp})  
```
> Now lets run the server *python manage.py runserver*

`Note: Above django project prepared and tested on django==2.2.3 and djangorestframework==3.10.2`
