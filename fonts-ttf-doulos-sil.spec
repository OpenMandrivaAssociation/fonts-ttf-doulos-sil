%define pkgname DoulosSIL

Summary:	Unicode Times-like font with only regular face
Name:		fonts-ttf-doulos-sil
Version:	4.110
Release:	%mkrel 1
License:	OFL
Group:		System/Fonts/True type
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=DoulosSILfont
Source0:	%{pkgname}-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
The goal for this product was to provide a single Unicode-based font family
that would contain a comprehensive inventory of glyphs needed for almost any
Roman- or Cyrillic-based writing system, whether used for phonetic
or orthographic needs. In addition, there is provision for other characters
and symbols useful to linguists. This font makes use of state-of-the-art font
technologies to support complex typographic issues, such as the need
to position arbitrary combinations of base glyphs and diacritics optimally.

Doulos is very similar to Times/Times New Roman, but only has a single face -
regular. It is intended for use alongside other Times-like fonts where
a range of styles (italic, bold) are not needed.

%prep
%setup -q -n %{pkgname}-%{version}
dos2unix *.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/doulos-sil

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/doulos-sil
ttmkfdir %{buildroot}%{_xfontdir}/TTF/doulos-sil -o %{buildroot}%{_xfontdir}/TTF/doulos-sil/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/doulos-sil/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/doulos-sil \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-doulos-sil:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt
%dir %{_xfontdir}/TTF/doulos-sil
%{_xfontdir}/TTF/doulos-sil/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/doulos-sil/fonts.dir
%{_xfontdir}/TTF/doulos-sil/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-doulos-sil:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.110-1mdv2012.0
+ Revision: 739486
- Update to 4.110

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 4.106-1
+ Revision: 690965
- imported package fonts-ttf-doulos-sil

