#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Escapes
Summary:	Pod::Escapes Perl module - for resolving Pod <...> sequences
Summary(pl):	Modu³ Perla Pod::Escapes - dekodowanie sekwencji Pod <...>
Name:		perl-Pod-Escapes
Version:	1.04
Release:	1
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	00ea2e0d2e84ed98517a4616708b68d3
BuildRequires:	perl-devel >= 1:5.8.0
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
