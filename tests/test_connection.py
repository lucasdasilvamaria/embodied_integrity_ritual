import gspread
from google.oauth2.service_account import Credentials

# Define os escopos certos
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Carrega as credenciais com escopos explícitos
creds = Credentials.from_service_account_file(
    'embodied-ritual-app-c081a8809cd1.json',
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Teste simples
spreadsheet = client.open("Embodied_Ritual_Log")
worksheet = spreadsheet.sheet1
print(worksheet.get_all_records())