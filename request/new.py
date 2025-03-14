import requests
import json

url = "https://api.chatanywhere.tech/v1/audio/speech"

payload = json.dumps({
   "model": "tts-1",
   "input": "The quick brown fox jumped over the lazy dog.",
   "voice": "alloy"
})
headers = {
   'Authorization': 'Bearer sk-CkZhCX8L86AaF9075485T3BLBkFJ913984F70b42477b8B7f',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
