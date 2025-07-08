from django.urls import path
from .views import item_list, item_detail  # for FBV
# or from .views import ItemList, ItemDetail  # for CBV

urlpatterns = [
    path('items/', item_list, name='item-list'),  # FBV
    path('items/<int:pk>/', item_detail, name='item-detail'),  # FBV
    
    # For CBV, use:
    # path('items/', ItemList.as_view(), name='item-list'),
    # path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
