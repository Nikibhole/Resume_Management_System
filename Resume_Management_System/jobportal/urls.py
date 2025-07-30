from django.urls import path
from .views import home1, register, custom_login, custom_logout, profilepage, jobs, applyjob, admindashboard, \
    update_status, my_applications, privacy_policy, faq, contact, about, logout_success, home2, home3, landing, \
    career_resources

urlpatterns = [
    path('', landing, name='landing'),
    path('home1/', home1, name='home'),
    path('home2/', home2, name='home2'),
    path('home3/', home3, name='home3'),
    path("register/", register, name='register'),
    path("login/", custom_login, name='login'),
    path("logout/", custom_logout, name='logout'),
    path("profile-page/", profilepage, name="profile-page"),
    path("jobs/", jobs, name="jobs"),
    path("apply/<int:id>/", applyjob, name="apply"),
    path("admin_dashboard", admindashboard, name="admin_dashboard"),
    path('update-status/<int:app_id>/', update_status, name='update_status'),
    path("my-applications/", my_applications, name="my_applications"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("faq/", faq, name="faq"),
    path("contact/", contact, name="contact"),
    path('about/', about, name='about'),
    path('logout/', custom_logout, name='logout'),
    path("logout-success/", logout_success, name="logout_success"),
    path('career-resources/', career_resources, name='career_resources'),

]
