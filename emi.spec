%define name	emi
%define version	1.5.1
%define release %mkrel 2

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Name: 	 	%{name}
Summary: 	Ecasound Mastering Interface
Version: 	%{version}
Release: 	%{release}

Source:		http://emi.thevtek.com/tarball/EMi_%{version}.zip
URL:		http://emi.thevtek.com/
License:	Python license
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

BuildRequires:	ImageMagick python
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

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="EMI" longtitle="Ecasound Mastering Interface" section="Multimedia/Sound" xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo
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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc doc
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/*