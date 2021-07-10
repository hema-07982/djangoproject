from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"input.html")

def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request,"result.html",{"result": res})
        res = "Only digits are allowed"
        return render(request, "result.html",{"result": res})

def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b

        return render(request,"result.html",{"result": res})
        res = "Only digits are allowed"
        return render(request, "result.html",{"result" : res})

def substraction(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a - b

        return render(request,"result.html",{"result": res})
        res = "Only digits are allowed"
        return render(request, "result.html",{"result" : res})

def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)

        if b==0:
            res = "Zero divide error"
            return render(request, "result.html",{"request":res})
        else:
            res = a / b
            return render(request, "result.html", {"request": res})

    else:
        res = "Only digits are allowed"







