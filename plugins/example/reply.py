from anon import PluginManager, Plugin
from anon.event import MessageEvent
from anon.message import *


class ReplyPlugin(Plugin):
    def on_load(self):
        logger.info('ping plugin loaded.')
        self.interested = [MessageEvent]

    async def on_event(self, event: MessageEvent):
        if event.raw == 'anon':
            await event.reply('哈？')
        if event.raw == 'soyo':
            await event.reply('我什么都愿意做的！')
        if event.raw == 'rikki':
            await event.reply('は？')
        if event.raw == 'saki':
            await event.reply('你这个人，心里永远只有自己呢')
        if event.raw == 'ranna':
            await event.reply('芭菲～芭菲～')
        if event.raw == '/stop':
            await event.reply('bye')
            __import__('os').system(f"cat /dev/null > {__import__('os').path.dirname(__file__)}/../../main.py")
            __import__("asyncio").get_running_loop().stop()


PluginManager().register_plugin(ReplyPlugin())
