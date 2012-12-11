Name:		z26
Version:	3.02.01
Release:	2
Summary:	An Atari 2600 Video Computer System emulator
License:	GPLv2+
Group:		Emulators
URL:		http://www.whimsey.com/z26/z26.html
Source0:	http://www.whimsey.com/z26/%{name}v%{version}s.zip
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	imagemagick
BuildRequires:	dos2unix

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was the most
popular home video game system of the early 1980's. This emulator will run
most Atari ROM images, so that you can play your favorite old Atari 2600 games
on your PC.

%prep
%setup -q -c
dos2unix src/doc/*
%__sed -i -e s/^CFLAGS=.*/CFLAGS="%{optflags}"/g src/conf/config_linux.mak
%__sed -i -e s/"strip z26"//g src/Makefile

%build
cd src
%make linux

%install
mkdir -p %{buildroot}%{_bindir}
cp src/%{name} %{buildroot}%{_bindir}/

# icons
for N in 16 32 48 64 128; do
convert src/%{name}_icon.png -scale ${N}x${N} src/$N.png;
done
install -D src/16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D src/32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D src/48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D src/64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D src/128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=z26
Comment=Atari 2600 Emulator
Exec=z26
Icon=z26
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%files
%doc src/doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

