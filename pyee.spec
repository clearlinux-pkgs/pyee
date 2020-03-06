#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyee
Version  : 6.0.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/1f/8e/ec9a9d07bcf316ebe8ef2c30b5c597988f5b8d324f8273c307843e63f49e/pyee-6.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/8e/ec9a9d07bcf316ebe8ef2c30b5c597988f5b8d324f8273c307843e63f49e/pyee-6.0.0.tar.gz
Summary  : A port of node.js's EventEmitter to python.
Group    : Development/Tools
License  : MIT
Requires: pyee-python = %{version}-%{release}
Requires: pyee-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest-asyncio
BuildRequires : pytest-runner
BuildRequires : vcversioner

%description
pyee
====
.. image:: https://travis-ci.org/jfhbrook/pyee.png
:target: https://travis-ci.org/jfhbrook/pyee
.. image:: https://readthedocs.org/projects/pyee/badge/?version=latest
:target: https://pyee.readthedocs.io

%package python
Summary: python components for the pyee package.
Group: Default
Requires: pyee-python3 = %{version}-%{release}

%description python
python components for the pyee package.


%package python3
Summary: python3 components for the pyee package.
Group: Default
Requires: python3-core
Provides: pypi(pyee)

%description python3
python3 components for the pyee package.


%prep
%setup -q -n pyee-6.0.0
cd %{_builddir}/pyee-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583533397
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
