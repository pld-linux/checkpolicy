Summary:	SELinux policy compiler
Name:		checkpolicy
Version:	1.0
Release:	1
License:	Public domain (uncopyrighted)
Group:		Development
# Source0-md5:	7b69ecafb4b8dd8313dae0e5fadc960e
Source0:	http://www.nsa.gov/selinux/lk/%{name}-%{version}.tgz
BuildRequires:	byacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler. Only
required for building policies.

%description -l pl
Security-enhanced Linux jest prototypem j±dra Linuksa i wielu aplikacji 
u¿ytkowych o funkcjach podwy¿szonego bezpieczeñstwa. Zaprojektowany jest
tak, aby w prosty sposób ukazaæ znaczenie mandatowej kontroli dostêpu dla 
spo³eczno¶ci Linuksowej. Ukazuje równie¿ jak tak± kontrolê mo¿na dodaæ do 
istniej±cego systemu typu Linuks. J±dro SELinux zawiera nowe sk³adniki 
architektury pierwotnie opracowane w celu ulepszenia bezpieczeñstwa systemu 
operacyjnego Flask. Te elementy zapewniaj± ogólne wsparcie we wdra¿aniu wielu 
typów polityk mandatowej kontroli dostêpu, w³±czaj±c te wzorowane na: Type 
Enforcement (TE), kontroli dostêpu opartej na rolach (RBAC) i zabezpieczeniach 
wielopoziomowych.

Ten pakiet zawiera chceckpolicy - kompilator polityki SELinux. Jest wymagany 
do zbudowania polityki.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkpolicy
