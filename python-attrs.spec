Summary:	Python library for attributes without boilerplate
Name:		python-attrs
Version:	21.4.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://files.pythonhosted.org/packages/source/a/attrs/attrs-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildArch:	noarch

%description
Python library for atrributes without boilerplate.

%prep
%autosetup -n attrs-%{version}

%build
%py3_build

%install
%py3_install

%files
%defattr(0644,root,root,0755)
%{py_puresitedir}/attr
%{py_puresitedir}/attrs
%{py_puresitedir}/*.egg-info
