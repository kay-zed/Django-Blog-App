# Generated by Django 2.0.7 on 2019-02-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'BlogEntries',
            },
        ),
        migrations.CreateModel(
            name='BlogTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogTopic')),
            ],
        ),
        migrations.AddField(
            model_name='blogentry',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogTopic'),
        ),
    ]
