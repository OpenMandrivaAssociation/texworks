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
