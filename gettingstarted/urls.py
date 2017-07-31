from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap
from hello import views


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [          url(r'^$', views.index, name="index"),
                       url(r'^home/', views.home, name="home"),
                       url(r'^about/', views.about, name="about"),
                        url(r'^admin/', admin.site.urls),
                       url(r'^portfolio/$', views.portfolio, name="portfolio"),
                       url(r'^contact/$', views.contact, name="contact"),
                       url(r'^resume/$', views.resume, name="resume"),
                       url(r'^tag/(?P<slug>[\w\-]+)/$', views.tagPostsPage, name='tag_posts_page'),

                       url(r'^blog/$', views.blog, name="blog"),
                       url(r'^blog/(?P<slug>[\w\-]+)/$', views.blogPage, name="blog_detail_page"),
                       url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                           name='django.contrib.sitemaps.views.sitemap'),
                       url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),  # noqa
                       url(r'^capy/$', TemplateView.as_view(template_name="capy.html")),  # noqa
                       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # noqa

urlpatterns += staticfiles_urlpatterns()
