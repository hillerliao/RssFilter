为方便薅阿里云函数计算的羊毛，将 [RSSHub-Python](https://github.com/hillerliao/RSSHub-python) 项目里的 [RSS 过滤器](https://pyrsshub.vercel.app/feeds)功能独立出来，做成阿里云函数计算的版本。

项目地址：`https://github.com/hillerliao/RssFilter`

部署方法记录如下：

## 一、创建服务

1、进入[阿里云函数计算](https://fcnext.console.aliyun.com/overview)后台，点击创建服务。

![阿里云函数计算概览](https://github.com/easychen/wecomchan/raw/main/python-aliyunfc/pic/image-20220205142747826.png)

2、填入服务名称，比如 `RssFilter`，点击确定。

![阿里云函数计算-创建服务](https://raw.githubusercontent.com/hillerliao/img/main/20220918133712.png)

## 二、配置函数

3、配置函数。

3.1 进入刚创建的服务，点击`创建函数`；  
3.2 选择`使用自定义运行时创建`，填写函数名称，如`main`；  
3.3 代码上传方式选择`通过 ZIP 包上传代码`，将本项目仓库中的[过滤器zip代码包](https://github.com/hillerliao/RssFilter/blob/main/func-code-4-RSSFilter.zip)`func-code-4-RSSFilter.zip`下载后上传；  
3.4 启动命令填入`python app.py`；  

点击 `创建`。

![阿里云函数计算-配置函数](https://raw.githubusercontent.com/hillerliao/img/main/20220918134114.png)

## 三、获取地址

4、获得测试地址，带上路径和参数，如 `/filter?feed=<rss 地址>&include_title=<过滤词>` 支持的参数同 RSSHub-Python 的 [RSS Filter参数](https://pyrsshub.vercel.app/feeds)

![阿里云函数计算-获取函数公网地址](https://raw.githubusercontent.com/hillerliao/img/main/20220918134337.png)

示例：

`http://<testing sub domain for fc>.cn-beijing.functioncompute.com/filter?feed=https://sspai.com/feed&include_title=派评`

5、测试验证通过后，点击 `部署代码`，部署完成。

![阿里云函数计算-在线编辑器](https://raw.githubusercontent.com/hillerliao/img/main/20220918134819.png)

## 四、制作 RSS 过滤器的初衷

回顾我作 RSS 过滤器的初心：提高信息获取效率。

比如，有些 RSS，我只关心带有特定关键词的内容；另一些 RSS，我不想看到含有特定关键词的广告内容。有了 RSS 过滤器，这些需求都能得到满足。

好了，如果你觉得本项目对你有用，不妨请我喝杯咖啡。

![个人微信收款码-智海](https://raw.githubusercontent.com/hillerliao/img/main/IMG_0096%20copy.jpg)

如果有改进建议，欢迎交流。微信： `hillerliao`。