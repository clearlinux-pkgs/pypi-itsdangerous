#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : pypi-itsdangerous
Version  : 2.1.2
Release  : 54
URL      : https://files.pythonhosted.org/packages/7f/a1/d3fb83e7a61fa0c0d3d08ad0a94ddbeff3731c05212617dff3a94e097f08/itsdangerous-2.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/7f/a1/d3fb83e7a61fa0c0d3d08ad0a94ddbeff3731c05212617dff3a94e097f08/itsdangerous-2.1.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/7f/a1/d3fb83e7a61fa0c0d3d08ad0a94ddbeff3731c05212617dff3a94e097f08/itsdangerous-2.1.2.tar.gz.asc
Summary  : Safely pass data to untrusted environments and back.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-itsdangerous-license = %{version}-%{release}
Requires: pypi-itsdangerous-python = %{version}-%{release}
Requires: pypi-itsdangerous-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ItsDangerous
============
... so better sign this
Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

%package license
Summary: license components for the pypi-itsdangerous package.
Group: Default

%description license
license components for the pypi-itsdangerous package.


%package python
Summary: python components for the pypi-itsdangerous package.
Group: Default
Requires: pypi-itsdangerous-python3 = %{version}-%{release}

%description python
python components for the pypi-itsdangerous package.


%package python3
Summary: python3 components for the pypi-itsdangerous package.
Group: Default
Requires: python3-core
Provides: pypi(itsdangerous)

%description python3
python3 components for the pypi-itsdangerous package.


%prep
%setup -q -n itsdangerous-2.1.2
cd %{_builddir}/itsdangerous-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648231734
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-itsdangerous
cp %{_builddir}/itsdangerous-2.1.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-itsdangerous/a814758bca3dc0a25555dabbf2576cdc43cd8423
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-itsdangerous/a814758bca3dc0a25555dabbf2576cdc43cd8423

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
