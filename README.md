## 本地部署教程

## 1. 下载源码

```git
git clone https://github.com/Li-CW/Job_Hunter.git
```

## 2. 启动后端

1. 进入后端目录`\backend\csweb`下，启动cmd，确保cmd目录在`\backend\csweb` 下。

2. 安装依赖

   ```bash
   pip install -r requirements.txt
   ```

3. 迁移数据库

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. 启动后端

   ```
   python manage.py runserver
   ```

   

## 3. 后端添加数据

1. 创建`django`的超级管理员，使用账号密码进入后端：http://127.0.0.1:8000/admin/login/?next=/admin/
2. 添加company，job，subject数据

