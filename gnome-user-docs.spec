Summary:	General GNOME User Documentation
Summary(pl):	Ogólna dokumentacja u¿ytkownika GNOME
Name:		gnome-user-docs
Version:	2.16.1
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-user-docs/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	4b0abfe5e24438414c22083851bae19e
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires(post,postun):	scrollkeeper
Requires:	yelp >= 2.16.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl
Ogólna dokumentacja u¿ytkownika GNOME.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
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
%dir %{_omf_dest_dir}/gnome-access-guide
%dir %{_omf_dest_dir}/system-admin-guide
%dir %{_omf_dest_dir}/user-guide

# access guide
%{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-C.omf
%lang(es) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-es.omf
%lang(it) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-it.omf
%lang(sv) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-sv.omf

# system guide
%{_omf_dest_dir}/system-admin-guide/system-admin-guide-C.omf
%lang(es) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-es.omf
%lang(it) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-it.omf
%lang(sv) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-sv.omf

# user guide
%{_omf_dest_dir}/user-guide/user-guide-C.omf
%lang(bg) %{_omf_dest_dir}/user-guide/user-guide-bg.omf
%lang(es) %{_omf_dest_dir}/user-guide/user-guide-es.omf
%lang(fr) %{_omf_dest_dir}/user-guide/user-guide-fr.omf
%lang(it) %{_omf_dest_dir}/user-guide/user-guide-it.omf
%lang(pt_BR) %{_omf_dest_dir}/user-guide/user-guide-pt_BR.omf
%lang(ru) %{_omf_dest_dir}/user-guide/user-guide-ru.omf
%lang(sv) %{_omf_dest_dir}/user-guide/user-guide-sv.omf
%lang(zh_CN) %{_omf_dest_dir}/user-guide/user-guide-zh_CN.omf
