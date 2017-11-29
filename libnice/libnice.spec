Name:           libnice
Version:        0.1.14
Release:        0.01%{?dist}
Summary:        GLib ICE implementation

Group:          System Environment/Libraries
License:        LGPLv2 and MPLv1.1
URL:            http://nice.freedesktop.org/wiki/
Source0:        http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	glib2-devel
BuildRequires:  gnutls-devel >= 2.12.0
BuildRequires:	gobject-introspection-devel
BuildRequires:  gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:  gstreamer1-devel >= 0.11.91
BuildRequires:	gstreamer1-plugins-base-devel >= 0.11.91
BuildRequires:	gupnp-igd-devel >= 0.1.2


%description
%{name} is an implementation of the IETF's draft Interactive Connectivity
Establishment standard (ICE). ICE is useful for applications that want to
establish peer-to-peer UDP data streams. It automates the process of traversing
NATs and provides security against some attacks. Existing standards that use
ICE include the Session Initiation Protocol (SIP) and Jingle, XMPP extension
for audio/video calls.


%package        gstreamer
Summary:        GStreamer plugin for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gstreamer
The %{name}-gstreamer package contains a gstreamer 0.10 plugin for %{name}.


%package        gstreamer1
Summary:        GStreamer plugin for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gstreamer1
The %{name}-gstreamer1 package contains a gstreamer 1.0 plugin for %{name}.


%package        examples
Summary:        Simple %{name} usage examples
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
The %{name}-examples package contains usage (simple, threaded and sdp) examples.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%check
#make check


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc NEWS README
%license COPYING COPYING.LGPL COPYING.MPL
%{_bindir}/stunbdc
%{_bindir}/stund
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Nice-0.1.typelib


%files gstreamer
%{_libdir}/gstreamer-0.10/libgstnice010.so


%files gstreamer1
%{_libdir}/gstreamer-1.0/libgstnice.so


%files examples
%{_bindir}/sdp-example
%{_bindir}/simple-example
%{_bindir}/threaded-example


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/nice.pc
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Nice-0.1.gir


%changelog
* Wed Nov 29 2017 Brian J. Murrell <brian.murrell@intel.com> - 0.1.14-0.01
- Update to 0.1.14

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Than Ngo <than@redhat.com> - 0.1.13-7
- Rebuilt for glibc: Revert sendmsg/recvmsg ABI changes

* Fri Jun 10 2016 David Woodhouse <dwmw2@infradead.org> - 0.1.13-6
- More updates from libnice git; use-after-free fixes

* Mon Jun 06 2016 David Woodhouse <dwmw2@infradead.org> - 0.1.13-5
- Wholesale update to git HEAD, which fixes SIPE again.

* Fri May 20 2016 David Woodhouse <dwmw2@infradead.org> - 0.1.13-4
- Backport patch to fix SIPE audio disconnections (#1337051)
- Fix candidate gathering with IPV6 tentative addresses (#1337412)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.13-1
- Update to 0.1.13
- Tighten dependencies with the _isa macro

* Tue Apr 21 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.11-1
- Update to 0.1.11
- Use license macro for COPYING files

* Mon Mar 02 2015 David Woodhouse <dwmw2@infradead.org> - 0.1.10-1
- Update to 0.1.10

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.1.8-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Oct 26 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.8-1
- Update to 0.1.8
- Build with gobject introspection support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4.
- Add examples subpackage.

* Fri May 10 2013 Matthias Clasen <mclasen@redhat.com> - 0.1.3-3
- Split the gstreamer plugins off in subpackages

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3.
- Add BR on gstreamer1 packages.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2.

* Mon Jan 16 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-3
- Rebuild for new gupnp-idg.

* Sun Jan 08 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-2
- Rebuild for new gcc.

* Wed Dec  7 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1.
- Drop ppc64 patch. Fixed upstream.

* Tue Aug 16 2011 David Woodhouse <dwmw2@infradead.org> - 0.1.0-5
- Apply portability patch to nice/Makefile.in too. I hate autocrap.

* Tue Aug 16 2011 David Woodhouse <dwmw2@infradead.org> - 0.1.0-4
- Fix non-portable symbol checks in nice/Makefile.am

* Fri Jun 17 2011 Peter Robinson <pbrobinson@gmail.com> - 0.1.0-3
- rebuild for new gupnp/gssdp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0.
- Enable make check.
- Drop buildroot and clean section. No longer needed.

* Wed Aug  4 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.0.13-1
- Update to 0.0.13.

* Wed May 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.0.12-1
- Update to 0.0.12.

* Fri Mar 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11.

* Wed Dec 16 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.10-2
- Rebuild for new gupnp-igd.

* Mon Nov  9 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10.

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.0.9-2
- Rebuild for new gupnp

* Sun Aug  2 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9.
- Drop sha1 patch. Fixed upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Warren Togami <wtogami@redhat.com> - 0.0.8-2
- stun sha1 patch from upstream to make it work at all

* Sun Jun 21 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8.

* Sun Jun 14 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.7-1
- Update to 0.0.7.
- Add BR on gupnp-igd-devel.

* Mon Apr 13 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-1
- Update to 0.0.6.

* Wed Mar 18 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-1
- Update to 0.0.5.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.0.4-1
- Initial Fedora spec.

