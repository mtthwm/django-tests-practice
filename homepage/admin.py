from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from homepage.models import BlogPost, PostTag, PortfolioProject

# Register your models here.
class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta: 
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    prepopulated_fields = {'title_slug': ('title',)}

class UserAdmin(admin.ModelAdmin):
    pass

class PostTagAdmin(admin.ModelAdmin):
    pass

class PortfolioProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(get_user_model(), UserAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(PortfolioProject, PortfolioProjectAdmin)