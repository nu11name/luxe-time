from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_en, name='index'),

    path('catalog/en', views.catalog_en, name='catalog'),
    path('catalog/brands/<slug>/en', views.catalog_brand, name='catalog-filter-brand'),
    path('catalog/filter/discount/en', views.catalog_discount, name='catalog-discount'),
    path('catalog/filter/category/<pk>/en', views.catalog_category, name='catalog-category'),
    path('catalog/filter/condition/<str:cond>/en', views.catalog_condition, name='catalog_condition'),
    path('catalog/filter/type/<slug>/en', views.catalog_type, name='catalog-type'),
    path('catalog/filter/price/en', views.catalog_price, name='catalog-price'),
    path('catalog/special-offers/<slug>/en', views.catalog_special_offers, name='special-offers'),

    path('catalog/<slug>/en', views.product_details_en, name='product-details'),

    path('about/en', views.about_en, name='about'),
    path('services/en', views.services_en, name='services'),
    path('contact/en', views.contact_en, name='contact'),


#####################################################################################################################


    path('ge', views.index_ge, name='index_ge'),

    path('catalog/ge', views.catalog_ge, name='catalog_ge'),
    path('catalog/brands/<slug>/ge', views.catalog_brand_ge, name='catalog-filter-brand_ge'),
    path('catalog/filter/discount/ge', views.catalog_discount_ge, name='catalog-discount_ge'),
    path('catalog/filter/category/<pk>/ge', views.catalog_category_ge, name='catalog-category_ge'),
    path('catalog/filter/condition/<str:cond>/ge', views.catalog_condition_ge, name='catalog_condition_ge'),
    path('catalog/filter/type/<slug>/ge', views.catalog_type_ge, name='catalog-type_ge'),
    path('catalog/filter/price/ge', views.catalog_price_ge, name='catalog-price_ge'),
    path('catalog/special-offers/<slug>/ge', views.catalog_special_offers_ge, name='special-offers_ge'),

    path('catalog/<slug>/ge', views.product_details_ge, name='product-details_ge'),

    path('about/ge', views.about_ge, name='about_ge'),
    path('services/ge', views.services_ge, name='services_ge'),
    path('contact/ge', views.contact_ge, name='contact_ge'),


#####################################################################################################################


    path('ru', views.index_ru, name='index_ru'),

    path('catalog/ru', views.catalog_ru, name='catalog_ru'),
    path('catalog/brands/<slug>/ru', views.catalog_brand_ru, name='catalog-filter-brand_ru'),
    path('catalog/filter/discount/ru', views.catalog_discount_ru, name='catalog-discount_ru'),
    path('catalog/filter/category/<pk>/ru', views.catalog_category_ru, name='catalog-category_ru'),
    path('catalog/filter/condition/<str:cond>/ru', views.catalog_condition_ru, name='catalog_condition_ru'),
    path('catalog/filter/type/<slug>/ru', views.catalog_type_ru, name='catalog-type_ru'),
    path('catalog/filter/price/ru', views.catalog_price_ru, name='catalog-price_ru'),
    path('catalog/special-offers/<slug>/ru', views.catalog_special_offers_ru, name='special-offers_ru'),

    path('catalog/<slug>/ru', views.product_details_ru, name='product-details_ru'),

    path('about/ru', views.about_ru, name='about_ru'),
    path('services/ru', views.services_ru, name='services_ru'),
    path('contact/ru', views.contact_ru, name='contact_ru'),





]
