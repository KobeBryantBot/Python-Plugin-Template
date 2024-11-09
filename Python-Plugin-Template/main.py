import LoggerAPI

logger = LoggerAPI.Logger("Python-Plugin-Template")


# 这里写插件加载时需要执行的操作
def on_enable():
    logger.info("Python插件模板已加载")


# 这里写插件加载时需要执行的操作
def on_disable():
    # 卸载插件时，你需要释放插件的所有资源
    # 你需要在这里执行清理全部后台任务，结束全部线程等操作
    # 其中监听的事件、注册的命令可以不手动清理，系统会自动清理
    # 仅使用 KobeBryant 提供的 ScheduleAPI 添加的定时任务可以不手动清理，系统会自动清理
    logger.info("Python插件模板已卸载")
