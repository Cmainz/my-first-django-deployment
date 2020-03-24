from django.urls import path, re_path
from basic_app.views import registration, user_login, index

app_name='basic_app'

urlpatterns=[
    re_path(r'^register/',registration, name='register'),
    re_path(r'^user_login', user_login, name='user_login'),
]
