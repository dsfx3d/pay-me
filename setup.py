from setuptools import setup


setup(
    name                = 'payme',
    version             = '0.1.1',
    description         = 'PayU Money Payment Gateway integration utilities',
    long_description    = 'README on GitHub',
    url                 = 'http://github.com/dsfx3d/payme',
    author              = 'dsfx3d',
    author_email        = 'dsfx3d@gmail.com',
    license             = 'MIT',
    packages            = ['payme'],
    zip_safe            = False,
    include_package_data=True,

    keywords            = 'payment gateway india integration',
    classifiers         = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
    ]
)