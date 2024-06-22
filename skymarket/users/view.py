from django.urls import get_resolver
from django.http import HttpResponse


def debug_urls(request):
    url_patterns = get_resolver().reverse_dict.keys()
    return HttpResponse("<br>".join(str(p) for p in url_patterns))
