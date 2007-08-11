%define version	0.5.7
%define release	%mkrel 3

%define scim_version	1.4.5
%define skim_version	1.4.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-tables
Summary:	Data files for SCIM Generic Table input method module
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.net/projects/scim/
Source0:		http://ovh.dl.sourceforge.net/sourceforge/scim/%{name}-%{version}.tar.bz2
Patch1:		scim-tables-0.5.0-fix-l10n.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		scim >= %{scim_version}
Requires:		%{libname} = %{version}
BuildRequires:		scim-devel >= 1.4.7-4mdk
BuildRequires:		libskim-devel >= %{skim_version}

%description
This package includes many data files for 
SCIM Generic Table input method module.
The data files are came from unicon and xcin.


%package -n %{libname}
Summary:	Scim-tables library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}

%description -n %{libname}
Scim-tables library.

%package skim
Summary:	Skim setup plugin for scim-tables
Group:		System/Internationalization
Requires:	%{name} = %{version} 
Requires:       skim = %{skim_version}

%description skim
This package contains skim setup plugin for scim-tables.


%prep
%setup -q
%patch1 -p1

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{scim_plugins_dir}/*/*.{a,la}

%find_lang %{name}
%find_lang skim-scim-tables

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/scim-make-table
%{_datadir}/scim/tables/*.bin
%{_datadir}/scim/icons/*.png
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so

%files skim -f skim-scim-tables.lang
%defattr(-,root,root)
%doc COPYING
%{_datadir}/apps/skim/pics/scim-tables.png
%{_datadir}/config.kcfg/generictable.kcfg
%{_datadir}/services/skimconfiguredialog/skimplugin_scim_table_config.desktop
%{_libdir}/kde3/kcm_skimplugin_scim_tables.la
%{_libdir}/kde3/kcm_skimplugin_scim_tables.so
