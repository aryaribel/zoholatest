from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company-Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company-Profile',views.company_profile,name='company_profile'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),




    # -------------------------------Staff section--------------------------------
    path('Staff-Dashboard',views.staff_dashboard,name='staff_dashboard'),
     path('Staff-Profile',views.staff_profile,name='staff_profile'),


    # -------------------------------Zoho Modules section--------------------------------
    
    #-------------------------Arya E.R---------------------------------------------------

    ####  Vendor ###########
    path('vendor',views.vendor,name='vendor'),
    path('view_vendor_list',views.view_vendor_list,name='view_vendor_list'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('view_vendor_active',views.view_vendor_active,name='view_vendor_active'),
    path('view_vendor_inactive',views.view_vendor_inactive,name='view_vendor_inactive'),
    path('sort_vendor_by_name',views.sort_vendor_by_name,name='sort_vendor_by_name'),
    path('sort_vendor_by_amount',views.sort_vendor_by_amount,name='sort_vendor_by_amount'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('import_vendor_excel',views.import_vendor_excel,name='import_vendor_excel'),
    path('Vendor_edit/<int:pk>',views.Vendor_edit,name='Vendor_edit'),
    path('do_vendor_edit/<int:pk>',views.do_vendor_edit,name='do_vendor_edit'),
    path('delete_vendors/<int:pk>',views.delete_vendors,name='delete_vendors'),
    path('vendor_status/<int:pk>',views.vendor_status,name='vendor_status'),
    path('vendor_add_comment/<int:pk>',views.vendor_add_comment,name='vendor_add_comment'),
    path('vendor_delete_comment/<int:pk>',views.vendor_delete_comment,name='vendor_delete_comment'),
    path('vendor_shareemail/<int:pk>',views.vendor_shareemail,name='vendor_shareemail'),
    path('payment_terms_add',views.payment_terms_add,name='payment_terms_add'),
    path('add_vendor_file/<int:pk>',views.add_vendor_file,name='add_vendor_file'),

#------------------------------End---------------------------------------------------------

]