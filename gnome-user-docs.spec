Summary:	General GNOME User Documentation
Summary(pl):	Ogólna dokumentacja u¿ytkownika GNOME
Name:		gnome2-user-docs
Version:	2.0.0
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.1/releases/final/%{name}-%{version}.tar.bz2
Requires(post,postun):scrollkeeper >= 0.3.11
Requires:	yelp >= 1.0.3
BuildRequires:	scrollkeeper >= 0.3.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME2
%define         _gtkdocdir      %{_defaultdocdir}/gtk-doc/html
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
General GNOME User Guide.

%description -l pl
Ogólna dokumentacja u¿ytkownika GNOME.

%prep
%setup -q

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
