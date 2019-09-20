#!/usr/bin/env python
# coding=utf-8

# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2019 NIWA & British Crown (Met Office) & Contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import codecs
from os.path import join, dirname, abspath

from setuptools import setup

here = abspath(dirname(__file__))


def read(*parts):
    with codecs.open(join(here, *parts), 'r') as fp:
        return fp.read()


install_requires = [
    'isodatetime==1!2.0.*',
    'cylc-flow==8.0a0'
]
tests_require = [
    'codecov==2.0.*',
    'coverage==4.5.*',
    'pytest-cov==2.6.*',
    'pytest==4.4.*',
    'pycodestyle==2.5.*',
    'testfixtures==6.6.*'
]

extra_requires = {
    'all': []
}
extra_requires['all'] += tests_require

setup(
    version="0.1",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=["cylc.flow.xtriggers"],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extra_requires,
    project_urls={
        "Documentation": "https://github.com/cylc/cylc-xtriggers",
        "Source": "https://github.com/cylc/cylc-xtriggers",
        "Tracker": "https://github.com/cylc/cylc-xtriggers/issues"
    }
)
