Summary:	Encoding files for poppler
Name:		poppler-data
Version:	0.4.6
Release:	12
License:	Distributable
Group:		Development/X11
Url:		http://poppler.freedesktop.org/
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildArch:	noarch

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
%makeinstall_std datadir=%{_datadir}

%files
%doc README COPYING
%{_datadir}/poppler/

