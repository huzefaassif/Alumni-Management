from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Student
from .models import Alumni
from .models import Questions
from .models import Answers
from .models import Chat
from .models import Blog
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'

class AlumniInline(admin.StackedInline):
    model = Alumni
    can_delete = False
    verbose_name_plural = 'Alumni'

class QuestionsInline(admin.StackedInline):
    model = Questions
    can_delete = False
    verbose_name_plural = 'Questions'
class AnswersInline(admin.StackedInline):
    model = Answers
    can_delete = False
    verbose_name_plural = 'Answers'

class UserAdmin(BaseUserAdmin):
    inlines = (AlumniInline, StudentInline , QuestionsInline ,AnswersInline )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Alumni)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Chat)
admin.site.register(Blog)
