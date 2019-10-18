# djando project road map
# to get started with django we need the following

# 1- create a folder
# 2- create a virtual environment and activate it
# 3- requirements.txt

# 4- open the terminal and run the command django-admin startproject(project name)
    #  think of a django project as the entire web application that might be compsed of diffrent parts
 
# 5- The projectname will create in two folders of the same name where the outer name is just a container thats holding following 5(five) py files ...
    # __init__.py
            #    tells us that the product directory is a python package and a python package is just a colection of a bunch of differnt python files that are grouped together for some purpose
    # settings.py
            #  has all the settings for our web application eg what other applications are installed with our project, what time zone is within our application or what soap of database dowe want to use within pur application etc all thses are defined in settings
    # urls.py
            # has the urls or routes that determin what user can go to when they visit a web application. this only contains the urls that pipo can go to. it associates those urls with aparticular function thats going to run in order to render the response we want to get back to the user
    # wsgi.py
            # server 
    # manage.py
            # the python script u gonna need to perform some very useful  operation on the web application
# 5- django project is the big picture containing all the files needed for our website. a django project consists of one or more apps where each of these individual apps usually just serves a parcular purpose or has some particular function. tho we nedd to build our apps, django has some build in apps for us
          # the django build in apps are........

# 6- inside product (project directory) is where we create these apps

# open terminal and run this command ......python manage.py startapp(name of the app) hello. this will create an app called hello with 6 python files and 1 directory called migrations. The files are ...
     # __init__.py
     # admin.py
     # apps.py
     # models.py
     # tests.py
     # views.py
        # The code here in views.py decides what the user sees  when they go to a particular route  
    # now we have the app and all the dafualt faulders it creates, but we have to create another urls.py inside app that will connect with the url on the project directory(in this case product)
    # urls.py
           # inside this foreign url.py, we import some variables from the current package
# 6- after the above process, now time to create some modules. in modules we will have classes that are going to define the typs of data that i want to be ables to store inside my databse for a particular application . now got models.py and define some models 

#7- after creating the modules, we to take this confuguration step, we need to make sure that this django project knows about these models. my project needs to knw that this appliaction exists and has these modes.
          #we do this by going to the settings.py file for the application , then scroll to find INSTALLED APPS variale which is alist of all the apps that are installed. inside the installed apps, include or add your applications app folder there. its more like saying the class is installed this project
         
# now we need to create the table for managing flights inside of our database. we do this on terminal with the command python manage.py makemigrations. python manage.py makemigrations will loomk thru my model file and look for any changes that have been made to tho model files, ans automatically generate a migration is goint to represent chnages made to the dta base in order the new changes made to the moodel file to to work. that will create a file called 0001_initial.py .lets go inside 000_initial.py . youll find the class.

# if you want to see the sql table that make migrations created, run this command >>>>> python manage.py sqlmigrate flights 0001 in terminal 

#- its now time tp make use migrations. django automactlly detects anytime we make a change to our models.py file and automatically generates the sequal code neccessary to run on our database in order to allow these changes to happen inside of our database

#for a better shell interaction, open terminal and run command python manage.py shell  on it, then there start interacting with the django shell like.....
         # from flights.models import Flight(its a class so capital f)
        #  then create avaribale may be called f and assign it the details in the model. in the case the details are....
        # f = (oringin="New York", destination="London",duration=415)
        # in the django shell defin flight and give it attribute eg define flight as f for variable flight orit could be anything anyname. the asign it props like f=(name="", age="" etc.)now here the acces will be like f.name f.age etc
        # then run f.save() which saves the details in the database;

# now if i want query for something in the database ill go like belowe
        # Flight.object.all() returns a number of all flights or querrying all flights. however, the return isnt that helpful to look at. a better string representation would be great and this is made possible by going back to models and write  a function .... def __str__(self): and returns f"{self.id}-{self.destination} to {self.duration}"
# when using the django shell, import all modules separated by coma

# read about CASCADE aopn deletion

#RENDERING TEMPLATES

#In Django, web pages and other content are delivered by views. Each view is represented by a simple Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

#so now other than just rendering a string, its time to render html templates. so to do this we have to go inside templates and write some html.
        #after that we come to views.py and in return write render mothod that takes in acouple of arguments and this case the first argument will be rquest and the second argument is the name if the html template that we want render and in the case, index.html like sooo.
        #  return render(request,"flights/index.html"). before running this, make sure that index.html exists. got the app folder in this flights then in their create a directory called templates and it will contain all html files.


 #RENDERING WHATS INSIDE OUR DATABASE;
       #how do we render whats inside the database in django? we use django templating engine. we render whats inside the database by passing whats inside the data base to the html by the use of django templating engine.

       # A Django project can be configured with one or several template engines (or even zero if you don’t use templates). Django ships built-in backends for its own template system, creatively called the Django Template Language (DTL), and for the popular alternative Jinja2. Backends for other template languages may be available from third-parties.
                
    
