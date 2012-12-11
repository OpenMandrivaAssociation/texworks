%define name	texworks
%define version	0.4.4
%define rel		r1004
%define release 0.%{rel}

Summary:	A simple interface for working with TeX documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}-%{rel}.tar.gz
Source1:	TeXworks.pro
License:	GPLv2
Group:		Publishing
Url:		http://texworks.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.5.2
BuildRequires:  libpoppler-devel >= 0.16, libpoppler-qt4-devel >= 0.16
BuildRequires:	hunspell-devel >= 1.2.8, dbus-devel

%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc)
documents, with a Unicode-based, TeX-aware editor, integrated PDF
viewer, and a clean, simple interface accessible to casual and
non-technical users.

TeXworks is inspired by Dick Koch's award-winning TeXShop program for
Mac OS X, which has made quality typesetting through TeX accessible to
a wider community of users, without a technical or intimidating
face. The goal of TeXworks is to deliver a similarly integrated,
easy-to-use environment for users on other platforms, especially
GNU/Linux and Windows.

%prep
%setup -q -n %{name}-%{version}
cp -f %SOURCE1 .

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
export INSTALL_ROOT=%{buildroot}
%makeinstall 

mv -f manual/en html

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README COPYING html/
%_bindir/texworks
%_mandir/man1/texworks.*
%_datadir/applications/texworks.desktop
%_datadir/pixmaps/TeXworks.png


%changelog
* Thu May 10 2012 Lev Givon <lev@mandriva.org> 0.4.4-0.r1004
+ Revision: 797856
- Update to 0.4.4.

* Thu Jul 21 2011 Lev Givon <lev@mandriva.org> 0.4.3-0.r858
+ Revision: 690840
- Update to 0.4.3.

* Tue May 31 2011 Lev Givon <lev@mandriva.org> 0.4.1-0.r829
+ Revision: 682073
- Update to 0.4.1-r829.

* Mon May 16 2011 Lev Givon <lev@mandriva.org> 0.4.0-0.r759
+ Revision: 675134
- Update to 0.4.0.

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.2.3-3
+ Revision: 655748
- rebuild for new hunspell

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2011.0
+ Revision: 615172
- the mass rebuild of 2010.1 packages

* Thu Dec 10 2009 Lev Givon <lev@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 475990
- import texworks

