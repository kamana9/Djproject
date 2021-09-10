from django.shortcuts import render
from .models import Blog 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView,LogoutView


# Create your views here.
class LoginView(LoginView):
    template_name='user/signin.html'
    fields='__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('user:index')



def index(request):
    return render(request,'user/index.html')

def nav(request):
    return render(request,'user/navigation.html')

class BlogList(ListView):
    model = Blog
    template_name='user/blog.html'
    context_object_name='blogs' 

class BlogDetail(DetailView):
    model = Blog
    template_name='user/detail.html'
    context_object_name='blog' 

class BlogCreate(CreateView):
    model = Blog
    fields ='__all__'
    success_url = reverse_lazy('index')

class BlogUpdate(UpdateView):
    model=Blog
    fields='__all__'
    success_url = reverse_lazy('blogs')

class BlogDelete(DeleteView):
    model=Blog
    fields='__all__'
    success_url = reverse_lazy('blogs')
    context_object_name='blog' 
    template_name='user/delete.html'





