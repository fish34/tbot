# -*- coding: utf8 -*-

import requests
import json


def crypto():
  items = []
  marketcurrencies = ['ETH','BTC','']
  basecurrencies = ['BTC','USDT']
  public = 'https://bittrex.com/api/v1.1/public/'
  template = 'for market {} last currency price is {}'

  # инициируем запрос на получение маркета
  r = requests.post(public+'getmarkets',
                    data={
                        })

  # разбираем ответ сервера
  j = json.loads(r.text)
  if j['success']:
      res=j['result']
      for r in res:
          if r['MarketCurrency'] in marketcurrencies and r['BaseCurrency'] in basecurrencies:
              item={}
              ticker = requests.post(public+'getticker?market='+r['MarketName'])
              j = json.loads(ticker.text)
              item['market'] = r['MarketName']
              item['ticker'] = round(j['result']['Last'],4)
              items.append(item)
              #return(template.format(r['MarketName'],j['result']['Last']))
  return items

def fiat():
    items=[]
    template="http://free.currencyconverterapi.com/api/v5/convert?q={}&compact=ultra"
    curs="USD_RUB,EUR_RUB"
    r = requests.get(template.format(curs))
    print(r.text)
    j=json.loads(r.text)
    for k,v in j.items():
        items.append({'market':k.replace("_","-"),'ticker':round(v,4)})
    return items
