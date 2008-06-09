%define name neXtaw
%define version 0.15.1
%define release %mkrel 5
 
%define major 0
%define libname  %mklibname %name %{major}
%define libnamedev  %mklibname %name %{major} -d

Summary:    A NeXt lookalike widget set
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:        http://siag.nu/neXtaw/#download
Source:    %{name}-%{version}.tar.bz2
License:   GPL-like
Group:     System/Libraries
Buildrequires: X11-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

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
Requires: %{libname} = %{version}
Requires: X11-devel
Provides: libneXtaw-devel

%description -n %{libnamedev}
Static libraries and header files for neXtaw app development

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure2_5x

%make

%install
%makeinstall includedir=$RPM_BUILD_ROOT/usr/X11R6/include

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog README*
%{_libdir}/lib*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
/usr/X11R6/include/X11/neXtaw/*.h
%{_libdir}/lib*.*a
%{_libdir}/lib*.so

