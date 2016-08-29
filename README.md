# pythonSkypeBot

Python Wrapper for Skype Bot API

##Initial Recommedation :
Read through this guide before beginning bot development [Skype v3 bot Development](https://docs.botframework.com/en-us/support/upgrade-to-v3/), [Activities](https://docs.botframework.com/en-us/csharp/builder/sdkreference/activities.html) [Attachments, Cards, Actions](https://docs.botframework.com/en-us/skype/getting-started/#navtitle)

##Requirements :

1. This API is tested with Python 2.7.
2. Client id and Client Secret from the app you will create on [Register a Bot](https://dev.botframework.com/bots/new)
3. Flask should be installed.
4. A webhook to receive messages. I used ngrok for development and created my own webhook using this --> [Create Proxy based Webhooks for Multiple Bots](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)

##Writing your First Bot

A template main.py is provided. You should use that as your bot page.

###Simple Echo Bot

```
import skypebot

client_id = 'The id from skype bot framework'
client_secret = 'The secret you get from you know from where :P'

bot = skypebot.SkypeBot(client_id,client_secret)

@app.route('/', methods=['POST'])
def webhook():
  if request.method == 'POST':
    try:
        data = json.loads(request.data)
        
        process_message(data)
        
    except Exception as e:
      print (traceback.format_exc()) # something went wrong

  return 'Ok'

def process_message(data):
  sender = data['conversation']['id']
  bot.send_message(sender,"Hello, lets have fun.")
  
if __name__ == '__main__':

    context = ('/etc/ssl/localcerts/mycert.pem', '/etc/ssl/localcerts/mykey.key')

    app.run(host='127.0.0.1',port=8000,debug=False,ssl_context=context)
```


###When you Add Bot for 1:1 Conversation

<img src="https://docs.botframework.com/en-us/images/skype/skype-bot-profile.png" alt="screenshot"><img src="https://docs.botframework.com/en-us/images/skype/skype-bot-welcome.png" alt="screenshot">

```
if data['type'] == 'contactRelationUpdate':
  if data['action']=='add':
        sender = data['conversation']['id']
        bot.send_message(sender,"Welcome! To start a new game, send the <b>start</b> command. To get your score, you can use the <b>score</b> command. If you need help, send the <b>help</b> command.")
        pass
    elif data['action']=='remove':
        pass
    else:
        pass
```


###Conversation in Groups

<img src="https://docs.botframework.com/en-us/images/skype/skype-bot-at-mention.png" alt="screenshot">

```
if data['type'] =='message':
    if 'isGroup' in data['conversation'].keys():
        sender = data['conversation']['id']
        # id's are in this form on skype and sent inside the text message when bot is mentioned <at id="28:ce34f9cda-4ae1-4161-sw8f-7548e9482d07">test</at>
          # So you need to handle these id's, you can use regex to match pattern like these in groups.
```


###Create Buttons

| Action Type       | Content of value property |
| ------------- |:-------------:| -----:|
| openUrl       | URL to be opened in the built-in browser.  |
| imBack      | Text of message which client will sent back to bot as ordinary chat message. All other participants will see that was posted to the bot and who posted this.    |
| call  | Destination for a call in following format: "tel:123123123123"   |
|showImage |show image referenced by URL |

Tip : You can use meta tags in imBack action to send hidden information.

```
button1 = bot.create_buttons("imBack","test1","testing success")
button2 = bot.create_buttons("openUrl","test3","https://www.youtube.com/watch/?v=pAHjNyJHllc")
```


##Attachment Cards

1. Hero card
2. Thumbnail card
3. Carousel card (with hero or thumbnail images)
4. Sign in card #Not Implemented in this wrapper
5. Receipt card #Not implemented in this wrapper

###Send Hero Card Attachment

<img src="https://docs.botframework.com/en-us/images/skype/skype-bot-hero-card.png" alt="screenshot">

```
def process_message(sender,text):

            button1 = bot.create_buttons("imBack","test1","testing success")
            button2 = bot.create_buttons("openUrl","test3","https://www.youtube.com/watch/?v=pAHjNyJHllc")
            
            url = 'https://i.ytimg.com/vi/EIu0_NVhrmM/hqdefault.jpg'
            img1 = bot.create_card_image(url,alt="hello")
            
            #here in place of `hero` you can specify `thumbnail` to send thumnail card.  
            attachment1 = bot.create_card_attachment("hero","hero card test",subtitle="hero card subtitle",text="card text",images=[img1],buttons=[button1,button2])

            bot.send_card(sender,"carousel", [attachment1],text="hello")
```

###Send Carousel Attachment

<img src="https://docs.botframework.com/en-us/images/skype/skype-bot-carousel-card.png" alt="screenshot">

```
# 5 Cards in 1 carousel

            button1 = bot.create_buttons("imBack","test1","testing success")
            button2 = bot.create_buttons("openUrl","test3","https://www.youtube.com/watch/?v=pAHjNyJHllc")
            
            url = 'https://i.ytimg.com/vi/EIu0_NVhrmM/hqdefault.jpg'
            img1 = bot.create_card_image(url,alt="hello")
            
            #here in place of `hero` you can specify `thumbnail` to send thumnail card.  
            attachment1 = bot.create_card_attachment("hero","hero card test",subtitle="hero card subtitle",text="card text",images=[img1],buttons=[button1,button2])

            bot.send_card(sender,"carousel", [attachment1,attachment1,attachment1,attachment1,attachment1],text="hello")
```

###Send Media Attachment

| Property       | Description |
| ------------- |:-------------:| -----:|
| content type      | mimetype/contenttype of the URL |
| content url      |a link to the actual file  |

```
def process_message(sender,text):

  bot.send_media(sender,"image/jpg", 'http://foo.com/1312312 ')
```

###To Do's

1. Message Handlers (Done, will update if other contribute for its development)
2. Threading (Done, will update if other contribute for its development)
3. Async Version
4. Support for other channel, (Not a priority at all)
5. JWT Security Support


####This is the first wrapper for skype bot api. I tried to keep it really simple from understanding point of view. If you feel that you have something to contribute and imporve this wrapper, you are welcome to send pull requests.

I will mention every person's name who will contribute for it's developement.

I hope you all will accept this initial start from me and start creating bots in python for skype too.



##Bots created using this API Wrapper

<a href="https://www.youtube.com/watch?v=SxTkIG-YlkQ
" target="_blank"><img src="https://img.youtube.com/vi/SxTkIG-YlkQ/maxresdefault.jpg" 
alt="Sift Bot for Skype" width="420" height="315" border="10" /></a>


