Summary:	General GNOME User Documentation
Summary(pl):	Ogólna dokumentacja u¿ytkownika GNOME
Name:		gnome-user-docs
Version:	2.14.2
Release:	2
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-user-docs/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	4f5a7114ccf9e4e31137da50b7333570
BuildRequires:	gnome-doc-utils >= 0.5.6
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires(post,postun):	scrollkeeper
Requires:	yelp >= 2.14.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl
Ogólna dokumentacja u¿ytkownika GNOME.

%prep
%setup -q

%build
gnome-doc-prepare --copy --force
%configure \
	 --disable-scrollkeeper
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

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_omf_dest_dir}/*-guide
