
print("""
    Discord Notification Pusher by Mayu
""")

#imports
from dhooks import Webhook


#prompts
message = ("藍的店2號館的 \"maimai DX International Ver.\" 剛剛開機了!")
url = (<your url>) #insert webhook url
webhookurl = Webhook(url)
webhookurl.send(message)
print("Done sending.")