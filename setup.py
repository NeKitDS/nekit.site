from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='nekit.site',
    author='NeKitDS',
    author_email='gdpy13@gmail.com',
    url='https://github.com/NeKitDS/nekit.site',
    project_urls={
        "Issue tracker": "https://github.com/NeKitDS/nekit.site/issues",
    },
    version='0.1.1',
    packages=[
        'nekit_site', 'nekit_site.ext'
    ],
    license='MIT',
    description='NeKit\'s Site',
    install_requires=requirements,
    python_requires='>=3.5.3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'console_scripts': [
            'run_site = nekit_site.__main__',
        ]
    }
)