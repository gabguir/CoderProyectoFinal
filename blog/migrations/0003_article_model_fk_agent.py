# Generated by Django 3.2 on 2022-09-17 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_auto_20220917_1739'),
        ('blog', '0002_auto_20220917_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_model',
            name='fk_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent_model', verbose_name='Agente'),
        ),
    ]
