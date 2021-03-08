
import speedtest


def download_speed_test():
     test = speedtest.Speedtest()
     down = round(test.download()/10**6,1)

     return down 

def upload_speed_test():
     test = speedtest.Speedtest()
     upload = round(test.upload()/10**6,1)
     return upload