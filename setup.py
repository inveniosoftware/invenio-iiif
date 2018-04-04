# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""IIIF API for Invenio."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    # FIXME: Remove elasticsearch once pytest-invenio have fixed the es import.
    'elasticsearch>=5.0.0',
    'elasticsearch-dsl>=5.0.0',
    'isort>=4.3.3',
    'pydocstyle>=1.0.0',
    'pytest-cov>=1.8.0',
    'pytest-invenio>=1.0.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0,!=3.3.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'Flask-CeleryExt>=0.3.0',
    'Flask-IIIF>=0.3.1',
    'invenio-files-rest>=1.0.0a9',
    'invenio-records-files>=1.0.0a1',
    'Wand>=0.4.4',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_iiif', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-iiif',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio IIIF',
    license='MIT',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-iiif',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.api_apps': [
            'invenio_iiif = invenio_iiif:InvenioIIIF',
        ],
        'invenio_celery.tasks': [
            'invenio_iiif = invenio_iiif.tasks',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 1 - Planning',
    ],
)
