
print("""
    Discord Notification Pusher by Mayu
""")

#imports
from dhooks import Webhook


#prompts
message = ("Hello World!")
url = (<your url>) #insert webhook url
webhookurl = Webhook(url)
webhookurl.send(message)
print("Done sending.")
