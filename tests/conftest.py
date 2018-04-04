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


@pytest.fixture(scope='module')
def create_app():
    """Application factory fixture."""
    def factory(**kwargs):
        app = Flask('testapp', **kwargs)
        app.config.update(
            SECRET_KEY='SECRET_KEY',
            TESTING=True,
        )
        return app
    return factory
