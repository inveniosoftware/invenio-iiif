# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_iiif import InvenioIIIF


def test_version():
    """Test version import."""
    from invenio_iiif import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioIIIF(app)
    assert 'invenio-iiif' in app.extensions

    app = Flask('testapp')
    ext = InvenioIIIF()
    assert 'invenio-iiif' not in app.extensions
    ext.init_app(app)
    assert 'invenio-iiif' in app.extensions
