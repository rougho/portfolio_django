# Generated by Django 4.2.6 on 2023-10-16 12:52

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'export.json'

def load_data(apps, schema_editor):
    Shop = apps.get_model('near_me', 'Shops')
    jsonfile = Path(__file__).parent.parent / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        object = json.load(datafile)
        for obj in object['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name', 'no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(
                        f'POINT({longitude} {latitude})', srid=4326
                    )
                    Shop(name=name, location=location).save()
            except KeyError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('near_me', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
