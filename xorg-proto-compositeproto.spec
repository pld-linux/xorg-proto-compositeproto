Summary:	Composite protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Composite i pomocnicze
Name:		xorg-proto-compositeproto
Version:	0.3
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{version}.tar.bz2
# Source0-md5:	85e7abb79de5b49cb83524a608744b0b
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
%setup -q -n compositeproto-%{version}

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
