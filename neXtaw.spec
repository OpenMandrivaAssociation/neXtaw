%define name neXtaw
%define version 0.15.1
%define release %mkrel 10
 
%define major 0
%define libname  %mklibname %name %{major}
%define libnamedev  %mklibname %name -d

Summary:    A NeXt lookalike widget set
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:        http://siag.nu/neXtaw/#download
Source:    %{name}-%{version}.tar.bz2
Patch0:    neXtaw-0.15.1-fix-link.patch
License:   GPL-like
Group:     System/Libraries
Buildrequires: libx11-devel
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.%{major}.*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_includedir}/X11/neXtaw
%{_libdir}/lib*.*a
%{_libdir}/lib*.so


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-10mdv2011.0
+ Revision: 613041
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 0.15.1-9mdv2010.1
+ Revision: 508949
- simplify BR

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 0.15.1-8mdv2010.1
+ Revision: 508946
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.15.1-5mdv2008.1
+ Revision: 134097
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.15.1-4mdv2008.1
+ Revision: 130625
- kill re-definition of %%buildroot on Pixel's request
- import neXtaw


* Mon May 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.15.1-4mdk
- fix requires

* Fri May 19 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.15.1-3mdk
- fix buildrequires

* Wed Jan 04 2005 Lenny Cartier <lenny@mandriva.com> 0.15.1-2mdk
- rebuild

* Mon Nov 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.15.1-1mdk
- 0.15.1

* Sat Sep 13 2003 Stefan van der Eijk <stefan@eijk.nu> 0.14.0-3mdk
- Move files from /usr/include/X11 to /usr/X11R6/include/X11)
- -devel package Requires XFree86-devel

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.14.0-2mdk
- buildrequires

* Fri Feb 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.14.0-1mdk
- 0.14.0

* Thu Jan 30 2003 Charles A Edwards <eslrahc@bellsouth.net> 0.13.0-1mdk
- initial Mdk pkg
