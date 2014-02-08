Name: poppler-data
Version: 0.4.6
Release: 6
Summary: Encoding files for poppler
Source0: http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
License: Distributable
Group: Development/X11
Url: http://poppler.freedesktop.org/
BuildArch: noarch

%description
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them
if they are present.  When installed, the encoding files enables
poppler to correctly render CJK and Cyrillic properly.  While poppler
is licensed under the GPL, these encoding files are copyright Adobe
and licensed much more strictly, and thus distributed separately.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%makeinstall_std datadir=%_datadir

%files
%defattr(-,root,root)
%doc README COPYING
%_datadir/poppler/


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-2mdv2011.0
+ Revision: 667803
- mass rebuild

* Sun Oct 31 2010 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdv2011.0
+ Revision: 590875
- update to new version 0.4.4

* Mon Aug 02 2010 Lev Givon <lev@mandriva.org> 0.4.3-1mdv2011.0
+ Revision: 565023
- Update to 0.4.3.

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 550292
- update to new version 0.4.2

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 484015
- update to new version 0.4.0

* Thu Nov 26 2009 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 470277
- update to new version 0.3.1

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 448018
- update to new version 0.3.0

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.1-2mdv2010.0
+ Revision: 426737
- rebuild

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 292030
- New version 0.2.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 225021
- rebuild

* Sat Jan 26 2008 Helio Chissini de Castro <helio@mandriva.com> 0.2.0-1mdv2008.1
+ Revision: 158342
- Update for new upstream minor version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 97844
- New version 0.1.1

* Fri Sep 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1-3mdv2008.0
+ Revision: 81862
- rebuild


* Wed Oct 11 2006 Götz Waschk <waschk@mandriva.org> 0.1-1mdv2007.1
- initial package

