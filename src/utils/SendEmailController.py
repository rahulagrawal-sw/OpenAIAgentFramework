from fastapi import APIRouter
from src.utils.send_email_using_gmail_api import send_email

send_email_router = APIRouter(tags=["send_email_util"])


@send_email_router.get("/send_email")
async def run_search_agent_api():
    to_email = "rahulagrawal.sw@gmail.com"
    subject = "My Test Email API one"
    email_body = """
        <html>
            <body>
                <h1> TEST EMAIL </h1>
                <b> Trial one </b>
                <p>
                    Attempting uninstall: protobuf
                    Found existing installation: protobuf 7.34.1
                    Uninstalling protobuf-7.34.1:
                </p>
                <br/><br/><br/><br/>
                <h2>
                    Sent by:
                    <br/>
                    RAFreelance AI Agent
                </h2>
            </body>
        </html>
    """

    message_id = send_email(to_email, subject, email_body)
    return {"status": "ok", "message": "Email sent successfully", "message_id": message_id}