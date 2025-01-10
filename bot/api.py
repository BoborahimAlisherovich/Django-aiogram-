import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'

def create_user(username,name,user_id):
    url = f"{BASE_URL}/bot-users"
    respose = requests.get(url=url).text
    data = json.loads(respose)
    users_exist = False
    for i in data:
        if i["user_id"] == str(user_id):
            users_exist = True
            break
    if users_exist == False:
      requests.post(url=url,data={"username":username,"name":name,"user_id":user_id})
      return "Foydalanuvchi yaratildi "
    else:
      return "Foydalanuvchi mavjud"

# create_user("Alisherovi","Dasturch","9857575775")

def create_feedback(user_id,body):
    url = f"{BASE_URL}/feedback"
    if body and user_id:
      post = requests.post(url=url,data={"user_id":user_id,"body":body})
      return "adminga yuborildi fikringiz uchun tashakkur"
    else:
      return  "amalga oshmadi"
    
