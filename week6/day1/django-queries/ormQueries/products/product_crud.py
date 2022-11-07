from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length
from functools import reduce


class ProductCrud:

    @classmethod
    def get_all_products(cls):
        return Product.objects.all()


    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)


    @classmethod
    def last_record(cls):
        return Product.objects.last()


    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating=rating)


    @classmethod
    def by_rating_range(cls, beg, end):
        return Product.objects.filter(rating__range=(beg, end))


    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating), Q(color=color))


    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) | Q(color=color))


    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()


    @classmethod
    def below_price_or_above_rating(cls, below, above):
        return Product.objects.filter(Q(price_cents__lt=below) | Q(rating__gt=above))


    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by('category', '-price_cents')


    @classmethod
    def products_by_manufacturer_with_name_like(cls, pattern):
        return Product.objects.filter(manufacturer__contains=pattern)


    @classmethod
    def manufacturer_names_for_query(cls, match):

        # clauses = (Q(manufacturer__contains=manufacturer_name) for manufacturer_name in manufacturer_list)

        # for clause in clauses:
        #     print(clause)

        # return Product.objects.filter(reduce(operator.and_, clauses))

        return Product.objects.filter(manufacturer__contains=match).values_list('manufacturer', flat=True)


    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.filter(~Q(category=category))


    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        return Product.objects.filter(~Q(category=category))[:limit]


    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(Q(category=category)).values_list('manufacturer', flat=True)


    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(Q(category=category)).aggregate(rating__avg=Avg('rating'))


    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(price_cents__max=Max('price_cents'))


    @classmethod
    def longest_model_name(cls):
        return Product.objects.order_by(Length('model')).last().id


    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model')).values_list('id', flat=True)
