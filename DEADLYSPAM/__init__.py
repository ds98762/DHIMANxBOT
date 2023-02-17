import os
from telethon import TelegramClient
from pyrogram import Client
from config import API_ID, API_HASH, STRING1, STRING2, STRING3, STRING4, STRING5


# CLIENT 1
if STRING1.endswith("=")::
    print("[TELETHON] STRING1 Found! Booting.. ") 
    cli1 = TelegramClient(StringSession(STRING1), API_ID, API_HASH)
else:
    Print("[PYROGRAM] STRING1 Found! Booting..") 
    cli1 = Client(session_name=STRING1, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLYSPAM.pyrogram"))
else:
    print("[INFO] STRING1 not Found! Skipped ⭐") 
    cli1 = None

# CLIENT 2
if STRING2.endswith("=")::
    print("[TELETHON] STRING1 Found! Booting.. ") 
    cli2 = TelegramClient(StringSession(STRING2), API_ID, API_HASH)
else:
    Print("[PYROGRAM] STRING2 Found! Booting..") 
    cli2 = Client(session_name=STRING2, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLYSPAM.pyrogram"))
else:
    print("[INFO] STRING2 not Found! Skipped ⭐") 
    cli2 = None

# CLIENT 3
if STRING3.endswith("=")::
    print("[TELETHON] STRING3 Found! Booting.. ") 
    cli3 = TelegramClient(StringSession(STRING3), API_ID, API_HASH)
else:
    Print("[PYROGRAM] STRING3 Found! Booting..") 
    cli3 = Client(session_name=STRING3, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLYSPAM.pyrogram"))
else:
    print("[INFO] STRING3 not Found! Skipped ⭐") 
    cli3 = None

# CLIENT 4
if STRING4.endswith("=")::
    print("[TELETHON] STRING4 Found! Booting.. ") 
    cli4 = TelegramClient(StringSession(STRING4), API_ID, API_HASH)
else:
    Print("[PYROGRAM] STRING4 Found! Booting..") 
    cli4 = Client(session_name=STRING4, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLYSPAM.pyrogram"))
else:
    print("[INFO] STRING4 not Found! Skipped ⭐") 
    cli4 = None

# CLIENT 5
if STRING5.endswith("=")::
    print("[TELETHON] STRING5 Found! Booting.. ") 
    cli5 = TelegramClient(StringSession(STRING5), API_ID, API_HASH)
else:
    Print("[PYROGRAM] STRING5 Found! Booting..") 
    cli5 = Client(session_name=STRING5, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLYSPAM.pyrogram"))
else:
    print("[INFO] STRING5 not Found! Skipped ⭐") 
    cli5 = None

