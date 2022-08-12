
from urllib import request
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from crud.models import BooksDetails,Users
import mysql.connector
# Create your views here.
def login(request):
    if(request.method=='POST'):
        # print(Users.objects.all())
        try:
            UserDetails=Users.objects.get(email=request.POST['email'] ,password=request.POST['password'])
            # print(UserDetails.email)
            request.session['email']=UserDetails.email;
            return HttpResponseRedirect('http://127.0.0.1:8000/index')
        except:
            messages.success(request,"invalid credientials")
        # if(request.POST.get('email') and request.POST.get('password')):
        #     print(request.POST.get('email'),request.POST.get('password'))
        #     # getUser=Users.objects.filter(email=request.POST.get('email')).using()
        #     try:
        #         # getUser= Users.objects.exists(email=email)
        #         # print(getUser)
        #         getrecord=Users.objects.get(email=request.POST('email'))
        #     except:
        #         print('error')
        #     return HttpResponseRedirect("http://127.0.0.1:8000/index/")
    return render(request,'login.html')
def signout(request):
    try:
        del request.session.email
    except:
        return render(request,'index.html')
    return HttpResponseRedirect('login.html')

def signup(request):
    if(request.method=='POST'):
        if(request.POST.get('name') and request.POST.get('email') and request.POST.get('password')):
            name=request.POST.get('name')
            email=request.POST.get('email') 
            password=request.POST.get('password')
            try:
                UserDetails=Users.objects.get(email=request.POST['email'] ,password=request.POST['password'])
                if(UserDetails.email==email):
                    messages.success(request,'User Already Exist')
                    return render(request,'signup.html')
            except:
                # Users(name=name,email=email,password=password).save()
                saverecord=Users()
                saverecord.name=request.POST.get('name')
                saverecord.email=request.POST.get('email')
                saverecord.password=request.POST.get('password')
                saverecord.save()
                messages.success(request,'User created Sucessfully')
                return render(request,'signup.html')
            # try:
            #     Users(name=name,email=email,password=password).save()
            #     messages.success(request,'User created Sucessfully')
            #     return render(request,'signup.html')
            # except:
            #     messages.success(request,'User Already Exist')
            #     return render(request,'signup.html')
            # try:
                # saverecord=Users()
                # saverecord.name=request.POST.get('name')
                # saverecord.email=request.POST.get('email')
                # saverecord.password=request.POST.get('password')
                # saverecord.save()
                # messages.success(request,'USer Created Sucessfully')
                # return HttpResponseRedirect("http://127.0.0.1:8000/login/")
            # except(Exception):
            #     messages.success(request,'User Already Exists')
            #     return render(request,'signup.html')
    return render(request,'signup.html')
def student(request):
    # return HttpResponse('Prasad')
    resultsDisplay=BooksDetails.objects.all()
    return render(request,'student.html',{'BooksDetails':resultsDisplay})
def show(request):
    # return HttpResponse('Prasad')
    resultsDisplay=BooksDetails.objects.all()
    return render(request,'index.html',{'BooksDetails':resultsDisplay})
def insert(request):
    if(request.method=='POST'):
        if(request.POST.get('bookname') and request.POST.get('bookdescription')):
            saverecord=BooksDetails()
            saverecord.book_name=request.POST.get('bookname')
            saverecord.book_description=request.POST.get('bookdescription')
            saverecord.save()
            messages.success(request,'Record Sucessfully Saved')
            return HttpResponseRedirect("index/")
    return render(request,'insert.html')
def update(request,book_id):
    updatebook=BooksDetails.objects.get(book_id=book_id)
    if(request.method=='POST'):
        id=book_id
        name=request.POST.get('name')
        desc=request.POST.get('description')
        b=BooksDetails.objects.filter(book_id=book_id).update(book_id=id,book_name=name,book_description=desc)
        return HttpResponseRedirect("http://127.0.0.1:8000/index")
    return render(request,'update.html',{'upd':updatebook})
def deleteData(request,book_id):
    d=BooksDetails.objects.get(book_id=book_id)
    d.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/index")
# def finalupdate(request,book_id):
#     finalupdate=BooksDetails.objects.get(book_id=book_id)
#     if(request.method=='POST'):
#         if(request.POST.get('id') and request.POST.get('name') and request.POST.get('description')):
#             id=request.POST.get('id')
#             name=request.POST.get('name')
#             desc=request.POST.get('description')
#             b=BooksDetails.objects.filter(book_id=book_id).update(id,name,desc)
#             return HttpResponseRedirect("index/")
#     return render(request,'update.html')
