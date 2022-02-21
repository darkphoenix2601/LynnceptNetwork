import os
os.system('clear')

welcome = """
Welcome to session string generator
​
Get the pyrogram & telethon session string from here
​
Get your API_ID and API_HASH from my.telegram.org
"""
print(welcome)

lib = """
Choose session string type:
​
p - Pyrogram 
t - Telethon 
q - stop all process
​
"""
ask = input(lib)

if ask == "p":
	print("\nyou selected Pyrogram")
	import pyrogram
	API_ID = input("Enter your API_ID : ")
	API_HASH = input("Enter your API_HASH : ")
 
	with pyrogram.Client(":memory:", api_id=API_ID, api_hash=API_HASH) as client:
	  session_str = client.export_session_string()
	  info = client.get_me()
	  fname = info.first_name
	  if info.is_bot == True:
	      id_send = input(f"I see, You gave the Bot Token to Generate String Session, \nStart the {info.username}\nSend /id to @Miss_AkshiV1_Bot and Enter the ID which She gave: ")
	      msg = client.send_message(id_send, f"```{session_str}```")
	      msg.reply_text("""☝️ This is your Pyrogram String Session of this Bot
        ​        
        💭 Join @LynnceptNetwork""")
	      exit("Check the Bot PM to get the String Session")
     
	  msg = client.send_message("me", f"`{session_str}`")
	  msg.reply_text("""
👆 This is your pyrogram string session
​
💭 Join @LynnceptNetwork
""")
	  print(f"\nSuccessfully Logged in as {fname}  \n\nCheck the User's Saved Messages for the Pyrogram String Session")
 
elif ask == "t":
	print("\nyou selected Telethon")
	from telethon.sync import TelegramClient
	from telethon.sessions import StringSession
 
	API_ID = input("Enter your API_ID : ")
	API_HASH = input("Enter your API_HASH : ")
 
	with TelegramClient(StringSession(), API_ID, API_HASH) as client:
		session_str = client.session.save()
		msg = client.send_message("me", f"`{session_str}`")
		msg.reply("""
👆 This is your telethon session string.
​
💭 Join @LynnceptNetwork
""")
		print("\nCheck your saved messages for the Telethon String Session")
 
elif ask == "q":
	print("stopped all proccess")
	exit()
 
else:
  print("""
  Invalid Option Selected
  Please only Choose between p/t
  Stopping all Process
  Restart Replit
""")
