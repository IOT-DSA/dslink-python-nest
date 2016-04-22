from setuptools import setup

setup(
    name="dslink-python-nest",
    version="0.1.0",
    description="Nest DSLink",
    url="http://github.com/IOT-DSA/dslink-python-nest",
    author="Logan Gorence",
    author_email="l.gorence@dglogik.com",
    license="Apache 2.0",
    install_requires=[
        "dslink == 0.6.13",
        "python-nest == 2.9.0"
    ]
)
