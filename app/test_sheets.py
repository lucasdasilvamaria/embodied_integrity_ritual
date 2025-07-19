import gspread
from google.oauth2.service_account import Credentials

# Caminho para o arquivo JSON com as credenciais
SERVICE_ACCOUNT_FILE = "embodied-ritual-app-c081a8809cd1.json"  # ou o nome que veio do download

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Autenticando
client = gspread.authorize(creds)

# Abrindo a planilha
spreadsheet = client.open("Embodied_Ritual_Log")
sheet = spreadsheet.sheet1

# Escrevendo algo
sheet.append_row(["Testando!", "Ritual funcionando", "🔥"])
print("Linha adicionada!")
