from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message, Bot
from nonebot.params import CommandArg
import time
from fox.check import qq_check

test = on_command("test", rule=to_me(), aliases={"测试"}, block=True)
Echo = on_command("echo", rule=to_me, block=True)

super_user = "./fox/data/config/superuser.txt"


@test.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if not await qq_check(event.get_user_id(), super_user):
        await test.finish("雪豹闭嘴")
    args = str(event.get_message()).strip().split(" ")
    args = args[1:]
    if len(args) != 0:
        state["par"] = args[0]


@test.got("par", prompt="1.获取系统时间\n2.测试命令")
async def test_handle(bot: Bot, event: Event, state: T_State):
    par = state["par"]
    msg = await test_mission(par)
    await test.finish(msg)


async def test_mission(par):
    if par == "1":
        localtime = time.asctime(time.localtime(time.time()))
        return localtime
    elif par == "2":
        return "test"
    else:
        return "错误的参数"


@Echo.handle()
async def _(bot: Bot, event: Event, msg: Message = CommandArg()):
    if not await qq_check(event.get_user_id(), super_user):
        await Echo.finish("雪豹闭嘴")
    msg = str(msg).strip()
    if msg == "":
        await Echo.finish("女子")
    else:
        await Echo.send(msg)
        await bot.call_api("sendMessage", msg)
        await Echo.finish(msg)
