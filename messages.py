# -*- coding: utf-8 -*-
#twitter.com/pijawca
import handlers.scripts.news as a

rss = '\n\n📰 Новости в категории "Интернет" от Яндекса:\n' + \
       '💌 ' + f'[{a.yt}]({a.__yt})\n' + '💌 ' + f'[{a.yt1}]({a.__yt1})\n' + '💌 ' + f'[{a.yt2}]({a.__yt2})\n' + \
       '💌 ' + f'[{a.yt3}]({a.__yt3})\n' + '💌 ' + f'[{a.yt4}]({a.__yt4})\n' + \
       '\n📰 Новости в категории "Гаджеты" от Яндекса:\n' + \
       '💌 ' + f'[{a.yg}]({a.__yg})\n' + '💌 ' + f'[{a.yg1}]({a.__yg1})\n' + '💌 ' + f'[{a.yg2}]({a.__yg2})\n' + \
       '💌 ' + f'[{a.yg3}]({a.__yg3})\n' + '💌 ' + f'[{a.yg4}]({a.__yg4})\n'

MESSAGES = {
    'rss': rss,
}
