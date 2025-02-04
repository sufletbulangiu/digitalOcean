from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter
# Create your views here.

def index (request):
    device = 'None'
    print(request.user_agent.browser)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        os = request.user_agent.os.family
        osVersion = request.user_agent.os.version_string
        browser = request.user_agent.browser.family
        browserVersion = request.user_agent.browser.version_string
        if request.user_agent.is_mobile:
            device = "Smartphone"
        elif request.user_agent.is_pc:
            device = "PC"
    else:
        ip = request.META.get('REMOTE_ADDR')   
        os = request.user_agent.os.family  
        osVersion = request.user_agent.os.version_string
        browser = request.user_agent.browser.family
        browserVersion = request.user_agent.browser.version_string
        if request.user_agent.is_mobile:
            device = "Smartphone"
        elif request.user_agent.is_pc:
            device = "PC"

    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()
    counter.count += 1
    counter.ip_address = ip
    counter.os = os
    counter.osVersion = osVersion
    counter.browser = browser
    counter.browserVersion = browserVersion
    counter.device = device
    counter.save()
    print(request.headers)
    context = {
        'count': counter.count,
        'ip': counter.ip_address,
        'os': counter.os,
        'osVersion': counter.osVersion,
        'browser': counter.browser,
        'browserVersion': counter.browserVersion,
        'device': counter.device
    }   
    return render(request, 'index.html', context)