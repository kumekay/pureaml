from __future__ import annotations

if False:  # MYPY
    from typing import Dict, Any  # NOQA

_package_data = dict(
    full_package_name="pureaml",
    version_info=(0, 18, 6),
    __version__="0.18.6",
    version_timestamp="2024-02-07 07:43:33",
    author="Anthon van der Neut",
    author_email="a.van.der.neut@ruamel.eu",
    description="pureaml is a fork of ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order",  # NOQA
    homepage="https://github.com/kumekay/pureaml",
    entry_points=None,
    since=2014,
    extras_require={
        "clib": ["ruamel.yaml.clib>=0.2.7"],
        "jinja2": ["ruamel.yaml.jinja2>=0.2"],
        "docs": ["ryd", "mercurial>5.7"],
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
        "Typing :: Typed",
    ],
    keywords="yaml 1.2 parser round-trip preserve quotes order config",
    read_the_docs="yaml",
    supported=[(3, 7)],  # minimum
    tox=dict(
        env="*",
        fl8excl="_test/lib,branch_default",
    ),
    # universal=True,
    python_requires=">=3.7",
)  # type: Dict[Any, Any]


version_info = _package_data["version_info"]
__version__ = _package_data["__version__"]

try:
    from .cyaml import *  # NOQA

    __with_libyaml__ = True
except (ImportError, ValueError):  # for Jython
    __with_libyaml__ = False

from ruamel.yaml.main import *  # NOQA
