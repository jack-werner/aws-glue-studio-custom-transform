from setuptools import setup

setup(
    name='aws_glue_custom_transforms',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
    packages=['transforms']
)