Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan adý sunucusu
Name:		bind
Version:	8.1.2
Release:	4d
Copyright:	distributable
Group:		Daemons
Group(pl):	Demony
Source0:	ftp://ftp.isc.org/isc/bind/cur/%{name}-%{version}-src.tar.gz
Source1:	ftp://ftp.isc.org/isc/bind/cur/%{name}-doc.tar.gz
Source2:	named.init
Prereq:		/sbin/chkconfig
Patch0:		%{name}.patch
Patch1:		%{name}-pselect.patch
URL:		http://www.isc.org/bind.html
Buildroot:	/tmp/%{name}-%{version}-root

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
Pakiet ten zawiera demona named, który s³u¿y do zmieniania nazw
komputerów na numery IP i odwrotnie. Mo¿e byæ on u¿ywany na stacjach
roboczych jako bufor odwo³añ do serwisu nazw (caching name server), ale
generalnie wystarczy tylko jedna jednostka wyposa¿ona w ten program na
fragment sieci.

%description -l tr
Bu paket, makina adýný IP numarasýna (ya da tersi) çevirmek için kullanýlan
alan adý sunucusunu içerir. Ýþ istasyonlarýnda bir önbellek isim sunucusu
olarak da kullanýlabilir ama genellikle bütün bir að için sadece bir makina
üzerinde kurulur.

%package	utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS araçlarý - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia

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
Pakiet ten zawiera zbiór aplikacji umo¿liwiaj±cych odpytywanie serwerów
nazw z innych domen w celu uzyskania informacji o komupterach i ich
adresach IP.

%description -l tr utils
Bu pakette isim sunucularýný sorgulamak ve makina adreslerini çözmek için
kullanýlan araçlar bulunmaktadýr.

%package	devel
Summary:	DNS development includes and libs
Summary(pl):	Pliki nag³ówkowe i biblioteka statyczna
Group:		Development
Group(pl):	Programowanie
Requires:	%{name} = %{version}

%description devel
All the include files and the library required for DNS development for
bind 8.x.x

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe i bibliotekê statyczn±. Je¿eli bêdziesz
pisa³ programy pod binda, lub kompilowa³ kod ¼ród³owy oprogramowania
korzystaj±cego z tych plików nag³ówkowych czy biblioteki powiniene¶
zainstalowaæ ten pakiet.

%prep
%setup -q -n src
%setup -q -n src -T -D -a 1
%patch0 -p1
%patch1 -p1

%build
RPM_PREFIX="" make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT

make install RPM_PREFIX=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,sbin,lib,man/man{1,3,5,7,8}}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

install bin/named/named-bootconf.pl $RPM_BUILD_ROOT/usr/bin

strip $RPM_BUILD_ROOT/usr/{sbin/*,bin/*} || :

cd doc/man
install {dig,host,dnsquery}.1 $RPM_BUILD_ROOT/usr/man/man1
install {gethostbyname,resolver,getnetent}.3 $RPM_BUILD_ROOT/usr/man/man3
install resolver.5 $RPM_BUILD_ROOT/usr/man/man5
install {named,ndc,named-xfer,nslookup}.8 $RPM_BUILD_ROOT/usr/man/man8
install hostname.7 $RPM_BUILD_ROOT/usr/man/man7

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/named

gzip -9fn $RPM_BUILD_ROOT/usr/man/man[13578]/* \
	../../{README,Version,CHANGES} 

%post
/sbin/chkconfig --add named

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del named
fi    

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Version,CHANGES}.gz

%attr(700,root,root) %config /etc/rc.d/init.d/named

%attr(755,root,root) /usr/sbin/named
%attr(755,root,root) /usr/sbin/named-xfer
%attr(750,root,root) /usr/sbin/ndc

/usr/man/man8/named.8.gz
/usr/man/man8/ndc.8.gz
/usr/man/man8/named-xfer.8.gz
/usr/man/man7/hostname.7.gz

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/nslookup
%attr(644,root,root) /usr/lib/nslookup.help
%attr(755,root,root) /usr/bin/host
%attr(755,root,root) /usr/bin/dig
%attr(755,root,root) /usr/bin/dnsquery
%attr(755,root,root) /usr/bin/addr
%attr(755,root,root) /usr/bin/named-bootconf.pl
%attr(755,root,root) /usr/bin/nsupdate

/usr/man/man1/dig.1.gz
/usr/man/man1/host.1.gz
/usr/man/man1/dnsquery.1.gz
/usr/man/man8/nslookup.8.gz
/usr/man/man5/resolver.5.gz

%files devel
%defattr(644,root,root,755)

/usr/include/bind/*
/usr/lib/*.a
/usr/man/man3/*

%changelog
* Wed Jan 13 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [8.1.2-3d]
- removed Requires: %{name} = %{version} from utils sub-package,
- compressed man pages,
- added Group(pl),
- minor changes.

* Tue Sep  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.1.2-2d]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using $RPM_OPT_FLAGS during compile (modified bind-makefile.patch),

* Wed Aug 26 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [8.1.2-1d]
- translation modified for pl,
- changed permissions of all binaries to 711,
- major changes -- needed for Linux PLD.

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
