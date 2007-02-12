Summary:	An alternative Polish dictionary for aspell by kurnik.pl
Summary(pl.UTF-8):   Alternatywny polski słownik dla aspella autorstwa kurnik.pl
Name:		aspell-pl-alt
Version:	20060902
Release:	1
License:	Creative Commons License (see legalcode.html)
Group:		Applications/Text
Source0:	http://www.kurnik.pl/dictionary/alt-aspell6-pl-6.0-%{version}.tar.bz2
# Source0-md5:	04cc0a16a7bcfc0055cdbbd044feb3a3
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
# Source1-md5:	0ed76e90db3d98d93cf6f7a610c10f77
URL:		http://www.kurnik.pl/slownik/ort/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
Obsoletes:	aspell-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternative Polish dictionary for aspell, done for gaming purposes
initially, at the moment contains 2.9 million words and has one of the
best grammatic rules.

Visit http://www.kurnik.pl/slownik/ once in awhile.

%description -l pl.UTF-8
Alternatywny polski słownik dla programu aspell, na początku tworzony
do gier ortograficznych, z czasem przerodził się w jeden z
największych (2,9 mln. słów), najlepiej ubogaconych (m.in. w zasady
gramatyczne) oraz najszybciej rozwijanych słowników.

Zapraszamy na <http://www.kurnik.pl/slownik/>.

%prep
%setup -q -n aspell6-pl-6.0-%{version}

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
