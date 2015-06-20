from django.contrib import admin
from goods.models import *

class WaresFotosInLine(admin.StackedInline):
    model = WaresImages
    extra = 5

class WaresPropertiesInLine(admin.StackedInline):
    model = WaresProperties
    extra = 2


class AdminWares(admin.ModelAdmin):
    inlines = [WaresFotosInLine, WaresPropertiesInLine, ]


admin.site.register(Producers)
admin.site.register(Categories)
admin.site.register(Wares, AdminWares)
admin.site.register(Properties)
admin.site.register(PropertiesValues)
admin.site.register(PropertiesByCategories)
admin.site.register(WaresProperties)
admin.site.register(WaresImages)
admin.site.register(Actions)
admin.site.register(ActionWares)