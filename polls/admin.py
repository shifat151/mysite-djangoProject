from django.contrib import admin
from .models import Question,choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model=choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text', 'pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']

    #Fieldsets for making a block for every field
    fieldsets = [
        (None,
         {
            "fields" :['question_text']
         }
        ),

        ('Date information', 
        {
            "fields":['pub_date'],
            "classes": ['collapse']
        
        }
        ),
    ]

    inlines=[ChoiceInline]

    


admin.site.register(Question, QuestionAdmin)



