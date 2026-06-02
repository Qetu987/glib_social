from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.views import View
from posts.models import Post


class Post_list_base(View):
    anonimys = AnonymousUser()

    def redirect_to_login(self):
        if self.request.user == self.anonimys:
            return redirect('login')

    def get_user_data(self):
        if self.request.user != self.anonimys:
            return self.request.user

    def get_data(self):
        context = {
            'user_data': self.get_user_data(),
        }
        return context

    def get(self, request):
        self.redirect_to_login()
        context = self.get_data()
        return render(request, self.template_name, context)


class HomePage(Post_list_base):
    template_name = 'index.html'

    def get_data(self):
        context = super().get_data()

        post_list = Post.objects.filter(is_active=True, is_visible=True).order_by('-date')

        context.update({
            'post_list': post_list,
        })
