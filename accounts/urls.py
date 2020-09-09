from django.urls import path, include
from accounts.api import *
from knox import views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
    path('friend-request', send_friend_request, name="friend-request"),
    path('accept-friend-request', accept_friend_request, name="accept-friend-request"),
    path('friends-location-list', get_friends_locations_list, name="friends-locations-list")
]
