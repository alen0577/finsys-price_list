from django.contrib import admin
from .models import *


admin.site.register(ProductModel)
admin.site.register(ItemModel)
admin.site.register(sign)

admin.site.register(estimate)

admin.site.register(salesorder)


admin.site.register(payment)
