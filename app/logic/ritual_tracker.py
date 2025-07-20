import gspread
from google.oauth2.service_account import Credentials
from datetime import date
from io import StringIO
import os
import streamlit as st

# Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
sheet_id = "1rP07vxav0Iovn0_SJU0hv1Ct7ulrVGWrVyF6hmFhUaw"

def connect_sheet():
    try:
        # ✅ Tenta ler do Streamlit secrets
        creds_dict = dict(st.secrets["gcp_service_account"])
        creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    except Exception:
        # 🔁 Fallback local
        creds_file = os.path.join("data", "credentials.json")
        creds = Credentials.from_service_account_file(creds_file, scopes=scope)

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