from setuptools import find_packages
from setuptools import setup

install_requires = [
    'pyramid==1.9',
    'SQLAlchemy==1.1.11',

    'psycopg2',
    'morfdict==0.4.5',
    'pyyaml',
]

if __name__ == '__main__':
    setup(
        name='kanar',
        version='0.1',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
        entry_points={
            'paste.app_factory': [
                'main = kanar:main'
            ],
            'console_scripts': [
            ]
        },
    )
