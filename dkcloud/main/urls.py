from django.conf.urls import patterns, url, include
from django.contrib.auth.views import logout

from . import views

urlpatterns = patterns('',
    url(r'^$', views.MainPageView.as_view(), name='index'),
    url(r'^(?P<node_id>\d+)/$', views.NodeView.as_view(), name='nodeview'),
    url(r'login/$', views.login_main, name='login'),
    url(r'logout/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'password_change/$', views.password_change_main, name='password_change'),
    url(r'password_change_done/$', views.password_change_done_main,
        name='password_change_done'),
    url(r'contact/', include('contact.urls'), {
        'contact_template': 'main/user_form.html',
        'message_template': 'main/user_message.html',
        'mail_from': 'robomailer@dk-cloud.net',
        'mail_list': ['dkuntz417@gmail.com',],
        }),
)