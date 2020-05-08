# Generated by Django 3.0.5 on 2020-05-09 04:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200508_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('paragraph_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('paragraph_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'hr', 'ol', 'ul', 'link', 'document-link'], icon='fa-paragraph'))])), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.core.blocks.StructBlock([('video_image', wagtail.images.blocks.ImageChooserBlock(help_text='Screenshot image of the video', required=True, verbose_name='Video screenshot')), ('video_url', wagtail.core.blocks.URLBlock(help_text='Paste the video embed url from youtube.', verbose_name='Video URL')), ('video_header', wagtail.core.blocks.CharBlock(blank=True, help_text='Text to displayed on top of video image. Max 50 chars.', label='e.g. Mary Berry', required=False)), ('video_intro', wagtail.core.blocks.TextBlock(help_text='Few lines to be displayed on the video image. Max 300 chars.', max_length=300, verbose_name='Video Intro'))])), ('full_width_image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, verbose_name='Page body'),
        ),
    ]
