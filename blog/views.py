from django.shortcuts import render

# Create your viewsdef post_list(request):
#return render(request, 'blog/post_list.html', {}) here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
