Summary:	Python library for attributes without boilerplate
Name:		python-attrs
Version:	21.2.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://files.pythonhosted.org/packages/ed/d6/3ebca4ca65157c12bd08a63e20ac0bdc21ac7f3694040711f9fd073c0ffb/attrs-21.2.0.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources
BuildArch:	noarch

%description
Python library for atrributes without boilerplate

%package -n python2-attrs
Summary:	Python 2.x library for attributes without boilerplate
Group:		Development/Python

%description -n python2-attrs
Python 2.x library for attributes without boilerplate

%prep
%setup -qn attrs-%{version}
%autopatch -p1

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
%py_build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
%py_install

%files
%defattr(0644,root,root,0755)
%{py_puresitedir}/attr
%{py_puresitedir}/*.egg-info

%files -n python2-attrs
%{py2_puresitedir}/attr
%{py2_puresitedir}/*.egg-info
