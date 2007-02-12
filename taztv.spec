Summary:	TV application with nagravision decryption capabilities
Summary(pl.UTF-8):   Aplikacja TV z możliwością odszyfrowywania nagravision
Name:		taztv
Version:	0.48
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geocities.com/taztv2001/%{name}-%{version}.tar.gz
# Source0-md5:	c1d0723ab72a4f3a15eb2bd335c42f41
URL:		http://www.geocities.com/taztv2001/
BuildRequires:	XFree86-devel
#BuildRequires:	alsa-lib-devel	# optional, off by default
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	lirc-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TV application with nagravision decryption capabilities.

%description -l pl.UTF-8
Aplikacja TV z możliwością odszyfrowywania nagravision.

%prep
%setup -q
sed 's/mkfontdir/echo/; /FONTDIR=/s/=.*/=ble/' \
	-i font/Makefile.in

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/misc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install font/led-fixed.pcf $RPM_BUILD_ROOT%{_fontsdir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
# already in xawdecode
#%{_fontsdir}/misc/led-fixed.pcf
