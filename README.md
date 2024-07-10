# django1
Django_Procedure

Step 0.1 : In Terminal - create a project with folder name and project name as django1

django-admin startproject django1
Step 0.2 : - change dirctory to django1

cd django1
Step 0.3 : - create an app with app name as app1

django-admin startapp app1  
Step1 : In django1/settings.py add

INSTALLED_APPS = [...,'app1', ]
Step2 : In django1/urls.py - add include in import, add path in urlpatterns

from django.urls import path,include
path('app1/' ,include('app1.urls')),
Step3 : Under app1 create new folder templates, Under templates create new folder app1, Under app1, create new file index.html

<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
Step4 : Go to app1/views.py

def home(request):
    return render(request,'app1/index.html',{'param1':"hello world"})
Step5 : Create new file urls.py in app1 and add

from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]
Step6 : Go to Project folder (django1), In Terminal run,

python manage.py runserver
You will get output as
Hello World
hello world
In Browser, We should make changes in the server at localhost port 8000 i.e; 127.0.0.1:8000/app1
