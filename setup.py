import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="python-sdk-ewallet",
    version="0.0.2",
    author="yangdm002",
    author_email="yangdm002@lianlianpay.com",
    description="Python SDK for LianLian Global e-wallet program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://developer.lianlianglobal.com/docs/e-wallet-openapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
