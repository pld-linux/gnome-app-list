Summary:	GNOME app list
Summary(pl.UTF-8):	Lista aplikacji GNOME
Name:		gnome-app-list
Version:	1.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-app-list/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	dbcb730311857a1de67f4f77dcbf4eb0
URL:		https://gitlab.gnome.org/GNOME/gnome-app-list
BuildRequires:	libxml2-progs >= 2.0
BuildRequires:	python3 >= 1:3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides app recommendation data for the GNOME project,
in the form of AppStream data which is installed in the standard
system location. This is mainly used by the GNOME Software app
(<https://gitlab.gnome.org/GNOME/gnome-software>).

%description -l pl.UTF-8
Ten projekt dostarcza dane rekomendowanych aplikacji dla projektu
GNOME w postaci danych AppStream, instalowanych w standardowym miejscu
w systemie. Jest to wykorzystywane głównie przez aplikację GNOME
Software (<https://gitlab.gnome.org/GNOME/gnome-software>).

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
# XXX: owned also by gnome-software
%dir %{_datadir}/swcatalog
%dir %{_datadir}/swcatalog/xml
%{_datadir}/swcatalog/xml/org.gnome.App-list.xml
