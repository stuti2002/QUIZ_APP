import json
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from home.models import *


# Create your views here.
def home(request):
    return render(request,'base.html')
def quizpage(request):
    return render(request,'quiz.html')
def getapi(request):
    questionobjs=list(Questions.objects.all())
    data=[]
    try:
        for questionobj in questionobjs:
            data.append({
               "category":questionobj.categoryname.categoryname,
                "question":questionobj.questionname,
                "marks":questionobj.marks,
                 "answers":questionobj.getanswers()
            })
        payload = {"status":True,"data":data}
        return JsonResponse(payload)
        

    except Exception as e:
        print(e)
    return HttpResponse("API")
    
    

