from django.urls import path
from profiles.views import edit_profile


urlpatterns = [
    path('edit_profile/',edit_profile.as_view(),name = "edit_profile"),




] 