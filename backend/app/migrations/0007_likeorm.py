# Generated by Django 3.1.3 on 2020-11-14 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_commentorm'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profileorm')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filmorm')),
            ],
        ),
    ]
