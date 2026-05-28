from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.views import View
from posts.models import Post

class HomePage(View):
    anonimys = AnonymousUser()

    def get(self, request):

        if request.user == self.anonimys:
            return redirect('login')


        post_list = Post.objects.filter(is_active=True, is_visible=True).order_by('-date')


        context = {
            'request': request,
            'post_list': post_list,
        }
        return render(request, 'base_1.html', context)
