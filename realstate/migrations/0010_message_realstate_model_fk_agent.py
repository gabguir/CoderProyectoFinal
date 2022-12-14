# Generated by Django 3.2 on 2022-10-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0007_agent_model_draft'),
        ('realstate', '0009_message_realstate_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_realstate_model',
            name='fk_agent',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent_model', verbose_name='Agente [*]'),
            preserve_default=False,
        ),
    ]
