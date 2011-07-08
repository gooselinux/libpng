Summary: A library of functions for manipulating PNG image format files
Name: libpng
Epoch: 2
Version: 1.2.44
Release: 1%{?dist}
License: zlib
Group: System Environment/Libraries
URL: http://www.libpng.org/pub/png/

# Note: non-current tarballs get moved to the history/ subdirectory,
# so look there if you fail to retrieve the version you want
Source: ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.bz2

Patch0: libpng-multilib.patch
Patch1: libpng-pngconf.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel, pkgconfig
Conflicts: qt < 0:2.2.2

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary: Development tools for programs to manipulate PNG image format files
Group: Development/Libraries
Requires: libpng = %{epoch}:%{version}-%{release} zlib-devel pkgconfig

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install
the libpng package.

%package static
Summary: Static PNG image format file library
Group: Development/Libraries
Requires: libpng-devel = %{epoch}:%{version}-%{release}

%description static
The libpng-static package contains the statically linkable version of libpng.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# We don't ship .la files.
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpng.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpng12.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc *.txt example.c README TODO CHANGES LICENSE 
%{_libdir}/libpng*.so.*
%{_mandir}/man5/*

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%files static
%defattr(-,root,root)
%{_libdir}/libpng*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jun 29 2010 Tom Lane <tgl@redhat.com> 2:1.2.44-1
- Update to libpng 1.2.44, includes fixes for CVE-2010-1205 and CVE-2010-2249
Resolves: #609160

* Mon Mar 15 2010 Tom Lane <tgl@redhat.com> 2:1.2.43-1
- Update to libpng 1.2.43, includes fix for CVE-2010-0205
Resolves: #573763

* Wed Jan 20 2010 Tom Lane <tgl@redhat.com> 2:1.2.42-1
- Update to libpng 1.2.42

* Thu Aug 20 2009 Tom Lane <tgl@redhat.com> 2:1.2.39-1
- Update to libpng 1.2.39

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.2.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Tom Lane <tgl@redhat.com> 2:1.2.37-1
- Update to libpng 1.2.37, to fix CVE-2009-2042
Related: #504782

* Wed Feb 25 2009 Tom Lane <tgl@redhat.com> 2:1.2.35-1
- Update to libpng 1.2.35, to fix CVE-2009-0040

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  9 2009 Tom Lane <tgl@redhat.com> 2:1.2.34-1
- Update to libpng 1.2.34

* Thu Dec 11 2008 Caolán McNamara <caolanm@redhat.com> 2:1.2.33-2
- rebuild to get provides pkgconfig(libpng)

* Sun Nov  2 2008 Tom Lane <tgl@redhat.com> 2:1.2.33-1
- Update to libpng 1.2.33

* Tue Sep  9 2008 Tom Lane <tgl@redhat.com> 2:1.2.31-2
- Apply upstream patch for zTXT buffer overrun (CVE-2008-3964)
Related: #461599

* Sat Aug 23 2008 Tom Lane <tgl@redhat.com> 2:1.2.31-1
- Update to libpng 1.2.31

* Sat May 31 2008 Tom Lane <tgl@redhat.com> 2:1.2.29-1
- Update to libpng 1.2.29 (fixes low-priority security issue CVE-2008-1382)
Related: #441839

* Tue Feb 12 2008 Tom Lane <tgl@redhat.com> 2:1.2.24-1
- Update to libpng 1.2.24

* Thu Oct 18 2007 Tom Lane <tgl@redhat.com> 2:1.2.22-1
- Update to libpng 1.2.22, primarily to fix CVE-2007-5269
Related: #324771

* Wed Aug 22 2007 Tom Lane <tgl@redhat.com> 2:1.2.16-3
- Update License tag
- Rebuild to fix Fedora toolchain issues

* Wed May 23 2007 Tom Lane <tgl@redhat.com> 2:1.2.16-2
- Add patch to fix CVE-2007-2445
Related: #239542

* Mon Feb 12 2007 Tom Lane <tgl@redhat.com> 2:1.2.16-1
- Update to libpng 1.2.16
Resolves: #211705, #216706, #227334
- Separate libpng.a into a -static subpackage
- Other minor packaging fixes per Fedora merge review
Resolves: #226038

* Mon Oct 02 2006 Jesse Keating <jkeating@redhat.com> - 2:1.2.10-7
- Require pkgconfig in the -devel subpackage as it gets called by
  /usr/bin/libpng-config

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 2:1.2.10-6
- Disable asm on arches other than i386  (#196580)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:1.2.10-5.1
- rebuild

* Thu May 25 2006 Matthias Clasen  <mclasen@redhat.com> - 2:1.2.10-5
- Fix some paths in the -config script

* Tue May 23 2006 Matthias Clasen  <mclasen@redhat.com> - 2:1.2.10-4
- fix multilib conflicts

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 2:1.2.10-3
- Add a comment about the need to keep static libraries

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 2:1.2.10-2
- Re-add static libraries

* Thu May  4 2006 Matthias Clasen  <mclasen@redhat.com>  - 2:1.2.10-1
- Update to 1.2.10
- Drop static libraries

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2:1.2.8-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2:1.2.8-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 2:1.2.8-2
- Rebuild with gcc4

* Mon Dec 06 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.8-1
- Update to 1.2.8

* Wed Sep 15 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.7-1
- Update to 1.2.7

* Tue Aug 17 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.6-1
- Update to 1.2.6
- Combine patches

* Wed Aug 4 2004 Matthias Clasen <mclasen@redhat.com> 2:1.2.5-9
- Build for FC3

* Fri Jul 30 2004 Matthias Clasen <mclasen@redhat.com> 
- Include LICENSE.

* Fri Jul 23 2004 Matthias Clasen <mclasen@redhat.com> 2:1.2.5-8
- Build for FC2

* Fri Jul 23 2004 Matthias Clasen <mclasen@redhat.com> 2:1.2.5-7
- Replace the patches for individual security problems with the
  cumulative patch issued by the png developers. 
- Build for FC1

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.5-5
- Rebuild for FC2

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.5-4
- Rebuild for FC1

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 2:1.2.5-3
- Reinstate and improve the transfix patch which got lost sometime ago, 
  but is still needed for CAN-2002-1363 (#125934)

* Mon May 24 2004 Than Ngo <than@redhat.com> 2:1.2.5-2
- add patch to link libm automatically
- get rid of rpath

* Wed May 19 2004 Matthias Clasen <mclasen@redhat.com> 2:1.2.5-1
- 1.2.5

* Mon May 3 2004 Matthias Clasen <mclasen@redhat.com> 2:1.2.2-22
- Redo the out-of-bounds fix in a slightly better way.

* Wed Apr 21 2004 Matthias Clasen <mclasen@redhat.com>
- Bump release number to disambiguate n-v-rs.

* Mon Apr 19 2004 Matthias Clasen <mclasen@redhat.com> 
- fix a possible out-of-bounds read in the error message 
  handler. #121229

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 27 2004 Mark McLoughlin <markmc@redhat.com> 2:1.2.2-19
- rebuild with changed bits/setjmp.h on ppc

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Mon Feb 24 2003 Jonathan Blandford <jrb@redhat.com> 2:1.2.2-15
- change pkg-config to use libdir instead of hardcoding /usr/lib

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 20 2003 Jonathan Blandford <jrb@redhat.com> 2:1.2.2-12
- add Provides: libpng.so.3, #67007

* Fri Jan 24 2003 Jonathan Blandford <jrb@redhat.com>
- change requires to include the Epoch

* Thu Jan 23 2003 Karsten Hopp <karsten@redhat.de> 2:1.2.2-11
- Bump & rebuild

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Elliot Lee <sopwith@redhat.com> 2:1.2.2-9
- Bump & rebuild

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 2:1.2.2-7
- merge changes in from -6hammer

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-4
- Don't own {_libdir}/pkgconfig
- Don't strip library, that's up to rpm

* Tue May  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-3
- Forgot png.h

* Mon May  6 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-2
- Fix compatibility with everyone else.

* Thu May  2 2002 Havoc Pennington <hp@redhat.com>
- 1.2.2 plus makefile patches tarball
- update file list to contain versioned libpng only

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec 17 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-1
- 1.2.1

* Wed Sep 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.0-1
- 1.2.0

* Mon Jul 16 2001 Trond Eivind Glomsrd <teg@redhat.com>
- s/Copyright/License/
- fix weird versioning system (epoch was set to "2" in the main
  package, serial to "1" in the devel package. Huh?)

* Wed Jun 20 2001 Than Ngo <than@redhat.com> 1.0.12-1
- update to 1.0.12
- add missing libpng symlink

* Thu May  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.11-2
- libpng-devel requires zlib-devel (since png.h includes zlib.h)
  (#38883)

* Wed May  2 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.11-1
- 1.0.11

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.0.10

* Tue Feb  6 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.0.9, fixes Mozilla problems

* Tue Dec 12 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Rebuild to get rid of 0777 dirs

* Wed Nov 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Remove the workaround for Bug #20018 (from Oct 30).
  Qt 2.2.2 fixes the problem the workaround addressed.

* Mon Oct 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Work around a problem causing konqueror to segfault in image preview
  mode (Bug #20018)
- Copy SuSE 7.0's patch to handle bad chunks

* Sun Sep  3 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- only include the man5 man-pages once in the main rpm

* Thu Jul 28 2000 Preston Brown <pbrown@redhat.com>
- upgrade to 1.0.8 - fixes small memory leak, other bugs

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- patchlevel c
- FHSify

* Tue Mar 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.0.6

* Mon Mar 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- change serial to Epoch to get dependencies working correctly

* Fri Feb 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- move buildroot and add URL

* Sat Feb  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- strip library
- rebuild to compress man pages

* Sun Nov 21 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.0.5
- some tweaks to spec file to make updating easier
- handle RPM_OPT_FLAGS

* Mon Sep 20 1999 Matt Wilson <msw@redhat.com>
- changed requires in libpng-devel to include serial
- corrected typo

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Sun Feb 07 1999 Michael Johnson <johnsonm@redhat.com>
- rev to 1.0.3

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- we are Serial: 1 now because we are reverting the 1.0.2 version from 5.2
  beta to this prior one
- install man pages; set defattr defaults

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel subpackage moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.0.1
- added buildroot

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- updated to new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

