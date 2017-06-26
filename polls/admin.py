from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'recentQuestion')
    list_filter = ['pub_date']
    fieldsets = [
        (None,          {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)
