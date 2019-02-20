# import webbrowser
#select the url you want to open
# url = 'http://docs.python.org/'

# #set browser path
# chrome_path = 'open -c /Applications/Google\ Chrome.app %s'

# #open browser, search URL
# webbrowser.get(chrome_path).open(url)

# import webbrowser 
# import time

# print("Type something:")
# new = 2
# while True:
#     a =  input()
#     url_text = a.split()
#     for i in url_text:
#         if i in ['search', 'open']:
#             url_text.remove(i)
#             if len(url_text) ==2:
#                 print("searching for {}{}.......".format(url_text[0],url_text[1] ))
#                 time.sleep(5)
#                 url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}+{}'.format(url_text[0], url_text[1])
#                 # webbrowser.get(using='google-chrome').open(url,new=new)
#             else:
#                 print("searching for {}....".format(url_text[0]))
#                 time.sleep(5)
#                 url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'.format(url_text[0])
#             webbrowser.get(using='google-chrome').open(url,new=new)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings
import json
import webbrowser
import time

# from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
# from rasa_core.channels.console import ConsoleInputChannel


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    # msg = interpreter.parse(u"what is the weather in newyork")
    # print(json.dumps(msg, indent=2))
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    # print(agent)
    # agent.handle_channel(ConsoleInputChannel())
    # if serve_forever:
    #     agent.handle_channel(ConsoleInputChannel())
    # return agent
    print("Type something:")
    new = 2
    while True:
        a =  input()
        url_text = a.split()
        for i in url_text:
            if i in ['search', 'open']:
                url_text.remove(i)
                if len(url_text) ==2:
                    print("searching for {}{}.......".format(url_text[0],url_text[1] ))
                    time.sleep(5)
                    url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}+{}'.format(url_text[0], url_text[1])
                    webbrowser.get(using='google-chrome').open(url,new=new)
                else:
                    print("searching for {}....".format(url_text[0]))
                    time.sleep(5)
                    url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'.format(url_text[0])
                    webbrowser.get(using='google-chrome').open(url,new=new)    
        if a == 'stop':
            print("bye, Take care")
            break
        responses = agent.handle_text(a)
        # print(responses)
        for response in responses:
            print("chat_bot:", response["text"])      

if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "run":
        run()
