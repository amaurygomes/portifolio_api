# Generated by Django 5.0.6 on 2024-06-07 00:27

import api.models
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('shortDescription', models.TextField()),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('githubUrl', models.URLField()),
                ('liveProjectUrl', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='projectImages/')),
                ('pagethumbnail', models.ImageField(upload_to='projectImages/')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('icon', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Link Contato',
                'verbose_name_plural': 'Links Contato',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('icon', models.TextField()),
                ('startDate', models.DateField()),
            ],
            options={
                'verbose_name': 'Tech',
                'verbose_name_plural': 'Techs',
            },
        ),
        migrations.CreateModel(
            name='HighlightProjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.ManyToManyField(to='api.project')),
            ],
            options={
                'verbose_name': 'Destaque',
                'verbose_name_plural': 'Destaques',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='sectionImages/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='api.technology'),
        ),
        migrations.CreateModel(
            name='PageInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('introduction', django_ckeditor_5.fields.CKEditor5Field()),
                ('profilePicture', models.ImageField(upload_to='profilePicture/')),
                ('cv', models.FileField(default='', upload_to='files/', validators=[api.models.validate_pdf])),
                ('socials', models.ManyToManyField(to='api.social')),
                ('technologies', models.ManyToManyField(to='api.technology')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home',
            },
        ),
        migrations.CreateModel(
            name='KnowTechs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('techs', models.ManyToManyField(to='api.technology')),
            ],
            options={
                'verbose_name': 'Conhecimento',
                'verbose_name_plural': 'Conhecimentos',
            },
        ),
    ]
