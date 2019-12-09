# -*- coding: utf-8 -*-
"""Setup file for Python ZeroTier Node API client."""
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.0.1'

ZTCLI_DOWNLOAD_URL = (
    'https://github.com/sarnold/ztcli/tarball/' + __version__
)


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
    name='ztcli',
    packages=['ztcli_api',],
    version=__version__,
    license='LGPL-3.0',
    description='Python API for the local ZT node API interface.',
    long_description=read_file('README.rst'),
    url='https://github.com/sarnold/ztcli',
    author='Stephen L Arnold',
    author_email='nerdboy@gentoo.org',
    install_requires=['aiohttp', 'async_timeout'],
    download_url=ZTCLI_DOWNLOAD_URL,
    keywords=['zerotier-cli', 'api'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL-3.0 License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
    ],
    python_requires='!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
)
