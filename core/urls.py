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
    path('categories/',views.main_categories, name="categories"),
    path('Sport/',views.Sport_categories, name="Sport_categories"),
    path('Luxury/',views.Luxury_categories, name="Luxury_categories"),
    path('Smart/',views.Smart_categories, name="Smart_categories"),
    path('watch_details/<int:id>/',views.watch_details, name="watchdetails"),
    path('Add_To_Cart/<int:id>',views.Add_To_Cart,name='AddToCart'),
    path('view_To_Cart/',views.view_To_Cart,name='viewCart'),
    path('add_to_quantity/<int:id>',views.add_to_quantity,name='addtoquantity'),
    path('delete_to_quantity/<int:id>',views.delete_to_quantity,name='deletetoquantity'),
    path('delete_the_Cart/<int:id>',views.delete_the_Cart,name='deletetheCart'),
    path('AddressPage',views.AddressPage,name='AddressPage'),
    path('Address_Add',views.Address_Add,name='Address_Add'),
    path('delete_Add/<int:id>',views.delete_Add,name='delete_Add'),
    path('Profile_edit',views.profile_edit,name='Profile_edit'),
    path('Check_Out',views.Check_Out,name='Check_Out'),
    path('Payment',views.Payment,name='Payment'),
    path('payment_success/<int:selected_address_id>',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    path('Buy_now/<int:id>',views.Buy_now,name='Buy_now'),
    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),
    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
    path('Order_Page/',views.User_order,name="Order"),
    path('About_Us/',views.About_us,name="About"),
    path('Forgot_Pass/',views.Forgot_pass,name="Forgot_pass"),
    path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
    path('Support/', views.Support, name='Support'),     
    path('search', views.member_search, name='member_search'), 
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='resetpassword'),
    path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
    path('contact-us/', views.contact_us, name='contact_us'),
   
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)