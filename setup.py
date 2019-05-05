from setuptools import setup

setup(
    name='pkg',
    version='0.1',
    description='',
    url='',
    author='',
    author_email='',
    license='',
    package_dir={'': 'src'},
    packages=['pkg'],
    install_requires=[
        'requests',
        'pyyaml'
    ],
    extras_requires={
        'test': ['pytest-cov', 'isort', 'flake8']
    }
)
