#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Escapes
Summary:	Pod::Escapes Perl module - for resolving Pod <...> sequences
Summary(pl):	Modu³ Perla Pod::Escapes - do dekodowania sekwencji Pod <...>
Name:		perl-Pod-Escapes
Version:	1.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides things that are useful in decoding Pod <...>
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.

%description -l pl
Ten modu³ udostêpnia rzeczy przydatne do dekodowania sekwencji Pod
<...>. Zapewne powinien byæ u¿ywany tylko przez programy analizuj±ce i
formatuj±ce Pod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
