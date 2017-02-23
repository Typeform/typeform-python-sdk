from setuptools import setup, find_packages

with open('README.rst') as fp:
    long_description = fp.read()

setup(
    name='typeform',
    version='0.1.0',
    description='HTTP API client for TypeForm',
    long_description=long_description,
    keywords=[
        'type',
        'form',
        'typeform',
        'api',
    ],
    author='Underdog.io Engineering',
    author_email='engineering@underdog.io',
    url='https://github.com/underdogio/typeform',
    packages=find_packages(),
    install_requires=['requests'],
    test_suite='typeform.test.suite.test_suite',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
    ]
)
