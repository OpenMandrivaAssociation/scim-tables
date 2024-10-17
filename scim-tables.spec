Summary:	Data files for SCIM Generic Table input method module
Name:		scim-tables
Version:	0.5.13
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		https://sourceforge.net/projects/scim/
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(scim) >= 1.4.9
BuildRequires:	pkgconfig(scim-gtkutils) >= 1.4.9
Requires:	scim-tables-lang = %{EVRD}

%description
This package includes many data files for SCIM Generic Table input method
module. The data files are came from unicon and xcin.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/scim-make-table
%{_datadir}/scim/icons/table.png
%{_mandir}/man1/*
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so

#----------------------------------------------------------------------------

%package en
Summary:	Dummy package for scim-tables-lang
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-en
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description en
This package is dummy package to satisfy scim-tables-lang.

%files en
%doc README

#----------------------------------------------------------------------------

%package am
Summary:	Data files for Amharic
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-am
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description am
This package includes table IM data files for Amharic.

%files am
%{_datadir}/scim/tables/Amharic.bin
%{_datadir}/scim/icons/Amharic.png

#----------------------------------------------------------------------------

%package ar
Summary:	Data files for Arabic
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ar
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ar
This package includes table IM data files for Arabic.

%files ar
%{_datadir}/scim/tables/Arabic.bin
%{_datadir}/scim/icons/Arabic.png

#----------------------------------------------------------------------------

%package bn
Summary:	Data files for Bengali
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-bn
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description bn
This package includes table IM data files for Bengali.

%files bn
%{_datadir}/scim/tables/Bengali-inscript.bin
%{_datadir}/scim/tables/Bengali-probhat.bin
%{_datadir}/scim/icons/Bengali-inscript.png
%{_datadir}/scim/icons/Bengali-probhat.png

#----------------------------------------------------------------------------

%package el
Summary:	Data files for Greek
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-el
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description el
This package includes table IM data files for Greek.

%files el
%{_datadir}/scim/tables/greekpoly.bin

#----------------------------------------------------------------------------

%package gu
Summary:	Data files for Gujarati
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-gu
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description gu
This package includes table IM data files for Gujarati.

%files gu
%{_datadir}/scim/tables/Gujarati-inscript.bin
%{_datadir}/scim/tables/Gujarati-phonetic.bin
%{_datadir}/scim/icons/Gujarati-inscript.png
%{_datadir}/scim/icons/Gujarati-phonetic.png

#----------------------------------------------------------------------------

%package he
Summary:	Data files for Hebrew
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-he
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description he
This package includes table IM data files for Hebrew.

%files he
%{_datadir}/scim/tables/classicalhebrew.bin
%{_datadir}/scim/tables/HebrewComputer.bin
%{_datadir}/scim/icons/HebrewComputer.png

#----------------------------------------------------------------------------

%package hi
Summary:	Data files for Hindi
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-hi
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description hi
This package includes table IM data files for Hindi.

%files hi
%{_datadir}/scim/tables/Hindi-remington.bin
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin
%{_datadir}/scim/icons/Hindi-remington.png
%{_datadir}/scim/icons/Hindi-inscript.png
%{_datadir}/scim/icons/Hindi-phonetic.png

#----------------------------------------------------------------------------

%package ja
Summary:	Data files for Japanese
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ja
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ja
This package includes table IM data files for Japanese.

%files ja
%doc tables/ja/kanjidic_licence.html tables/ja/kanjidic_doc.html tables/ja/kanjidic-permission-to-use-for-scim
%{_datadir}/scim/tables/HIRAGANA.bin
%{_datadir}/scim/tables/KATAKANA.bin
%{_datadir}/scim/tables/Nippon.bin
%{_datadir}/scim/icons/HIRAGANA.png
%{_datadir}/scim/icons/KATAKANA.png
%{_datadir}/scim/icons/Nippon.png

#----------------------------------------------------------------------------

%package kn
Summary:	Data files for Kannada
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-kn
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description kn
This package includes table IM data files for Kannada.

%files kn
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png

#----------------------------------------------------------------------------

%package ko
Summary:	Data files for Korean
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ko
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ko
This package includes table IM data files for Korean.

%files ko
%{_datadir}/scim/tables/Hangul.bin
%{_datadir}/scim/tables/HangulRomaja.bin
%{_datadir}/scim/tables/Hanja.bin
%{_datadir}/scim/icons/Hangul.png
%{_datadir}/scim/icons/Hanja.png

#----------------------------------------------------------------------------

%package ml
Summary:	Data files for Malayalam
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ml
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ml
This package includes table IM data files for Malayalam.

%files ml
%{_datadir}/scim/tables/Malayalam-inscript.bin
%{_datadir}/scim/tables/Malayalam-phonetic.bin
%{_datadir}/scim/icons/Malayalam-inscript.png
%{_datadir}/scim/icons/Malayalam-phonetic.png

#----------------------------------------------------------------------------

%package mr
Summary:	Data files for Marathi
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-mr
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description mr
This package includes table IM data files for Marathi.

%files mr
%{_datadir}/scim/tables/Marathi-remington.bin
%{_datadir}/scim/icons/Marathi-remington.png

#----------------------------------------------------------------------------

%package ne
Summary:	Data files for Nepali
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ne
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ne
This package includes table IM data files for Nepali.

%files ne
%{_datadir}/scim/tables/Nepali_Rom.bin
%{_datadir}/scim/tables/Nepali_Trad.bin
%{_datadir}/scim/icons/Nepali.png

#----------------------------------------------------------------------------

%package pa
Summary:	Data files for Punjabi
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-pa
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description pa
This package includes table IM data files for Punjabi.

%files pa
%{_datadir}/scim/tables/Punjabi-remington.bin
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin
%{_datadir}/scim/icons/Punjabi-remington.png
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png

#----------------------------------------------------------------------------

%package ru
Summary:	Data files for Yawerty
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ru
Conflicts:	scim-tables-uk < 0.5.13
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ru
This package includes table IM data files for Yawerty.

%files ru
%{_datadir}/scim/icons/Translit.png
%{_datadir}/scim/tables/Translit.bin
%{_datadir}/scim/tables/Yawerty.bin
%{_datadir}/scim/icons/Yawerty.png
%{_datadir}/scim/icons/RussianComputer.png
%{_datadir}/scim/tables/RussianTraditional.bin
%{_datadir}/scim/icons/RussianTraditional.png
%{_datadir}/scim/tables/RussianComputer.bin

#----------------------------------------------------------------------------

%package ta
Summary:	Data files for Tamil
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ta
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ta
This package includes table IM data files for Tamil.

%files ta
%{_datadir}/scim/tables/Tamil-tamil99.bin
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin
%{_datadir}/scim/tables/Tamil-remington.bin
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%{_datadir}/scim/icons/Tamil-remington.png
%{_datadir}/scim/icons/Tamil-tamil99.png

#----------------------------------------------------------------------------

%package te
Summary:	Data files for Telugu
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-te
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description te
This package includes table IM data files for Telugu.

%files te
%{_datadir}/scim/tables/Telugu-inscript.bin
%{_datadir}/scim/icons/Telugu-inscript.png

#----------------------------------------------------------------------------

%package th
Summary:	Data files for Thai
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-th
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description th
This package includes table IM data files for Thai.

%files th
%{_datadir}/scim/tables/Thai.bin
%{_datadir}/scim/icons/Thai.png

#----------------------------------------------------------------------------

%package ug
Summary:	Data files for Uyghur
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-ug
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description ug
This package includes table IM data files for Uyghur.

%files ug
%{_datadir}/scim/tables/Uyghur-Romanized.bin
%{_datadir}/scim/tables/Uyghur-Standard.bin
%{_datadir}/scim/icons/Uyghur.png

#----------------------------------------------------------------------------

%package uk
Summary:	Data files for Ukrainian
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-uk
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description uk
This package includes table IM data files for Ukrainian.

%files uk
%{_datadir}/scim/tables/Ukrainian-Translit.bin
%{_datadir}/scim/icons/Ukrainian-Translit.png

#----------------------------------------------------------------------------

%package vi
Summary:	Data files for Viqr
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-vi
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description vi
This package includes table IM data files for Viqr.

%files vi
%{_datadir}/scim/tables/Viqr.bin
%{_datadir}/scim/icons/Viqr.png

#----------------------------------------------------------------------------

%package zh
Summary:	Data files for Chinese
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
Requires:	locales-zh
Provides:	scim-tables-lang = %{EVRD}
BuildArch:	noarch

%description zh
This package includes table IM data files for Chinese.

%files zh
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
%{_datadir}/scim/tables/SmartCangJie6.bin
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
%{_datadir}/scim/icons/SmartCangJie6.png

#----------------------------------------------------------------------------

%package additional
Summary:	Data files for additional languages
Group:		System/Internationalization
Requires:	scim-tables = %{EVRD}
BuildArch:	noarch

%description additional
This package includes table IM data files for additional languages.

%files additional
%{_datadir}/scim/tables/LaTeX.bin
%{_datadir}/scim/tables/IPA-X-SAMPA.bin
%{_datadir}/scim/tables/IPA-Kirshenbaum.bin
%{_datadir}/scim/icons/LaTeX.png
%{_datadir}/scim/icons/IPA-X-SAMPA.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

