#
# spec file for packages mingw32-libhllapi
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (C) <2008> <Banco do Brasil S.A.>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}
%define __os_install_post %{_mingw32_debug_install_post} \
                          %{_mingw32_install_post}

#---[ Main package ]--------------------------------------------------------------------------------------------------

Name:		mingw32-libhllapi
Summary:	HLLAPI client library for lib3270/pw3270
Version:	5.2
Release:	0
License:	LGPL-3.0
Source:		libhllapi-%{version}.tar.xz

URL:		https://github.com/PerryWerneck/libhllapi

Group:		Development/Libraries/C and C++

BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  m4

BuildRequires:	mingw32-cross-binutils
BuildRequires:	mingw32-cross-gcc
BuildRequires:	mingw32-cross-gcc-c++
BuildRequires:	mingw32-cross-pkg-config
BuildRequires:	mingw32-filesystem
BuildRequires:	mingw32-zlib-devel
BuildRequires:	mingw32(lib:iconv)
BuildRequires:	mingw32(lib:intl)

BuildRequires:	mingw32(pkg:ipc3270)

%description

HLLAPI client library for pw3270/lib3270

See more details at https://softwarepublico.gov.br/social/pw3270/

#---[ Library ]-------------------------------------------------------------------------------------------------------

%define _product %(i686-w64-mingw32-pkg-config --variable=product_name lib3270)
%define MAJOR_VERSION %(echo %{version} | cut -d. -f1)
%define MINOR_VERSION %(echo %{version} | cut -d. -f2)
%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%package -n %{name}-%{_libvrs}
Summary:	IPC Library for pw3270
Group:		Development/Libraries/C and C++
Provides:	mingw32(lib:ipc3270)

%description -n %{name}-%{_libvrs}

HLLAPI client library for pw3270/lib3270

See more details at https://softwarepublico.gov.br/social/pw3270/

#---[ Development ]---------------------------------------------------------------------------------------------------

%package devel
Summary: Development files for %{name}
Requires: mingw32(pkg:ipc3270)

%description devel

HLLAPI client library for pw3270/lib3270

See more details at https://softwarepublico.gov.br/social/pw3270/

#---[ Build & Install ]-----------------------------------------------------------------------------------------------

%prep
%setup -n libhllapi-%{version}

NOCONFIGURE=1 \
	./autogen.sh

%{_mingw32_configure} \
	--enable-static

%build
make all

%{_mingw32_strip} \
	--strip-all \
    .bin/Release/*.dll

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%files -n %{name}-%{_libvrs}
%defattr(-,root,root)

%doc AUTHORS README.md
%license LICENSE

%{_mingw32_libdir}/libhllapi.dll
%{_mingw32_libdir}/libhllapi.dll.%{MAJOR_VERSION}
%{_mingw32_libdir}/libhllapi.dll.%{MAJOR_VERSION}.%{MINOR_VERSION}

%files devel
%defattr(-,root,root)

%{_mingw32_includedir}/lib3270/*.h
%{_mingw32_libdir}/*.a
%{_mingw32_libdir}/*.lib
%{_mingw32_datadir}/%{_product}/def/*.def

%changelog

