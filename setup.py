"""
Setup script for the MCP SSE Client Python package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if not line.startswith("#")]

setup(
    name="mcp_playground",
    version="0.2.0",
    author="zanetworker",
    author_email="",  # Add author email if available
    description="A comprehensive Python toolkit for interacting with remote Model Context Protocol (MCP) endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zanetworker/mcp-playground",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",  # Adjust if using a different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
)
