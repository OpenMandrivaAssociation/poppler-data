Summary:	Encoding files for poppler
Name:		poppler-data
Version:	0.4.11
Release:	1
License:	Distributable
Group:		Development/X11
Url:		http://poppler.freedesktop.org/
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them
if they are present.  When installed, the encoding files enables
poppler to correctly render CJK and Cyrillic properly.

%package devel
Summary:	Developer files for %{name}
Requires:	%{name} = %{EVRD}
Group:		Development/Other
%description devel
%{summary}.

%prep
%autosetup -p1

%build

%install
%make_install datadir=%{_datadir}

%files
%doc README COPYING COPYING.gpl2 COPYING.adobe
%{_datadir}/poppler/

%files devel
%{_datadir}/pkgconfig/poppler-data.pc
