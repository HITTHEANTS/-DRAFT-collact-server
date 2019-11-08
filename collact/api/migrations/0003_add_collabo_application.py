# Generated by Django 2.2.4 on 2019-11-08 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_change_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollaboApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job', models.CharField(choices=[('branding', 'branding'), ('digital_art', 'digital_art'), ('fine_art', 'fine_art'), ('graphic_design', 'graphic_design'), ('illustration', 'illustration'), ('photography', 'photography'), ('ui/ux', 'ui/ux'), ('typography', 'typography'), ('interaction', 'interaction'), ('animation', 'animation'), ('film', 'film'), ('interaction', 'interaction'), ('programming', 'programming'), ('media', 'media'), ('art', 'art'), ('developer', 'developer'), ('installation', 'installation'), ('music', 'music'), ('dance', 'dance'), ('influencer', 'influencer'), ('makeup', 'makeup'), ('sculpting', 'sculpting'), ('fashion', 'fashion'), ('installation', 'installation'), ('craft', 'craft'), ('jewerly', 'jewerly'), ('art-direction', 'art-direction'), ('idea-journalism', 'idea-journalism'), ('storytelling', 'storytelling')], db_index=True, max_length=20, null=True)),
                ('self_introduction', models.TextField(blank=True, null=True)),
                ('where', models.CharField(choices=[('seoul', 'seoul'), ('gyeonggi', 'gyeonggi'), ('gangwon', 'gangwon')], db_index=True, max_length=20, null=True)),
                ('when', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], db_index=True, max_length=20, null=True)),
                ('style', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], db_index=True, max_length=20, null=True)),
                ('money', models.CharField(choices=[('later', 'later'), ('divide', 'divide'), ('pay', 'pay')], db_index=True, max_length=20, null=True)),
                ('tool', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('plan_start_dt', models.DateTimeField(db_index=True, null=True)),
                ('plan_end_dt', models.DateTimeField(db_index=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collabo',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='collabo', to='api.CollaboApplication'),
        ),
    ]
