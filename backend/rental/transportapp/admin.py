from django.contrib import admin

# Register your models here.
from .models import TransportModel, TransportTypeModel, ManufacturerModel

admin.site.register(TransportTypeModel)
admin.site.register(TransportModel)
admin.site.register(ManufacturerModel)


