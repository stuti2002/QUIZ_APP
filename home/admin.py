from django.contrib import admin

from home.models import Answers,Category, Questions

# Register your models here.
admin.site.register(Category)
#class Inline(admin.StackedInline):
#   model = 
#   extra

class AnswerAdmin(admin.StackedInline):
    model = Answers
    fk_name='question'
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin] 
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Answers)

