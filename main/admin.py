from django.contrib import admin
from main.models import Classes, Auth, Works, DoneWorks, Grades, Schools

admin.site.register(Grades)
admin.site.register(DoneWorks)
admin.site.register(Works)
admin.site.register(Auth)
admin.site.register(Classes)
admin.site.register(Schools)
