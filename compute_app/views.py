from django.shortcuts import render
import math
# Create your views here.

def compute(request):
    num1 = float(request.GET.get('num1'))
    num2 = float(request.GET.get('num2'))
    operation = request.GET.get('operation')

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

    if result - math.floor(result) == 0:
        result = int(result)

    my_dict = {
        'result': result
    }
    return render(request,'compute_app/index.html',context=my_dict)
