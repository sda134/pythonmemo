# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
    name='sample',
    version='0.1.0',
    description='パッケージサンプルです。',
    long_description=readme,
    author='伊佐治',
    author_email='isaji@m-tec-m.co.jp',
    license=license,
    install_requires='None',                            # 依存のパッケージ情報
    packages=find_packages(exclude=('tests', 'docs'))
)

