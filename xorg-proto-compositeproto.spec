Summary:	Composite protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Composite i pomocnicze
Name:		xorg-proto-compositeproto
Version:	0.3.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{version}.tar.bz2
# Source0-md5:	54f1fbd567f57093df054f8440a60a5e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Composite i pomocnicze.

%package devel
Summary:	Composite protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Composite i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	compositeext

%description devel
Composite protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Composite i pomocnicze.

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
