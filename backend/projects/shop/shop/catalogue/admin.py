from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.register(Product)
from .models import Category
admin.site.register(Category)
from .models import Tag
admin.site.register(Tag)
# from.models import Membership
# admin.site.register(Membership)
# from.models import Farmer
# admin.site.register(Farmer)

