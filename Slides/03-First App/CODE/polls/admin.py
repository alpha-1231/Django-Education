from django.contrib import admin
from .models import Question,Choices

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3
    


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date","question_text"]
    list_display=["id","pub_date","question_text","was_published_recently"]
    fieldsets = [
        ("Question",
            {'fields': ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"],"classes":["collapse"]}
            ),
    ]
    inlines =[ChoiceInline]
    search_fields=["question_text",]
    list_filter = ["pub_date"]
    
admin.site.register(Question,QuestionAdmin)

admin.site.register(Choices)