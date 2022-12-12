from __future__ import print_function

import datetime
import os.path
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

TOKEN_PICKLE = "token.pickle"

# If modifying these scopes, delete the file token.json.
CREDENTIAL_FILE = "credentials.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    credentials = None
    if os.path.exists(TOKEN_PICKLE):
        with open(TOKEN_PICKLE, "rb") as tkn:
            credentials = pickle.load(tkn)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIAL_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)

        with open(TOKEN_PICKLE, "wb") as tkn:
            pickle.dump(credentials, tkn)

    service = build("calendar", "v3", credentials=credentials)
    return service
