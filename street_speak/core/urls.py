from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report'),
]

urlpatterns += [
    path('tokens/', views.token_history, name='token_history'),
]

urlpatterns += [
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

urlpatterns += [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)