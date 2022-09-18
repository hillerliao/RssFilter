将 [RSSHub-Python](https://github.com/hillerliao/RSSHub-python) 项目里的 [RSS 过滤](https://pyrsshub.vercel.app/feeds)功能独立出来，部署到阿里云云函数上。

# 部署方法

## 创建服务

1、进入阿里云[函数计算](https://fcnext.console.aliyun.com/overview)后台，点击创建服务。

![阿里云函数计算概览](https://github.com/easychen/wecomchan/raw/main/python-aliyunfc/pic/image-20220205142747826.png)

2、填入服务名称，比如 `RssFilter`，点击确定。

![函数计算-创建服务](https://raw.githubusercontent.com/hillerliao/img/main/20220918133712.png)

## 配置函数

3、配置函数。

3.1 进入刚创建的服务，点击`创建函数`；  
3.2 选择`使用自定义运行时创建`，填写函数名称，如`main`；  
3.3 代码上传方式选择`通过 ZIP 包上传代码`，将本项目仓库中的 zip 包`func-code-4-RSSFilter.zip`下载后上传；  
3.4 启动命令填入`python app.py`；  

点击 `创建`。

![](https://raw.githubusercontent.com/hillerliao/img/main/20220918134114.png)

## 获取地址

4、获得测试地址，带上路径和参数，如 `/filter?feed=<rss 地址>&include_title=<过滤词>` 支持的参数同 rsshub-python的rss [RSS Filter参数](https://pyrsshub.vercel.app/feeds)

![](https://raw.githubusercontent.com/hillerliao/img/main/20220918134337.png)

示例：

`http://<testing sub domain for fc>.cn-beijing.functioncompute.com/filter?feed=https://sspai.com/feed&include_title=派评`

5、测试验证通过后，点击 `部署代码`，部署完成。

![](https://raw.githubusercontent.com/hillerliao/img/main/20220918134819.png)

如果你觉得本项目对你有用，请我喝杯咖啡。

![](https://raw.githubusercontent.com/hillerliao/img/main/20220918135531.png)