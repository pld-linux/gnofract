Summary:	Fractal generator/browser
Summary(pl):	Generator i przegl±darka fraktali
Name:		gnofract
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.multimania.com/mason/%{name}-%{version}.tar.gz
# Source0-md5:	d35369281f199067b6fa6410873949f4
# URL:		http://www.multimania.com/mason
BuildRequires:	gnome-libs-devel >= 1.0.12
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gnofract is a Fractal generator/browser.

%description -l pl
Gnofract to generator i przegl±darka fraktali.

%prep
%setup -q

%build
%{__gettextize}
LDFAGS="-s"; export LDFAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnofract
