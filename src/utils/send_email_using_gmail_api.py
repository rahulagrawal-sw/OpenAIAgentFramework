import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

def send_email(to_email:str, subject:str, email_body:str) -> str:
    return "12345"

"""
SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
cred_path = "C:\\ML\\OpenAIAgentFramework\\src\\utils\\credentials.json"
flow = InstalledAppFlow.from_client_secrets_file(
            cred_path, SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)



def send_email(to_email:str, subject:str, email_body:str) -> str:
    message = MIMEText(email_body)
    message['to'] = to_email
    message['subject'] = subject

    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    
    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        message_id = message["id"]
        print(F'Email message sent to {to_email}. Message Id: {message_id}')
        return message_id
    except HTTPError as error:
        print(F'An error occurred while sending email: {error}')
        return None
"""