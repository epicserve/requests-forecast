from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    name='requests-forecast',
    license='BSD',
    version=version,
    description='',
    long_description=readme,
    author='Jeff Triplett',
    author_email='jeff.triplett@gmail.com',
    url='https://github.com/jefftriplett/requests-forecast',
    py_modules=['requests_forecast'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)