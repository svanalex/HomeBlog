from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request, 'blog/home.html')

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')  
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.view_count += 1
        post.save(update_fields=['view_count'])
        return post
    

class CreatePost(generic.CreateView):
    model = Post
    fields = ['title', 'body', 'category', 'tags', 'scheduled_publish', 'attachments']
    template_name = 'blog/post_form.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
