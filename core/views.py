from django.http import HttpResponse
from django.shortcuts import render
from core.models import (
    Category,
    Vendor,
    Product,
    ProductImages,
    CartOrder,
    CartOrderItems,
    ProductReview,
    Wishlist,
    Address,
)


def index(request):
    products = Product.objects.filter(
        product_status="published", featured=True
    ).order_by("-id")

    context = {
        "products": products
    }
    return render(request, "core/index.html", context)
