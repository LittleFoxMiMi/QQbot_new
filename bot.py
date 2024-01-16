#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
# 引用 nonebot_adapter_mirai2
from nonebot.adapters.mirai2 import Adapter as MIRAI2Adapter


# Custom your logger
#
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(MIRAI2Adapter)


nonebot.load_builtin_plugins()
nonebot.load_plugins("./fox/plugins")


# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.run()
