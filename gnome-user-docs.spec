Summary:	General GNOME User Documentation
Summary(pl.UTF-8):	Ogólna dokumentacja użytkownika GNOME
Name:		gnome-user-docs
Version:	2.20.1
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-user-docs/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	d6bba44acaed20117769ec8dce378f71
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires(post,postun):	scrollkeeper
Requires:	yelp >= 2.20.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl.UTF-8
Ogólna dokumentacja użytkownika GNOME.

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
%lang(de) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-de.omf
%lang(el) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-el.omf
%lang(en_GB) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-en_GB.omf
%lang(es) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-fr.omf
%lang(it) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-it.omf
%lang(pt) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-pt.omf
%lang(sv) %{_omf_dest_dir}/gnome-access-guide/gnome-access-guide-sv.omf

# system guide
%{_omf_dest_dir}/system-admin-guide/system-admin-guide-C.omf
%lang(es) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-es.omf
%lang(fr) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-fr.omf
%lang(it) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-it.omf
%lang(pa) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-pa.omf
%lang(pt) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-pt.omf
%lang(sv) %{_omf_dest_dir}/system-admin-guide/system-admin-guide-sv.omf

# user guide
%{_omf_dest_dir}/user-guide/user-guide-C.omf
%lang(ar) %{_omf_dest_dir}/user-guide/user-guide-ar.omf
%lang(bg) %{_omf_dest_dir}/user-guide/user-guide-bg.omf
%lang(de) %{_omf_dest_dir}/user-guide/user-guide-de.omf
%lang(el) %{_omf_dest_dir}/user-guide/user-guide-el.omf
%lang(es) %{_omf_dest_dir}/user-guide/user-guide-es.omf
%lang(fi) %{_omf_dest_dir}/user-guide/user-guide-fi.omf
%lang(fr) %{_omf_dest_dir}/user-guide/user-guide-fr.omf
%lang(hu) %{_omf_dest_dir}/user-guide/user-guide-hu.omf
%lang(it) %{_omf_dest_dir}/user-guide/user-guide-it.omf
%lang(ko) %{_omf_dest_dir}/user-guide/user-guide-ko.omf
%lang(pa) %{_omf_dest_dir}/user-guide/user-guide-pa.omf
%lang(pt) %{_omf_dest_dir}/user-guide/user-guide-pt.omf
%lang(pt_BR) %{_omf_dest_dir}/user-guide/user-guide-pt_BR.omf
%lang(ru) %{_omf_dest_dir}/user-guide/user-guide-ru.omf
%lang(sv) %{_omf_dest_dir}/user-guide/user-guide-sv.omf
%lang(zh_CN) %{_omf_dest_dir}/user-guide/user-guide-zh_CN.omf
