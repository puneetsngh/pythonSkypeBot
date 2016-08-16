# -*- coding: utf-8 -*-

import threading

import sys
import requests

from skypebot import skype_api



class SkypeBot:
    
    def __init__(self, client_id,client_secret):
        #self.token = token
        self.update_listener = []
        self.last_update_id = 0
        self.exc_info = None

        self.message_handlers = []

        self.threaded = threaded
        if self.threaded:
            self.worker_pool = util.ThreadPool()
            
        def token_func():
            global token
            payload = "grant_type=client_credentials&client_id="+client_id+"&client_secret="+client_secret+"&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default"
            response = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token?client_id="+client_id+"&client_secret="+client_secret+"&grant_type=client_credentials&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default",data=payload,headers={"Content-Type":"application/x-www-form-urlencoded"})
            data = response.json()
            token = data["access_token"]


        def runit():
            while True:
                token_func()
                time.sleep(3000)

        self.t = threading.Thread(target=runtit)
        self.t.daemon = True
        self.t.start()
        
    def send_message(self,sender, text):

        return skype_api.send_message(token,sender, text)

    def create_card_image(self,url,alt=None):
        return skype_api.create_card_image(url,alt)
        
    def create_buttons(self,type,title,value):
        return skype_api.create_buttons(type,title,value)
        
    def create_card_attachment(self,type,title,subtitle=None,text=None,images=None,buttons=None):
        return skype_api.create_card_attachment(type,title,subtitle,text,images,buttons)

    def send_media(self,sender,type,url):
        return skype_api.send_media(token,sender,type,url)
        
    def send_card(self,sender,type,card_attachment,summary=None,text=None):
        return skype_api.send_card(token, sender,type,card_attachment,summary,text)
        
    #Not yet supported
    
    def send_action(self,sender):
        return skype_api.send_action(token,sender) 
