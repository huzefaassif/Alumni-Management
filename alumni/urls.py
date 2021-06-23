from django.urls import path,include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='alumni'),
    path('login_request/',views.login_request,name='login_request'),
    path('home/', views.home, name='home'),
    path('logout/' , views.logout_request, name='logout_request'),
    path('studentprofileupdate/', views.studentupdate, name='studentupdate'),
    path('alumniprofileupdate/', views.alumniupdate, name='alumniupdate'),
    path('searchalumni/', views.searchalumni, name='searchalumni'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('sprofileupdated/', views.studentprofileupdate, name='profileupdated'),
    path('aprofileupdated/', views.alumniprofileupdate, name='profileupdated'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('noofhits/', views.noofhits, name='noofhits'),
    path('cards/', views.cards, name='cards'),
    path('cardviewprofile/', views.cardviewprofile, name='cardviewprofile'),
    path('cardviewprofile2/', views.cardviewprofile2, name='cardviewprofile2'),
    path('branchfilter/', views.branchfilter, name='branchfilter'),
    path('companyfilter/', views.companyfilter, name='companyfilter'),
    path('viewblog/', views.viewblog, name='viewblog'),
    path('searchstudents/', views.searchstudents, name='searchstudents'),
    path('studentviewprofile/', views.studentviewprofile, name='studentviewprofile'),
    path('addchat/', views.addchat, name='addchat'),
    path('chats/', views.chats, name='chats'),
    path('signupstudent/', views.signupstudent, name='signupstudent'),
    path('signupalumni/', views.signupalumni, name='signupalumni'),
    path('signedupsuccessfully/', views.signedupsuccessfully, name='signedupsuccessfully'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/upload/', views.upload_blog, name='upload_blog'),
    path('blogs/<int:pk>/', views.delete_blog, name='delete_blog'),

    path('accounts/', include('django.contrib.auth.urls')),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)