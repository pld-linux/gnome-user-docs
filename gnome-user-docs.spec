Summary:	General GNOME User Documentation
Summary(pl.UTF-8):	Ogólna dokumentacja użytkownika GNOME
Name:		gnome-user-docs
Version:	41.0
Release:	1
License:	CC-BY v3.0
Group:		Documentation
Source0:	https://download.gnome.org/sources/gnome-user-docs/41/%{name}-%{version}.tar.xz
# Source0-md5:	724bab8811cc183702c4423927ec3bda
URL:		https://wiki.gnome.org/DocumentationProject
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools >= 3.4.1
Requires:	yelp >= 3.4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl.UTF-8
Ogólna dokumentacja użytkownika GNOME.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gnome-help and system-admin-guide
%find_lang gnome-help --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gnome-help.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README
