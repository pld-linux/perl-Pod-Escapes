#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Escapes
Summary:	Pod::Escapes Perl module - for resolving Pod <...> sequences
Summary(pl.UTF-8):	Moduł Perla Pod::Escapes - dekodowanie sekwencji Pod <...>
Name:		perl-Pod-Escapes
Version:	1.07
Release:	1
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d0c0470284733eca869cb5d146ab372
URL:		http://search.cpan.org/dist/Pod-Escapes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides things that are useful in decoding Pod <...>
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.

%description -l pl.UTF-8
Ten moduł udostępnia rzeczy przydatne do dekodowania sekwencji Pod
<...>. Zapewne powinien być używany tylko przez programy analizujące i
formatujące Pod.

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
%{perl_vendorlib}/Pod/Escapes.pm
%{_mandir}/man3/Pod::Escapes.3pm*
