Summary:	Composite extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Composite
Name:		xorg-proto-compositeproto
Version:	0.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{version}.tar.bz2
# Source0-md5:	6281344d656d4e0c8e9db4918efe3d1d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Composite.

%package devel
Summary:	Composite extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Composite
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	compositeext

%description devel
Composite extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Composite.

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
%doc AUTHORS COPYING ChangeLog README compositeproto.txt
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/compositeproto.pc
