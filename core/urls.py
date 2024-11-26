from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.log_out, name="logout"),
    path('Profile/',views.User_Profile, name="Profile"),
    path('ChangePassword/',views.User_Change_Password, name="changePassword"),
    path('Forgot_Password/',views.User_Password_forgot_Form, name="ForgotPassword"),
    path('categories/',views.User_categories, name="categories"),
    path('watch_details/<int:id>',views.watch_details, name="watchdetails"),
    path('Add_To_Cart/<int:id>',views.Add_To_Cart,name='AddToCart'),
    path('view_To_Cart/',views.view_To_Cart,name='viewCart'),
    path('add_to_quantity/<int:id>',views.add_to_quantity,name='addtoquantity'),
    path('delete_to_quantity/<int:id>',views.delete_to_quantity,name='deletetoquantity'),
    path('delete_the_Cart/<int:id>',views.delete_the_Cart,name='deletetheCart'),
    path('AddressPage',views.AddressPage,name='AddressPage'),
    path('Address_Add',views.Address_Add,name='Address_Add'),
    path('delete_Add/<int:id>',views.delete_Add,name='delete_Add'),
    path('Profile_edit',views.Profile_edit,name='Profile_edit'),
    path('Check_Out',views.Check_Out,name='Check_Out'),
    path('Payment',views.Payment,name='Payment'),
    path('payment_success/',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    
   
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)