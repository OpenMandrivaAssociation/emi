%define name	emi
%define version	1.5.1
%define release 8

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Name: 	 	%{name}
Summary: 	Ecasound Mastering Interface
Version: 	%{version}
Release: 	%{release}

Source:		http://emi.thevtek.com/tarball/EMi_%{version}.zip
URL:		https://emi.thevtek.com/
License:	Python license
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

BuildRequires:	imagemagick python
Requires:	pyecasound tkinter

%description
EMI is a python front end to ecasound, it's a virtual rackmount effect that
can be use to record and mix audio.  You will be able to export to *.ecs as
well.  This nice light interface give you full control over ecasound effect
parameters in real time.  EMI Interface use real ecasound parameter name so
you can use ecasound documentation to catch the basic's.

%prep
%setup -q -n EMI
perl -p -i -e 's|/usr/local/bin/python|/usr/bin/python||g' *.py
perl -p -i -e 's|/usr/python|/usr/bin/python||g' *.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
chmod 644 *.py
%python_compile_opt
%python_compile
cp *.py* $RPM_BUILD_ROOT/%_datadir/%name
echo '#!/bin/bash' > $RPM_BUILD_ROOT/%_bindir/%name
echo 'cd /usr/share/emi' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'python EMI.py $@' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod 755 $RPM_BUILD_ROOT/%_bindir/%name

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Ecasound Mastering Interface
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc doc
%{_bindir}/%name
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-7mdv2011.0
+ Revision: 618229
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.5.1-6mdv2010.0
+ Revision: 428599
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5.1-5mdv2009.0
+ Revision: 244887
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.5.1-3mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Funda Wang <fwang@mandriva.org> 1.5.1-3mdv2008.0
+ Revision: 80905
- Rebuild
- Import emi




* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.5.1-2mdv2007.0
- xdg

* Sat Apr 29 2006 Austin Acton <austin@mandriva.org> 1.5.1-1mdk
- 1.5.1

* Mon Dec 27 2004 Austin Acton <austin@mandrake.org> 1.2.1-1mdk
- 1.2.1

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 1.0-2mdk
- fix /usr/python
- fix file permissions
- compile bytecode

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 1.0-1mdk
- initial package
