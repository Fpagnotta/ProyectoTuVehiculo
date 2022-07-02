from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from profiles.models import profile 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


     



class edit_profile(LoginRequiredMixin,UpdateView):
    model = profile
    template_name = "edit_profile.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("index", kwargs= {"pk": self.object.pk})