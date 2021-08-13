from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms
from ckeditor.widgets import CKEditorWidget
from homepage.models import BlogPost

# Register your models here.
class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta: 
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    prepopulated_fields = {'title_slug': ('title',)}

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(get_user_model(), UserAdmin)