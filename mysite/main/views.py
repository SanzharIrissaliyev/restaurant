from django.shortcuts import render
from main.models import *


# Create your views here.


def indexHandler(request):
    about = AboutUs.objects.all()
    welcome = Welcome.objects.all()
    products = Product.objects.all()
    category = Category.objects.all()
    offers = Product.objects.all().order_by('price')
    delicious = Product.objects.all().order_by('title')
    news = Product.objects.all().order_by('-category')[:3]
    gallery = Product.objects.all().order_by('category')
    contacts = Contact.objects.all()

    if request.POST:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        pochta = Feedback()
        name1 = Feedback.objects.filter(name=name)
        email1 = Feedback.objects.filter(email=email)
        message1 = Feedback.objects.filter(message=message)
        if not name1:
            pochta.name = name
            pochta.save()
        if not email1:
            pochta.email = email
            pochta.save()
        if not message1:
            pochta.message = message
            pochta.save()

    return render(request, 'index.html', {'about': about,
                                          'welcome': welcome,
                                          'products': products,
                                          'category': category,
                                          'offers': offers,
                                          'delicious': delicious,
                                          'news': news,
                                          'gallery': gallery,
                                          'contacts': contacts,

                                          })
