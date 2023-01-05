import setuptools

exec(open('SungrowClient/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SungrowClient",
    version=__version__,
    author="Bohdan Flower",
    author_email="github@bohdan.net",
    description="A wrapper for talking to Sungrow Inverters via Modbus and HTTP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bohdan-s/SungrowClient",
    packages=setuptools.find_packages(),
    install_requires=[
        'pymodbus~=2.5.3',
        'SungrowModbusTcpClient>=0.1.5',
        'SungrowModbusWebClient>=0.3.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.0',
)