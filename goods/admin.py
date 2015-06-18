from django.contrib import admin
from goods.models import *

admin.site.register(Producers)
admin.site.register(Categories)
admin.site.register(Wares)
admin.site.register(Properties)
admin.site.register(PropertiesValues)
admin.site.register(PropertiesByCategories)
admin.site.register(WaresProperties)
admin.site.register(WaresImages)
admin.site.register(Actions)
admin.site.register(ActionWares)