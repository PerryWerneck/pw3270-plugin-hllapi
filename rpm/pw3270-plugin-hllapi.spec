#
# spec file for packages pw3270-plugin-ipc
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

#---[ Versions ]------------------------------------------------------------------------------------------------------

%define MAJOR_VERSION 5
%define MINOR_VERSION 2

#---[ Main package ]--------------------------------------------------------------------------------------------------

Summary:	HLLAPI plugin and client library for pw3270
Name:		pw3270-plugin-hllapi
Version:	5.2
Release:	0
License:	LGPL-3.0
Source:		%{name}-%{version}.tar.xz

Url:		https://portal.softwarepublico.gov.br/social/pw3270/

Group:		System/X11/Terminals
BuildRoot:	/var/tmp/%{name}-%{version}


BuildRequires:	lib3270-devel >= 5.2
BuildRequires:	libv3270-devel >= 5.2
BuildRequires:	pw3270-devel >= 5.2
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  m4

%if 0%{?fedora} ||  0%{?suse_version} > 1200

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)

%else

BuildRequires:  openssl-devel
BuildRequires:  dbus-1-devel
BuildRequires:	gtk3-devel

%endif

%description

Plugin and client library for compatibility with the old HLLAPI.

See more details at https://softwarepublico.gov.br/social/pw3270/

#---[ Build & Install ]-----------------------------------------------------------------------------------------------

%prep
%setup

NOCONFIGURE=1 ./autogen.sh

%configure \
	--with-sdk-version=%{version}

%build
make clean
make all

%install
rm -rf $RPM_BUILD_ROOT

make \
	DESTDIR=%{?buildroot:%{buildroot}} \
	install

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md

%{_libdir}/pw3270-plugins/*.so

%{_libdir}/libhllapi.so
%{_libdir}/libhllapi.so.%{MAJOR_VERSION}
%{_libdir}/libhllapi.so.%{MAJOR_VERSION}.%{MINOR_VERSION}

%pre
/sbin/ldconfig
exit 0

%post
/sbin/ldconfig
exit 0

%postun
/sbin/ldconfig
exit 0

%changelog
