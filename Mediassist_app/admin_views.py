from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from Mediassist_app.forms import LoginRegister, DonorRegister
from Mediassist_app.models import donor, users, Medicine_approval, Medicine_request


class CompanyRegistrationView(View):

    def get(self, request):
        user = LoginRegister()
        company_form = DonorRegister()


        return render(request, 'admin/register_cmp.html', {"user": user, "company_form": company_form})

    def post(self, request):
        user = LoginRegister(request.POST)

        company_form = DonorRegister(request.POST)

        if user.is_valid() and company_form.is_valid():

            a = user.save(commit=False)
            print(a)
            a.is_donor = True
            a.save()
            user1 = company_form.save(commit=False)
            print(user1)
            user1.user = a
            user1.save()
            return redirect('login_page')
        return render(request,'admin/register_cmp.html', {"user": user, "company_form": company_form})



def cmp_list(request):
    cmp=donor.objects.all()
    return render(request,'admin/cmp_list.html',{'cmp':cmp})


def user_list(request):
    user=users.objects.all()
    return render(request,'admin/user_list.html',{'user':user})


def requests(request):
    data = Medicine_approval.objects.all()
    return render(request, 'admin/approval.html', {'data': data})

def admin_approval(request):
    data=Medicine_approval.objects.filter(approval__status_1 = 1)
    return render(request,'admin/approval.html',{'data':data})




def approve_donation(request, id):
    n = Medicine_request.objects.get(id=id)
    n.status_1 = 2
    n.save()
    messages.info(request, 'Donation Confirmed')
    return redirect('requests')

def reject_donation(request, id):
    n = Medicine_request.objects.get(id=id)
    n.status_1 = 3
    n.save()
    messages.info(request, 'Rejected')
    return redirect('requests')