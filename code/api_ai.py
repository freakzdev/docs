#! /usr/bin/env python
# Main Script: api_ai.py
# PHP script
import os
import requests
import json
import base64
#LOADING ENVIRONMENT VARIABLES
bot_api_host = os.environ.get("BOT_API_HOST")
bot_api_id = os.environ.get("BOT_API_ID")
bot_apy_token = os.environ.get("BOT_API_TOKEN")

def bot_request(module, data, headers={ "Content-Type": "application/json", "Auth": str(bot_api_id), "Authorization": str(bot_apy_token) } ):
  url=str(bot_api_host) + "/api/v1/ai/"+str(module)+"/"
  response = requests.post(url, headers=headers, json=data)
  return response

##### AI MODULE ####
#######################################################################################################################

#### designer: method
params={
  "method": "designer",
  "args": {
    "prompt": "realistic single cog black and white", # Description of the required image
    "n": 1, # Number of images to generate (Max: 5)
    "size": "1024x1024" # Image size ( 1024x1024 | 512x512 | 256x256 )
  }
}
#response = bot_request("composer", params)
#print("JSON Response:", response.json())

#### writer: method
params={
  "method": "writer",
  "args": {
    "instruction": "Redacta una mensaje de felicitación de cumpleaños para los clientes de mi cafetería" # Indication to generate the text
  }
}
#response = bot_request("composer", params)
#print("JSON Response:", response.json())

#### rewriter: method
params={
  "method": "rewriter",
  "args": {
    "input": "Al parecer la implementación del api, no es complicada en lo absoluto", # Text to edit
    "instruction": "Traduce al ruso" # Editing statement
  }
}
#response = bot_request("composer", params)
#print("JSON Response:", response.json())

#######################################################################################################################


##### TRAINING MODULE ####
#######################################################################################################################

#### failover: method
#params={
#  "method": "failover",
#  "args": {
#    "lang": "es"  # Failover module language
#  }
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### learn: method
#params={
#  "method": "learn",
#  "args": {
#    "tag": "ZONA_PRIVADA_006", # Unique identification tag. ( IMPORTANT: This data allows the modification of the learning text )
#    "input": str(base64.b64encode(("Nuestro local cuenta con un salon privado donde bajo reserva tu puedes celebrar pequenños eventos como cumpleaño, reuniones de trabajo, etc.").encode("utf-8")), "utf-8"), # Natural language text
#    "keywords": {}, # Keywords variables
#    "action": {}  # Callback actions
#  }
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### learning_file: method
#params={
#  "method": "learning_file",
#  "args": "https://dev.scriptra.ec/_STORE_/temp/es_trainig_data.xlsx" # URL of the file to upload
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### relearning: method
#params={
#  "method": "relearning",
#  # Does not require additional arguments
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### relearning: method
#params={
#  "method": "relearning",
#  # Does not require additional arguments
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### relearning: learnings_get
#params={
#  "method": "learnings_get",
#  "args": {
#    "format": "json" # File Format: .xlsx | .json
#  }
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())



#### learn: method
####Learning useful prompts. ( Test purpose only )
#params={"method": "learn","args": {"tag": "UNLEARN_001","input": str(base64.b64encode(("Texto a eliminar 1 ").encode("utf-8")), "utf-8"),"keywords": {},"action": {}}}
#response = bot_request("training", params)
#print("JSON Response:", response.json())
#params={"method": "learn","args": {"tag": "UNLEARN_002","input": str(base64.b64encode(("Texto a eliminar 2").encode("utf-8")), "utf-8"),"keywords": {},"action": {}}}
#response = bot_request("training", params)
#print("JSON Response:", response.json())
#params={"method": "learn","args": {"tag": "UNLEARN_003","input": str(base64.b64encode(("Texto a eliminar 3").encode("utf-8")), "utf-8"),"keywords": {},"action": {}}}
#response = bot_request("training", params)
#print("JSON Response:", response.json())
#params={"method": "learn","args": {"tag": "UNLEARN_004","input": str(base64.b64encode(("Texto a eliminar 4").encode("utf-8")), "utf-8"),"keywords": {},"action": {}}}
#response = bot_request("training", params)
#print("JSON Response:", response.json())
#params={"method": "learn","args": {"tag": "UNLEARN_005","input": str(base64.b64encode(("Texto a eliminar 5").encode("utf-8")), "utf-8"),"keywords": {},"action": {}}}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#### unlearn: method
#params={
#  "method": "unlearn",
#  "args": {
#    "tags": [ "UNLEARN_001", "UNLEARN_002", "UNLEARN_003", "UNLEARN_004", "UNLEARN_005" ] # Unique identification tags array
#  }
#}
#response = bot_request("training", params)
#print("JSON Response:", response.json())

#######################################################################################################################


##### BOT MODULE ####
#######################################################################################################################

#### reply: method
#params={
#  "method": "reply",
#  "args": {
#    "input": "Hola buenos días", # User requirement
#    "max": 2 # Maximum number of responses requested (IMPORTANT: In a chatbot it is advisable to request the most matching response)
#    # Solo como prueba, solicitamos las 2 respuestas más coincidentes
#  }
#}
#response = bot_request("bot", params)
#print("JSON Response:", response.json())

#### reply: method
#params={
#  "method": "reply",
#  "args": {
#    "input": "Donde estan ubicados?",
#    "max": 1
#  }
#}
#response = bot_request("bot", params)
#print("JSON Response:", response.json())

#### reply: method
#params={
#  "method": "reply",
#  "args": {
#    "input": "Al parecer no puedes ayudarme que puedo hacer?",
#    "max": 1
#  }
#}
#response = bot_request("bot", params)
#print("JSON Response:", response.json())


#######################################################################################################################


##### WEBHOOK MODULE ####
#######################################################################################################################


#### relearning: set
#params={
#  "method": "set",
#  "args": {
#    "mechanism": "telegram",
#    "config": {
#      "name": "API Bot",
#      "username": "scriptra_bot",
#      "token": "5877083878:AAE7oep-GG0cQin4Dp7N01BEF8Y5SNrvuRo"
#    }
#  }
#}
#response = bot_request("webhook", params)
#print("JSON Response:", response.json())