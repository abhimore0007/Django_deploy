from django.contrib import admin
from .models import Watch,Cart,Customer_Detail,Order,OrderItem,ContactMessage



@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display= ['id','name','small_description','description','original_price','discounted_price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']


@admin.register(Customer_Detail)
class DetailsAdmin(admin.ModelAdmin):
    list_display= ['id','user','name','address','city','state','pincode']

class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 1  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'order_at', 'status')  
    list_filter = ('status', 'order_at')
    search_fields = ('user__username', 'customer__name')
    inlines = [OrderItemInline] 

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'watch', 'quantity')
    search_fields = ('order__id', 'watch__name')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')  
    list_filter = ('created_at',) 
    search_fields = ('name', 'email', 'message')  
    ordering = ('-created_at',)  