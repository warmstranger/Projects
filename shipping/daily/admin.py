__author__ = 'konglingkai'

from django.contrib import admin

from models import Provider, Department, EnergyLog, WorkLog, ToolLog

admin.site.register(Provider)
admin.site.register(Department)
admin.site.register(EnergyLog)
admin.site.register(WorkLog)
admin.site.register(ToolLog)