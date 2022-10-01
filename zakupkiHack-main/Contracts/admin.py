from django.contrib import admin

# Register your models here.

from .models import Contracts
 
@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Contracts._meta.get_fields()]

# admin.site.register(Contracts, ContractsAdmin)