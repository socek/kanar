from setuptools import find_packages
from setuptools import setup

install_requires = [
    'pyramid==1.9',
    'SQLAlchemy==1.1.11',
    'psycopg2',
]

if __name__ == '__main__':
    setup(
        name='kanar-backend',
        version='0.1',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
        entry_points={
            'console_scripts': [
            ]
        },
    )
