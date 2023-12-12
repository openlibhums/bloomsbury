import os
import shutil

from django.conf import settings


def build():
    image_file = os.path.join(
        settings.BASE_DIR,
        'themes',
        'bloomsbury',
        'assets',
        'preprint_thumb.jpg'
    )
    dest_path = os.path.join(
        settings.BASE_DIR,
        'static',
        'bloomsbury',
        'assets',
    )

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    shutil.copy(
        image_file,
        dest_path
    )
