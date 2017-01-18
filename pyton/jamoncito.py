#!/usr/bin/env python

import logging
import telegram
import random
import sys
import os
import requests
import urllib2  
from urllib2 import HTTPError, URLError
import time
 
LAST_UPDATE_ID = None

def creartxt():
    archi=open('/path/log','w')
    archi.close()

def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot('tu_Api')
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)


def echo(bot):
    global LAST_UPDATE_ID
    
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        foto = 0
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')
        nro=random.randint(0,3)
        msj=message+str(nro)
        
        def grabartxt():
            archi=open('/path/log','w')
            archi.write(time.ctime()+' - '+message+'\n')
            archi.close()

        hola="Holaaa! como va, todo bien?"
        buenDia="Bueeenos dias! No sabes tengo unos jamoncitos para arrancar el dia a pleno."
        chau="Buuu ya te vas? bue despues la seguimos exitos."
        noCmd="Vaya creo que lograste romperme... felicitaciones!"
        noPlayer="Me cagaste a "+message+" no lo tengo pero si pensas que es un jamoncito subilo al drive y vemos de sumarlo. Si podes ponele el nick del agente como nombre a la foto"
        help="Asi que estas queriendo conocer los jamoncitos que tiene el universo de ingress eh pilluelo. Es muy sencillo envia /nick y listo."
        start="Asi que estas queriendo conocer los jamoncitos que tiene el universo de ingress eh pilluelo. Es muy sencillo envia /nick y listo."
        nick="Ta bien pero el nick del jugador que queres mirar."
        noSoyPoringa="Para un cacho mostro no soy poringa."
        adivino="Pero pone algo mas papaaa no soy un puto adivino."
        ponete='Ajajaja ponete y lo charlamos.'
        tb="Genial!"
        ponerla="Mas bien!"
        sapo="Todos cometemos errores."
        verde="Perdonalos no saben lo que hacen."
        dormir="Nos hablamos luego que descanses."
        vos="Claaaro porque pelearle a un bot no es de " + message + " salamin"
        link="https://drive.google.com/folderview?id=0B_EGpfTyOxPDdzliOG5fM2RSc1U&usp=sharing"
        
        print "Fecha y hora actuales: ", time.ctime()
        print "msj: "+message
        mensaje=message
        grabartxt()
        
        if (message == "/help"):
            bot.sendMessage(chat_id=chat_id,text=help)
        elif (message == "/start"):
            bot.sendMessage(chat_id=chat_id,text=help)    
        elif ('ola' in message) or ('olaaa' in message)  or ('ole' in message):
            bot.sendMessage(chat_id=chat_id,text=hola)
        elif ('oy sapo' in message) or ('luminado' in message) or ('oy verde' in message):
            bot.sendMessage(chat_id=chat_id,text=sapo)    
        elif ('odo bien' in message) or ('odo tran' in message) or ('y vos' in message) or ('vos' == message):
            bot.sendMessage(chat_id=chat_id,text=tb)
        elif ('racias' in message) or ('uy amable' in message):
            bot.sendMessage(chat_id=chat_id,text="Cuando quieras "+telegram.Emoji.SMILING_FACE_WITH_OPEN_MOUTH_AND_SMILING_EYES)        
        elif ('uen dia' in message) or ('uenos dias' in message) or ('uen dia' in message):
            bot.sendMessage(chat_id=chat_id,text=buenDia)
        elif ('ue descan' in message) or ('uenas noche' in message):
            bot.sendMessage(chat_id=chat_id,text=dormir)        
        elif (message == '/puto') or (message == '/puta') or (message == '/Puto') or (message == '/Puta') or (message == '/gay') or (message == '/Gay') or (message == 'puto') or (message == 'puta') or (message == 'Puto') or (message == 'Puta') or (message == 'gay') or (message == 'Gay'):
            bot.sendMessage(chat_id=chat_id,text=ponete)
        elif (message == '/gil') or (message == '/Gil') or (message == '/salame') or (message == '/Salame') or (message == '/bobo') or (message == '/Bobo')  or (message == '/menso') or (message == '/pelotudo') or (message == 'gil') or (message == 'Gil') or (message == 'salame') or (message == 'Salame') or (message == 'bobo') or (message == 'Bobo')  or (message == 'menso') or (message == 'pelotudo')  or (message == 'alamin'):
            bot.sendMessage(chat_id=chat_id,text=vos+" "+telegram.Emoji.UNAMUSED_FACE)    
        elif ('ueres' in message) or ('onerla' in message) or ('amos a' in message) or ('os gros' in message) or ('lamame' in message):
            bot.sendMessage(chat_id=chat_id,text=ponerla)
        elif ('ue paja' in message) or ('burrido' in message):
            bot.sendMessage(chat_id=chat_id,text="Mal")            
        elif ('chau' in message) or ('Chau' in message) or ('adios' in message) or ('Adios' in message) or ('e voy' in message):
            bot.sendMessage(chat_id=chat_id,text=chau)            
        elif ('orete' in message) or ('ierda' in message) or (message == "/kk") or ('aca' in message):    
            bot.sendMessage(chat_id=chat_id, text=telegram.Emoji.PILE_OF_POO)
        elif ('e amo' in message) or ('e quiero' in message) or ('oy pitufo' in message):    
            bot.sendMessage(chat_id=chat_id,text="Aaaaawwww yo tambien "+telegram.Emoji.BLUE_HEART)
        elif ('os azules' in message) or ('os pitufo' in message):    
            bot.sendMessage(chat_id=chat_id,text="Tienen aguante!")    
        elif ('os sapos' in message) or ('os verdes' in message) or ('os iluminad' in message) or ('apo puto' in message):    
            bot.sendMessage(chat_id=chat_id,text=verde)
        elif ('ulos' in message) or ('orno' in message) or ('etas' in message) or ('utas' in message) or ('esnud' in message) or ('pitos' in message):    
            bot.sendMessage(chat_id=chat_id,text=noSoyPoringa)        
        elif ('esistencia' in message):        
            bot.sendMessage(chat_id=chat_id, text=telegram.Emoji.BLUE_HEART+" "+telegram.Emoji.BLUE_HEART+" "+telegram.Emoji.BLUE_HEART)
        elif ('aja' in message):        
            bot.sendMessage(chat_id=chat_id, text="Jajaja "+telegram.Emoji.SMILING_FACE_WITH_OPEN_MOUTH_AND_SMILING_EYES)    
        elif ('buena que est' in message) or ('bueno que est' in message) or ('bueno est' in message) or ('buena est' in message) or ('ue perr' in message) or ('ue fuerte que est' in message):        
            bot.sendMessage(chat_id=chat_id, text="Si, como tu hermana.")       
        elif (message == "/"):
            bot.sendMessage(chat_id=chat_id,text=adivino)
        elif (message == "/VamoLoPibe") or (message == "/vamolopibe")  or ('oPibe' in message) or ('opibe' in message):
            bot.sendPhoto(chat_id=chat_id,photo='http://mabregu.xyz/img/tg/vamolopibe.jpg')        
        elif (message == "/nick"):
            bot.sendMessage(chat_id=chat_id,text=nick)
        elif (message == "/jamoncito") or (message == "/Jamoncito"):
            bot.sendDocument(chat_id=chat_id,document='http://mabregu.xyz/img/tg/jamoncito.gif')
        elif ('estoy sol' in message) or ('anas de co' in message) or ('omerla' in message) or ('anas de garch' in message) or ('amos a garch' in message) or ('vamos a co' in message) or ('r a dormir' in message) or ('archar' in message) or ('ulear' in message):
            bot.sendMessage(chat_id=chat_id, text=telegram.Emoji.SMIRKING_FACE)
        elif ('omida' in message) or ('ambre' in message) or ('cenar' in message) or ('lmorza' in message) or ('omer' in message):        
            bot.sendMessage(chat_id=chat_id, text=telegram.Emoji.FRENCH_FRIES)
        elif (message == "/cargar"):
            bot.sendMessage(chat_id=chat_id, text=link)
        elif (message == "/lista"):
            bot.sendMessage(chat_id=chat_id, text="/AzulCeleste\n/lalii\n/marian522\n/Zoenice\n/LadyGotham\n/shadowlady9\n"
            +"/Katvinci\n/V4NS25K\n/UMAQueen\n/Hadanna")
        else:
            try:
                r = requests.get("http://mabregu.xyz/img/tg"+msj+".jpg")
                r1 = requests.get("http://mabregu.xyz/img/tg"+mensaje+".jpg")	
                
                if (r.status_code == 200) :
                    print('Todo Ok!')
                    bot.sendPhoto(chat_id=chat_id,photo='http://mabregu.xyz/img/tg'+msj+'.jpg')
                elif (r1.status_code == 200) :
                    bot.sendPhoto(chat_id=chat_id,photo='http://mabregu.xyz/img/tg'+mensaje+'.jpg')
                elif (r.status_code == 404) :
                    bot.sendMessage(chat_id=chat_id,text=noPlayer)
                else :
                    print('Baia baia no anda!')
                    bot.sendMessage(chat_id=chat_id,text=noPlayer)

            except HTTPError, e:  
                print 'Ocurrio un error'
                print e.code
                bot.sendMessage(chat_id=chat_id,text=noCmd)
            except URLError, e:  
                print "Ocurrio un error"
                print e.reason
                bot.sendMessage(chat_id=chat_id,text=noCmd)
	LAST_UPDATE_ID = update.update_id + 1
if __name__ == '__main__':
    main()
