from django.conf.urls import include,patterns,url
urlpatterns=patterns('',
url(r'^$','account.views.base',name='base'),

url(r'^main/$','account.views.main', name='main'),
url(r'^(?P<id>\d+)/editprofilepage/$','account.views.editProfilePage', name='editprofilepage'),
url(r'^(?P<id>\d+)/editprofile/$','account.views.editProfile', name='editprofile'),
url(r'^rlogin/$','account.views.renderLogin', name='rlogin'),
url(r'^rsignup/$','account.views.renderSignup', name='rsignup'),
url(r'^login/$','account.views.handleLogin', name='login'),
url(r'(?P<id>\d+)/account//follow/$','account.views.follow', name ='follow'),
url(r'(?P<id>\d+)/account//unfollow/$','account.views.unfollow', name ='unfollow'),
url(r'^signup/$','account.views.handleSignup', name='signup'),
url(r'^(?P<id>\d+)/$','account.views.profile', name='profile'),
url(r'^logout/$','account.views.logoutview', name='logout'),
)
