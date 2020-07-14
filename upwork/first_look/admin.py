from django.contrib import admin

# Register your models here.

from  .models import Designer, Manager, Accountant, Other, SoftwareEngineer, WebDesigner


admin.site.register(Designer)
admin.site.register(Manager)
admin.site.register(Other)
admin.site.register(Accountant)
admin.site.register(SoftwareEngineer)
admin.site.register(WebDesigner)