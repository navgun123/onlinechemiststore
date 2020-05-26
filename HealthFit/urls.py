"""HealthFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminRegisteration', adminRegisteration),
    path('adminLogin', adminLogin),
    path('adminlogout', adminlogout),
    path('adminview', adminview),
    path('alladmin', alladmin),
    path('adminChangePassword', adminChangePassword),
    path('adminUpdate', adminUpdate),
    path('adminDelete', adminDelete),
    path('addCategory', addCategory),
    path('showCategory', showCategory),
    path('categorydelete', categorydelete),
    path('updateCategorySave', updateCategorySave),
    path('addSubCategory', addSubCategory),
    path('viewcategory', viewcategory),
    path('viewcategory', viewcategory),
    path('subcategoryupdate', subcategoryupdate),
    path('showCatName', showCatName),
    path('deleteSubCategory', deleteSubCategory),
    path('showSubCategory', showSubCategory),
    path('addProduct', addProduct),
    path('viewallProduct', viewallProduct),
    path('showProduct', showProduct),
    path('deleteProduct', deleteProduct),
    path('updateProduct', updateProduct),
    path('filterSubCat', filterSubCat),
    path('',index),
    path('contact',contact),
    path('about',about),
    path('shop',shop),
    path('shopsingle',shopsingle),
    path('clientRegistration', clientRegistration),
    path('clientLogin', clientLogin),
    path('clientlogout', clientlogout),
    path('clientChangePassword', clientChangePassword),
    path('sessionProduct', sessionProduct),
    path('cart', cart),
    path('cardDelete',cardDelete),
    path('cartDetail',cartDetail),
    path('navcategory',navcategory),
    path('navstore',navstore),
    path('checkout',checkout),
    path('paymentBill',paymentBill),
    path('thanks',thanks),
    path('failedPayment',failedPayment),
    path('myorder',myorder),
    path('orderdetails',orderdetails),
    path('cientproductdetail',cientproductdetail),
    path('cancelledorder',cancelledorder),
    path('billdetails',billdetails),
    path('shipping',shipping),
    path('searchdata',searchdata),
    path('dispatched',dispatched),
    # path('searchName',searchName),
    path('searchmed',searchmed),
    path('chemistRegisteration',chemistRegisteration),
    path('chemistview',chemistview),
    path('deletechemist',deletechemist),
    path('chemistupdate',chemistupdate),
    path('chemistLogin',chemistLogin),
    path('allchemist',allchemist),
    path('chemistlogout',chemistlogout),
    path('chemistChangePassword',chemistChangePassword),
]
