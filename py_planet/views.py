# -*- coding: utf8 -*-

import logging,time,telepot,urllib3,json

from telepot.loop import OrderedWebhook,MessageLoop
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, JsonResponse
from django.views.generic import View
from django.conf import settings

from .utils import parse_planetpy_rss

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

TelegramBot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)

logger = logging.getLogger('telegram.bot')


def _display_help():
    return render_to_string('help.md')

def _display_planetpy_feed():
    return render_to_string('feed.md', {'items': parse_planetpy_rss()})


class CommandReceiveView(View):
    def post(self, request, bot_token):
        if bot_token != settings.TELEGRAM_BOT_TOKEN:
            return HttpResponseForbidden('Invalid token')

        commands = {
            '/start': _display_help,
            'help': _display_help,
            'feed': _display_planetpy_feed,
        }

        def handle(msg):
            logger.info(msg)

            #bot.sendMessage(chat_id, msg['text'])
            cmd=msg['message']['text']
            chat_id = msg['message']['chat']['id']
            func = commands.get(cmd.split()[0].lower())
            if func:
                TelegramBot.sendMessage(chat_id, func(), parse_mode='Markdown')
            else:
                TelegramBot.sendMessage(chat_id, 'I do not understand you, Sir!')

        #bot = telepot.Bot(bot_token)
        #MessageLoop(bot, handle).run_as_thread()
        #webhook = OrderedWebhook(bot,handle=handle)
        response=request.body.decode('utf-8')
        msg=json.loads(response)
        print(msg)
        handle(msg)
        #webhook.feed(data=request.body.decode('utf-8'))
        #webhook.run_as_thread()
        print("Listening..")
        # Keep the program running.
        #while 1:
        #     time.sleep(10)
        return JsonResponse({}, status=200)

