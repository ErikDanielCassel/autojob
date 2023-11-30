from email.message import EmailMessage
from email.policy import SMTP
from smtplib import SMTP_SSL
from getpass import getpass
import requests, json


#Change these to you personal information
server = 'mailout.telia.com'
port = 465
user = 'erik.cassel@telia.com'
#password = getpass() #uncomment this if you need to log in with a password, I don't need to for some weird reason TODO Make this uncomment make the sendMail function send a 
introFile = "personligtbrevVildmark.txt" #The text you want in the email but check on your email providers website
personligtBrev = ""
CurriculumVitae = "cv final.pdf"
quarry = "it" #search term for the job application quarry


#variables
url = 'https://jobsearch.api.jobtechdev.se'
url_for_search = f"{url}/search"
sender = user

#testing variables
reciever = 'erik.cassel@telia.com'

#constuct message
message= EmailMessage(policy=SMTP)
message['Subject'] = "Erik Cassel's jobbansökan"
message['From'] = sender
message['To'] = reciever
message.set_charset("RFC822")
with open(introFile, "r", encoding="utf-8") as file:
    message.set_content(file.read())

def sendMail(reciever):
    #connect to server, send email and disconnect
    with SMTP_SSL(server) as smtp:
        smtp.set_debuglevel(2)
        #smtp.login(user, password)
        smtp.send_message(message, sender, reciever)
    print("done")

def getAds(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.content.decode('utf-8'))

def search_loop_through_hits(query):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    search_params = {'q': query, 'limit': 100}
    json_response = getAds(search_params)
    hits = json_response['hits']
    for hit in hits:
        print(f"{hit['headline']}, {hit['employer']['name']}")

def getAllAds(query):
    hits = 0
    search_params = {'q': query, 'limit': 100, 'offset': 0}
    search_params.update({'offset': hits})
    json_response = getAds(search_params)
    #while:


#sendMail(reciever)
#search_loop_through_hits('it')
print(getAds({'q': 'supporttekniker', 'limit': 2, 'offset': 100}))