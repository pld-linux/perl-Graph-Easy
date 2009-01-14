#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Graph
%define	pnam	Easy
Summary:	Graph::Easy - Convert or render graphs (as ASCII, HTML, SVG or via Graphviz)
#Summary(pl.UTF-8):	
Name:		perl-Graph-Easy
Version:	0.64
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graph/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ea6bb574f6055c351382e26bf570e21d
URL:		http://search.cpan.org/dist/Graph-Easy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph::Easy lets you generate graphs consisting of various shaped
nodes connected by edges (with optional labels).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Graph/*.pm
%{perl_vendorlib}/Graph/Easy
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
