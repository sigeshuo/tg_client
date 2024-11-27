![Python](https://img.shields.io/badge/python-3.10.11-blue.svg)
[![Follow on X](https://img.shields.io/badge/Follow_on_X-1DA1F2?style=flat&logo=x&logoColor=white)](https://x.com/@sigeshuo)
[![Blog](https://img.shields.io/badge/Blog-FF5722?style=flat&logo=blogger&logoColor=white)](https://www.sigeshuo.com)
[![xLog](https://img.shields.io/badge/xLog-4CAF50?style=flat&logo=blogger&logoColor=white)](https://blog.sigeshuo.com)
[![Join Telegram Channel](https://img.shields.io/badge/Join_Telegram_Channel-0088cc?style=flat&logo=telegram&logoColor=white)](https://t.me/sigeshuo_channel)
[![Join Telegram Group](https://img.shields.io/badge/Join_Telegram_Group-0088cc?style=flat&logo=telegram&logoColor=white)](https://t.me/sigeshuo_group)


# 简介

本项目支持登录 Telegram 帐号后导出会话信息。供该会话今年自动登录使用。

本项目支持导出的会话存储方式分为两种：
- Session 文件
- Session 字符串

Session 文件保存会话，会话存放在 `sessions` 文件夹中。

Session 字符串保存会话（默认方式），会话存放在 sessions.txt 文件中。

会话串格式如下：

```plaintext
会话名称|手机号|会话串
```

# 功能

- 添加帐号导出会话
- 批量挂机保活
- 启用/禁用消息

# 作用

基于`Python`的`Telegram`脚本大多数使用`Pyrogram`作为客户端。在使用`Pyrogram`登录后，可以将会话保存下来，以便在后续的脚本中实现自动登录。建议使用字符串的方式来保存会话，这样可以更方便地管理多个账号。通过这种方式，一个文件可以管理成千上万个`Telegram`账号。此外，您还可以利用 Gist 来分批保存会话，并通过远程获取的方式动态地添加或删除会话。

# 准备

使用本项目需要 Telegram Application `API_ID`、`API_HASH`，[申请地址](https://my.telegram.org/)

将申请后的`API_ID`、`API_HASH`配置到`.env`或`docker-compose.yaml`文件的`environment`中。

# 运行

```shell
docker compose run app python3 main.py
```

> 说明
> 
> 频繁的使用三方客户端登录同一个 TG 号容易被风控，风控会清除该号的所有登录会话重新登录。被风控后建议24小时后再使用本工具。