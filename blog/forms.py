from django import forms
from .models import Post, Comment

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
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter post title'})
        self.fields['body'].widget.attrs.update({'placeholder': 'Write your post content here'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Select a category'})
        self.fields['tags'].widget.attrs.update({'placeholder': 'Add tags separated by commas'})
        self.fields['attachments'].widget.attrs.update({'multiple': True})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
        labels = {
            'content': 'Add a comment',
        }
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your comment here'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        