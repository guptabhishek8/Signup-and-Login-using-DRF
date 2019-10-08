from django.contrib import admin

# Register your models here.

from api import models


class userprofile(admin.ModelAdmin):
    list_display = (
        'email', 'name', 'is_active', 'is_staff', 'is_student', 'sap_id', 'dept_name'
    )


admin.site.register(models.UserProfile, userprofile)
