Summary:	SJP.pl Polish dictionary for aspell
Summary(pl.UTF-8):	Słownik polski SJP.pl aspella
Name:		aspell-pl-alt
Version:	20110122
Release:	1
License:	Creative Commons License (see legalcode.html)
Group:		Applications/Text
Source0:	http://sjp.pl/slownik/ort/sjp-aspell6-pl-6.0_%{version}-0.tar.bz2
# Source0-md5:	d1b6cc48374ded9f9c797d09b71156fd
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
# Source1-md5:	0ed76e90db3d98d93cf6f7a610c10f77
URL:		http://www.sjp.pl/slownik/ort/
BuildRequires:	aspell >= 3:0.60.0
BuildRequires:	which
Requires:	aspell >= 3:0.60.0
Conflicts:	aspell-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SJP.pl (formerly called "alternative") Polish dictionary for aspell,
done for gaming purposes initially, at the moment contains 2.9 million
words and has one of the best grammatic rules.

%description -l pl.UTF-8
Słownik polski SJP.pl (dawniej znany jako "alternatywny") dla programu
aspell, na początku tworzony do gier ortograficznych, z czasem
przerodził się w jeden z największych (2,9 mln. słów), najlepiej
ubogaconych (m.in. w zasady gramatyczne) oraz najszybciej rozwijanych
słowników.

%prep
%setup -q -n aspell6-pl-6.0_%{version}-0

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
%{_libdir}/aspell/pl.*
%{_libdir}/aspell/polish.alias
%{_datadir}/aspell/pl.dat
%{_datadir}/aspell/pl_affix.dat
