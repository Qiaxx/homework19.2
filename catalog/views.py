from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'name: {name}, phone: {phone}, message: {message}')

    return render(request, 'contacts.html')