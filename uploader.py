import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def upload_video(file="output.mp4", title="فيديو تلقائي", description="تم إنشاؤه تلقائيا"):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    youtube = build('youtube', 'v3', credentials=creds)

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['تلقائي', 'Python'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    mediaFile = MediaFileUpload(file, mimetype='video/mp4', resumable=True)
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    print("تم رفع الفيديو:", response['id'])
