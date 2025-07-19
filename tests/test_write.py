import gspread
from google.oauth2.service_account import Credentials

# Carrega credenciais
creds = Credentials.from_service_account_file("embodied-ritual-app-c081a8809cd1.json")
scoped_creds = creds.with_scopes(["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(scoped_creds)

# Abre a planilha
spreadsheet = client.open("Embodied_Ritual_Log")
worksheet = spreadsheet.sheet1

# Escreve na célula A1
worksheet.update("A1", [["Testado com sucesso!"]])

print("✅ Escrita realizada!")
