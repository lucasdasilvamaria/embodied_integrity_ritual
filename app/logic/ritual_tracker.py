import streamlit as st
import json
from datetime import date
from google.oauth2 import service_account
import gspread

def connect_sheet():
    creds_info = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(creds_info)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1rP07vxav0Iovn0_SJU0hv1Ct7ulrVGWrVyF6hmFhUaw").sheet1
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