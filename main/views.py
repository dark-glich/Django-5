from django.shortcuts import render
from .data import upload_speed_test, download_speed_test
def SpeedView(request):
     download_speed = '00.0'
     upload_speed = '00.0'
     if request.method == 'POST':
          download_speed = download_speed_test()
          upload_speed = upload_speed_test()
     context = {
          'download_speed': download_speed,
          'upload_speed':upload_speed
          }
     return render(request, 'enternet.html', context)

