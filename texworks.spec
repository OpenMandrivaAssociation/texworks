%define name	texworks
%define version	0.2.3
%define release %mkrel 2

Summary:	A simple interface for working with TeX documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Publishing
Url:		http://texworks.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel, libpoppler-devel, libpoppler-qt4-devel
BuildRequires:	hunspell-devel, dbus-devel

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
%setup -q

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
%__install -D -m 755 texworks %{buildroot}%{_bindir}/texworks

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%_bindir/*

