import requests as req
import socket
h = socket.gethostname()
ip = socket.gethostbyname(h)
print(ip)
def req1():
    url = "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pQ=="
    header = {
            "Host": ip,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pQ==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "61",
            "Connection": "close",
            "Cookie": "PHPSESSID=rfnvlffjeo9rrak0h0jrsb6r71",
            "Upgrade-Insecure-Requests": "1"
        }
    data = {'host':'localhost','username':'admin','password':'password','dbname':'sentry'}
    res = req.post(url=url,headers=header,data=data)
    print res.status_code
def req2():
    url = "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pg=="
    header = {
            "Host": ip,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pg==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "71",
            "Connection": "close",
            "Cookie": "PHPSESSID=rfnvlffjeo9rrak0h0jrsb6r71",
            "Upgrade-Insecure-Requests": "1"
        }
    data = {'app_name':'Sentrifugo','email':'debabratasharma656@40gmail.com','submit':'Confirm'}
    res = req.post(url=url,headers=header,data=data)

def req3():
    url = "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pw=="
    header = {
            "Host": ip,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://"+ip+"/Sentrifugo_3.2/install/index.php?s=pw==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "144",
            "Connection": "close",
            "Cookie": "PHPSESSID=rfnvlffjeo9rrak0h0jrsb6r71",
            "Upgrade-Insecure-Requests": "1"
        }
    data = {'auth':'true','username':'debabratasharma656@gmail.com','password':'GcHxEK5t4UPXOqFa','smtpserver':'smtp-relay.sendinblue.com','tls':'tls','port':'587','submit':'Confirm'}
    req.post(url=url,headers=header,data=data)
def req4():
    url = "http://localhost/Sentrifugo_3.2/install/index.php?s=pw=="
    header = {
            "Host": "localhost",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://localhost/Sentrifugo_3.2/install/index.php?s=pw==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "61",
            "Connection": "close",
            "Cookie": "PHPSESSID=rfnvlffjeo9rrak0h0jrsb6r71",
            "Upgrade-Insecure-Requests": "1"
        }
    data = {'auth':'true','username':'debabratasharma656%40gmail.com','password':'GcHxEK5t4UPXOqFa','smtpserver':'smtp-relay.sendinblue.com','tls':'tls','port':'587','submit':'Confirm'}
    req.post(url=url,headers=header,data=data)
def req5():
    url = "http://"+ip+"/Sentrifugo_3.2/success.php"
    header = {
            "Host": ip,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": " http://"+ip+"/Sentrifugo_3.2/install/index.php?s=qA==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "549",
            "Connection": "close",
            "Cookie": "PHPSESSID=rfnvlffjeo9rrak0h0jrsb6r71",
            "Upgrade-Insecure-Requests": "1"
        }
    data = {'mailcontent':'kiba','dbhost':'localhost','dbusername':'admin','dbpassword':'password','dbname':'sentry','appname':'Sentrifugo','appemail':'debabratasharma656@gmail.com','mailusername':'debabratasharma656@gmail.com','mailpassword':'GcHxEK5t4UPXOqFa','mailsmtp':'smtp-relay.sendinblue.com','mailtls':'tls','mailport':'587','mailauth':'true','cronjoburl':'http://172.17.0.2/Sentrifugo_3.2/index.php/cronjob','expirydocurl':'http://172.17.0.2/Sentrifugo_3.2/index.php/cronjob/empdocsexpiry','tmcronurl':'http://172.17.0.2/Sentrifugo_3.2/index.php/timemanagement/cronjob','btnfinish':'Finish'}
    res = req.post(url=url,headers=header,data=data)
    print res.text
req1()
req2()
req3()
#req4()
req5()
print "Visit http://"+ip+"/Sentrifugo_3.2 in your browser"
