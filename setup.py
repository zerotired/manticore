#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name='zt.manticore',
    version='2.0.0',
    url='https://github.com/zerotired/manticore',
    download_url='',
    license='BSD',
    author='Andreas Motl',
    author_email='a.motl@zerotired.com',
    description='Python documentation generator based on Sphinx',
    long_desc='',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    namespace_packages=['zt'],
    extras_require=dict(
        test=[],
    ),
    install_requires=[
        'setuptools',
        'zt.manticore.ext',
        'PIL==1.1.6',
    ],
    dependency_links=[
        'https://github.com/zerotired/manticore-ext/tarball/master#egg=zt.manticore.ext-0.1.2',
    ]
)
