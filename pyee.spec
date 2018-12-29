#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyee
Version  : 5.0.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/c6/35/b37e4ffbf46063c883675e028e38e2a24b67433fd587f188e2a5005d9329/pyee-5.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/35/b37e4ffbf46063c883675e028e38e2a24b67433fd587f188e2a5005d9329/pyee-5.0.0.tar.gz
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
====

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

%description python3
python3 components for the pyee package.


%prep
%setup -q -n pyee-5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541263900
python3 setup.py build

%install
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
