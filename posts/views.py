from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.views import View
from posts.models import Post
from users.models import User


class Post_list_base(View):
    anonimys = AnonymousUser()

    def redirect_to_login(self):
        if self.request.user == self.anonimys:
            return redirect('login')

    def get_user_data(self):
        user = User.objects.filter(id=self.request.user.id).first()
        return user
        

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
    template_name = 'posts/home.html'
    page_title = 'Home page'

    def get_data(self):
        context = super().get_data()

        post_list = Post.objects.filter(is_active=True, is_visible=True).order_by('-date')

        context.update({
            'page_title': self.page_title,
            'post_list': post_list,
        })
        
        return context


class CreatePost(View):
    anonimys = AnonymousUser()
    template_name = 'create_post_old.html'
    page_title = 'Creating post'
    
    def get(self, request):
        context = {
            'page_title': self.page_title,
        }

        context = context
        return render(request, self.template_name, context)
    
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        poster = request.POST.get('poster')

        if not title:
            context = {
                'page_title': self.page_title,
                'errors': 'Немає Title'
            }
            return render(request, self.template_name, context)

        if request.user == self.anonimys:
            context = {
                'page_title': self.page_title,
                'errors': 'Треба авторизація'
            }
            return render(request, self.template_name, context)

        post = Post.objects.create(
            title = title, 
            description = description,
            poster = poster,
            owner = request.user
        )

        return redirect('home_page')