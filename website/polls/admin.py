# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import question,choice
# Register your models here.
class choiceinline(admin.TabularInline):
    model=choice
    extra = 3
class questionadmin(admin.ModelAdmin):
    fieldsets = [
        ("Question",{"fields":['question_text']}),
        ("Date Information",{"fields":["pub_date"]}),
    ]
    inlines = [choiceinline]
    list_display = ("question_text","pub_date")
admin.site.register(choice)
admin.site.register(question,questionadmin)
