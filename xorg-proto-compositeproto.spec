Summary:	Composite protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Composite i pomocnicze
Name:		xorg-proto-compositeproto
Version:	0.2.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/compositeproto-X11R7.0-%{version}.tar.bz2
# Source0-md5:	4de13ee64fdfd409134dfee9b184e6a9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Composite i pomocnicze.

%package devel
Summary:	Composite protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Composite i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	compositeext

%description devel
Composite protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Composite i pomocnicze.

%prep
%setup -q -n compositeproto-X11R7.0-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/compositeproto.pc
