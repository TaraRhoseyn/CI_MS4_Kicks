from django.urls import path
from . import views

urlpatterns = [
     path('', views.show_all_products, name='products'),
     path('<product_id>', views.show_individual_product, name='individual_product'),
     path('add_review/<int:product_id>/', views.add_review,
         name="add_review"),
     path('edit_review/<int:review_id>/', views.edit_review,
         name="edit_review"),
     path('delete/review/<int:review_id>/', views.delete_review,
        name="delete_review"),
     path('add_product/', views.add_product, name='add_product'),
]
