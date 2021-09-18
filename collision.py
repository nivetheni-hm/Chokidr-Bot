import time

# from ipfshttpclient.client import Client
import text
import time
from googletrans import Translator

# Destination language for translation
dest = 'en'
translator = Translator()

# Conversation flow for collision

Bot = []
User = []

# user input
def UserResponse(message):
  if message == text.text14:
      collision_Call()

  if message == text.text16:
      translated18 = translator.translate(text.text18, src='en', dest=dest)
      reply = translated18.text
      print('Bot: ' + reply)
      Bot.append("BOT:" + reply)
      collision_ProblemConfirmation()
   
  if message == text.text13:
      translated17 = translator.translate(text.text17, src='en', dest=dest)
      reply = translated17.text
      print('Bot: ' + reply)
      Bot.append("BOT:" + reply)
      collision_ProblemConfirmation()

  if message == text.text15:
      translated8 = translator.translate(text.text8, src='en', dest=dest)
      reply = translated8.text
      print('Bot: ' + reply)
      Bot.append("BOT:" + reply)
      collision_End()
    
    
# initial alert message
def Collision():
    translated1 = translator.translate(text.text1, src='en', dest=dest)
    print("BOT:" + translated1.text)
    Bot.append("BOT:" + translated1.text)
    # time.sleep(1)
    # return collision_Location()

# location details
def collision_Location(location):
    translated2 = translator.translate(text.text2, src='en', dest=dest)
    print("BOT:" + translated2.text)
    Bot.append("BOT:" + translated2.text)
    message = ("LATITUDE = " + location['latitude'] + '\n'
          "LONGITUDE = " + location['longitude'] + '\n'
          "DIRECTION = " + location['direction'])
    print(message)
    Bot.append(message)
    # time.sleep(1)
    # return collision_Details()

# details about the collision
def collision_Details(vehicle_info):
    translated3 = translator.translate(text.text3, src='en', dest=dest)
    print("BOT:" + translated3.text)
    Bot.append("BOT:" + translated3.text)
    message = ("TYPE OF VEHICLE = " + vehicle_info['type'] + '\n'
               "VEHICLE REGISTRATION NUMBER = " + vehicle_info['registrationNumber'])
    print(message)
    Bot.append(message)
    # time.sleep(1)
    # return collision_Livestatus()

# live information of the incident
def collision_Livestatus():
    translated4 = translator.translate(text.text4, src='en', dest=dest)
    print("BOT:" + translated4.text)
    Bot.append("BOT:" + translated4.text)
    # time.sleep(1)
    # return collision_EmergencyNum()

# listing the emergency numbers
def collision_EmergencyNum():
    translated5 = translator.translate(text.text5, src='en', dest=dest)
    print("BOT:" + translated5.text)
    Bot.append("BOT:" + translated5.text)
    message = ("For Ambulance dial 108" + '\n'
               "For Police Station dial 100")
    print(message)
    Bot.append(message)
    # time.sleep(1)
    # return collision_Call()

# getting confirmation whether the call is made
def collision_Call():
    translated6 = translator.translate(text.text6, src='en', dest=dest)
    translated7 = translator.translate(text.text7, src='en', dest=dest)
    print("BOT:" + translated6.text)
    Bot.append("BOT:" + translated6.text)
    # time.sleep(3)
    #time.sleep(300)
    print("BOT:" + translated7.text)
    Bot.append("BOT:" + translated7.text)
    message = input('Human: ')
    User.append(message)
    UserResponse(message)

# getting confirmation whether the incident is resolved
def collision_ProblemConfirmation():
    translated9 = translator.translate(text.text9, src='en', dest=dest)
    print("BOT:" + translated9.text)
    message = input('Human: ')
    User.append(message)
    UserResponse(message)

# getting confirmation from all stakeholders
def collision_End():
    translated10 = translator.translate(text.text10, src='en', dest=dest)
    translated11 = translator.translate(text.text11, src='en', dest=dest)
    print("BOT:" + translated10.text)
    Bot.append("BOT:" + translated10.text)
    print("BOT:" + translated11.text)
    Bot.append("BOT:" + translated11.text)

