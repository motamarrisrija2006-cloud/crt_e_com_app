from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'name': 'SRIJA',
        'email': 'srija@gmail.com',
        'phone': '9876543210',
        'profession': 'Python Full Stack Developer',
        'experience': '2 Years Experience in Django Development',

        'skills': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'MySQL'
        ],

        'projects': [
            'Portfolio Website',
            'Student Management System',
            'E-Commerce Website',
            'Blog Application'
        ]
    }

    return render(request, 'home.html', context)


def contact(request):

    message = ""

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        user_message = request.POST.get('message')

        print(name)
        print(email)
        print(user_message)

        message = "Form submitted successfully!"

    return render(request, 'contact.html', {'message': message})
from django.http import HttpResponse


def grade(request, marks):

    if marks > 80:
        result = "Grade A"

    elif marks > 60:
        result = "Grade B"

    else:
        result = "Fail"

    return HttpResponse(result)

def students(request):
    students = [{
        'name': 'SRIJA','email':'srija@gmail.com'},
        {'name': 'manoj','email':'srija@gmail.com'},
        {'name': 'liki', 'email': 'srija@gmail.com'}]
    return render(request, 'students.html', {'students': students})

def user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')