%define	module attrs

Summary:	Python library for attributes without boilerplate
Name:		python-attrs
Version:	25.4.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://pypi.org/packages/source/a/attrs/attrs-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildArch:	noarch

%description
Python library for atrributes without boilerplate.

%files
%{py_puresitedir}/attr
%{py_puresitedir}/attrs
%{py_puresitedir}/attrs-*.*-info
