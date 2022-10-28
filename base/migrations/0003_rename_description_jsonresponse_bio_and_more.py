# Generated by Django 4.1.2 on 2022-10-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_jsonresponse_completed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jsonresponse',
            old_name='description',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='jsonresponse',
            old_name='name',
            new_name='slackUsername',
        ),
        migrations.AddField(
            model_name='jsonresponse',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jsonresponse',
            name='backend',
            field=models.BooleanField(default=False),
        ),
    ]
