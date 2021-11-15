# 导入QPT
from qpt.executor import CreateExecutableModule as CEM


# -----关于路径的部分，强烈建议使用绝对路径避免出现问题-----
# [项目文件夹]待打包的目录，并且该目录下需要有↓下方提到的py文件
# [主程序文件]用户启动EXE文件后，QPT要执行的py文件
# [输出目录]打包后相关文件的输出目录
# [Python依赖]此处可填入依赖文件路径，也可设置为auto自动搜索依赖
# [终端窗口]设置为True后，运行时将不会展示黑色终端窗口  
# [跨版本编译]需要预先from qpt.modules.python_env import Python37
# [自定义图标文件]支持将exe文件设置为ico/JPG/PNG等格式的自定义图标

module = CEM(work_dir=r"E:\dataFiles\github\eiseg_to_exe\EISeg",
             launcher_py_path=r"E:\dataFiles\github\eiseg_to_exe\EISeg\eiseg\exe.py",
             save_path=r"E:\dataFiles\github\eiseg_to_exe\out")
           # requirements_file="auto"
           # hidden_terminal=False
           # interpreter_module=Python37()
           # icon="your_ico.ico"
# 开始打包
module.make()