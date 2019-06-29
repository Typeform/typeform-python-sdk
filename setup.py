from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='typeform',
    version='1.1.0',
    description='Python Client wrapper for Typeform API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        'type',
        'form',
        'typeform',
        'api',
    ],
    author='Typeform',
    author_email='michael.solati@typeform.com',
    url='https://github.com/MichaelSolati/typeform-python-sdk',
    packages=find_packages(),
    install_requires=['requests'],
    test_suite='typeform.test.suite.test_suite',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
    ]
)
