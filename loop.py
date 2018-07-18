import telepot,time, urllib3
from telepot.loop import MessageLoop
TOKEN=""

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])
        command=msg['text']
        print(command)


proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

#payload = json.loads(request.body.read().decode('utf-8'))

# Keep the program running.
while 1:
    time.sleep(10)