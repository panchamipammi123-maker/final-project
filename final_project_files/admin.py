from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Inline for Choices in Question admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Inline for Questions in Lesson admin
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Admin for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)from django.contrib import admin

# Register your models here.
