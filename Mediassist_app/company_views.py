from django.contrib import messages
from django.shortcuts import render, redirect

from Mediassist_app.models import Medicine_request, donor, Medicine_approval


def med_view_cmp(request):
    n = Medicine_request.objects.all()

    return render(request, 'company/med_request_view.html',{'medicine':n})



#donate

def donate(request,id):
    approval = Medicine_request.objects.get(id=id)
    u = donor.objects.get(user=request.user)
    appointment = Medicine_approval.objects.filter(user=u , approval=approval)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Donation..we will reach you soon')
        return redirect("med_view_cmp")
    else:
        if request.method == 'POST':
            obj = Medicine_approval()
            obj.user = u
            obj.approval = approval

            obj.save()

            approval.status_1 = 1
            approval.save()
            print("hi")

            messages.info(request, 'Thanks for your support..we will reach you soon')
            return redirect('med_view_cmp')
    return render(request, 'company/donate.html', {'approval': approval})