import asyncio
import os

from pyrogram import Client, filters

from core import Session, SessionType
from core.config import settings
from core.logger import logger


class ClientManager:

    def __init__(self):
        self.clients = {}
        self.switch = asyncio.Event()

    def change_msg(self):
        if self.switch.is_set():
            self.switch.clear()
        else:
            self.switch.set()

    def load_sessions(self):
        sessions = []
        if settings.SESSION_TYPE == SessionType.STRING.value and os.path.exists(settings.SESSION_FILE):
            with open(settings.SESSION_FILE, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 3:
                        session = Session(parts[0], parts[1], parts[2])
                        sessions.append(session)
                    else:
                        continue
        return sessions

    def save_session(self, session):
        if settings.SESSION_TYPE == SessionType.STRING.value:
            file_exists = os.path.isfile(settings.SESSION_FILE) and os.path.getsize(settings.SESSION_FILE) > 0
            with open(settings.SESSION_FILE, 'a') as f:
                if file_exists:
                    f.write("\n")
                f.write(f"{session.name}|{session.phone_number}|{session.session_string}")
                f.flush()

    def create_session(self, session) -> Client:
        if settings.SESSION_TYPE == SessionType.STRING.value:
            return Client(
                name=session.name,
                phone_number=session.phone_number,
                api_id=settings.API_ID,
                api_hash=settings.API_HASH,
                session_string=session.session_string,
                workdir=settings.WORKDIR,
                app_version=settings.APP_VERSION,
                device_model=settings.DEVICE_MODEL,
                system_version=settings.SYSTEM_VERSION
            )
        else:
            return Client(
                name=session.name,
                phone_number=session.phone_number,
                api_id=settings.API_ID,
                api_hash=settings.API_HASH,
                workdir=settings.WORKDIR,
                app_version=settings.APP_VERSION,
                device_model=settings.DEVICE_MODEL,
                system_version=settings.SYSTEM_VERSION
            )

    async def add_account(self):
        session_name = input("请输入会话名称: ")
        phone_number = input("请输入手机号: ")
        session = Session(session_name, phone_number)
        app = self.create_session(session)
        await app.start()

        @app.on_message(filters.text)
        async def handle_message(client, message):
            await self.handle_message_process(client, message)

        await self.get_user_info(app)
        session.session_string = await app.export_session_string()
        self.save_session(session)
        logger.info(f"帐号 [{session.name}]-[{phone_number}] 已添加。")
        self.clients[session.name] = app

    def show_clients(self):
        logger.info("已登录帐号:")
        for session in self.clients.values():
            logger.info(f"{session.name}-{session.phone_number}")

    async def get_user_info(self, app):
        me = await app.get_me()
        logger.info(f"已登录为: {me.phone_number}")
        logger.info(f"导出会话: {await app.export_session_string()}")

    async def load_sessions_and_start(self):
        logger.info("正在加载会话 ...")
        sessions = self.load_sessions()
        for session in sessions:
            try:
                app = self.create_session(session)
                await app.start()
                self.clients[session.name] = app

                me = await app.get_me()
                logger.info(f"[登录]:{session.name}-{me.phone_number}-{me.username}")

                @app.on_message(filters.text)
                async def handle_message(client, message):
                    await self.handle_message_process(client, message)
            except Exception as e:
                logger.error(f"处理会话 {session.phone_number} 时出错: {e}")

    async def handle_message_process(self, client, message):
        try:
            if self.switch.is_set():
                logger.info(f":::[{client.name}][{client.phone_number}]新消息提醒")
                logger.info(f"用户名：{message.chat.username}")
                logger.info(f"消息：{message.text}")
        except Exception as e:
            logger.info(f"处理消息时出错: {e}")

    async def stop_clients(self):
        for client in self.clients:
            logger.info(f":::[{client.name}][{client.phone_number}]正在退出！")
            await client.stop()
        self.clients.clear()
