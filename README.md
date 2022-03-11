# Web3DVisualization-BackEnd

Web3DVisualization-BackEnd

<p align="center">
  <img src="https://img.shields.io/badge/Flask-1.1.4-ff7675.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Python-2.7.18-41b883.svg" alt="vue">
  <img src="https://img.shields.io/badge/Vite-1.3.0-ffeaa7.svg" alt="Vite">
  <img src="https://img.shields.io/badge/Typescript-4.4.3-74b9ff.svg" alt="vue">
</p>

> 一个 3D 可视化大屏项目, 正在建设中...

## 目录结构

```shell
│  .gitignore
│  config.py              # （TODO）不同环境的SQLALCHEMY REDIS配置
│  LICENSE
│  manage.py              # 入口文件
│  README.md
│  schema.sql             # 数据库结构
│
├─.docker
│    dockerfile           # (TODO)

├─app
│  │  __init__.py
│  │
│  ├─base
│  │      __init__.py     # Flask base blueprint
│  │
│  ├─models               # flask_sqlalchemy数据库模型
│  │      Assest.py
│  │      User.py
│  │      __init__.py
│  │
│  ├─routes               # 路由
│  │      admin.py
│  │      assets.py
│  │      user.py
│  │      __init__.py
│  │
│  └─utils                # 工具类
│          index.py
│          status_code.py
│
└─tests                   # （TODO）测试文件
        conftest.py
        connect_db.py
        data.sql
        test_auth.py
        test_db.py
```

## Quick Start

快速启动项目

### Windows 环境

```shell
> set FLASK_APP=DVIS
> set FLASK_ENV=development
> python manage.py runserver
```

### mac / Linux 环境

```shell
> export FLASK_APP=DVIS
> export FLASK_ENV=development
> python manage.py runserver
```

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) + [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

### 容器创建

> 也可以本地安装 mysql

```bash
> sudo docker pull mysql
> sudo docker run -itd -p 3306:3306 --name dvis-mysql --restart always -e MYSQL_ROOT_PASSWORD=<your password> mysql:8.0.2
> sudo docker exec -it dvis-mysql bash  # 进入容器
```

开放 SQL root 用户远程连接

```SQL
> docker exec -it mysql1 mysql -uroot -p
> ALTER USER 'root'@'localhost' IDENTIFIED BY '<your password>';
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '<your password>' WITH GRANT OPTION;
> FLUSH PRIVILEGES;
```

<!-- TODO manage.py migrate -->
