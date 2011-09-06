Name: poppler-data
Version: 0.4.5
Release: %mkrel 1
Summary: Encoding files for poppler
Source0: http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
License: Distributable
Group: Development/X11
Url: http://poppler.freedesktop.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%_datadir/poppler/
