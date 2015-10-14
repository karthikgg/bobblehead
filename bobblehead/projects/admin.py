from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Tag
from .models import Articles


admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Articles)
