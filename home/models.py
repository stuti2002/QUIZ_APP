from django.db import models
from django.db.models.deletion import CASCADE
import uuid 

# Create your models here.
class Baseclass(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    createdat=models.DateField(auto_now_add=True)
    updatedat=models.DateField(auto_now=True)
    
    #this tag is use when we want to inherit
    #our parent class
    class meta:
        abstract=True
    
class Category(Baseclass):
    categoryname=models.CharField(max_length=50)

    def __str__(self) :
        return self.categoryname

    

class Questions(Baseclass):
    categoryname=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    questionname=models.CharField(max_length=50)
    marks=models.IntegerField(default=5)
    
    def __str__(self):
        return self.questionname
    def getanswers(self):
        answerobjs=list(Answers.objects.filter(question=self))
        data=[]
        for answerobj in answerobjs:
            data.append({
                "answer":answerobj.answer,
                "iscorrect":answerobj.iscorrect
            })
        return data

class Answers(Baseclass):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='ques')
    answer=models.CharField(max_length=30)
    iscorrect=models.BooleanField(default=False)

    def __str__(self):
        return self.Answer

    
    
    