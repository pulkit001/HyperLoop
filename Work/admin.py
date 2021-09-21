from django.contrib import admin
from .models import Product , Material
# Register your models here.
admin.site.site_header = "Hyperloop Admin "
admin.site.register(Product)
admin.site.register(Material)
