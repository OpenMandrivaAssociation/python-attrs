%define module attrs

Name:		python-attrs
Summary:	Python library for attributes without boilerplate
Version:	26.1.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/attrs/
Source0:	https://pypi.org/packages/source/a/attrs/attrs-%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
