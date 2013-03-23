__author__ = 'konglingkai'

from django.contrib import admin

import models

admin.site.register(models.AssignWork)
admin.site.register(models.Acceptance)
admin.site.register(models.Estimate)
admin.site.register(models.Bidding)
admin.site.register(models.Payment)