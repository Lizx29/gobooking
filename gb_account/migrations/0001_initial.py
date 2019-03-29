# Generated by Django 2.1.2 on 2019-03-28 09:03

from django.db import migrations, models
import django.utils.timezone
import gb_account.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchants',
            fields=[
                ('shopid', models.CharField(help_text='26位及邮编加时间戳', max_length=26, primary_key=True, serialize=False, verbose_name='门店编号')),
                ('shopAPhone', models.DecimalField(decimal_places=0, help_text='11位且唯一', max_digits=11, unique=True, verbose_name='手机号')),
                ('shopPassWd', models.CharField(help_text='6-20位及md5加密', max_length=32, verbose_name='门店密码')),
                ('shopName', models.CharField(help_text='最多30位', max_length=30, verbose_name='门店名称')),
                ('shopAddress', models.CharField(help_text='最多50位', max_length=50, verbose_name='门店地址')),
                ('shopCoordinate', models.CharField(help_text='百度地图api坐标', max_length=20, verbose_name='门店坐标')),
                ('shopCPhone', models.CharField(help_text='可填多个且最多35位', max_length=35, verbose_name='门店联系电话')),
                ('shopHours', models.CharField(help_text='最多50位', max_length=50, verbose_name='门店营业时间')),
                ('shopImg', models.ImageField(help_text='门店头像', upload_to=gb_account.models.Merchants.mer_img_path, verbose_name='门店头像')),
                ('shopLicense', models.ImageField(help_text='门店执照', upload_to=gb_account.models.Merchants.mer_license_path, verbose_name='门店执照')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建账户时间')),
                ('lastLoginTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后登录时间')),
                ('shopStatus', models.CharField(choices=[('200', '状态正常'), ('404', '审核中'), ('202', '信息已修改')], default='404', help_text='200正常 404审核中 202信息已修改', max_length=3, verbose_name='门店状态')),
                ('shopToken', models.CharField(default='初始化', help_text='门店验证号及md5加密', max_length=32, verbose_name='门店验证号')),
            ],
            options={
                'verbose_name': '门店',
                'verbose_name_plural': '门店',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='uuid', primary_key=True, serialize=False, verbose_name='用户号')),
                ('userName', models.CharField(help_text='6-20位且唯一不可变', max_length=20, unique=True, verbose_name='用户名')),
                ('userPhone', models.DecimalField(decimal_places=0, help_text='11位且唯一', max_digits=11, unique=True, verbose_name='手机号')),
                ('userPassWd', models.CharField(help_text='6-20位及md5加密', max_length=32, verbose_name='用户密码')),
                ('trueName', models.CharField(help_text='最多15位', max_length=15, verbose_name='姓名')),
                ('userGender', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=1, verbose_name='性别')),
                ('userImg', models.ImageField(help_text='用户头像', upload_to=gb_account.models.Users.user_img_path, verbose_name='用户头像')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建账户时间')),
                ('lastLoginTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后登录时间')),
                ('userToken', models.CharField(default='初始化', help_text='登录验证号及md5加密', max_length=32, verbose_name='用户验证号')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
