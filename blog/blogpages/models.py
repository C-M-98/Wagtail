from django.db import models
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.
class BlogIndex(Page):
    template = 'blogpages/blog-index-page.html';
    
    subtitle = models.CharField(blank=True, max_length=100)
    body = RichTextField(blank=True, null=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]
    
class BlogDetail(Page):
    template = 'blogpages/blog-detail-page.html';
    
    subtitle = models.CharField(blank=True, max_length=100)
    body = RichTextField(blank=True, null=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]