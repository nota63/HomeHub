import io
from django.shortcuts import render, redirect
import pywhatkit as kit
from .forms import WorkScheduleForm
import decimal
from datetime import datetime, date, time
import decimal
from django.http import HttpResponse
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import random
from special.models import Special
from plyer import notification
import time
import datetime
from credentials.models import Credentials


def home2(request):
    return render(request, 'home.html')


def convert_to_serializable(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    return obj


def schedule_work(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        city=request.POST.get('city')
        pin_code=request.POST.get('pin_code')
        nearest_location=request.POST.get('nearest_location')
        phone_number=request.POST.get('phone_number')
        alternate_phone=request.POST.get('alternate_phone')
        date=request.POST.get('date')
        service=request.POST.get('service')
        special_instructions=request.POST.get('special_instructions')
        specified_time=request.POST.get('specified_time')
        referal=request.POST.get('referal')
        another_name=request.POST.get('another_name')
        colony=request.POST.get('colony')
        house_number=request.POST.get('house_number')
        my_contact="+919022216598"
        send=f" New order from {name}\nHello kindly confirm my order\n Order details\n Name: {name}\n City: {city}\n Pin Code: {pin_code}\n Nearest location: {nearest_location}\n Phone number: {phone_number}\n Alternate Phone: {alternate_phone}\n Date: {date}\n Service: {service}\n Special instructions: {special_instructions}\n Specified time: {specified_time}\n Referal: {referal}\n Another name: {another_name}\n Colony: {colony}\n House number: {house_number}"
        kit.sendwhatmsg_instantly(my_contact,send)
        display_data={'name':name,'city':city,'pin_code':pin_code,'nearest_location':nearest_location,
                      'phone_number':phone_number,'alternate_phone':alternate_phone,'date':date,
                      'service':service,'special_instructions':special_instructions,'specified_time':specified_time,
                      'referal':referal,'another_name':another_name,'colony':colony,'house_number':house_number

                      }
        request.session['display_data']=display_data
        return render(request,'confirmation.html')
    return render(request, 'schedule_work.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def summery(request):
    return render(request, 'summery.html')


def request_changes(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        name = request.POST.get('name')
        pin_code = request.POST.get('pin_code')
        city = request.POST.get('city')
        changes = request.POST.get('changes')
        data_to_send = (
            f"hey there kindly please make some changes in my order\n service: {service}\n name: {name}\n pin_code:{pin_code}\n city:{city}\n ***Changes i want***\n Changes: {changes}\n kindly make the changes ASAP")
        my_contact = "+919022216598"
        kit.sendwhatmsg_instantly(my_contact, data_to_send)
        data_to_display = {'service': service, 'name': name, 'pin_code': pin_code, 'city': city, 'changes': changes}
        request.session['data_to_display'] = data_to_display
        return render(request, 'summery.html')

    return render(request, 'request_changes.html')


def charge(request):
    return render(request, 'charge.html')


def view_team(request):
    return render(request, 'view_team.html')


def view_rates(request):
    return render(request, 'view_rates.html')


def cancel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        order_name = request.POST.get('order_name')
        city = request.POST.get('city')
        feedback = request.POST.get('feedback')

        cancel_data = (
            f"Hey there, my name is {name}. Please cancel my order.\n"
            f"Here are my order details:\n"
            f"Name: {name}\n"
            f"Order Name: {order_name}\n"
            f"City: {city}\n"
            f"Why I am cancelling this order: {feedback}"
        )

        my_contact = "+919022216598"

        notification.notify(
            title=f"HomeHub - {datetime.date.today()}",
            message=(
                f"Hello Dear {name},\n"
                f"Your order of {order_name} is being processed for cancellation as requested.\n"
                f"Thanks for interacting with us."
            ),
            app_icon="static/ap.png",
            timeout=6,
        )

        kit.sendwhatmsg_instantly(my_contact, cancel_data)

        info = (
            f"Your order of {order_name} has been cancelled and your order will be erased from our database within "
            f"24 hours."
        )

        request.session['info'] = info

        return render(request, 'summery.html', {'info': info})

    return render(request, 'cancel.html')


def feedback(request):
    return render(request, 'feedback.html')

def what_we_are(request):
    return render(request,'what_we_are.html')

def about_owner(request):
    return render(request,'about_owner.html')


# ADMIN AREA STARTS
def admin_home(request):
    return render(request, 'admin_home.html')


def admin_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'a@@d@@m##i%':
            return render(request, 'admin_home.html')
        else:
            return HttpResponse("Wrong Credentials")

    return render(request, 'admin_password.html')


def generate_bills(request):
    if request.method == 'POST':
        # Get form data
        shop_name = request.POST.get('shop_name')
        customer_name = request.POST.get('customer_name')
        service_name = request.POST.get('service_name')
        hourly_rate = float(request.POST.get('hourly_rate'))
        working_hours = int(request.POST.get('working_hours'))

        total_bill = working_hours * hourly_rate

        buffer = io.BytesIO()

        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, f"Shop Name: {shop_name}")
        c.drawString(100, height - 120, f"Customer Name: {customer_name}")
        c.drawString(100, height - 140, f"Service Name: {service_name}")
        c.drawString(100, height - 160, f"Working Hours: {working_hours}")
        c.drawString(100, height - 180, f"Hourly Rate: ${hourly_rate:.2f}")
        c.drawString(100, height - 200, f"Total Bill: ${total_bill:.2f}")

        logo_path = "static/ap.png"
        logo = ImageReader(logo_path)
        c.drawImage(logo, width - 150, height - 100, width=100, height=50)  # Adjust position and size as needed

        c.showPage()
        c.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='invoice.pdf')
    else:
        return render(request, 'generate_bills.html')


def special(request):
    special = Special.objects.all()
    return render(request, 'special.html', {'special': special})


def manage_admin_passwords(request):
    credentials = Credentials.objects.all()
    return render(request, 'manage_admin_passwords.html', {'credentials': credentials})
