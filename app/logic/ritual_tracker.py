import pandas as pd
from datetime import datetime
import os

DATA_PATH = 'data/ritual_log.xlsx'

def log_ritual_step(step_name, notes=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"Timestamp": timestamp, "Step": step_name, "Notes": notes}

    if os.path.exists(DATA_PATH):
        df = pd.read_excel(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])

    df.to_excel(DATA_PATH, index=False)