# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-License-Identifier: MIT

"""Module tests."""

from __future__ import absolute_import, print_function


def test_version():
    """Test version import."""
    from invenio_iiif import __version__
    assert __version__


def test_init(base_app):
    """Test extension initialization."""
    assert 'invenio-iiif' in base_app.extensions
    assert 'iiif' in base_app.extensions
