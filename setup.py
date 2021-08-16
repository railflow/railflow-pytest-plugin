# import os
# import re
# import io

from setuptools import setup


setup(
    name="pytest-railflow-testrail-reporter",
    version="3-Alpha",
    description="json report generationusing pytest with optional metadata input",
    # long_description=io.open("README.md", encoding="utf-8", errors="ignore").read(),
    # author="",
    # author_email=u"",
    # url=u"",
    # license = "",
    # license_file = "",
    packages=["pytest_railflow_testrail_reporter"],
    entry_points={
        "pytest11": [
            "pytest_railflow_testrail_reporter = pytest_railflow_testrail_reporter.plugin"
        ]
    },
    install_requires=["pytest"],
    keywords="py.test pytest json railflow report",
    classifiers=[
        "Development Status :: 3 - Development/Alpha",  # change to Production/Stable
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        # " License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
