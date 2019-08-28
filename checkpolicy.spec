Summary:	SELinux policy compiler
Summary(pl.UTF-8):	Kompilator polityki SELinux
Name:		checkpolicy
Version:	2.9
Release:	1
License:	GPL v2
Group:		Development
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/20190315/%{name}-%{version}.tar.gz
# Source0-md5:	3b0e327f6c1a143f9720a1fbefede3c0
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libselinux-devel >= 2.9
# it uses libsepol symbols not exported in shared library
BuildRequires:	libsepol-static >= 2.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler. Only
required for building policies.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera checkpolicy - kompilator polityki SELinux. Jest
wymagany do zbudowania polityki.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -pipe" \
	YACC="bison -y" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkmodule
%attr(755,root,root) %{_bindir}/checkpolicy
%{_mandir}/man8/checkmodule.8*
%{_mandir}/man8/checkpolicy.8*
%lang(ru) %{_mandir}/ru/man8/checkmodule.8*
%lang(ru) %{_mandir}/ru/man8/checkpolicy.8*
