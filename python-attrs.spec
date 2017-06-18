Summary:	Python library for attributes without boilerplate
Name:		python-attrs
Version:	17.2.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/attrs/
Source0:	https://files.pythonhosted.org/packages/be/41/e909cb6d901e9689da947419505cc7fb7d242a08a62ee221fce6a009a523/attrs-%{version}.tar.gz
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
