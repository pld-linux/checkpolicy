Summary:	SELinux policy compiler
Summary(pl.UTF-8):	Kompilator polityki SELinux
Name:		checkpolicy
Version:	2.0.21
Release:	1
License:	GPL v2
Group:		Development
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	97080e8d11f307db2bcc2b9a03dd6b8e
URL:		http://userspace.selinuxproject.org/trac
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libselinux-devel >= 2.0
# it uses libsepol symbols not exported in shared library
BuildRequires:	libsepol-static >= 2.0.41
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
	CFLAGS="%{rpmcflags} -pipe" \
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
%doc ChangeLog
%attr(755,root,root) %{_bindir}/checkmodule
%attr(755,root,root) %{_bindir}/checkpolicy
%{_mandir}/man8/checkmodule.8*
%{_mandir}/man8/checkpolicy.8*
