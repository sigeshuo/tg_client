import asyncio
from contextlib import suppress

from pyrogram import idle

from banner import banner_text
from core.client_manager import ClientManager

client_manager = ClientManager()


async def main():
    print(banner_text)
    await client_manager.load_sessions_and_start()
    user_input_task = asyncio.create_task(process_user_input())
    try:
        await idle()
    finally:
        user_input_task.cancel()
        for app in client_manager.clients.values():
            await app.stop()


async def get_user_input():
    loop = asyncio.get_event_loop()
    message = (
        "\n选择操作:\n"
        "1. 添加帐号\n"
        "2. 查看登录客户端\n"
        "3. {}\n"
        "4. 退出\n"
        "请输入选项: "
    ).format('禁用消息' if client_manager.switch.is_set() else '启用消息')
    return await loop.run_in_executor(None, input, message)


async def process_user_input():
    while True:
        choice = await get_user_input()
        if choice == '1':
            await client_manager.add_account()
        elif choice == '2':
            await client_manager.show_clients()
        elif choice == '3':
            client_manager.change_msg()
        else:
            print("无效选项，请重新选择。")


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
