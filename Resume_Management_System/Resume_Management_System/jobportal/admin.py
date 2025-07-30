from django.contrib import admin
from django.db import models
from .models import Job, Application, Skill, CareerTip, AptitudePaper, MockTestSchedule, HRQuestion

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'location', 'technology', 'posted_on')
    search_fields = ('title', 'location', 'technology')
    list_filter = ('location', 'technology')
    list_per_page = 10
    filter_horizontal = ('skills',)
    fields = ('posted_by', 'title', 'description', 'technology', 'skills', 'location')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'applied_on', 'user')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('applied_on',)
    list_per_page = 10

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


admin.site.register(CareerTip)
admin.site.register(AptitudePaper)

@admin.register(MockTestSchedule)
class MockTestScheduleAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date', 'time', 'get_time_slot', 'duration')

    def get_time_slot(self, obj):
        hour = obj.time.hour
        if 0 <= hour < 5:
            return "Midnight"
        elif 5 <= hour < 12:
            return "Morning"
        elif hour == 12:
            return "Noon"
        elif 12 < hour < 17:
            return "Afternoon"
        elif 17 <= hour < 20:
            return "Evening"
        else:
            return "Night"
    get_time_slot.short_description = 'Time Slot'


@admin.register(HRQuestion)
class HRQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']