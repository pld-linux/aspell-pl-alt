Summary:	An alternative Polish dictionary for aspell by kurnik.pl
Summary(pl):	Alternatywny polski s³ownik dla ispella autorstwa kurnik.pl
Name:		aspell-pl-alt
Version:	20030818
Release:	1
License:	Creative Commons License (see legalcode.html)
Group:		Applications/Text
Source0:	http://www.kurnik.pl/slownik/ort/alt-aspell-pl-%{version}.tar.gz
# Source0-md5:	eeddac2f6ccac24a2dec4dadb0dd141b
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
URL:		http://www.kurnik.pl/slownik/ort/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternative Polish dictionary for ispell, done for gaming purposes
initially, at the moment contains 2.2 million words and has one of the
best grammatic rules.

Visit http://www.kurnik.pl/slownik/ once in awhile.

%description -l pl
Alternatywny polski s³ownik dla programu ispell, na pocz±tku tworzony
do gier ortograficznych, z czasem przerodzi³ siê w jeden z
najwiêkszych (2,2 mln. s³ów), najlepiej ubogaconych (m.in. w zasady
gramatyczne) oraz najszybciej rozwijanych.

Zapraszamy na http://www.kurnik.pl/slownik/ .

%prep
%setup -q -n alt-aspell-pl-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

cp %{SOURCE1} ./legalcode.html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright legalcode.html
%{_libdir}/aspell/*
%{_datadir}/aspell/*
