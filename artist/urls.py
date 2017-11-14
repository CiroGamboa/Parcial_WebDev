from django.conf.urls import url
from artist import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

	url(r'^$', views.imageView),
	url(r'^index$', views.finalView)
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)