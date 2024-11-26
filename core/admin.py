from django.contrib import admin
from .models import Watch,Cart,Customer_Detail
# Register your models here.


@admin.register(Watch)
class PetAdmin(admin.ModelAdmin):
    list_display= ['id','name','small_description','description','original_price','discounted_price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']


@admin.register(Customer_Detail)
class DetailsAdmin(admin.ModelAdmin):
    list_display= ['id','user','name','address','city','state','pincode']
