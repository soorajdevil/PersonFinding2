from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from .views import logout
urlpatterns=[
    
     
     path('',views.Index,name='index'),
     path('userindex/', views.userIndex, name='userindex'),
     path('adminindex/', views.admin, name='adminindex'),
     path('policeindex/', views.policeindex, name='policeindex'),
     
     path('Useradd/',views.useradd,name='Useradd'),
     path('userview/',views.dataview,name='userview'),
     path('useredit/<int:user_id>',views.useredit,name='useredit'),
     path('userdelete/<int:user_id>',views.userdelete,name='userdelete'),

     path('policeadd/',views.policeadd,name='policeadd'),
     path('policeview/',views.policeview,name='policeview'),
     path('hospitaladd/',views.hospitaladd, name='hospitaladd'),
     path('hospitalview/',views.hospitalview, name='hospitalview'),
     path('hospitaledit/<int:hospital_id>',views.hospitaledit,name='hospitaledit'),
     path('hospitaldelete/<int:hospital_id>',views.hospitaldelete,name='hospitaldelete'),

     path('useradminview/',views.useradminview, name='useradminview'),
     #path('useradmindelete/<int:user_id>',views.useradmindelete,name='useradmindelete'),
     
     path('hospitaladminview/',views.hospitaladminview, name='hospitaladminview'),
     path('policeadminview/',views.policeadminview, name='policeadminview'),
     path('loginindex/<str:usertype>/',views.loginindex, name='loginindex'),
     path('logout/',views.logout,name='logout'),
     path('edit_User/<int:user_id>/',views.Update_User_profile, name='edit_User'),
     path('edit_police/<int:Station_id>/',views.Update_Police_profile, name='edit_police'),
     path('edit_hospital/<int:hospital_id>/',views.update_Hospitals_profile, name='edit_hospital'),
     path('hospitalindex/', views.hospital_index, name='hospitalindex'),
     
     path('Usermissingadd/',views.User_missingadd, name='Usermissingadd'),
     path('usermissingview/',views.usermissingview,name='usermissingview'),
     path('policemissingview/',views.policemissingview,name='policemissingview'),

     path('public_missing_view/',views.public_missing_view,name='public_missing_view'),
     path('public_missing_view/<int:id>',views.missing_people_view_public,name='public_missing_view'),

     path('editusermissingadd/<int:id>',views.edituser_missing,name='editusermissingadd'),
     path('delete_usermissing/<int:id>',views.deleteuser_missing,name='delete_usermissing'),

     path('Accidentadd',views.Accident,name='Accidentadd'),
     path('accidentview/', views.accidentview, name='accidentview'),
     path('policeaccidentview/', views.policeaccidentview, name='policeaccidentview'),
     path('editaccident/<int:id>',views.editaccident,name='editaccident'),
     path('accidentdelete/<int:id>',views.accidentdelete,name='accidentdelete'),

     path('casesheetadd',views.casesheetadd,name='casesheetadd'),
     path('casesheetview/', views.casesheetview, name='casesheetview'),

     path('editcasesheet/<int:id>',views.editcasesheetadd,name='editcasesheet'),
     path('deletecasesheet/<int:id>',views.deletecasesheetadd,name='deletecasesheet'),

     path('policecasesheetview/',views.policecasesheetview,name='policecasesheetview'),
     path('logout/<str:token>/', logout, name='logout'),
     path('editpoliceview/<int:id>',views.editpoliceview,name='editpoliceview'),
     path('deletepoliceview/<int:id>',views.deletepoliceview,name='deletepoliceview'),
     path('userpoliceview/',views.userpoliceview,name='userpoliceview'),
     
     path('user_enquiry/',views.user_enquiry,name='user_enquiry'),
     
     path('user_enquirypage/<int:hospital_id>/', views.user_enquiryaddDetails, name='user_enquirypage'),
     path('user_enquiryview/',views.user_enquiryview,name='user_enquiryview'),
     
     path('user_replyadd/<int:enquiry_id>/', views.user_replyadd, name='user_replyadd'),

     path('user_replyview/', views.user_replyview, name='user_replyview'),

     path('police_enquiry/',views.police_enquiry,name='police_enquiry'),
     path('police_enquirypage/<int:hospital_id>/', views.police_enquiryaddDetails, name='police_enquirypage'),
   
     path('police_enquiryview/',views.police_enquiryview,name='police_enquiryview'),

     path('replyadd_police/<int:enquiry_id>/', views.replyadd_police, name='replyadd_police'),

     path('replyview_police/', views.replyview_police, name='replyview_police'),

     path('complaintadd/', views.file_complaint, name='complaintadd'),
     path('complaintview/',views.complaintview,name='complaintview'),
     
     path('public_enquiry/', views.public_enquiry, name='public_enquiry'),
     path('public_enquiryview/', views.enquiryview_public, name='public_enquiryview'),
     path('reply_add_public/<int:enquiry_id>/', views.reply_public_add, name='reply_add_public'),
     path('replyview_public/', views.replyview_public, name='replyview_public'),
     path('found_missing_add/', views.missing_found, name='found_missing_add'),
     path('found_view/', views.found_view, name='found_view'),
     path('find/<int:missing_person_id>/', views.find_missing_person, name='find_missing_person'),
     path('run_apriori_algorithm/', views.run_apriori_algorithm, name='run_apriori_algorithm'),
     path('error',views.run_apriori_algorithm,name='error')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
