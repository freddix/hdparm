Summary:	Utility for setting (E)IDE performance parameters
Name:		hdparm
Version:	9.43
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/hdparm/%{name}-%{version}.tar.gz
# Source0-md5:	f73233be118d86c779a8463d8b6a3cdb
Patch0:		%{name}-man.patch
URL:		http://sourceforge.net/projects/hdparm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a utility for setting Hard Drive parameters. It is useful for
tweaking performance and for doing things like spinning down hard
drives to conserve power.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install hdparm $RPM_BUILD_ROOT%{_sbindir}
install hdparm.8 $RPM_BUILD_ROOT%{_mandir}/man8
install contrib/idectl $RPM_BUILD_ROOT%{_sbindir}
install contrib/ultrabayd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib/README Changelog README.acoustic
%attr(755,root,root) %{_sbindir}/hdparm
%attr(755,root,root) %{_sbindir}/idectl
%attr(755,root,root) %{_sbindir}/ultrabayd
%{_mandir}/man8/*

