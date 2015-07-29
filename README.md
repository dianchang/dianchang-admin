电场城管大队
=======

## 开发环境搭建

```
git clone https://github.com/dianchang/dianchang-admin.git --recursive
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -r application/models/dc/requirements.txt
bower install
```

将`development_sample.py`另存为`development.py`，并按需更新配置项。

```
python manage.py db upgrade
python manage.py run
```
