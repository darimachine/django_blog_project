from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #login requred samo che se izpolzva za klas

# def home(request):
#     context={
#         'posts':Post.objects.all(),
#     }
#     return render(request,'blog/index.html',context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self): # smenq kakvo shte se returne
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView): # Pisheme LoginRequiredMixin ot nay lqvo na klasa
    model = Post
    fields = ['title','content']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author=self.request.user #dava usera koito e suzdal posta
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # Pisheme LoginRequiredMixin ot nay lqvo na klasa
    model = Post
    fields = ['title','content']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author=self.request.user #dava usera koito e suzdal posta
        return super().form_valid(form)
    def test_func(self): #izpolzva se za UserPassesTestMixin
        post = self.get_object() # vzima segashniq post koyto se opitvame da updatevame
        if self.request.user== post.author: # proverqva dali avtora na posta e segashniq user
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'
    def test_func(self): #izpolzva se za UserPassesTestMixin
        post = self.get_object() # vzima segashniq post koyto se opitvame da updatevame
        if self.request.user== post.author: # proverqva dali avtora na posta e segashniq user
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

