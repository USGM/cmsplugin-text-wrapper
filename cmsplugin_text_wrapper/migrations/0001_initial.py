# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_text_wrapper.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextWrapper',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('wrapper', models.CharField(blank=True, max_length=50, verbose_name='Wrap into', choices=[(b'Orange Call to Action', b'Orange Call to Action'), (b'Green Call to Action', b'Green Call to Action'), (b'Blue Call to Action', b'Blue Call to Action')])),
                ('classes', cmsplugin_text_wrapper.fields.MultiSelectField(max_length=250, null=True, verbose_name='Apply extra classes', blank=True)),
            ],
            options={
                'db_table': 'cmsplugin_text',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
