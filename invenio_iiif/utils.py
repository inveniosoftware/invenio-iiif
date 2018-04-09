# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Utilities for IIIF."""

from __future__ import absolute_import, print_function

from flask import current_app
from invenio_files_rest.models import ObjectVersion


def iiif_image_key(obj):
    """Generate the IIIF image key."""
    if isinstance(obj, ObjectVersion):
        bucket_id = obj.bucket_id
        version_id = obj.version_id
        key = obj.key
    else:
        bucket_id = obj.get('bucket')
        version_id = obj.get('version_id')
        key = obj.get('key')
    return '{}:{}:{}'.format(
        bucket_id,
        version_id,
        key,
    )


def ui_iiif_image_url(obj, version='v2', region='full', size='full',
                      rotation=0, quality='default', image_format='png'):
    """Generate IIIF image URL from the UI application."""
    return '{prefix}{version}/{identifier}/{region}/{size}/{rotation}/' \
        '{quality}.{image_format}'.format(
            prefix=current_app.config['IIIF_UI_URL'],
            version=version,
            identifier=iiif_image_key(obj),
            region=region,
            size=size,
            rotation=rotation,
            quality=quality,
            image_format=image_format,
        )
