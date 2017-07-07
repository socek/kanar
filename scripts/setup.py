from setuptools import find_packages
from setuptools import setup

install_requires = [
    'baelfire>=0.5.1',
]

if __name__ == '__main__':
    setup(
        name='kanar-bael-host',
        version='0.1',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
        entry_points={
            'console_scripts': [
                'kbh=kbh.cmd:run',
            ]
        },
    )
