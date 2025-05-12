from django.contrib import admin
from .models import Student, ActivationCode

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'created_at')
    search_fields = ('user__username', 'phone_number')
    list_select_related = ('user',)

@admin.register(ActivationCode)
class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'prefix', 'video', 'uses_left', 'created_at')
    list_filter = ('uses_left', 'video__course')
    search_fields = ('code', 'prefix', 'video__title')
    list_select_related = ('video', 'video__course')
    readonly_fields = ('prefix', 'code') 