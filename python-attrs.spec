Summary:	Python library for attributes without boilerplate
Name:		python-attrs
Version:	16.3.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://files.pythonhosted.org/packages/01/b0/3ac73bf6df716a38568a16f6a9cbc46cc9e8ed6fe30c8768260030db55d4/attrs-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	python2-setuptools
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
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/attr
%{py_sitedir}/*.egg-info

%files -n python2-attrs
%{py2_puresitedir}/attr
%{py2_puresitedir}/*.egg-info