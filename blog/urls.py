from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
        path('', views.index,  name='index'),
        path('user/login/', views.login,  name='login'),
        path('user/logout/', views.logout_view, name='logout'),
        path('contact/', views.contact, name='contact'),
        path('post/show/<int:post_id>/<post_slug>/', views.post_detail, name='post_detail'),

        path('warning/', views.response_check_upload_image, name='response_check_upload_image'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
