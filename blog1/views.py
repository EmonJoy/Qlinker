from django.shortcuts import render
import qrcode
from io import BytesIO
import base64
import pyshorteners

def home(request):
    qr_image_base64 = None

    if request.method == "POST":
        data = request.POST.get('data') 
        if data:
           
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'home.html', {'qr_image': qr_image_base64})

def about(request):
    return render(request, "about.html") 

import pyshorteners
from django.shortcuts import render

def urlShort(request):
    short_url = None
    error_msg = None

    if request.method == "POST":
        try:
            long_url = request.POST.get("long_url")
            
            s = pyshorteners.Shortener()
            
     
            short_url = s.isgd.short(long_url)
            
        except Exception as e:

            error_msg = "Error shortening URL. Please check the link and try again."

    context = {

        
        "short_url": short_url, 
        "error": error_msg
    }
    
    return render(request, "urlShort.html", context)