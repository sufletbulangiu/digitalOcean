from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter
from django.conf import settings
import socket
# Create your views here.

def index (request):
    device = 'None'
    #print(request.user_agent.browser)    
    print(request.session.session_key)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = socket.gethostbyaddr(x_forwarded_for.split(',')[-1].strip())[0]  
        os = request.user_agent.os.family
        osVersion = request.user_agent.os.version_string
        browser = request.user_agent.browser.family
        browserVersion = request.user_agent.browser.version_string
        session_key = request.session._get_or_create_session_key()
        if request.user_agent.is_mobile:
            device = "Smartphone"
        elif request.user_agent.is_pc:
            device = "PC"
    else:
        ip = socket.gethostbyaddr(request.META.get('REMOTE_ADDR'))[0]  
        os = request.user_agent.os.family  
        osVersion = request.user_agent.os.version_string
        browser = request.user_agent.browser.family
        browserVersion = request.user_agent.browser.version_string
        session_key = request.session._get_or_create_session_key()     
        if request.user_agent.is_mobile:
            device = "Smartphone"
        elif request.user_agent.is_pc:
            device = "PC"

    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()
    counter.id +=1
    counter.count += 1
    counter.ip_address = ip
    counter.os = os
    counter.osVersion = osVersion
    counter.browser = browser
    counter.browserVersion = browserVersion
    counter.device = device
    counter.session_key = session_key
    counter.save()
    print(request.headers)
    context = {
        'count': counter.count,
        'ip': counter.ip_address,
        'os': counter.os,
        'osVersion': counter.osVersion,
        'browser': counter.browser,
        'browserVersion': counter.browserVersion,
        'device': counter.device,
        'session_key': counter.session_key
    }   
    return render(request, 'index.html', context)