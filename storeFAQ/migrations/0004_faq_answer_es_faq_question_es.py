# Generated by Django 5.1.5 on 2025-02-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeFAQ', '0003_remove_faq_translations_alter_faq_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es',
            field=models.TextField(blank=True, null=True),
        ),
    ]
