# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Handler functions for Flask-IIIF to open image and protect API."""

import tempfile

from invenio_files_rest.models import ObjectVersion


def image_opener(uuid):
    """Find a file based on its UUID.

    :param uuid: a UUID in the form bucket:filename
    :returns: a file path or handle to the file or its preview image
    :rtype: string or handle
    """
    # Drop the "version" that comes after the second ":" - we use this version
    # only as key in redis cache
    bucket, _file = uuid.split(':')[:2]

    ret = ObjectVersion.get(bucket, _file).file.uri
    # Open the Image
    opened_image = file_opener_xrootd(ret, 'rb')
    if '.' in _file:
        ext = _file.split('.')[-1]
        if ext in ['txt', 'pdf']:
            from wand.image import Image
            img = Image(opened_image)
            # Get the first page from text and pdf files
            first_page = Image(img.sequence[0])
            tempfile_ = tempfile.TemporaryFile()
            with first_page.convert(format='png') as converted:
                converted.save(file=tempfile_)
            return tempfile_
    # Return an open file to IIIF
    return opened_image
