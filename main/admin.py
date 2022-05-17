from django.contrib import admin
from main.models import Classe, Auth, Work, DoneWork, Grade, School

admin.site.register(Grade)
admin.site.register(DoneWork)
admin.site.register(Work)
admin.site.register(Auth)
admin.site.register(Classe)
admin.site.register(School)
