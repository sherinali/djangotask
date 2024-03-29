from django.shortcuts import render , redirect
from Students.models import Req_st
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from accounts.views import auth
from accounts.models import Sponsor
# Create your views here.



@requires_csrf_token
def sponserRequest(request,id):
    if auth(request) == 2:  # sponsor
            a = Req_st.objects.filter(req_spon=request.user,disable = False)
            aa = len(a)
            if aa < 3:
                e = Req_st.objects.get(id=id,disable = False)
                a = Sponsor.objects.get(username=request.user.username,disable = False)
                e.req_spon = request.user.username
                e.sNumberReq = a.phone_number
                e.save()
                return redirect('kafalaty')
            else:
                return HttpResponse('لا يمككن طلب اكثر من ثلاث كفالات في وقت واحد, الرجاء الانتضار لحين موافقه طلبات كفالتك')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def sponserdelete(request,id):
    if auth(request) == 2:  # sponsor
            d = Req_st.objects.get(id=id,disable = False)
            d.sponser = ""
            d.req_spon = ""
            d.sNumberReq = ""
            d.sNumber = ""
            d.save()
            return redirect('kafalaty')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def displayKafalat(request):
    if auth(request) == 2:  #sponsor
        kT = Req_st.objects.filter(sponser='',req_spon='',approved = True,disable = False)
        return render(request, 'kafalat.html',{'kT':kT})
    elif auth(request) == 1: #admin
        kta = Req_st.objects.filter(approved = True,sponser='',req_spon='',disable = False)
        ktb = Req_st.objects.filter(approved = True,sponser='',disable = False).exclude(req_spon__exact='')
        ktc = Req_st.objects.filter(approved = True,req_spon='',disable = False).exclude(sponser__exact='')
        kf = Req_st.objects.filter(approved = False,disable = False)
        return render(request, 'kafalat.html',{ 'kta':kta, 'ktb':ktb, 'ktc':ktc, 'kf':kf})
    else:
        return redirect('home')




@requires_csrf_token
def displayMyKafalat(request):
    if auth(request) == 2:  # sponsor
        u = request.user
        m = Req_st.objects.filter(sponser=u, approved=True,req_spon='',disable = False)
        ma = Req_st.objects.filter(req_spon=u,approved=True,sponser='',disable = False)
        return render(request,'myKafalat.html',{'m':m, 'ma':ma})
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def acceptAdmin(request,id):
    if auth(request) == 1:  # admin
        a = Req_st.objects.get(id=id,disable = False)
        a.sponser = a.req_spon
        a.req_spon = ""
        a.sNumber = a.sNumberReq
        a.sNumberReq = ""
        a.save()
        return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def refuseAdmin(request,id):
    if auth(request) == 1:  # admin
        a = Req_st.objects.get(id=id,disable = False)
        a.req_spon = ""
        a.sNumberReq = ""
        a.save()
        return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def delAdmin(request,id):
    if auth(request) == 1:  # admin
            da = Req_st.objects.get(id=id,disable = False)
            da.sponser = ""
            da.sNumber = ""
            da.save()
            return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def adminReq_stA(request,id):
    if auth(request) == 1:  # admin
            a = Req_st.objects.get(id=id,disable = False)
            a.approved = True
            a.save()
            return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def adminReq_stB(request,id):
    if auth(request) == 1:  # admin
            a = Req_st.objects.get(id=id,disable = False)
            a.disable = True
            a.save()
            return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')
