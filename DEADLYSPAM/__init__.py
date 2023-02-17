import os





if CLI_TYPE.startwith("T"):
    print("[INFO]Starting SpamUserbot with Telethon Clients")
    try:
        if STRING1:
            print("[INFO] STRING1 found so Booting.. ") 
            cli1 = TelegramClient(StringSession(STRING1), API_ID, API_HASH)
        else:
            Print("[INFO] STRING1 Not found, Skipping.. ") 
        if STRING2:
            print("[INFO] STRING2 found so Booting.. ") 
            cli2 = TelegramClient(StringSession(STRING2), API_ID, API_HASH)
        else:
            Print("[INFO] STRING2 Not found, Skipping.. ") 
        if STRING3:
            print("[INFO] STRING3 found so Booting.. ") 
            cli3 = TelegramClient(StringSession(STRING3), API_ID, API_HASH)
        else:
            Print("[INFO] STRING3 Not found, Skipping.. ") 
        if STRING4:
            print("[INFO] STRING4 found so Booting.. ") 
            cli4 = TelegramClient(StringSession(STRING4), API_ID, API_HASH)
        else:
            Print(" [INFO] STRING4 Not found, Skipping..")
else:
    print("[INFO]Starting SpamUserbot with Pyrogram Client")
    try:



print("[INFO] Processing To Development!") 


