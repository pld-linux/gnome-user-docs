Summary:	General GNOME User Documentation
Summary(pl):	Ogólna dokumentacja u¿ytkownika GNOME
Name:		gnome2-user-docs
Version:	2.0.1
Release:	2
License:	GFDL
Group:		Documentation
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
Patch0:		%{name}-xml.patch
Requires(post,postun):scrollkeeper >= 0.3.11-4
Requires:	yelp >= 2.1.2-4
BuildRequires:	scrollkeeper >= 0.3.11-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl
Ogólna dokumentacja u¿ytkownika GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13 \
	--with-html-path=%{_gtkdocdir}

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
scrollkeeper-update

%postun
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_omf_dest_dir}/%{name}
