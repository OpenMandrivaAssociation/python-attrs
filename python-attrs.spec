%global module attrs

Summary:	Python library for attributes without boilerplate
Name:		python-%{module}
Version:	23.2.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://pypi.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
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
%{py_puresitedir}/%{module}-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

