from django.shortcuts import render
# Create your views here.

def hello(request):
    firstname = request.GET.get('firstname').capitalize()
    lastname = request.GET.get('lastname').capitalize()
    gender = request.GET.get('gender')

    if gender == "m":
        honorific = "Mr"
    else:
        honorific = "Ms"

    greeting = "Hello %s %s %s" % (honorific, firstname, lastname)

    my_dict = {
        'greeting': greeting
    }
    return render(request,'hello_app/index.html',context=my_dict)
