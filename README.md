## 本地部署教程

## 1. 下载源码并解压

```git
git clone https://github.com/Li-CW/Job_Hunter.git
```

## 2. 启动后端

1. 进入后端目录`\backend\csweb`下。

2. 启动命令行，切换到上面目录，安装依赖

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

   

