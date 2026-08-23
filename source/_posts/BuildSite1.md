---
title: Windows建站教程丨运用Hexo框架快速建立自己的博客(一)
date: 2022-11-04 20:00:00
categories: 建站教程
tags: 
  - 建站教程
  - Hexo
description: 本篇主要介绍如何在本地安装Hexo基础框架以及在本地启动Hexo博客站点丨Windows系统
---
#### <center>一、安装基础程序

（一）Node.js

>Official Download Site：[Node.js丨https://nodejs.org/](https://nodejs.org/)

（二）Git

>Official Download Site：[Git丨https://gic-scm.com/](https://git-scm.com/downloads)

#### <center>二、安装基础Hexo框架

（一）将Hexo安装到全局：

创建一个用来放置博客文件的空文件夹，并在里面空白处右击，点击Git Bash Here，Git会自动在本目录下处理命令。


在Git中输入Hexo框架安装指令：

`npm install hexo-cli -g`

如果等候许久未反应，则需要在Git中输入命令，切换国内淘宝镜像（如果上一步还在处理中，需要在Git中输入Ctrl+C组合键结束）：

`npm config set registry https://registry.npm.taobao.org`

使用

`npm config get registry`

观察返回信息，验证镜像是否切换成功，成功后再输入Hexo安装指令以安装

使用

`hexo -v`

观察返回信息版本号，验证Hexo是否安装成功


（二）新建安装博客的文件夹并安装框架

使用命令

`hexo init yourblogname`

其中yourblogname修改为你希望博客文件存储的文件夹名字

成功安装后，刚创建好的文件夹根目录里多出了如下文件

>/.github
>/node_modules
>/scaffolds
>/source----资源文件夹
>/themes----主题文件夹
>.gitignore
>_config.landscape.yml
>_config.yml----配置文件
>package.json
>package-lock

我们在这个文件夹的空白处右击，点击Git Bash Here，输入指令安装npm：

`npm install`

于是我们的站点就安装完毕了！我们输入如下指令将其在本地启动：

`hexo server(或hexo s)`

然后我们在浏览器地址栏中输入

`localhost:4000`

即可进入本地站点！

我们可以看到目前我们的网站除了基础框架和自动创建的Hello World外，没有其他内容，但是我们不必心急写内容，先要发布到互联网上才能确保能被人看到，所以下一篇我们将会学习：

>如何将Hexo框架的服务通过Netlify部署到互联网，使其可被访问
>>准备一个Github账号
>>准备一个Netlify账号
>>如需自定网址则需在服务商购买域名

<p align="right">Edited by Acr1mony</p>