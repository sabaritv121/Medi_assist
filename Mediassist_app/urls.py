from django.urls import path

from Mediassist_app import views, user_views, admin_views, company_views
from Mediassist_app.admin_views import CompanyRegistrationView
from Mediassist_app.views import RegistrationView

urlpatterns = [
   # path("",views.Test,name='test'),
   # path("",views.landing_page,name="landing"),
   path('', RegistrationView.as_view(), name='registration'),
   path("login_page",views.login_page,name="login_page"),
   path("admin_base",views.admin_base,name="admin_base"),
   path("donator_home",views.donator_home,name="donator_home"),
   path("user_home",views.user_home,name="user_home"),

   path("logout_view/",views.logout_view,name='logout_view'),

   #user

   path("med_add",user_views.med_add,name="med_add"),
   path("med_view", user_views.med_view, name="med_view"),

   #admin

   path('CompanyRegistrationView', CompanyRegistrationView.as_view(), name='CompanyRegistrationView'),
   path('cmp_list',admin_views.cmp_list,name="cmp_list"),
   path('user_list',admin_views.user_list,name='user_list'),
   path("admin_approval",admin_views.admin_approval,name='admin_approval'),
   path('approve_donation/<int:id>/',admin_views.approve_donation, name='approve_donation'),
   path('reject_donation/<int:id>/',admin_views.reject_donation, name='reject_donation'),
   path("admin_approval",admin_views.admin_approval,name='admin_approval'),
   path('requests',admin_views.requests,name='requests'),

   #company
   path("med_view_cmp", company_views.med_view_cmp, name="med_view_cmp"),
   path('donate/<int:id>/', company_views.donate, name='donate'),

]