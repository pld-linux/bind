Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan adý sunucusu
Name:		bind
Version:	8.2.2_P5
Release:	11
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.src.tar.gz
Source1:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.doc.tar.gz
Source2:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.contrib.tar.gz
Source3:	named.init
Source4:	named.sysconfig
Source5:	named.logrotate
Source6:	named.conf
Patch1:		bind-pselect.patch
Patch2:		bind-fds.patch
Patch3:		bind-nonlist.patch
Patch4:		bind-host.patch
Patch5:		bind-glibc21.patch
Patch6:		bind-mkdep.patch
Patch7:		bind-probe_ipv6.patch
Patch8:		bind-host-forcetype.patch
Patch9:		bind-pidfile.patch
Patch10:	bind-ttl.patch
BuildRequires:	flex
Prereq:		/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:      caching-nameserver
URL:		http://www.isc.org/bind.html
Buildroot:	/tmp/%{name}-%{version}-root

%define		_datadir	%{_prefix}/share/misc
%define		_sysconfdir	/etc

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS (Domain
Name System) protocols. BIND includes a DNS server (named), which resolves
host names to IP addresses, and a resolver library (routines for
applications to use when interfacing with DNS). A DNS server allows clients
to name resources or objects and share the information with other network
machines. The named DNS server can be used on workstations as a caching name
server, but is generally only needed on one machine for an entire network.
Note that the configuration files for making BIND act as a simple caching
nameserver are included in the caching-nameserver package.

Install the bind package if you need a DNS server for your network.  If you
want bind to act a caching name server, you will also need to install the
caching-nameserver package.

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

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS araçlarý - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain Name
Service) name servers to find out information about Internet hosts. These
tools will provide you with the IP addresses for given host names, as well
as other information about registered domains and network addresses.

You should install bind-utils if you need to get information from DNS name
servers.

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

%package devel
Summary:	DNS development includes and libs
Summary(pl):	Pliki nag³ówkowe i biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
The bind-devel package contains all the include files and the 
library required for DNS (Domain Name Service) development for 
BIND versions 8.x.x.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind.

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe i bibliotekê statyczn±. Je¿eli bêdziesz
pisa³ programy pod binda, lub kompilowa³ kod ¼ród³owy oprogramowania
korzystaj±cego z tych plików nag³ówkowych czy biblioteki powiniene¶
zainstalowaæ ten pakiet.

%package doc
Summary:	Bind documentation
Summary(pl):	Dokumentacja programu bind
Group:		Documentation
Group(pl):	Dokumentacja

%description doc
Bind documentations

%decscription doc -l pl
Dokumentacja programu bind

%prep
%setup -q -c -n %{name}-%{version} -a 1 -a 2

%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch10 -p1

%build
rm -f compat/include/sys/cdefs.h
cd src
make 	clean \
	depend \
	all \
	DESTDIR="" \
	CDEBUG="$RPM_OPT_FLAGS" \
	DESTBIN="%{_bindir}" \
	DESTSBIN="%{_sbindir}" \
	DESTMAN="%{_mandir}" \
	DESTHELP="%{_datadir}" \
	DESTETC="%{_sysconfdir}" \
	DESTRUN="/var/run"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir},%{_datadir}} \
	$RPM_BUILD_ROOT/etc/{sysconfig,logrotate.d,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5,7,8}

cd src
make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	DESTINC="%{_includedir}/bind" \
	DESTLIB="%{_libdir}" \
        DESTBIN="%{_bindir}" \
        DESTSBIN="%{_sbindir}" \
        DESTMAN="%{_mandir}" \
        DESTHELP="%{_datadir}" \
        DESTETC="%{_sysconfdir}" \
        DESTRUN="/var/run" \
	INSTALL_LIB=" " \
	INSTALL_EXEC=" "

strip $RPM_BUILD_ROOT{%{_sbin}/*,%{_bindir}/*} || :
cd ..

cd doc/man
make clean
make install \
	MANROFF=cat \
	CATEXT=\$\$N \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTMAN=%{_mandir} \
	MANDIR=man

cd ../../
install -d $RPM_BUILD_ROOT/var/{log,state/named/{M,S}}

install src/bin/named/test/127.*    $RPM_BUILD_ROOT/var/state/named/M
install src/bin/named/test/loca*    $RPM_BUILD_ROOT/var/state/named/M
install src/conf/workstation/root.* $RPM_BUILD_ROOT/var/state/named/root.hint
install %{SOURCE6}              $RPM_BUILD_ROOT/etc

cp src/bin/named/named.conf EXAMPLE-CONFIG

install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/named
touch $RPM_BUILD_ROOT/var/log/named

mv $RPM_BUILD_ROOT%{_bindir}/nsupdate $RPM_BUILD_ROOT%{_sbindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/mkservdb \
	$RPM_BUILD_ROOT%{_mandir}/man5/resolver.5

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[13578]/* \
	src/README src/Version src/CHANGES EXAMPLE-CONFIG 

%pre
if [ -f /etc/named.boot ]; then
	cp /etc/named.boot /etc/named.boot.2conf
	mv -f /etc/named.boot /etc/named.rpmsave
	echo "Warrnig: /etc/named.boot saved as /etc/named.rpmsave" 1>&2
fi
if ! id -g named; then
	%{_sbindir}/groupadd -g 58 named
fi
if ! id -u named; then
	%{_sbindir}/useradd -u 58 -g 58 -d /dev/null -s /bin/false -c "BIND user" named
fi
%{_bindir}/update-db

%post
/sbin/chkconfig --add named

if [ -f /var/lock/subsys/named ]; then
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named" 1>&2
fi

if [ -f /etc/named.boot.2conf ]; then
	/usr/sbin/named-bootconf </etc/named.boot.2conf >/etc/named.conf
	rm /etc/named.boot.2conf
fi

umask 137
/bin/touch /var/log/named
chown root.named /var/log/named

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/named ]; then
		/etc/rc.d/init.d/named stop 1>&2
	fi
	/sbin/chkconfig --del named
fi    

%postun
if [ "$1" = "0" ]; then
	%{_sbindir}/groupdel named
	%{_sbindir}/userdel named
	%{_bindir}/update-db
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {src/README,src/Version,src/CHANGES,EXAMPLE-CONFIG}.gz

%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) /etc/named.conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man8/named.8*
%{_mandir}/man8/ndc.8*
%{_mandir}/man8/named-xfer.8*
%{_mandir}/man8/named-bootconf.8*
%{_mandir}/man7/hostname.7*
%{_mandir}/man5/irs.conf.5*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man1/dnskeygen.1*
%{_mandir}/man8/nsupdate.8*

%attr(770,root,named) %dir /var/state/named
%attr(750,root,root) %dir /var/state/named/M
%attr(750,root,named) %dir /var/state/named/S

/var/state/named/M/*
/var/state/named/root.*

%attr(660,root,named) %ghost /var/log/named

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_datadir}/nslookup.help

%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
%{_mandir}/man1/dnsquery.1*
%{_mandir}/man8/nslookup.8*

%files devel
%defattr(644,root,root,755)

%{_includedir}/bind
%{_libdir}/*.a
%{_mandir}/man3/*

%files doc
%defattr(644,root,root,755)
%doc doc/html doc/rfc doc/misc doc/notes
