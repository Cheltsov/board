# Generated by Django 2.2.7 on 2019-11-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rubric', '0002_additionalimage_bb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commetn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Автор')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Выводить на экран?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubric.Bb', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at'],
            },
        ),
    ]
