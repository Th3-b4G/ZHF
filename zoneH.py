import requests

def FuckerH(notifier,target):
    try:
        payload = "http://zone-h.com/notify/single"
        post_data = {
            "defacer" : notifier,
            "domain1" : target,
            "hackmode" : "9",
            "reason" : "6"
                     }
        x = requests.post(payload, data = post_data)
        if x.status_code == 200:
            print("[+] [mirror done]: "+target)
        else:
            print("[+] [problema mf] "+target)
    except:
        pass

print('''
      ,___,
      [O.o]
      /)__)
     /-"--"-
[mass zone-h submiter]
''')
notifierx = raw_input("defacer name : ")
targetx = raw_input("site list (with https://): ")
lixtx = open(targetx, 'r').read().splitlines()
for x in lixtx:
    FuckerH(notifierx,x)
