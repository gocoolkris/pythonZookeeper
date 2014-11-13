from django.conf.urls import patterns
import views

urlpatterns = patterns('zapp.views',
    (r'^$',views.search),
#    (r'results.*$','results????')
)