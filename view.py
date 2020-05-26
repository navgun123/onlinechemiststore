from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from database import *
from database import mail,SMS
from django.core.files.storage import FileSystemStorage
from random import randint
from datetime import *
import http.client
import smtplib


@csrf_exempt
def adminRegisteration(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['passw']
            fullname = request.POST['fname']
            mobile = request.POST['mobile']
            if email and password and fullname and mobile and ('@' in email) and (
                    str(mobile).isnumeric() == True) and str(
                fullname).isnumeric() == False:
                s = 'insert into adminregistration values ("{}","{}","{}","{}")'.format(email, password, fullname,
                                                                                        mobile)

                result = Insert(s)
                if result == 'success':
                    return render(request, 'adminHome.html', {'message': 'Admin Added SuccessFully'})
                else:
                    return render(request, 'adminRegistration.html',
                                  {'title': 'Admin Registration', 'message': 'Admin Already Exist'})
            else:
                return render(request, 'adminRegistration.html',
                              {'title': 'Admin Registration', 'message': 'Data is not valid'})
        return render(request, 'adminRegistration.html', {'title': 'Admin Registration'})
    else:
        return redirect(adminLogin)


def adminDelete(request):
    s = 'delete from adminregistration where email="{}"'.format(request.GET['email'])
    result = Delete(s)
    return HttpResponse(result)


@csrf_exempt
def adminUpdate(request):
    if 'admin' in request.session:
        email = request.POST['email']
        # password = request.POST['passw']
        fullname = request.POST['fname']
        mobile = request.POST['mobile']
        if fullname and mobile and ('@' in email) and (str(mobile).isnumeric() == True) and str(
                fullname).isnumeric() == False:
            s = 'update adminregistration set fullname="{}",mobile="{}" where email="{}"'.format(fullname, mobile,
                                                                                                 email)
            print(s)
            result = Update(s)
            return HttpResponse(result)
    else:
        return redirect(adminLogin)


def adminview(request):
    if 'admin' in request.session:
        s = 'select * from adminregistration'
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result:
            d = {}
            d['srno'] = count
            d['email'] = i[0]
            d['password'] = i[1]
            d['fullname'] = i[2]
            d['mobile'] = i[3]
            count += 1
            lt.append(d)
        return render(request, 'adminview.html', {'context': lt})
    return redirect(adminLogin)


def adminLogin(request):
    if 'admin' in request.session:
        return redirect(alladmin)
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select email,password from adminregistration where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result != None:
                request.session['admin'] = {'adminEmail': request.POST['email']}
                return redirect(alladmin)
            else:
                return render(request, 'adminLogin.html',
                              {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
        else:
            return render(request, 'adminLogin.html',
                          {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
    request.session.flush()
    return render(request, 'adminLogin.html', {'title': 'Admin Login'})


def adminChangePassword(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            s = 'select password from adminregistration where email="{}"'.format(request.session['admin']['adminEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                u = 'update adminregistration set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                                         request.session['admin'][
                                                                                             'adminEmail'])
                result = Update(u)
                if result == 'success':
                    return render(request, 'adminHome.html', {'message': 'Password updated successfully'})
            else:
                return render(request, 'adminHome.html', {'message': 'Wrong Password'})
        return redirect(alladmin)
    else:
        return redirect(adminLogin)


def alladmin(request):
    if 'admin' in request.session:
        return render(request, 'adminHome.html')
    else:
        return redirect(adminLogin)


def adminlogout(request):
    if 'admin' in request.session:
        request.session['admin'] = ''
        del request.session['admin']
    return redirect(adminLogin)


def addCategory(request):
    if 'admin' in request.session:
        if request.method == "POST":
            if request.POST['catname'] and str(request.POST['catname']).isnumeric() == False and request.POST[
                'catdesp'] and str(request.POST['catdesp']).isnumeric() == False:
                s = 'insert into category values (null,"{}","{}")'.format(request.POST['catname'],
                                                                          request.POST['catdesp'])
                result = Insert(s)
                if result:
                    return redirect(showCategory)
                else:
                    return render(request, 'addCategory.html',
                                  {'title': 'Add Category', 'message': 'Please Enter Valid Data'})
            else:
                return render(request, 'addCategory.html',
                              {'title': 'Add Category', 'message': 'Please Enter Valid Data'})
        return render(request, 'addCategory.html', {'title': 'Add Category'})
    else:
        return redirect(adminLogin)


def showCategory(request):
    if 'admin' in request.session:
        s = 'select catName,catid,catDescp from category'
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result:
            d = {}
            d['catName'] = i[0]
            d['catid'] = i[1]
            d['catDescp'] = i[2]
            d['srno'] = count
            count += 1
            lt.append(d)
        return render(request, 'viewcategory.html', {'title': 'View Category', 'context': lt})
    else:
        return redirect(adminLogin)


def categorydelete(request):
    if 'admin' in request.session:
        s = 'delete from category where catid="{}"'.format(request.GET['delete'])
        result = Delete(s)
        return HttpResponse(result)
    else:
        return redirect(adminLogin)


@csrf_exempt
def updateCategorySave(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            if request.POST['up_catname'] and str(request.POST['up_catname']) and request.POST['catDescp'] and str(
                    request.POST['catDescp']):
                u = 'update category set catName="{}", catDescp="{}" where catid="{}"'.format(
                    request.POST['up_catname'],
                    request.POST['catDescp'],
                    request.POST['catid'])
                result = Update(u)
                return HttpResponse(result)
    else:
        return redirect(adminLogin)


def addSubCategory(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            if request.POST['catname'] and request.POST['subcatname'] and request.POST['subDescription'] and str(
                    request.POST['subcatname']).isnumeric() == False and str(
                request.POST['subDescription']).isnumeric() == False:
                s = 'insert into subcategory values(null,"{}","{}","{}")'.format(request.POST['subcatname'],
                                                                                 request.POST['subDescription'],
                                                                                 request.POST['catname'])
                # print(s)
                result = Insert(s)
                if result == 'success':
                    return redirect(viewcategory)
            else:
                return render(request, 'addSubCategory.html', {'title': 'Sub-Category', 'message': 'Data is not Valid'})
        return render(request, 'addSubCategory.html', {'title': 'Sub-Category'})
    else:
        return redirect(adminLogin)


def viewcategory(request):
    if 'admin' in request.session:
        return render(request, 'showSubCategory.html', {'title': 'View Category'})
    else:
        return redirect(adminLogin)


@csrf_exempt
def deleteSubCategory(request):
    if 'admin' in request.session:
        s = 'delete from subcategory where subid="{}"'.format(request.GET['delete'])
        result = Delete(s)
        return HttpResponse(result)
    else:
        return redirect(adminLogin)


@csrf_exempt
def subcategoryupdate(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            if request.POST['subname'] and request.POST['subDescription'] and str(
                    request.POST['subname']).isnumeric() == False and str(
                request.POST['subDescription']).isnumeric() == False:
                s = 'update subcategory set subname="{}",subDescription="{}" where subid="{}"'.format(
                    request.POST['subname'],
                    request.POST['subDescription'],
                    request.POST['subid'])
                # print(s)
                result = Update(s)
                return HttpResponse(result)
    else:
        return redirect(adminLogin)


@csrf_exempt
def showCatName(request):
    if 'chemist' in request.session:
        s = 'select catName,catid from category'
        result = Fetchall(s)
        lt = []
        for i in result:
            d = {'catName': i[0], 'catid': i[1]}
            lt.append(d)
        return JsonResponse(lt, safe=False)
    else:
        return redirect(adminLogin)


def showSubCategory(request):
    if 'admin' in request.session:
        search = request.GET['search']
        if search == "main":
            s = "select subname,subDescription,subid,catid from subcategory"
        else:
            s = 'select subname,subDescription,subid,catid from subcategory where catid="{}"'.format(search)
        # print(s)
        result = Fetchall(s)
        # print(result)
        # print(result)
        lt = []
        for i in result:
            d = {}
            d['subname'] = i[0]
            d['subdesc'] = i[1]
            d['subid'] = i[2]
            d['catid'] = i[3]
            lt.append(d)
        return JsonResponse(lt, safe=False)
    else:
        return redirect(adminLogin)


@csrf_exempt
def addProduct(request):
    if 'chemist' in request.session:
        if request.method == 'POST':
            pic_name = str(randint(1, 10000)) + request.FILES['photo'].name
            if request.POST['catname'] and request.POST['pprice'] and request.POST[
                'subcatname'] and request.POST[
                'pname'] and request.POST['pdesc'] and request.POST['sprice'] and str(
                request.POST['pname']).isnumeric() == False and str(request.POST['pdesc']).isnumeric() == False and str(
                request.POST['sprice']).isnumeric() == True and str(
                request.POST['pprice']).isnumeric() == True:
                s = 'insert into product values(null,"{}","{}","{}","{}","{}","{}","{}","{}")'.format(request.POST['pname'],
                                                                                                 request.POST['pprice'],
                                                                                                 request.POST['sprice'],
                                                                                                 request.POST[
                                                                                                     'pdiscount'],
                                                                                                 request.POST['pdesc'],
                                                                                                 pic_name,
                                                                                                 request.POST[
                                                                                                     'subcatname'],
                                                                                                      request.session['chemist']['chemistEmail'])
                result = Insert(s)
                if result == 'success':
                    f = FileSystemStorage()
                    f.save(pic_name, request.FILES['photo'])
                    return redirect(viewallProduct)
            else:
                return render(request, 'addProduct.html',
                              {'message': 'Please enter Valid Data'})
        return render(request, 'addProduct.html')
    else:
        return redirect(chemistLogin)


def viewallProduct(request):
    if 'chemist' in request.session:
        return render(request, 'viewallProduct.html')
    else:
        return redirect(chemistLogin)


def deleteProduct(request):
    if 'chemist' in request.session:
        s = 'delete from product where pid="{}"'.format(request.GET['pid'])
        result = Delete(s)
        return HttpResponse(result)
    else:
        return redirect(adminLogin)


def filterSubCat(request):
    if 'chemist' in request.session:
        s = 'select subname,subDescription,subid from subcategory where catid="{}"'.format(request.GET['cat'])
        # print(s)
        result = Fetchall(s)
        lt = []
        for i in result:
            d = {'subname': i[0], 'subdesc': i[1], 'subid': i[2]}
            lt.append(d)
        return JsonResponse(lt, safe=False)
    else:
        return redirect(adminLogin)


def showProduct(request):
    search = request.GET['search']
    if search == "main":
        s = "select * from product where chemistemail='{}'".format(request.session['chemist']['chemistEmail'])
    else:
        s = 'select * from product where subid="{}" and chemistemail="{}"'.format(search,request.session['chemist']['chemistEmail'])
    result = Fetchall(s)
    lt = []
    count = 1
    for i in result[::-1]:
        d = {}
        d['srno'] = count
        d['pid'] = i[0]
        d['productname'] = i[1]
        d['productprice'] = i[2]
        d['productstock'] = i[3]
        d['productdiscount'] = i[4]
        d['productdesc'] = i[5]
        d['productimage'] = i[6]
        d['subid'] = i[7]
        count += 1
        lt.append(d)
    return JsonResponse(lt, safe=False)


@csrf_exempt
def updateProduct(request):
    if 'chemist' in request.session:
        # file = ''
        try:
            file = request.FILES['file']
            fs = FileSystemStorage()
            pic_name = str(randint(1, 10000)) + request.FILES['file'].name
            s = 'update product set productname="{}",productprice="{}",productstock="{}",productdiscount="{}",productdesc="{}",productimage="{}" where pid="{}"'.format(
                request.POST['pname'], request.POST['pprice'], request.POST['sprice'], request.POST['pdiscount'],
                request.POST['pdesc'], pic_name, request.POST['pid'])
            # print(s)
            result = Update(s)
            if result == 'success':
                fs.save(pic_name, file)
        except Exception as e:
            s = 'update product set productname="{}",productprice="{}",productstock="{}",productdiscount="{}",productdesc="{}" where pid="{}"'.format(
                request.POST['pname'], request.POST['pprice'], request.POST['sprice'], request.POST['pdiscount'],
                request.POST['pdesc'], request.POST['pid'])
            # print(s)
            result = Update(s)
        return HttpResponse(result)
    else:
        return redirect(adminLogin)


# ----------------- Admin Work Done ---------------
def index(request):
    s = "select * from product limit 0,15"
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['pid'] = i[0]
        d['productname'] = i[1]
        d['productprice'] = i[2]
        d['productstock'] = i[3]
        d['productdiscount'] = i[4]
        d['productdesc'] = i[5]
        d['productimage'] = i[6]
        d['subid'] = i[7]
        d['discountedprice'] = round(i[2] - (i[2] * i[4]) / 100, 2)
        lt.append(d)
    return render(request, 'index.html', {'context': lt})


def navcategory(request):
    r = 'select catid,catName from category'
    resultd = Fetchall(r)
    ltd = []
    for j in resultd:
        l = {}
        l['catname'] = j[1]
        p = 'select subid,subname from subcategory where catid="{}"'.format(j[0])
        resultfgh = Fetchall(p)
        lts = []
        for k in resultfgh:
            m = {}
            m['subid'] = k[0]
            m['subname'] = k[1]
            lts.append(m)
        l['sub'] = lts
        ltd.append(l)
    # print(ltd)
    return JsonResponse(ltd, safe=False)


def shop(request):
    filter = "All"
    try:
        s = 'select * from product where productname like "{}"'.format("%" + request.GET['search'] + "%")
        filter = ''
    except:
        try:
            s = 'select * from product where subid="{}"'.format(request.GET['subid'])
            filter = ''
        except:
            try:
                sort = request.GET['sort']
                if sort == 'a-z':
                    s = 'select * from product order by productname ASC'
                    filter = 'A-Z'
                elif sort == 'z-a':
                    s = 'select * from product order by productname DESC'
                    filter = 'Z-A'
                elif sort == 'low-high':
                    s = 'select * from product order by productprice ASC'
                    filter = 'Price Low-High'
                elif sort == 'high-low':
                    s = 'select * from product order by productprice DESC'
                    filter = 'Price High-Low'
            except:
                try:
                    load = request.GET['load']
                    if load == '50':
                        s = 'select * from product where productdiscount between 0 and 50'
                        filter = 'Discount 50%'
                except:
                    try:
                        s = 'select * from product where chemistemail="{}"'.format(request.GET['storeemail'])
                        filter = 'Store'
                    except:
                        s = 'select * from product'
                        filter = ''
    result = Fetchall(s)
    lt = []
    if result != ():
        for i in result:
            d = {}
            d['pid'] = i[0]
            d['productname'] = i[1]
            d['productprice'] = i[2]
            d['productstock'] = i[3]
            d['productdiscount'] = i[4]
            d['productdesc'] = i[5]
            d['productimage'] = i[6]
            d['subid'] = i[7]
            d['discountedprice'] = round(i[2] - (i[2] * i[4]) / 100, 2)
            lt.append(d)
        return render(request, 'shop.html', {'context': lt, 'filter': filter})
    else:
        return render(request, 'shop.html', {'message': 'No result found'})


def shopsingle(request):
    s = 'select * from product where pid="{}"'.format(request.GET['pid'])
    result = Fetchone(s)
    d = {}
    if 'product' in request.session:
        for i in request.session['product']:
            if str(request.GET['pid']) == str(i[0]):
                qty = i[7]
                break
        else:
            qty = 1
    else:
        qty = 1
    d['qty'] = qty
    d['pid'] = result[0]
    d['productname'] = result[1]
    d['productprice'] = result[2]
    d['productstock'] = result[3]
    d['productdiscount'] = result[4]
    d['productdesc'] = result[5]
    d['productimage'] = result[6]
    d['subid'] = result[7]
    d['discountedprice'] = round(result[2] - (result[2] * result[4]) / 100, 2)
    d['savemoney'] = round(result[2] * result[4] / 100, 2)
    return render(request, 'shop-single.html', {'i': d})


def contact(request):
    if request.method == 'POST':
        fullname = request.POST['first_name']
        lastname = request.POST['last_name']
        email_address = request.POST['email_address']
        contact_subject = request.POST['contact_subject']
        message = request.POST['message']
        msg = "name: " + fullname + " " + lastname + "\n\n" + "subject: " + contact_subject + "\n\n" + "message: " + message
        mail.send_Mail(email_address,msg)
        return render(request, 'contact.html',{'message':'Message Sended Successfully'})
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def checkout(request):
    if 'product' in request.session and len(request.session['product']) > 0:
        grandtotal = 0
        for i in list(request.session['product']):
            grandtotal += i[8]
        return render(request, 'checkout.html', {'grandtotal': int(grandtotal)})
    return redirect(index)


def clientLogin(request):
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select email,password,mobile,fullname from clientregistration where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result != None:
                request.session['client'] = {'clientEmail': request.POST['email'], "clientPhone": result[2],
                                             "clientName": result[3]}
                return redirect(index)
            else:
                return render(request, 'loginregister.html',
                              {'message': 'Email and Password is not correct'})
        else:
            return render(request, 'loginregister.html',
                          {'message': 'Email and Password is not correct'})
    return render(request, 'loginregister.html')


@csrf_exempt
def clientRegistration(request):
    request.session.flush()
    if request.method == 'POST':
        email = request.POST['clientemail']
        password = request.POST['cpassw']
        fullname = request.POST['fname']
        mobile = request.POST['mobile']
        if email and password and fullname and mobile and ('@' in email) and (str(mobile).isnumeric() == True):
            s = 'insert into clientregistration values ("{}","{}","{}","{}")'.format(email, password, fullname, mobile)
            result = Insert(s)
            return render(request, 'loginregister.html', {'message': 'Registration Successfull and Login Please'})
        else:
            return render(request, 'loginregister.html', {'message': 'Data is not correct'})
    return render(request, 'loginregister.html')


def clientlogout(request):
    if 'client' in request.session:
        request.session['client'] == ''
        del request.session['client']
        return redirect(index)
    else:
        return redirect(index)


def clientChangePassword(request):
    if 'client' in request.session:
        if request.method == 'POST':
            s = 'select password from clientregistration where email="{}"'.format(
                request.session['client']['clientEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                if request.POST['cpassw'] == request.POST['npassw']:
                    u = 'update clientregistration set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                                              request.session['client'][
                                                                                                  'clientEmail'])
                    result = Update(u)
                    if result == 'success':
                        request.session.client = ''
                        request.session.flush()
                        return render(request, 'loginregister.html',
                                      {'message': 'Password Has Changed Successfully. Please Login Again'})
                else:
                    return render(request, 'clientChangePassword.html', {'message': 'Password Does not Match'})
            else:
                return render(request, 'clientChangePassword.html', {'message': 'Wrong Password.'})
        return render(request, 'clientChangePassword.html')
    else:
        return render(request, 'loginregister.html', {'message': 'You need To login First'})


def sessionProduct(request):
    s = 'select pid,productname,productprice,productstock,productdiscount,productdesc,productimage from product where pid="{}"'.format(
        request.GET['q'])
    result = Fetchone(s)
    if 'product' in request.session:
        lt = list(request.session['product'])
        for i in lt:
            if str(i[0]) == str(request.GET['q']):
                try:
                    qty = request.GET['qty']
                    i[7] = int(qty)
                    i[8] = round((i[2] - (i[2] * i[4]) / 100) * i[7], 2)
                    i[9] = round(i[2] - (i[2] * i[4]) / 100, 2)
                    request.session['product'] = lt
                    break
                except:
                    i[7] += int(1)
                    i[8] = round((i[2] - (i[2] * i[4]) / 100) * i[7], 2)
                    i[9] = round(i[2] - (i[2] * i[4]) / 100, 2)
                    request.session['product'] = lt
                    break
        else:
            try:
                qty = request.GET['qty']
                d = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], qty,
                     round((result[2] - (result[2] * result[4]) / 100) * 1, 2),
                     round(result[2] - (result[2] * result[4]) / 100, 2)]
                lt.append(d)
                request.session['product'] = lt
            except:
                d = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], 1,
                     round((result[2] - (result[2] * result[4]) / 100) * 1, 2),
                     round(result[2] - (result[2] * result[4]) / 100, 2)]
                lt.append(d)
                request.session['product'] = lt
    else:
        lt = []
        try:
            qty=request.GET['qty']
        except:
            qty=1
        d = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], int(qty),
             round((result[2] - (result[2] * result[4]) / 100) * int(qty), 2),
             round(result[2] - (result[2] * result[4]) / 100, 2)]
        lt.append(d)
        request.session['product'] = lt
    # print(request.session['product'])
    return HttpResponse(len(lt))


def cart(request):
    if 'product' in request.session and len(request.session['product']) > 0:
        grandtotal = 0
        for i in list(request.session['product']):
            grandtotal += i[8]
        return render(request, 'cart.html', {'grandtotal': round(grandtotal, 2)})
    return redirect(index)


def cardDelete(request):
    pid = request.GET['pid']
    lb = request.session['product']
    k = 0
    for i in lb:
        if str(i[0]) == str(pid):
            del lb[k]
            break
        k += 1
    request.session['product'] = lb
    return redirect(cart)


def cartDetail(request):
    data = request.GET['qty']
    q = str(request.GET['q'])
    grandtotal = 0
    qty = 0
    nettotal = 0
    if 'product' in request.session:
        lt = list(request.session['product'])
        for i in lt:
            if str(i[0]) == q:
                i[7] += int(data)
                qty = i[7]
                i[8] = round((i[2] - (i[2] * i[4]) / 100) * i[7], 2)
                i[9] = round(i[2] - (i[2] * i[4]) / 100, 2)
                nettotal = i[8]
                request.session['product'] = lt
                break
        for j in lt:
            grandtotal += j[8]
    lts = [{'qty': qty, 'nettotal': nettotal, 'grandtotal': round(grandtotal, 2)}]
    return JsonResponse(lts, safe=False)


@csrf_exempt
def paymentBill(request):
    result3 = ""
    msg = ""
    if request.method == "POST":
        streetAddress = request.POST['streetAddress']
        town = request.POST['town']
        zipcode = request.POST['zipcode']
        ordernote = request.POST['ordernote']
        grandtotal = request.POST['grandtotal']
        paymentmethod = request.POST['paymentmethod']
        print(paymentmethod)
        if streetAddress and town and zipcode and str(zipcode).isnumeric() == True and str(town) != '#':
            s = 'insert into bill (billID,datatime,grandtotal,payment_method,city,zipcode,address,remarks,email,status) values (null,"{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                datetime.today().now(),
                grandtotal,
                paymentmethod, town,
                zipcode, streetAddress,
                ordernote, str(request.session['client']['clientEmail']), 'pending')
            print(s)
            result = Insert(s)
            print(result)
            if result == 'success':
                s1 = 'select billID,datatime from bill order by billID DESC'
                result1 = Fetchone(s1)
                print(result1[0])
                msg = "Dear " + str(request.session['client'][
                                        'clientName']) + ",\nThank you for Shopping with us.\n Order No. " + str(
                    result1[
                        0]) + "\n Order Date/Time " + str(result1[1]) + "\n"
                lb = list(request.session['product'])
                print(lb)
                for i in lb:
                    s2 = 'insert into billdetail values (null,"{}","{}","{}","{}")'.format(i[8], i[7], i[0], result1[0])
                    result2 = Insert(s2)
                    print(result2)
                    b = 'select productname from product where pid="{}"'.format(i[0])
                    rest = Fetchone(b)
                    msg += str(rest[0]) + "( " + str(int(i[2]) - int((int(i[2]) * int(i[7]) / 100))) + " X " + str(
                        i[7]) + " ) = " + str(i[8]) + "\n"
                    if result2 == 'success':
                        u = 'update product set productstock="{}" where pid="{}"'.format(str(int(i[3]) - int(i[7])),
                                                                                         str(i[0]))
                        result3 = Update(u)
        else:
            return render(request, 'checkout.html', {'message': 'Data not Valid'})
        if result3 == 'success':
            msg += 'Total Amount = ' + str(grandtotal)
            # print(msg)
            # msg = msg.replace(" ", "%20")
            try:
                mail.send_Mail(request.session['client']['clientEmail'],msg)
            except:
                return redirect(failedPayment)
            # return HttpResponse(s)
            print(result3)
            request.session['product'] = ''
            del request.session['product']
            return HttpResponse(result1[0])
        else:
            return redirect(failedPayment)
    return redirect(checkout)


def thanks(request):
    if 'client' in request.session:
        return render(request, 'thankyou.html', {'orderid': request.GET['orderid']})
    else:
        return redirect(index)


def failedPayment(request):
    if 'product' in request.session:
        return render(request, 'failedPayment.html')
    else:
        return redirect(index)


def myorder(request):
    if 'client' in request.session:
        s = 'select * from bill where email="' + request.session['client']['clientEmail'] + '"'
        print(s)
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result[::-1]:
            d = {}
            d['srno'] = count
            d['billid'] = i[0]
            d['billtime'] = i[1]
            d['grandtotal'] = i[2]
            d['paymentmethod'] = i[3]
            d['address'] = i[6]
            d['status'] = i[12]
            lt.append(d)
            count += 1
        return render(request, 'myaccount.html', {'context': lt})
    else:
        return redirect(index)


def cientproductdetail(request):
    h = 'select * from bill where billid="{}"'.format(request.GET['billid'])
    print(h)
    result1 = Fetchone(h)
    # lt = []
    k = {}
    # k['srno'] = count1
    k['billid'] = result1[0]
    k['billtime'] = result1[1]
    k['grandtotal'] = result1[2]
    k['paymentmethod'] = result1[3]
    k['city'] = result1[4]
    k['zipcode'] = result1[5]
    k['address'] = result1[6]
    k['status'] = result1[12]
    print(k)

    s = 'select * from billdetail where billid="{}"'.format(request.GET['billid'])
    result = Fetchall(s)
    lt = []
    count = 1
    for i in result:
        d = {}
        d['srno'] = count
        d['price'] = i[1]
        d['quantity'] = i[2]
        p = 'select productname,productprice,productdiscount,productimage from product where pid="{}"'.format(i[3])
        result1 = Fetchone(p)
        d['product'] = [result1[0], result1[1], result1[2], result1[3]]
        lt.append(d)
        count += 1
    return render(request, 'myaccountdetail.html', {'context': lt, 'i': k})


def cancelledorder(request):
    result3 = ""
    s = 'update bill set status="cancelled",cancelledremarks="{}" where billID="{}"'.format(str(request.GET['remarks']),
                                                                                            request.GET['billid'])
    result = Update(s)
    # print(result)
    p = 'select quantity,productid from billdetail where billid="{}"'.format(request.GET['billid'])
    result1 = Fetchall(p)
    # print(result1)
    for i in result1:
        f = 'select productstock from product where pid="{}"'.format(i[1])
        result2 = Fetchone(f)
        # print('result2', result2)
        u = 'update product set productstock="{}" where pid="{}"'.format(int(result2[0]) + int(i[0]), i[1])
        result3 = Update(u)
        # print('result3', result3)
    return HttpResponse(result3)


def orderdetails(request):
    search = request.GET['search']
    if search == 'all':
        s = 'select * from bill'
    else:
        s = 'select * from bill where status="{}"'.format(search)
    result = Fetchall(s)
    lt = []
    count = 1
    for i in result[::-1]:
        d = {}
        d['srno'] = count
        d['orderno'] = i[0]
        d['datatime'] = i[1]
        d['grandtotal'] = i[2]
        d['paymentmethod'] = i[3]
        d['useremail'] = i[11]
        f = 'select fullname,mobile from clientregistration where email="{}"'.format(i[11])
        result2 = Fetchone(f)
        d['userdetails'] = [result2[0], result2[1]]
        d['status'] = i[12]
        p = 'select mobile from clientregistration where email="{}"'.format(i[11])
        result1 = Fetchone(p)
        d['phone'] = result1[0]
        count += 1
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


def billdetails(request):
    s = 'select * from billdetail where billid="{}"'.format(request.GET['billid'])
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['price'] = i[1]
        d['quantity'] = i[2]
        s1 = 'select productname,productimage,pid from product where pid="{}"'.format(i[3])
        result1 = Fetchone(s1)
        d['product'] = [result1[0], result1[1], result1[2]]
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


@csrf_exempt
def shipping(request):
    if request.method == 'POST':
        if request.POST['trackingid'] and request.POST['companyname'] and request.POST['trackingurl'] and request.POST[
            'email'] and str(request.POST['trackingid']).isnumeric() == True and str(
            request.POST['companyname']).isnumeric() == False:
            s = 'update bill set trackid="{}", companyname="{}", trackurl="{}", status="Shipped", remarks="{}" where email="{}" and status!="cancelled"'.format(
                request.POST['trackingid'], request.POST['companyname'], request.POST['trackingurl'],
                request.POST['remark'], request.POST['email'])
            result1 = Update(s)
            if result1 == 'success':
                mobile = request.POST["phone"]
                # print('test', mobile)
                msg = "Your Package has been Shipped. And Your Tracking ID is: " + request.POST['trackingid']
                print(msg)
                msg = msg.replace(" ", "%20")
                conn = http.client.HTTPConnection("server1.vmm.education")
                conn.request('GET',
                             '/VMMCloudMessaging/AWS_SMS_Sender?username=djangoJan2020&password=QZLIU7IH&message=' + msg + '&phone_numbers=' + str(
                                 mobile))
                response = conn.getresponse()
                print(response)
            return HttpResponse(s)
        else:
            return HttpResponse('Data not valid')


@csrf_exempt
def dispatched(request):
    if request.method == 'POST':
        if request.POST['disemail'] and request.POST['personrecieved'] and str(
                request.POST['personrecieved']).isnumeric() == False:
            s = 'update bill set status="Dispatched", personrecieved="{}" where email="{}" and status!="cancelled"'.format(
                request.POST['personrecieved'], request.POST['disemail'])
            result1 = Update(s)
            if result1 == 'success':
                mobile = request.POST["disphone"]
                print('test', mobile)
                msg = "Thank You For Shopping With us. Your Package has been dispatched"
                print(msg)
                msg = msg.replace(" ", "%20")
                conn = http.client.HTTPConnection("server1.vmm.education")
                conn.request('GET',
                             '/VMMCloudMessaging/AWS_SMS_Sender?username=djangoJan2020&password=QZLIU7IH&message=' + msg + '&phone_numbers=' + str(
                                 mobile))
                response = conn.getresponse()
                print(response)
            return HttpResponse(s)
        else:
            return HttpResponse('Data not valid')


def searchdata(request):
    datafrom = request.GET['datafrom']
    datato = request.GET['dateto']
    status = str(request.GET['status'])
    print(status, type(status))
    if status == 'all':
        s = 'SELECT * FROM bill WHERE datatime BETWEEN "{}" AND "{}"'.format(datafrom, datato)
    else:
        s = 'SELECT * FROM bill WHERE datatime BETWEEN "{}" AND "{}" and status="{}"'.format(datafrom, datato, status)
    # print(s)
    result = Fetchall(s)
    # print("result",list(result))
    lt = []
    count = 1
    for i in result[::-1]:
        d = {}
        d['srno'] = count
        d['orderno'] = i[0]
        d['datatime'] = i[1]
        d['grandtotal'] = i[2]
        d['paymentmethod'] = i[3]
        d['useremail'] = i[11]
        f = 'select fullname,mobile from clientregistration where email="{}"'.format(i[11])
        result2 = Fetchone(f)
        d['userdetails'] = [result2[0], result2[1]]
        d['useremail'] = i[11]
        d['status'] = i[12]
        p = 'select mobile from clientregistration where email="{}"'.format(i[11])
        result1 = Fetchone(p)
        d['phone'] = result1[0]
        count += 1
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


def searchmed(request):
    s = 'select productname from product'
    result = Fetchall(s)
    lt = []
    for i in result:
        lt.append(i[0])
    # print(lt)
    return JsonResponse(lt, safe=False)


def chemistRegisteration(request):
    if 'admin' not in request.session:
        return redirect(adminLogin)
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['passw']
        dname = request.POST['dname']
        licensenumber = request.POST['licensenumber']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        s = f'INSERT INTO `chemist`(`email`, `city`, `state`, `licensenumber`, `displayname`, `address`, `password`) VALUES ("{email}","{city}","{state}","{licensenumber}","{dname}","{address}","{passw}")'
        print(s)
        result = Insert(s)
        print(result)
        if result == 'success':
            return redirect(chemistview)
    return render(request, 'chemistRegisteration.html')


def chemistview(request):
    if 'admin' not in request.session:
        return redirect(adminLogin)
    s = 'select * from chemist'
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['email'] = i[0]
        d['city'] = i[1]
        d['state'] = i[2]
        d['licensenumber'] = i[3]
        d['dname'] = i[4]
        d['address'] = i[5]
        lt.append(d)
    return render(request, 'chemistview.html', {'context': lt})


def deletechemist(request):
    if 'admin' not in request.session:
        return redirect(adminLogin)
    email = request.GET['email']
    s = 'DELETE FROM `chemist` WHERE `email`="{}"'.format(email)
    result = Delete(s)
    return HttpResponse(result)


def chemistupdate(request):
    if 'admin' not in request.session:
        return redirect(adminLogin)
    if request.method == 'POST':
        email = request.POST['email']
        dname = request.POST['dname']
        licensenumber = request.POST['licensenumber']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        s = f'UPDATE `chemist` SET `city`="{city}",`state`="{state}",`licensenumber`="{licensenumber}",`displayname`="{dname}",`address`="{address}" WHERE `email`="{email}"'
        result = Update(s)
        return HttpResponse(result)


def chemistLogin(request):
    if 'chemist' in request.session:
        return redirect(alladmin)
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select email,password from chemist where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result != None:
                request.session['chemist'] = {'chemistEmail': request.POST['email']}
                return redirect(allchemist)
            else:
                return render(request, 'chemistLogin.html',
                              {'message': 'Email and Password is not correct'})
        else:
            return render(request, 'chemistLogin.html',
                          {'message': 'Email and Password is not correct'})
    return render(request, 'chemistLogin.html')


def allchemist(request):
    if 'chemist' not in request.session:
        return redirect(chemistLogin)
    s = 'SELECT * FROM `billdetail` INNER JOIN product on billdetail.productid=product.pid INNER JOIN bill on billdetail.billid=bill.billID where product.chemistemail="{}"'.format(
        request.session['chemist']['chemistEmail'])
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['productname'] = i[6]
        d['payment'] = i[1]
        d['quantity'] = i[2]
        d['productimage'] = i[11]
        d['clientemail'] = i[25]
        lt.append(d)
    return render(request, 'chemistHome.html',{'context':lt})


def chemistlogout(request):
    if 'chemist' in request.session:
        request.session['chemist'] = ''
        del request.session['chemist']
    return redirect(chemistLogin)

def chemistChangePassword(request):
    if 'chemist' in request.session:
        if request.method == 'POST':
            s = 'select password from chemist where email="{}"'.format(request.session['chemist']['chemistEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                u = 'update chemist set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                                         request.session['chemist'][
                                                                                             'chemistEmail'])
                result = Update(u)
                return HttpResponse(result)
            else:
                return HttpResponse('Wrong Old Password')
        return redirect(allchemist)
    else:
        return redirect(chemistLogin)

def navstore(request):
    s = 'select email,displayname from chemist'
    result = Fetchall(s)
    ltd = []
    for i in result:
        d={}
        d['email']=i[0]
        d['displayname']=i[1]
        ltd.append(d)
    return JsonResponse(ltd, safe=False)

