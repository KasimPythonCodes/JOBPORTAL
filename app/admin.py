from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(CustomUser)
admin.site.register(Resume)
admin.site.register(job_post)


