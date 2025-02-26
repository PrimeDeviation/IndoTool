from setuptools import setup, find_packages

setup(
    name="indotool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PySide6>=6.5.0",
        "pyyaml>=6.0",
        "markdown>=3.4.3",
        "python-json-logger>=2.0.7",
        "networkx>=3.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
            "pytest-qt>=4.2.0",
            "pytest-cov>=4.1.0",
            "pre-commit>=3.3.2",
            "black>=23.3.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "indotool=indotool.main:main",
        ],
    },
)