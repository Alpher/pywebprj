from django.contrib import admin

# Register your models here.
from profiles.models import *

admin.site.register(AcctType)
admin.site.register(AcctStatus)
admin.site.register(Region)
admin.site.register(UserTitle)