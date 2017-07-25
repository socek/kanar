from setuptools import find_packages
from setuptools import setup

install_requires = [
    'baelfire>=0.5.1',
    'docker==2.4.2',
]

if __name__ == '__main__':
    setup(
        name='rotarran-bael-host',
        version='0.1',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
        entry_points={
            'console_scripts': [
                'container = rbh.cmd:containers',
                'backend = rbh.cmd:backend',
                'btest = rbh.cmd:pytest',
                'balembic = rbh.cmd:alembic',
            ]
        },
    )
