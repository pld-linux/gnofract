Summary:	Fractal generator/browser
Summary(pl):	Generator i przeglądarka fraktali
Name:		gnofract
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.multimania.com/mason/%{name}-%{version}.tar.gz
# URL:		http://www.multimania.com/mason
BuildRequires:	gnome-libs-devel >= 1.0.12
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gnofract is a Fractal generator/browser.

%description -l pl
Gnofract to generator i przeglądarka fraktali.

%prep
%setup -q

%build
gettextize --copy --force
LDFAGS="-s"; export LDFAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnofract
