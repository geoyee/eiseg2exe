# EISeg打包

参考repo：[QPT](https://github.com/geoyee/QPT)

## 打包步骤

1. 在当前能够正常使用的环境中安装QPT：

   ```shell
   python -m pip install qpt -i https://mirrors.bfsu.edu.cn/pypi/web/simple
   ```

2. 将EISeg最新的代码（去掉.git文件）替换文件夹下的EISeg文件夹，再运行`qpt_pack.py`脚本：

   ```shell
   python qpt_pack.py
   ```

3. 进入`EISeg/requirements_with_opt.txt`，注释掉GDAL，添加QPT，并将paddlepaddle-gpu改为paddlepaddle，回车确认，等待打包完成。

   ```
   # -------------Mainly depends on package analysis results--------------
   
   pycocotools==2.0.2
   paddlepaddle==2.2.0  # 替换 paddlepaddle-gpu==2.2.0
   beautifulsoup4==4.9.3
   # gdal==3.2.3  # 注释
   qtpy==1.9.0
   albumentations==0.5.2
   simpleitk==2.0.2
   easydict==1.9
   visualdl==2.2.0
   pyqt5==5.15.4
   paddleseg==2.3.0
   imgaug==0.4.0
   qpt==1.0b1.dev11  # 增加
   ```

4. 复制目录下的`GDAL-3.2.3-cp38-cp38-win_amd64.whl`到`out/Debug(Release)/opt/packages`下，完成GDAL的打包。

## 使用

1. Debug下的exe用于测试。
2. 发布只需把Release打包为zip即可。
