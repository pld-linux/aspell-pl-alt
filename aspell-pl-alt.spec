Summary:	An alternative Polish dictionary for aspell by kurnik.pl
Summary(pl):	Alternatywny polski s�ownik dla ispella autorstwa kurnik.pl
Name:		aspell-pl-alt
Version:	20040916
Release:	1
License:	Creative Commons License (see legalcode.html)
Group:		Applications/Text
Source0:	http://www.kurnik.pl/slownik/ort/alt-aspell-pl-%{version}.tar.bz2
# Source0-md5:	639a8fef5af03048c868cdae6d99a292
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
# Source1-md5:	8071e8643cd6a26ba5da38cf94acb250
Patch0:		%{name}-configure.patch
URL:		http://www.kurnik.pl/slownik/ort/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
Obsoletes:	aspell-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternative Polish dictionary for aspell, done for gaming purposes
initially, at the moment contains 2.9 million words and has one of the
best grammatic rules.

Visit http://www.kurnik.pl/slownik/ once in awhile.

%description -l pl
Alternatywny polski s�ownik dla programu aspell, na pocz�tku tworzony
do gier ortograficznych, z czasem przerodzi� si� w jeden z
najwi�kszych (2,9 mln. s��w), najlepiej ubogaconych (m.in. w zasady
gramatyczne) oraz najszybciej rozwijanych s�ownik�w.

Zapraszamy na http://www.kurnik.pl/slownik/ .

%prep
%setup -q -n alt-aspell-pl-%{version}
%patch0 -p1

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
