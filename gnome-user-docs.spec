Summary:	General GNOME User Documentation
Summary(pl):	Ogólna dokumentacja u¿ytkownika GNOME
Name:		gnome2-user-docs
Version:	2.6.0
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	4cb05dd312aaf0cd000a9741274f8b47
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires:	yelp >= 2.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl
Ogólna dokumentacja u¿ytkownika GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	HTML_DIR=%{_gtkdocdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_omf_dest_dir}/%{name}
