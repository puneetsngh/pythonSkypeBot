# -*- coding: utf-8 -*-
import requests
import json
import traceback
import sys

import time
from datetime import *
from time import *
import os
import re
import base64

from sys import version_info
import string

reload(sys)
sys.setdefaultencoding('utf8')

#text should be UTF-8 and has a 320 character limit

def send_message(token,service,sender,text):
    try:
        payload = {
                    "type": "message",
                    "text": text
                    }
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',headers={"Authorization": "Bearer "+token,"Content-Type":"application/json"},json=payload)

        print r

    except Exception as e:
        print e
        pass
        

        
#openUrl  URL to be opened in the built-in browser.  
#imBack  Text of message which client will sent back to bot as ordinary chat message. All other participants will see that was posted to the bot and who posted this.  
#postBack  Text of message which client will post to bot. Client applications will not display this message.  
#call  Destination for a call in following format: "tel:123123123123"  
#playAudio  playback audio container referenced by URL  
#playVideo  playback video container referenced by URL  
#showImage  show image referenced by URL  
#downloadFile  download file referenced by URL  
#signin  OAuth flow URL  


def create_buttons(type,title,value):

	buttons_dict={}
	buttons_dict["type"] = type
	buttons_dict["title"] = title
	#buttons_dict['image'] = image
	buttons_dict["value"] = value
	
	return buttons_dict
	
	
def create_card_image(url,alt):
	img_dict = {}
	img_dict["url"] = url
	img_dict["alt"] = alt
	return img_dict
	
def create_card_attachment(type,title,subtitle,text,images,buttons):
    card_attachment={}
    card_attachment={
		"contentType": "application/vnd.microsoft.card."+type,
		"content": {
			"title": title,
			"subtitle": subtitle,
            "text": text,
			"images": images,
			"buttons": buttons
            }
        }
    
    return card_attachment



def send_media(token,service,sender,type,url):
    try:
        response = requests.get(url).content
        
        payload = {
            "type":"message",  
            "attachments": [{
                "contentType":type,
                "contentUrl": url
            }]
        }
        
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',headers={"Authorization": "Bearer "+token,"Content-Type":"application/json"},json=payload)
        print r
    except Exception as e:
        print e
        pass
        
        
	
	
def send_card(token,service,sender,type,card_attachment,summary,text):
    try:
        payload = {
        "type":"message,
        "attachmentLayout":type,
        "summary":summary,
        "text":text,
        "attachments":card_attachment
        }
        
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',headers={"Authorization": "Bearer "+token,"Content-Type":"application/json"},json=payload)
        print payload
        print r
    except Exception as e:
        print e
        pass
        
#typing action not yet supported
        
def send_action(token,service,sender):
    try:
        payload = {
            "type":"typing"
        }
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',headers={"Authorization": "Bearer "+token,"Content-Type":"application/json"},json=payload)
        print payload
        print r
    except Exception as e:
        print e
        pass


def create_animation(type,url,images,title,subtitle,text,buttons):
    card_animation={}
    card_animation={
        "contentType": "application/vnd.microsoft.card."+type,
        "content": {
            "autoloop":True,
            "autostart":True,
            "shareable":True,
            "media":[{"profile":"gif","url":url}],
            "title": title,
            "subtitle": subtitle,
            "text": text,
            "images": images,
            "buttons": buttons
            }
        }
    
    return card_animation
