import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client.json', scope)
client = gspread.authorize(creds)

sheet = client.open('adultCheckupFormatted').sheet1

mappingsheet = client.open('Master Mapping').sheet1

values_list = sheet.col_values(5)

values_list.pop(0)
values_list = list(filter(None, values_list))


mappingColumns = mappingsheet.col_values(5)
mappingColumns = list(filter(None, mappingColumns))


for template in mappingColumns:
    if template not in values_list:
        print(template)
