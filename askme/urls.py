"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import logout
from django.conf import settings
from django.conf.urls.static import static

from app import views
from askme.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,  name="index"),
    path('hot/', views.hot, name="hot"),
    path('tags/<int:ind_que>/', views.tag, name="tag"),
    path('question/<int:ind_que>/', views.question, name="question"),
    # path('question/35', views.question, name="question"),
    path('login/', views.login_, name="login_"),
    path('signup/', views.signup, name="signup"),
    path('ask/', views.ask, name="ask"),
    path('settings/', views.settings, name="settings"),
    path('logout', include('django.contrib.auth.urls')),
    path('vote/', views.vote, name="vote"),
    path('correct_answer/', views.correct_answer, name="correct_answer"),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


