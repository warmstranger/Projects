__author__ = 'konglingkai'

from django.contrib import admin
from models import ProjectItem

import models

admin.site.register(models.Project)
#admin.site.register(models.ClaimMaterial)
#admin.site.register(models.AssignWork)
##admin.site.register(models.Contract)
#admin.site.register(models.Event)
from django.forms import ModelForm
from models import Contract
class DocumentAdmin(admin.ModelAdmin):
    exclude= ['parent','rank','index']
#    def save_model(self, request, obj, form, change):
#        obj.parent=request.POST['parent']
#        obj.pro_id=form.POST['pro_id']
#        obj.next_sibling= 0
#        obj.save()
#    def
admin.site.register(models.Contract, DocumentAdmin)
admin.site.register(models.ClaimMaterial, DocumentAdmin)
admin.site.register(models.AssignWork, DocumentAdmin)
admin.site.register(models.Event, DocumentAdmin)