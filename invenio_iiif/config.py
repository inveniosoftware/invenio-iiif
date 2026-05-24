# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-License-Identifier: MIT

"""IIIF API for Invenio."""

IIIF_API_PREFIX = '/iiif/'
"""URL prefix to IIIF API."""

IIIF_UI_URL = '/api{}'.format(IIIF_API_PREFIX)
"""URL to IIIF API endpoint (allow hostname)."""

IIIF_PREVIEWER_PARAMS = {
    'size': '750,'
}
"""Parameters for IIIF image previewer extension."""

IIIF_PREVIEW_TEMPLATE = 'invenio_iiif/preview.html'
"""Template for IIIF image preview."""

IIIF_API_DECORATOR_HANDLER = 'invenio_iiif.handlers:protect_api'
"""Image opener handler decorator."""

IIIF_IMAGE_OPENER_HANDLER = 'invenio_iiif.handlers:image_opener'
"""Image opener handler function."""
