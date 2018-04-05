# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Handler functions for Flask-IIIF to open image and protect API."""

import tempfile

import pkg_resources
from invenio_files_rest.models import ObjectVersion

try:
    pkg_resources.get_distribution('wand')
    from wand.image import Image
    HAS_IMAGEMAGICK = True
except pkg_resources.DistributionNotFound:
    # Python module not installed
    HAS_IMAGEMAGICK = False
except ImportError:
    # ImageMagick notinstalled
    HAS_IMAGEMAGICK = False


def image_opener(key):
    """Handler to locate file based on key.

    :param key: A key encoded in the format "<bucket>:<version>:<object_key>".
    :returns: A file-like object.
    """
    # Drop the "version" that comes after the first ":" - we use this version
    # only as key in redis cache
    bucket, version, object_key = key.split(':', 2)

    obj = ObjectVersion.get(bucket, object_key)
    fp = obj.file.storage().open('rb')

    # If ImageMagick with Wand is installed, extract first page for PDF/text.
    if HAS_IMAGEMAGICK and obj.mimetype in ['application/pdf', 'text/plain']:
        first_page = Image(Image(fp).sequence[0])
        tempfile_ = tempfile.TemporaryFile()
        with first_page.convert(format='png') as converted:
            converted.save(file=tempfile_)
        return tempfile_
    return fp
