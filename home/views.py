from django.shortcuts import render
from django.views.decorators.cache import cache_page

from mysite.settings.base import SITE_VERSION


# 30 days cache, example using site version to invalidate cache (increment to
# invalidate)
@cache_page(60 * 60 * 24 * 30,
            key_prefix=SITE_VERSION)
def home(request):
    return render(request, 'home/home.html')
