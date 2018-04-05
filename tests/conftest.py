# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import shutil
import tempfile

import pytest
from flask import Flask
from invenio_db import InvenioDB
from invenio_files_rest import InvenioFilesREST
from invenio_files_rest.models import Bucket, Location, ObjectVersion
from six import BytesIO, b

from invenio_iiif import InvenioIIIF


@pytest.fixture(scope='module')
def location_path():
    """Temporary directory for location path."""
    tmppath = tempfile.mkdtemp()

    yield tmppath

    shutil.rmtree(tmppath)


@pytest.fixture(scope='module')
def location(location_path, database):
    """File system locations."""
    loc = Location(
        name='testloc',
        uri=location_path,
        default=True
    )

    database.session.add(loc)
    database.session.commit()

    return loc


@pytest.fixture(scope='module')
def image_object(database, location):
    """Image object."""
    bucket = Bucket.create()
    database.session.commit()

    data_bytes = b('test object')
    obj = ObjectVersion.create(
        bucket, 'test.jpg', stream=BytesIO(data_bytes),
        size=len(data_bytes)
    )
    database.session.commit()

    return obj


@pytest.fixture(scope='module')
def create_app():
    """Application factory fixture."""
    def factory(**config):
        app = Flask('testapp')
        app.config.update(
            **config
        )

        InvenioDB(app)
        InvenioFilesREST(app)
        InvenioIIIF(app)

        return app
    return factory
