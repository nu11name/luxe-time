from .models import Category, Manufacturer, Type, SpecialOffer


def filter_context(request):
    return {
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'types': Type.objects.all(),
        'special_offers': SpecialOffer.objects.all()
    }
