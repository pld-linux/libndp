Summary:	Library for Neighbor Discovery Protocol
Summary(pl.UTF-8):	Biblioteka obsługująca protokół NDP (Neighbor Discovery Protocol)
Name:		libndp
Version:	1.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://libndp.org/
Source0:	http://libndp.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	ea4a2a3351991c1d561623772364ae14
URL:		http://libndp.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a library which provides a wrapper for IPv6
Neighbor Discovery Protocol. It also provides a tool named ndptool for
sending and receiving NDP messages.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę obudowującą protokół IPv6 NDP (Neighbor
Discovery Protocol). Dostarcza także narzędzie ndptool do wysyłania i
odbierania komunikatów NDP.

%package devel
Summary:	Header files for libndp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libndp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libndp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libndp.

%package static
Summary:	Static libndp library
Summary(pl.UTF-8):	Statyczna biblioteka libndp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libndp library.

%description static -l pl.UTF-8
Statyczna biblioteka libndp.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config; no external dependencies anyway
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libndp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ndptool
%attr(755,root,root) %{_libdir}/libndp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libndp.so.0
%{_mandir}/man8/ndptool.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libndp.so
%{_includedir}/ndp.h
%{_pkgconfigdir}/libndp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libndp.a
