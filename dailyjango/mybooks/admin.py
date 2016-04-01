from django.contrib import admin

# Register your models here.
from .models import Question,Choice

# admin.site.register(Question)
# admin.site.register(Choice)


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']

    fieldsets = [
        ("hah",  {'fields': ['question_text']}),
        ('Data info',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
admin.site.register(Question, QuestionAdmin)