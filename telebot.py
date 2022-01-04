#!/usr/bin/env python
# coding: utf-8

# In[2]:

TOKEN = "5086123846:AAFnJQhbgPH38uW7SYZnoF2gZ9JCSMtz5Xw"
import telegram
bot = telegram.Bot(TOKEN)
if bot.get_updates():
    chat_id = bot.get_updates()[-1].message.chat_id
    video = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"
    bot.send_video(chat_id, video)

