import requests
import smtplib
from email.message import EmailMessage

# Send message alerts to phone 
def msg_alert(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	# Simply paste your email_addr and app_pwd as a string
	email_addr = "email@gmail.com" # Enter your email address
	msg['from'] = email_addr
	app_pwd = "app_pwd" # App password (Refer to Readme on acquiring app_pwd)

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(str(email_addr), str(app_pwd))
	server.send_message(msg)
	server.quit()

state = "CA"  # Enter your state abbreviation
phone_number = "your_phone_number@vtext.com" # Enter your phone number with your carrier's SMS Gateway Address (Refer to Readme)

# Get payload from CVS vaccine website and convert it as json
response = requests.get("https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status."+ state.lower() + ".json?vaccineinfo", headers={"Referer":"https://www.cvs.com/immunizations/covid-19-vaccine"})
response = response.json()

mappings = {}
for item in response["responsePayloadData"]["data"][state]:
    mappings[item.get('city')] = item.get('status') 

message = []
cities = ['City-1', 'City-2', 'City-3'] # Cities for which you want to get notified
for key in mappings:
    if (key in cities) and (mappings[key] != 'Fully Booked'):
        message.append(key + ": " + (mappings[key]))

# Formatting message by sending complete list
message = '\n'.join(map(str, message))
print(message)

# Sending alerts 
if len(message) > 0:
	message += "\n* https://www.cvs.com/immunizations/covid-19-vaccine"
	msg_alert("Status: ", message, phone_number)  
	