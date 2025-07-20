from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'tags', 'scheduled_publish', 'is_published', 'attachments']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'scheduled_publish': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Post Title',
            'body': 'Content',
            'category': 'Category (optional)',
            'tags': 'Tags (optional)',
            'scheduled_publish': 'Schedule Publish Date',
            'is_published': 'Publish Now',
            'attachments': 'Upload Attachments (optional)',
        }