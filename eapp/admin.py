from django.contrib import admin
from . models import Product,Category,Customer_account,Cart,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer_account)
admin.site.register(Cart)
admin.site.register(Contact)