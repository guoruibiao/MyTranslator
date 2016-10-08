# coding:utf-8
from setuptools import setup, find_packages

setup(
    name='mytranslator',
    description='Simple translator in English and Chinese, easier to use',
    url='http://',
    version='1.0.1',
    license='MIT',
    packages=find_packages(),
    entry_points = {
        "console_points": ['trans = mytranslator.translate:main']
    },
)