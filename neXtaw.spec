%define major 0
%define libname  %mklibname %name %{major}
%define libnamedev  %mklibname %name -d

Summary:    A NeXt lookalike widget set
Name:      neXtaw
Version:   0.15.1
Release:   13
URL:        https://siag.nu/neXtaw/#download
Source:    %{name}-%{version}.tar.bz2
Patch0:    neXtaw-0.15.1-fix-link.patch
License:   GPL-like
Group:     System/Libraries
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)

%description 
A replacement library for the Athena (libXaw) widget set.
It is based on Xaw3d, by Kaleb Keithley. 
Its goal is to try to emulate the look and feel of the N*XTSTEP GUI.

%package -n %{libname}
Summary:  A NeXt lookalike widget set
Group: System/Libraries

%description -n %{libname}
A replacement library for the Athena (libXaw) widget set.

%package -n %{libnamedev}
Summary:  A NeXt lookalike widget set
Group:    Development/C
Requires: %{libname} = %{version}-%{release}
Provides: libneXtaw-devel = %{version}-%{release}
Provides: neXtaw-devel = %{version}-%{release}
Obsoletes: %{_lib}neXtaw0-devel < %{version}-%{release}

%description -n %{libnamedev}
Static libraries and header files for neXtaw app development

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc ChangeLog README*
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.%{major}.*

%files -n %{libnamedev}
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_includedir}/X11/neXtaw
%{_libdir}/lib*.*a
%{_libdir}/lib*.so
