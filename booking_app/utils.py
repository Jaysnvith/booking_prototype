from django.urls import reverse

def generate_breadcrumbs(request):
    breadcrumbs = []
    path_parts = request.path.strip('/').split('/')

    for i in range(len(path_parts)):
        name = path_parts[i].replace('-', ' ').capitalize()
        url = '/' + '/'.join(path_parts[:i + 1]) + '/'
        breadcrumbs.append((name, url))
    
    return breadcrumbs