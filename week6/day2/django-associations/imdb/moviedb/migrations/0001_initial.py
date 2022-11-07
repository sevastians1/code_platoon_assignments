# Generated by Django 3.2.4 on 2022-11-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.movie')),
            ],
            options={
                'unique_together': {('movie', 'actor')},
            },
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(through='moviedb.Role', to='moviedb.Movie'),
        ),
    ]