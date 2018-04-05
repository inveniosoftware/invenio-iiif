# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Handlers tests."""

from __future__ import absolute_import, print_function

from io import IOBase

from invenio_iiif.handlers import image_opener


def test_image_opener(image_object):
    """Test image opener."""
    key = str(image_object)
    img = image_opener(key)

    assert isinstance(img, IOBase)
