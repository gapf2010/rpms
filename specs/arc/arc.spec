# $Id$
# Authority: dag

Summary: Arc archiver
Name: arc
Version: 5.21p
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://arc.sourceforge.net/

Source: http://downloads.sourceforge.net/project/arc/arc/arc-%{version}/arc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%prep
%setup -q

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 arc %{buildroot}%{_bindir}/arc
%{__install} -Dp -m0755 marc %{buildroot}%{_bindir}/marc
%{__install} -Dp -m0644 arc.1 %{buildroot}%{_mandir}/man1/arc.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Arc521.doc Arcinfo Changelog COPYING LICENSE Readme
%doc %{_mandir}/man1/arc.1*
%{_bindir}/arc
%{_bindir}/marc

%changelog
* Tue Sep 07 2010 David Hrbáč <david@hrbac.cz> - 5.21p-1
- new upstream release

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 5.21o-1
- Updated to release 5.21o.

* Mon Jun 20 2005 Dries Verachtert <dries@ulyssis.org> - 5.21j-0
- Updated to release 5.21j.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
