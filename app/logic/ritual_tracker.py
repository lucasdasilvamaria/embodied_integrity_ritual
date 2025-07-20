import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from io import StringIO
import os
import streamlit as st

# Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
sheet_id = "1rP07vxav0Iovn0_SJU0hv1Ct7ulrVGWrVyF6hmFhUaw"

def connect_sheet():
    try:
        # ✅ Streamlit Cloud: usa os secrets
        creds_dict = dict(st.secrets["gcp_service_account"])
        creds_json = StringIO(str(creds_dict).replace("'", '"'))
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    except Exception:
        # 🧪 Local (modo desenvolvedor)
        creds_file = os.path.join("data", "credentials.json")
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)

    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet

def log_ritual_completion(steps):
    sheet = connect_sheet()
    today = date.today().strftime("%Y-%m-%d")
    for step in steps:
        name = step["name"]
        category = step["category"]
        tag = step.get("tag", "")
        row = [today, name, category, tag]
        sheet.append_row(row)
