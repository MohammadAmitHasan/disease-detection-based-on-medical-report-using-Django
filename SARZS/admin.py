from django.contrib import admin

from .models import *

admin.site.register(test)
admin.site.register(hospitals)
admin.site.register(diagnostic_centers)
admin.site.register(doctor_list)
admin.site.register(record)
admin.site.register(docReview)
admin.site.register(hospitalReview)
admin.site.register(diagnosticReview)