#zadanie 1

filepath = "students0.txt"
filepath1 = "students3.txt"
info_list = []
info_dict = {}
ind = 0
with open(filepath1) as file:
    for line in file:
        info = line.strip().split(",")
        if len(info) > 4:
            user = {
                "email": info[0],
                "imie": info[1],
                "nazwisko": info[2],
                "punkty": info[3],
                "ocena": info[4],
                "status": info[5]
            }
        if len(info) <= 4:
            user = {
                "email": info[0],
                "imie": info[1],
                "nazwisko": info[2],
                "punkty": info[3]
            }
        info_dict[ind] = user
        ind += 1
with open(filepath) as file:
    for line in file:
        info = line.strip().split(",")
        if len(info) > 4:
            user = {
                "email": info[0],
                "imie": info[1],
                "nazwisko": info[2],
                "punkty": info[3],
                "ocena": info[4],
                "status": info[5]
            }
        if len(info) <= 4:
            user = {
                "email": info[0],
                "imie": info[1],
                "nazwisko": info[2],
                "punkty": info[3],
                "ocena": "",
                "status": ""
            }
        info_dict[ind] = user
        ind += 1

#zadanie 2
def set_grade():
    for i in info_dict:
        punkty = int(info_dict[i]["punkty"])
        if info_dict[i]["status"] != "GRADED" or info_dict[i]["status"] != "MAILED":
            if punkty <= 50:
                info_dict[i]["ocena"] = "2"
            if punkty >= 51 and punkty <= 60:
                info_dict[i]["ocena"] = "3"
            if punkty >= 61 and punkty <= 70:
                info_dict[i]["ocena"] = "3.5"
            if punkty >= 71 and punkty <= 80:
                info_dict[i]["ocena"] = "4"
            if punkty >= 81 and punkty <= 90:
                info_dict[i]["ocena"] = "4.5"
            if punkty >= 91 and punkty <= 100:
                info_dict[i]["ocena"] = "5"
set_grade()
#zadanie 3
def delete_student(email):
    for key, value in info_dict.items():
        if value['email'] == email:
            del info_dict[key]
            break
def add_student():
    email = input("email: ")
    valid = True
    for key, value in info_dict.items():
        if value['email'] == email:
            print("ten email jest już dodany")
            valid = False
            break
    if valid is False:
        return
    imie = input("imie: ")
    nazwisko = input("nazwisko: ")
    punkty = input("punkty: ")
    user = {
        email,
        imie,
        nazwisko,
        punkty
    }
    info_dict[len(info_dict) + 1] = user

#zadanie 4
import smtplib
from email.mime.text import MIMEText
def send_email(subject,body,sender,recipents,password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recipents)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.login(sender,password)
    smtp_server.sendmail(sender, recipents, msg.as_string())
    smtp_server.quit()

subject = "Email wysłany z Pythona"
body = ""
sender = ""
recipients = []

for key, value in info_dict.items():
    if value["status"] != "MAILED":
        recipients.append(value["email"])

for key, value in info_dict.items():
    if value["status"] != "MAILED":
        body += "nazwisko: "+ value["nazwisko"] + ", ocena: " + value["ocena"] + '\n'
password = ""
#send_email(subject , body , sender , recipients , password)

#zadanie 5
def write_dict_to_file(d, filename):
    with open(filename, "w") as f:
        write_dict_to_file_helper(d, f)

def write_dict_to_file_helper(d, f, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            f.write("\t" * indent + str(key) + ":\n")
            write_dict_to_file_helper(value, f, indent+1)
        else:
            f.write("\t" * indent + str(key) + ": " + str(value) + "\n")
file = "StudentsOut.txt"

write_dict_to_file(info_dict, file)






