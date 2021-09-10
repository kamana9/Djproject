from django.urls import path
from . import views
from .views import BlogList,BlogDetail,BlogCreate,BlogDelete,BlogUpdate,LoginView,LogoutView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('navi',views.nav,name="nav"),
    path('blog/',BlogList.as_view(),name='blogs'),
    path('detail/<int:pk>/',BlogDetail.as_view(),name='blogdetail'),
    path('create/',BlogCreate.as_view(),name='blogcreate'),
    path('remove/<int:pk>/',BlogDelete.as_view(),name='blogdelete'),
    path('edit/<int:pk>/',BlogUpdate.as_view(),name='update'),
    path('signin/',LoginView.as_view(),name='signin'),
    path('logout/',LogoutView.as_view(next_page='user:signin'),name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)