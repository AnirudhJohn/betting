from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView

from users.models import Profile
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from .forms import CustomUserCreationForm


# Global Variable #
# is_following = False
##################

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(View):
    def get(self, request, slug, *args, **kwargs):
        profile = Profile.objects.get(slug=slug)
        user = profile.user
        posts = ShortStory.objects.filter(author=user).order_by('-created_on')
        
        
        followers = profile.followers.all()

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
        no_of_followers = len(followers)

        context = {
            'user' : user,
            'profile' : profile,
            'posts' : posts,
            'is_following': is_following,
            'no_of_followers' : no_of_followers,
        }

        return render(request, 'profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields =['name','location']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('profile', kwargs={'slug':slug})

    def test_func(self):
        profile = self.get_object()
        return  self.request.user == profile.user

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        profile = Profile.objects.get(slug=slug)

        profile.followers.add(request.user)

        return redirect('profile', slug=profile.slug)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        profile = Profile.objects.get(slug=slug)

        profile.followers.remove(request.user)

        return redirect('profile', slug=profile.slug)

