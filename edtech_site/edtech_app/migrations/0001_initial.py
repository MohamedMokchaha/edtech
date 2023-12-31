# Generated by Django 4.1.3 on 2023-05-05 17:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import edtech_app.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, help_text='Optional', null=True, upload_to='media/catlogo')),
                ('top_ten_cat', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
            ],
        ),
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('reqs', models.CharField(blank=True, max_length=2000)),
                ('image', models.ImageField(upload_to='media/image_cours')),
                ('image_alt_name', models.CharField(blank=True, max_length=200)),
                ('desciption', models.TextField(blank=True, null=True)),
                ('teacher', models.CharField(default='admin', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VideoCours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to=edtech_app.models.cour_directory_path)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('titre', models.CharField(blank=True, max_length=200)),
                ('chapitre', models.CharField(blank=True, max_length=200)),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech_app.cours')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biographie', models.TextField(max_length=280)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('specialite', models.CharField(blank=True, max_length=20)),
                ('experience', models.CharField(blank=True, max_length=20)),
                ('City', models.CharField(blank=True, max_length=20)),
                ('Parcour', models.CharField(blank=True, max_length=20)),
                ('linkedin', models.CharField(max_length=20)),
                ('skills', models.CharField(max_length=280)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='edtech_app.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ordred', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech_app.cours')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_note', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech_app.videocours')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='langue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edtech_app.language'),
        ),
        migrations.AddField(
            model_name='cours',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='cour_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
