from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f"{name} ({email})")
    return render(request, 'catalog/contact.html')
