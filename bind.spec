Summary:     BIND - DNS name server
Summary(de): BIND - DNS-Namenserver  
Summary(fr): BIND - serveur de noms DNS
Summary(pl): BIND - serwer nazw DNS
Summary(tr): DNS alan adý sunucusu
Name:        bind
Version:     8.1.2
Release:     3
Copyright:   distributable
Group:       Networking/Daemons
Source0:     ftp://ftp.isc.org/isc/bind/cur/%{name}-src.tar.gz
Source1:     ftp://ftp.isc.org/isc/bind/cur/%{name}-doc.tar.gz
Source2:     named.init
Patch0:      bind-makefile.patch
Patch1:      bind-libelf.patch
URL:         http://www.isc.org/bind.html
Buildroot:   /tmp/%{name}-%{version}-root

%description
Includes the named name server, which is used to define host name
to IP address translations (and vice versa).  It can be used on
workstations as a caching name server, but is generally only needed
on one machine for an entire network.

%description -l de
Enthält den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf
Workstations als caching Namen-Server verwendet werden, ist aber
i.d.R. nur auf einem Recher des Netzwerks erforderlich.

%description -l fr
Contient le serveur de noms named, utilisé pour définir les traductions
nom d'hôte vers adresse IP (et vice versa). Il peut être utilisé sur
les stations de travail comme serveur de nom en cache mais n'est souvent
nécessaire que sur une machine pour un réseau entier.

%description -l pl
Includes the named name server, which is used to define host name
to IP address translations (and vice versa).  It can be used on
workstations as a caching name server, but is generally only needed
on one machine for an entire network.

Pakiet ten zawiera demona named, który s³u¿y do zmieniania nazw
komuterów na numery IP i odwrotnie. Mo¿e byæ on u¿ywany na na stacjach
roboczych jako bufor odwo³añ do serwisu naz (caching name server) ale
generalnie wystarczy tylko jedna jednostka wyposa¿ona w ten program na
fragment sieci.

%description -l tr
Bu paket, makina adýný IP numarasýna (ya da tersi) çevirmek için kullanýlan
alan adý sunucusunu içerir. Ýþ istasyonlarýnda bir önbellek isim sunucusu
olarak da kullanýlabilir ama genellikle bütün bir að için sadece bir makina
üzerinde kurulur.

%package utils
Summary:     DNS utils - host, dig, dnsquery, nslookup
Summary(de): DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr): Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl): Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(tr): DNS araçlarý - host, dig, dnsquery, nslookup
Group:       Networking/Utilities

%description utils
Collection of utilities for querying name servers and looking up hosts.
These tools let you determine the IP addresses for given host names,
and find information about registered domains and network addresses.

%description -l de utils
Dienstprogrammsammlung zum Abfragen von Namen-Servern und Hosts.
Diese Tools bestimmen die IP-Adresse eines angegebenen Host-Namen
und finden Informationen über registrierte Domains und Netzwerk-Adressen.

%description -l fr utils
Ensemble d'utilitaires pour interroger les serveurs de noms et rechercher
des hôtes. Ces outils vous permettent de déterminer les adresses IP pour
des noms d'hôtes donnés, et trouver des informations sur les noms de
domaine déclarés et les adresses réseau.

%description -l pl utils
Collection of utilities for querying name servers and looking up hosts.
These tools let you determine the IP addresses for given host names,
and find information about registered domains and network addresses.

Pakiet ten zawiera zbiór aplikacji umo¿liwiaj±cych odpytywanie swerwerów
nazw z innych domen w celu uzyskania ifnormacji o komupterach i ich
adresach IP.

%description -l tr utils
Bu pakette isim sunucularýný sorgulamak ve makina adreslerini çözmek için
kullanýlan araçlar bulunmaktadýr.

%package devel
Summary: DNS development includes and libs
Summary(pl): pliki nag³ówkowe i biblioteka statyczna
Group: Networking/Development

%description devel
All the include files and the library required for DNS development for
bind 8.x.x

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe i bibliotekê statyczn±. Je¿eli bêdziesz
pisa³ programy pod binda, lub kompilowa³ kod ¼ród³owy opragramowania
korzystaj±cego z tych plików nag³ówkowych czy biblioteki powiniene¶
zainstalowaæ ten pakiet.

%prep
%setup -q -n src
%setup -q -n src -T -D -a 1

%patch0 -p1
%patch1 -p1

%build
RPM_PREFIX="" make


%install
rm -rf $RPM_BUILD_ROOT
make install RPM_PREFIX=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,sbin,lib,man/man{1,3,5,7,8}}
install -d $RPM_BUILD_ROOT/etc/rc.d/{init,rc{0,1,2,3,4,5,6}}.d

strip $RPM_BUILD_ROOT/usr/{sbin/*,bin/*} || :

cd doc/man
install {dig,host,dnsquery}.1 $RPM_BUILD_ROOT/usr/man/man1
install {gethostbyname,resolver,getnetent}.3 $RPM_BUILD_ROOT/usr/man/man3
install resolver.5 $RPM_BUILD_ROOT/usr/man/man5
install {named,ndc,named-xfer,nslookup}.8 $RPM_BUILD_ROOT/usr/man/man8
install hostname.7 $RPM_BUILD_ROOT/usr/man/man7

install $RPM_SOURCE_DIR/named.init $RPM_BUILD_ROOT/etc/rc.d/init.d/named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K10named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K10named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc2.d/K10named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S55named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc4.d/S55named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S55named
ln -sf ../init.d/named $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K10named

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README Version CHANGES TODO bin/named/named-bootconf.pl

%attr(700, root, root) /etc/rc.d/init.d/named
/etc/rc.d/rc*.d/*named

%attr(711, root, root) /usr/sbin/named
%attr(755, root, root) /usr/sbin/named-xfer
%attr(755, root, root) /usr/sbin/ndc

%attr(644, root,  man) /usr/man/man8/named.8
%attr(644, root,  man) /usr/man/man8/ndc.8
%attr(644, root,  man) /usr/man/man8/named-xfer.8
%attr(644, root,  man) /usr/man/man7/hostname.7

%files utils
%attr(711, root, root) /usr/bin/nslookup
%attr(644, root, root) /usr/lib/nslookup.help
%attr(711, root, root) /usr/bin/host
%attr(711, root, root) /usr/bin/dig
%attr(711, root, root) /usr/bin/dnsquery
%attr(711, root, root) /usr/bin/addr
%attr(711, root, root) /usr/bin/nsupdate
%attr(644, root,  man) /usr/man/man1/dig.1
%attr(644, root,  man) /usr/man/man1/host.1
%attr(644, root,  man) /usr/man/man1/dnsquery.1
%attr(644, root,  man) /usr/man/man8/nslookup.8
%attr(644, root,  man) /usr/man/man5/resolver.5

%files devel
%defattr(644, root, root, 755)
/usr/include/bind
/usr/lib/lib*.a
%attr(644, root, man) /usr/man/man3/*

%changelog
* Tue Sep  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.1.2-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile (modified bind-makefile.patch),
- bind header files moved to /usr/include/bind,
- static library moved to /usr/lib,
- added full %attr description in %files.

* Wed Aug 26 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [8.1.2-2]
- added pl translation,
- changed permissions of all binaries to 711,

* Wed Jun 10 1998 Manuel J. Galan <manolow@step.es>
- Builds on RedHat 5.1 -Manhattan-
- Some more modifications to install correctly (includes).

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
