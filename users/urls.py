from django.urls import path 

from .views import ProfileEditView, ProfileView, SignupPageView, AddFollower, RemoveFollower
urlpatterns =[

    path('signup/', SignupPageView.as_view(), name='signup'),
    path('<slug>/', ProfileView.as_view(), name='profile'),
    path('edit/<slug>/', ProfileEditView.as_view(), name='profile_edit'),
    path('<slug>/followers/add', AddFollower.as_view(), name='add_follower'),
    path('<slug>/followers/remove', RemoveFollower.as_view(), name='remove_follower'),
    
]