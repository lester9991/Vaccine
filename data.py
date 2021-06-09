from pprint import pprint
import openpyxl
import pandas

data = pandas.read_excel("Paid Vaccination Drive - Kandarpada Extension (Responses).xlsx", index_col=False)
x = data.to_dict(orient="records")

user = {(str(item['AadhaarNumber']), item['Contact number']): item for item in x}



def check_user(info):
    if info in user:
        return True
    else:
        return False
def get_info(info):
    return user[info]