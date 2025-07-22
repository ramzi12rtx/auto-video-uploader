from video_generator import generate_video
from uploader import upload_video

generate_video("هذا الفيديو تم إنشاؤه تلقائيًا 😎")
upload_video()
from google_auth_oauthlib.flow import InstalledAppFlow
import json
client_config = json.loads(os.environ["CLIENT_SECRET_JSON"])
flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
