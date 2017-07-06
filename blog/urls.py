from django.conf.urls import url
from . import views
# Here we're importing Django's function url and all of our views from the blog application.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#this above menas we assign a view (called post_list) to the ^$ URL. The regex will mat ^(a beginning) followed by $ (an end).
#so, only an empty string will match.
# the name='post_list' is the name of the URL that will be used to identify the view
