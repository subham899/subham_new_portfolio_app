from django.shortcuts import render,get_object_or_404
from .models import myblogmodels

def myblog_aplication(request):
    blogs = myblogmodels.objects.order_by('-date')[:4]
    return render(request, 'myblog_app/blog.html', {'blogs':blogs})


def blog_details(request,myblog_id):
    blog = get_object_or_404(myblogmodels, pk=myblog_id)
    return render(request, 'myblog_app/details.html', {'blog':blog})

