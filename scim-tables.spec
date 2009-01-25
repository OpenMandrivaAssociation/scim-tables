%define version	0.5.9
%define release	%mkrel 1

Name:		scim-tables
Summary:	Data files for SCIM Generic Table input method module
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.net/projects/scim/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/scim/%{name}-%{version}.tar.gz
Patch1:		scim-tables-0.5.0-fix-l10n.patch
Patch2:		scim-tables-0.5.8-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim-client = %{scim_api}
Obsoletes:	%mklibname %name 0
BuildRequires:	scim-devel >= 1.4.7-4mdk
Requires:	scim-tables-lang = %{version}-%{release}

%description
This package includes many data files for 
SCIM Generic Table input method module.
The data files are came from unicon and xcin.

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/scim-make-table
%{_datadir}/scim/icons/table.png
%_mandir/man1/*
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so

#-------------------------------------------------------------
%package en
Summary:        Dummy package for scim-tables-lang
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:	locales-en
Conflicts:	scim-tables < 0.5.7-4
Provides:	scim-tables-lang = %{version}-%{release}

%description en
This package is dummy package to satisfy scim-tables-lang.

%files en
%defattr(-, root, root)
%doc README

#-------------------------------------------------------------
%package am
Summary:        Data files for Amharic
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-am
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description am
This package includes table IM data files for Amharic.

%files am
%defattr(-, root, root)
%{_datadir}/scim/tables/Amharic.bin
%{_datadir}/scim/icons/Amharic.png

#-------------------------------------------------------------
%package ar
Summary:        Data files for Arabic
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ar
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ar
This package includes table IM data files for Arabic.

%files ar
%defattr(-, root, root)
%{_datadir}/scim/tables/Arabic.bin
%{_datadir}/scim/icons/Arabic.png

#-------------------------------------------------------------
%package bn
Summary:        Data files for Bengali
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-bn
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description bn
This package includes table IM data files for Bengali.

%files bn
%defattr(-, root, root)
%{_datadir}/scim/tables/Bengali-inscript.bin
%{_datadir}/scim/tables/Bengali-probhat.bin
%{_datadir}/scim/icons/Bengali-inscript.png
%{_datadir}/scim/icons/Bengali-probhat.png

#-------------------------------------------------------------
%package gu
Summary:        Data files for Gujarati
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-gu
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description gu
This package includes table IM data files for Gujarati.

%files gu
%defattr(-, root, root)
%{_datadir}/scim/tables/Gujarati-inscript.bin
%{_datadir}/scim/tables/Gujarati-phonetic.bin
%{_datadir}/scim/icons/Gujarati-inscript.png
%{_datadir}/scim/icons/Gujarati-phonetic.png

#-------------------------------------------------------------
%package hi
Summary:        Data files for Hindi
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-hi
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description hi
This package includes table IM data files for Hindi.

%files hi
%defattr(-, root, root)
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin
%{_datadir}/scim/icons/Hindi-inscript.png
%{_datadir}/scim/icons/Hindi-phonetic.png

#-------------------------------------------------------------
%package ja
Summary:        Data files for Japanese
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ja
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ja
This package includes table IM data files for Japanese.

%files ja
%defattr(-, root, root)
%doc tables/ja/kanjidic_licence.html tables/ja/kanjidic_doc.html tables/ja/kanjidic-permission-to-use-for-scim
%{_datadir}/scim/tables/HIRAGANA.bin
%{_datadir}/scim/tables/KATAKANA.bin
%{_datadir}/scim/tables/Nippon.bin
%{_datadir}/scim/icons/HIRAGANA.png
%{_datadir}/scim/icons/KATAKANA.png
%{_datadir}/scim/icons/Nippon.png

#-------------------------------------------------------------
%package kn
Summary:        Data files for Kannada
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-kn
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description kn
This package includes table IM data files for Kannada.

%files kn
%defattr(-, root, root)
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png

#-------------------------------------------------------------
%package ko
Summary:        Data files for Korean
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ko
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ko
This package includes table IM data files for Korean.

%files ko
%defattr(-, root, root)
%{_datadir}/scim/tables/Hangul.bin
%{_datadir}/scim/tables/HangulRomaja.bin
%{_datadir}/scim/tables/Hanja.bin
%{_datadir}/scim/icons/Hangul.png
%{_datadir}/scim/icons/Hanja.png

#-------------------------------------------------------------
%package ml
Summary:        Data files for Malayalam
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ml
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ml
This package includes table IM data files for Malayalam.

%files ml
%defattr(-, root, root)
%{_datadir}/scim/tables/Malayalam-inscript.bin
%{_datadir}/scim/tables/Malayalam-phonetic.bin
%{_datadir}/scim/icons/Malayalam-inscript.png
%{_datadir}/scim/icons/Malayalam-phonetic.png

#-------------------------------------------------------------
%package ne
Summary:        Data files for Nepali
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ne
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ne
This package includes table IM data files for Nepali.

%files ne
%defattr(-, root, root)
%{_datadir}/scim/tables/Nepali_Rom.bin
%{_datadir}/scim/tables/Nepali_Trad.bin
%{_datadir}/scim/icons/Nepali.png

#-------------------------------------------------------------
%package pa
Summary:        Data files for Punjabi
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-pa
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description pa
This package includes table IM data files for Punjabi.

%files pa
%defattr(-, root, root)
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png

#-------------------------------------------------------------
%package ru
Summary:        Data files for Yawerty
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ru
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ru
This package includes table IM data files for Yawerty.

%files ru
%defattr(-, root, root)
%{_datadir}/scim/tables/Yawerty.bin
%{_datadir}/scim/icons/Yawerty.png
%{_datadir}/scim/tables/RussianTraditional.bin
%{_datadir}/scim/icons/RussianTraditional.png

#-------------------------------------------------------------
%package ta
Summary:        Data files for Tamil
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-ta
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description ta
This package includes table IM data files for Tamil.

%files ta
%defattr(-, root, root)
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin
%{_datadir}/scim/tables/Tamil-remington.bin
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%{_datadir}/scim/icons/Tamil-remington.png

#-------------------------------------------------------------
%package te
Summary:        Data files for Telugu
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-te
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description te
This package includes table IM data files for Telugu.

%files te
%defattr(-, root, root)
%{_datadir}/scim/tables/Telugu-inscript.bin
%{_datadir}/scim/icons/Telugu-inscript.png

#-------------------------------------------------------------
%package th
Summary:        Data files for Thai
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-th
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description th
This package includes table IM data files for Thai.

%files th
%defattr(-, root, root)
%{_datadir}/scim/tables/Thai.bin
%{_datadir}/scim/icons/Thai.png

#-------------------------------------------------------------
%package uk
Summary:        Data files for Ukrainian
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-uk
Provides:       scim-tables-lang = %{version}-%{release}

%description uk
This package includes table IM data files for Ukrainian.

%files uk
%defattr(-, root, root)
%{_datadir}/scim/tables/Ukrainian-Translit.bin
%{_datadir}/scim/tables/Translit.bin

#-------------------------------------------------------------
%package vi
Summary:        Data files for Viqr
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:       locales-vi
Conflicts:      scim-tables < 0.5.7-4
Provides:       scim-tables-lang = %{version}-%{release}

%description vi
This package includes table IM data files for Viqr.

%files vi
%defattr(-, root, root)
%{_datadir}/scim/tables/Viqr.bin
%{_datadir}/scim/icons/Viqr.png

#-------------------------------------------------------------
%package zh
Summary:        Data files for Chinese
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Requires:	locales-zh
Conflicts:	scim-tables < 0.5.7-4
Provides:	scim-tables-lang = %{version}-%{release}

%description zh
This package includes table IM data files for Chinese.

%files zh
%defattr(-, root, root)
%doc tables/zh/README-Erbi.txt tables/zh/README-CangJie.txt
%doc tables/zh/README-Wu.txt
%{_datadir}/scim/tables/Erbi.bin
%{_datadir}/scim/tables/Erbi-QS.bin
%{_datadir}/scim/tables/Wubi.bin
%{_datadir}/scim/tables/Ziranma.bin
%{_datadir}/scim/icons/Erbi.png
%{_datadir}/scim/icons/Erbi-QS.png
%{_datadir}/scim/icons/Wubi.png
%{_datadir}/scim/icons/Ziranma.png

%{_datadir}/scim/tables/Array30.bin
%{_datadir}/scim/tables/CangJie.bin
%{_datadir}/scim/tables/CangJie3.bin
%{_datadir}/scim/tables/CangJie5.bin
%{_datadir}/scim/tables/Cantonese.bin
%{_datadir}/scim/tables/CantonHK.bin
%{_datadir}/scim/tables/CNS11643.bin
%{_datadir}/scim/tables/Dayi3.bin
%{_datadir}/scim/tables/EZ-Big.bin
%{_datadir}/scim/tables/Jyutping.bin
%{_datadir}/scim/tables/Quick.bin
%{_datadir}/scim/tables/Simplex.bin
%{_datadir}/scim/tables/Stroke5.bin
%{_datadir}/scim/tables/Wu.bin
%{_datadir}/scim/tables/ZhuYin.bin
%{_datadir}/scim/tables/ZhuYin-Big.bin
%{_datadir}/scim/icons/Array30.png
%{_datadir}/scim/icons/CangJie.png
%{_datadir}/scim/icons/CangJie3.png
%{_datadir}/scim/icons/Cantonese.png
%{_datadir}/scim/icons/CantonHK.png
%{_datadir}/scim/icons/CNS11643.png
%{_datadir}/scim/icons/Dayi.png
%{_datadir}/scim/icons/EZ.png
%{_datadir}/scim/icons/Jyutping.png
%{_datadir}/scim/icons/Quick.png
%{_datadir}/scim/icons/Simplex.png
%{_datadir}/scim/icons/Stroke5.png
%{_datadir}/scim/icons/Wu.png
%{_datadir}/scim/icons/ZhuYin.png

#-------------------------------------------------------------
%package additional
Summary:        Data files for additional languages
Group:          System/Internationalization
Requires:       scim-tables >= %{version}-%{release}
Conflicts:      scim-tables < 0.5.7-4

%description additional
This package includes table IM data files for additional languages.

%files additional
%defattr(-, root, root)
%{_datadir}/scim/tables/LaTeX.bin
%{_datadir}/scim/tables/IPA-X-SAMPA.bin
%{_datadir}/scim/icons/LaTeX.png
%{_datadir}/scim/icons/IPA-X-SAMPA.png

#-------------------------------------------------------------
%prep
%setup -q
%patch1 -p1
%patch2 -p0

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{scim_plugins_dir}/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT
