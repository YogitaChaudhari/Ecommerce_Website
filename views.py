from django.shortcuts import render,redirect
from django.http import HttpResponse
from itvedantapp1.forms import userform,productform,categoryform
from itvedantapp1.models import Users,Category,Products,Carts
from django.contrib import messages
# from .import dbm as db

# def __init__(request):
#     c=Category.objects.all()
#     return render(request,'sidebar.html',{'c':c})

def signup(request):
    c1=Category.objects.all()
    p1=Products.objects.all()
    a=userform()
    return render(request,'sign_up.html',{'user':a,'c1':c1,'p1':p1})

def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'login.html')

def Loginto(request):
    try:
        e=request.POST.get('ename')
        p=request.POST.get('pname')
        v=Users.objects.get(email=e)
        if e=='yogita@gmail.com' and p=='yogita@123':
            request.session['admin']=e
            return redirect('/')
        elif e==v.email and p==v.password:
            request.session['username']=e
            return redirect('/')
        else:
            return HttpResponse('<h1>Error</h1>')
    except:
        return HttpResponse("<script>alert('No such user Exist')</script>")
        

def delete_session(request):
    request.session.flush()
    # ls=list(request.session.keys())
    # print(ls)
    # for i in ls:
    #     del request.session[i]
    return redirect('/')

def slist(request):
    x=request.GET.get('cname')
    c1=Category.objects.all()
    p1=Products.objects.filter(pro_category_name=x)
    return render(request,'home.html',{'c1':c1,'p1':p1})

def additemdb(request,id):
    try:
        t=Products.objects.get(id=id)
        e=request.session.get('username')
        u=Users.objects.get(email=e)
        c=Carts()
        c.email=u
        c.pro_id=t
        c.save()
        messages.info(request,"Item added to Cart Successfully")
        return redirect('/')
    except:
        return HttpResponse("admin Not allowed.")

def deleteitemfromdb(request):
    pid=request.GET["pid"]
    p_id=Carts.objects.get(id=pid)
    p_id.delete()
    email=request.session.get('username')
    cartlist=Carts.objects.filter(email=email)
    cl=Category.objects.all()
    return render(request,'cart.html',{'p':cartlist,'cl':cl})


def cart(request):
    email=request.session.get('username')
    cartlist=Carts.objects.filter(email=email)
    # item = Carts.orderitem_set.all()
    return render(request,'cart.html',{'p':cartlist})

def increment(request):
    email=request.session.get('username')
    cartlist=Carts.objects.filter(email=email)
    c=request.GET['count']
    
    v.Carts()
    v.count=c
    v.save()
    return render(request,'cart.html',{'p':cartlist})

def decrement(request):
    pass

def home(request):
    c1=Category.objects.all()
    p1=Products.objects.all()
    if request.session.get('username',False):
        e=request.session.get('username')
        u=Users.objects.get(email=e)
        
        return render(request,'home.html',{'c1':c1,'p1':p1,'u':u})
    else:
        return render(request,'home.html',{'c1':c1,'p1':p1})

def adduser(request):
    c1 = Category.objects.all()
    a=userform()
    return render(request,'adduser.html',{'user':a,'c1':c1})
def addproduct(request):
    c1 = Category.objects.all()
    b=productform()
    return render(request,'addproduct.html',{'product':b,'c1':c1})
def addcategory(request):
    c1 = Category.objects.all()

    c=categoryform()
    return render(request,'addcategory.html',{'category':c,'c1':c1})

def adduserdb(request):
    uf=userform(request.POST)
    uf.save()
    return redirect('/home.html')
def addcategorydb(request):
    cat=categoryform(request.POST)
    cat.save()
    return redirect('/addcategory.html')
def addproductdb(request):
    pd=productform(request.POST,request.FILES)    
    pd.save()
    return redirect('/addproduct.html')

def listusers(request):
    c1 = Category.objects.all()
    ul=Users.objects.all()
    return render(request,'listusers.html',{'ul':ul,'c1':c1})
def Listcategory(request):
    c1 = Category.objects.all()
    ul=Category.objects.all()
    return render(request,'Listcategory.html',{'ul':ul,'c1':c1})
def productlist(request):
    c1 = Category.objects.all()
    ul=Products.objects.all()
    return render(request,'productlist.html',{'ul':ul,'c1':c1})
# sidebar.html
# def whileopening(request):
#     ul=Category.objects.all()
#     return render(request,'sidebar.html',{'ul':ul})

def deleteuser(request,email):
    c=Users.objects.get(email=email)
    c.delete()
    return redirect('/listusers.html')
def deletecategory(request,pro_category_name):
    delc=Category.objects.get(pro_category_name=pro_category_name)
    delc.delete()
    return redirect('/Listcategory.html')
def deleteproduct(request,id):
    dp=Products.objects.get(id=id)
    dp.delete()
    return redirect(('/productlist.html'))

def edituser(request):
    email=request.GET.get('email')
    e=Users.objects.get(email=email)
    f=userform(instance=e)
    return render(request,'updateuser.html',{'form':f,'email':email})

def updateUser(request):
    email=request.GET.get('email')
    e=Users.objects.get(email=email)
    f=userform(request.POST,instance=e)
    f.save()
    return redirect("/listusers.html")

def editproduct(request):
    k=request.GET.get('id')
    i=Products.objects.get(id=k)
    p=productform(instance=i)
    return render(request,'editproduct.html',{'form':p,'id':id})

def updateProduct(request):
    pc=request.GET.get('pro_category_name')
    i=Products.objects.get(pro_category_name=pc)
    f=productform(request.GET,instance=i)
    f.save()
    return redirect('/productlist.html')

# def myform(request):
#     ut=UserForm()
#     pt=ProductForm()
#     return render(request,'myform.html',{'form':pt})
# Create your views here.
