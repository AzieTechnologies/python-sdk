import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="devpay",
    version="1.0.0",
    description="A Python SDK for Devpay Payment Gateway Get your API Keys at https://devpay.io",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-pay/python-sdk",
    author="devpay-dev",
    author_email="dev@devpay.io",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    packages=["devpay"],
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    entry_points={"console_scripts": ["devpay=devpay.__main__:main"]},
)
