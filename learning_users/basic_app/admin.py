from django.contrib import admin
from basic_app.models import UserProfileInfo, User,appl,notifications,grievances

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(appl)
admin.site.register(notifications)
admin.site.register(grievances)