Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan adý sunucusu
Name:		bind
Version:	8.2.2_P5
Release:	27
License:	Distributable
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.src.tar.gz
Source1:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.doc.tar.gz
Source2:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}.contrib.tar.gz
Source3:	named.init
Source4:	named.sysconfig
Source5:	named.logrotate
Source6:	named.conf
Source7:	named-chroot.init
Source8:	ftp://ftp.obtuse.com/pub/utils/utils-1.0.tar.gz
Patch1:		%{name}-pselect.patch
Patch2:		%{name}-fds.patch
Patch3:		%{name}-nonlist.patch
Patch4:		%{name}-host.patch
Patch5:		%{name}-glibc21.patch
Patch6:		%{name}-mkdep.patch
Patch7:		%{name}-probe_ipv6.patch
Patch8:		%{name}-host-forcetype.patch
Patch9:		%{name}-pidfile.patch
Patch10:	%{name}-ttl.patch
Patch11:	ftp://ftp.6bone.pl/pub/ipv6/set-glibc-2.1.new/host_991529+.diff
Patch12:	%{name}-res_randomid.patch
Patch20:	utils-holelogd-linux.patch
Patch21:	%{name}-chroot-ndc.patch
BuildRequires:	flex
Prereq:		/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Obsoletes:	caching-nameserver
Conflicts:	%{name}-chroot
URL:		http://www.isc.org/bind.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc
%define		_chroot		/var/lib/named/chroot

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses, and a resolver library
(routines for applications to use when interfacing with DNS). A DNS
server allows clients to name resources or objects and share the
information with other network machines. The named DNS server can be
used on workstations as a caching name server, but is generally only
needed on one machine for an entire network. Note that the
configuration files for making BIND act as a simple caching nameserver
are included in the caching-nameserver package.

Install the bind package if you need a DNS server for your network. If
you want bind to act a caching name server, you will also need to
install the caching-nameserver package.

%description -l de
Enthält den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf Workstations als
caching Namen-Server verwendet werden, ist aber i.d.R. nur auf einem
Recher des Netzwerks erforderlich.

%description -l fr
Contient le serveur de noms named, utilisé pour définir les
traductions nom d'hôte vers adresse IP (et vice versa). Il peut être
utilisé sur les stations de travail comme serveur de nom en cache mais
n'est souvent nécessaire que sur une machine pour un réseau entier.

%description -l pl
Pakiet ten zawiera demona named, który s³u¿y do zmieniania nazw
komputerów na numery IP i odwrotnie. Mo¿e byæ on u¿ywany na stacjach
roboczych jako bufor odwo³añ do serwisu nazw (caching name server),
ale generalnie wystarczy tylko jedna jednostka wyposa¿ona w ten
program na fragment sieci.

%description -l tr
Bu paket, makina adýný IP numarasýna (ya da tersi) çevirmek için
kullanýlan alan adý sunucusunu içerir. Ýþ istasyonlarýnda bir önbellek
isim sunucusu olarak da kullanýlabilir ama genellikle bütün bir að
için sadece bir makina üzerinde kurulur.

%package chroot
Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan adý sunucusu
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Prereq:		/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Obsoletes:	caching-nameserver
Conflicts:	%{name}
URL:		http://www.isc.org/bind.html

%description chroot
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses, and a resolver library
(routines for applications to use when interfacing with DNS). A DNS
server allows clients to name resources or objects and share the
information with other network machines. The named DNS server can be
used on workstations as a caching name server, but is generally only
needed on one machine for an entire network. Note that the
configuration files for making BIND act as a simple caching nameserver
are included in the caching-nameserver package.

Install the bind package if you need a DNS server for your network. If
you want bind to act a caching name server, you will also need to
install the caching-nameserver package.

The bind-chroot package runs the DNS server daemon under the non-root
user and group and in the chroot()ed directory.

%description -l de chroot
Enthält den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf Workstations als
caching Namen-Server verwendet werden, ist aber i.d.R. nur auf einem
Recher des Netzwerks erforderlich.

%description -l fr chroot
Contient le serveur de noms named, utilisé pour définir les
traductions nom d'hôte vers adresse IP (et vice versa). Il peut être
utilisé sur les stations de travail comme serveur de nom en cache mais
n'est souvent nécessaire que sur une machine pour un réseau entier.

%description -l pl chroot
Pakiet ten zawiera demona named, który s³u¿y do zmieniania nazw
komputerów na numery IP i odwrotnie. Mo¿e byæ on u¿ywany na stacjach
roboczych jako bufor odwo³añ do serwisu nazw (caching name server),
ale generalnie wystarczy tylko jedna jednostka wyposa¿ona w ten
program na fragment sieci.

%description -l tr chroot
Bu paket, makina adýný IP numarasýna (ya da tersi) çevirmek için
kullanýlan alan adý sunucusunu içerir. Ýþ istasyonlarýnda bir önbellek
isim sunucusu olarak da kullanýlabilir ama genellikle bütün bir að
için sadece bir makina üzerinde kurulur.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS araçlarý - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name Service) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install bind-utils if you need to get information from DNS
name servers.

%description -l de utils
Dienstprogrammsammlung zum Abfragen von Namen-Servern und Hosts. Diese
Tools bestimmen die IP-Adresse eines angegebenen Host-Namen und finden
Informationen über registrierte Domains und Netzwerk-Adressen.

%description -l fr utils
Ensemble d'utilitaires pour interroger les serveurs de noms et
rechercher des hôtes. Ces outils vous permettent de déterminer les
adresses IP pour des noms d'hôtes donnés, et trouver des informations
sur les noms de domaine déclarés et les adresses réseau.

%description -l pl utils
Pakiet ten zawiera zbiór aplikacji umo¿liwiaj±cych odpytywanie
serwerów nazw z innych domen w celu uzyskania informacji o komupterach
i ich adresach IP.

%description -l tr utils
Bu pakette isim sunucularýný sorgulamak ve makina adreslerini çözmek
için kullanýlan araçlar bulunmaktadýr.

%package devel
Summary:	DNS development includes and libs
Summary(pl):	Pliki nag³ówkowe i biblioteka statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
The bind-devel package contains all the include files and the library
required for DNS (Domain Name Service) development for BIND versions
8.x.x.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind.

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe i bibliotekê statyczn±. Je¿eli
bêdziesz pisa³ programy pod binda, lub kompilowa³ kod ¼ród³owy
oprogramowania korzystaj±cego z tych plików nag³ówkowych czy
biblioteki powiniene¶ zainstalowaæ ten pakiet.

%package doc
Summary:	Bind documentation
Summary(pl):	Dokumentacja programu bind
Group:		Documentation
Group(de):	Dokumentation
Group(pl):	Dokumentacja

%description doc
Bind documentations

%decscription doc -l pl
Dokumentacja programu bind

%prep
%setup -q -c -n %{name}-%{version} -a 1 -a 2 -a 8

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
%patch12 -p1
%patch20 -p1
cd contrib/host
%patch11 -p1

%build
rm -f compat/include/sys/cdefs.h
cd src
%{__make} 	clean \
	depend \
	all \
	DESTDIR="" \
	CDEBUG="$RPM_OPT_FLAGS" \
	DESTBIN="%{_bindir}" \
	DESTSBIN="%{_sbindir}" \
	DESTMAN="%{_mandir}" \
	DESTHELP="%{_datadir}/misc" \
	DESTETC="%{_sysconfdir}" \
	DESTRUN="/var/run"
cd ..
cd contrib/host
%{__make}

# Now build stuff for chroot
cd ../..
mv -f src/bin/named/named src/bin/named/named.dynamic
mv -f src/bin/named-xfer/named-xfer src/bin/named-xfer/named-xfer.dynamic
mv -f src/bin/ndc/ndc src/bin/ndc/ndc.nonc

patch -p1 < %{PATCH21}

eval "make -C src/bin/named named \
	'DESTDIR=' \
	'CDEBUG=$RPM_OPT_FLAGS' \
	'DESTBIN=%{_bindir}' \
	'DESTSBIN=%{_sbindir}' \
	'DESTMAN=%{_mandir}' \
	'DESTHELP=%{_datadir}/misc' \
	'DESTETC=%{_sysconfdir}' \
	'DESTRUN=%{_chroot}/var/run' \
	'LDFLAGS=-static %{!?debug:-s}' \
	'SYSTYPE=linux' \
	`sh ./src/port/settings ./src/.settings < ./src/port/linux/Makefile.set` \
	VER=`cat ./src/Version`"

eval "make -C src/bin/named-xfer named-xfer \
	'DESTDIR=' \
	'CDEBUG=$RPM_OPT_FLAGS' \
	'DESTBIN=%{_bindir}' \
	'DESTSBIN=%{_sbindir}' \
	'DESTMAN=%{_mandir}' \
	'DESTHELP=%{_datadir}/misc' \
	'DESTETC=%{_sysconfdir}' \
	'DESTRUN=%{_chroot}/var/run' \
	'LDFLAGS=-static %{!?debug:-s}' \
	'SYSTYPE=linux' \
	`sh ./src/port/settings ./src/.settings < ./src/port/linux/Makefile.set` \
	VER=`cat ./src/Version`"

eval "make -C src/bin/ndc ndc \
	'DESTDIR=' \
	'CDEBUG=$RPM_OPT_FLAGS' \
	'DESTBIN=%{_bindir}' \
	'DESTSBIN=%{_sbindir}' \
	'DESTMAN=%{_mandir}' \
	'DESTHELP=%{_datadir}/misc' \
	'DESTETC=%{_sysconfdir}' \
	'DESTRUN=%{_chroot}/var/run' \
	'LDFLAGS=%{!?debug:-s}' \
	'SYSTYPE=linux' \
	`sh ./src/port/settings ./src/.settings < ./src/port/linux/Makefile.set` \
	VER=`cat ./src/Version`"

patch -p1 -R < %{PATCH21}
touch src/bin/ndc/*

mv -f src/bin/named/named src/bin/named/named.static
mv -f src/bin/named-xfer/named-xfer src/bin/named-xfer/named-xfer.static
mv -f src/bin/ndc/ndc src/bin/ndc/ndc.chroot

mv -f src/bin/named/named.dynamic src/bin/named/named
mv -f src/bin/named-xfer/named-xfer.dynamic src/bin/named-xfer/named-xfer
mv -f src/bin/ndc/ndc.nonc src/bin/ndc/ndc

cd utils-1.0
gcc $RPM_OPT_FLAGS -o holelogd holelogd.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir},%{_datadir}/misc} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig,logrotate.d,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5,7,8}

install -d $RPM_BUILD_ROOT%{_chroot}/{%{_sbindir},%{_datadir}/zoneinfo} \
	$RPM_BUILD_ROOT%{_chroot}/{etc,dev,var/{tmp,run,log,lib/named/{M,S}}}

cd src
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	DESTINC="%{_includedir}/bind" \
	DESTLIB="%{_libdir}" \
        DESTBIN="%{_bindir}" \
        DESTSBIN="%{_sbindir}" \
        DESTMAN="%{_mandir}" \
        DESTHELP="%{_datadir}/misc" \
        DESTETC="%{_sysconfdir}" \
        DESTRUN="/var/run" \
	INSTALL_LIB=" " \
	INSTALL_EXEC=" "

cd ..

cd doc/man
%{__make} clean
%{__make} install \
	MANROFF=cat \
	CATEXT=\$\$N \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTMAN=%{_mandir} \
	MANDIR=man

cd ../../
install -d $RPM_BUILD_ROOT/var/{log,lib/named/{M,S}}

install src/bin/named/test/127.* $RPM_BUILD_ROOT/var/lib/named/M
install src/bin/named/test/loca* $RPM_BUILD_ROOT/var/lib/named/M
install src/conf/workstation/root.* $RPM_BUILD_ROOT/var/lib/named/root.hint
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}

install contrib/host/host $RPM_BUILD_ROOT%{_bindir}/host6

cp src/bin/named/named.conf EXAMPLE-CONFIG

# Now chroot install
# This will be log daemon for our jail alone so we can easily start and
# stop it if there are others for other jails.
install utils-1.0/holelogd $RPM_BUILD_ROOT%{_sbindir}/holelogd.named
mv -f utils-1.0/LICENSE LICENSE.holelogd
mv -f utils-1.0/README README.holelogd

install src/bin/named/named.static $RPM_BUILD_ROOT%{_chroot}%{_sbindir}/named
install src/bin/named-xfer/named-xfer.static $RPM_BUILD_ROOT%{_chroot}%{_sbindir}/named-xfer
install src/bin/ndc/ndc.chroot $RPM_BUILD_ROOT%{_sbindir}

install src/bin/named/test/127.* $RPM_BUILD_ROOT%{_chroot}/var/lib/named/M
install src/bin/named/test/loca* $RPM_BUILD_ROOT%{_chroot}/var/lib/named/M
install src/conf/workstation/root.* $RPM_BUILD_ROOT%{_chroot}/var/lib/named/root.hint
install %{SOURCE6} $RPM_BUILD_ROOT%{_chroot}%{_sysconfdir}

ln -sf ../../..%{_sysconfdir}/localtime $RPM_BUILD_ROOT%{_chroot}%{_datadir}/zoneinfo/localtime
ln -sf localtime $RPM_BUILD_ROOT%{_chroot}%{_datadir}/zoneinfo/posixrules
ln -sf localtime $RPM_BUILD_ROOT%{_chroot}%{_datadir}/zoneinfo/posixtime

touch $RPM_BUILD_ROOT%{_chroot}%{_sysconfdir}/{localtime,group}
touch $RPM_BUILD_ROOT%{_chroot}/dev/{log,null}
touch $RPM_BUILD_ROOT%{_chroot}/var/log/named
# ...continue

install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/named-chroot
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/named
touch $RPM_BUILD_ROOT/var/log/named

mv -f $RPM_BUILD_ROOT%{_bindir}/nsupdate $RPM_BUILD_ROOT%{_sbindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/mkservdb \
	$RPM_BUILD_ROOT%{_mandir}/man5/resolver.5

rm -f $RPM_BUILD_ROOT%{_mandir}/man3/{gethostbyname,getipnodebyname,getaddrinfo}.3

gzip -9nf src/README src/Version src/CHANGES EXAMPLE-CONFIG \
	*.holelogd

%pre
if [ -f /etc/named.boot ]; then
	cp /etc/named.boot /etc/named.boot.2conf
	mv -f /etc/named.boot /etc/named.rpmsave
	echo "Warrnig: /etc/named.boot saved as /etc/named.rpmsave" 1>&2
fi
if ! id -g named > /dev/null 2>&1 ; then
	%{_sbindir}/groupadd -g 58 named
fi
if ! id -u named > /dev/null 2>&1 ; then
	%{_sbindir}/useradd -u 58 -g 58 -d /dev/null -s /bin/false -c "BIND user" named
fi

%post
/sbin/chkconfig --add named

if [ -f /var/lock/subsys/named ]; then
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named" 1>&2
fi

if [ -f /etc/named.boot.2conf ]; then
	/usr/sbin/named-bootconf </etc/named.boot.2conf >/etc/named.conf
	rm -f /etc/named.boot.2conf
fi

umask 117
/bin/touch /var/log/named
chown named.named /var/log/named

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/named ]; then
		/etc/rc.d/init.d/named stop 1>&2
	fi
	/sbin/chkconfig --del named
fi    

%postun
if [ "$1" = "0" ]; then
	%{_sbindir}/userdel named
	%{_sbindir}/groupdel named
fi

%pre chroot
if [ -f /etc/named.boot ]; then
	cp /etc/named.boot /etc/named.boot.2conf
	mv -f /etc/named.boot /etc/named.rpmsave
	echo "Warrnig:/etc/named.boot saved as /etc/named.rpmsave" 1>&2
fi
if ! id -g named > /dev/null 2>&1 ; then
	%{_sbindir}/groupadd -g 58 named
fi
if ! id -u named > /dev/null 2>&1 ; then
	%{_sbindir}/useradd -u 58 -g 58 -d /dev/null -s /bin/false -c "BIND user" named
fi

%post chroot
ln -sf named-chroot /etc/rc.d/init.d/named
/sbin/chkconfig --add named

if [ -f /var/lock/subsys/named ]; then
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named" 1>&2
fi

if [ -f /etc/named.boot.2conf ]; then
	/usr/sbin/named-bootconf </etc/named.boot.2conf >%{_chroot}/etc/named.conf
	rm -f /etc/named.boot.2conf
fi

mknod -m a+rw %{_chroot}/dev/null c 1 3
cp -rf /etc/localtime %{_chroot}/etc/localtime
grep "^named:" /etc/group > %{_chroot}/etc/group
ln -sf %{_chroot}/etc/named.conf /etc/named.conf

cd /var/lib/named
ln -s chroot/var/lib/named/* .

umask 117
/bin/touch %{_chroot}/var/log/named
chown named.named %{_chroot}/var/log/named

%preun chroot
if [ "$1" = "0" ]; then
	for i in /var/lib/named/{M,S,root.hint}; do
		[ -L $i ] && rm -f $i
	done
	if [ -f /var/lock/subsys/named ]; then
		/etc/rc.d/init.d/named stop 1>&2
	fi
	/sbin/chkconfig --del named
fi    

%postun chroot
if [ "$1" = "0" ]; then
	%{_sbindir}/userdel named
	%{_sbindir}/groupdel named
fi

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {src/README,src/Version,src/CHANGES,EXAMPLE-CONFIG}.gz

%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/dnskeygen
%attr(755,root,root) %{_sbindir}/irpd
%attr(755,root,root) %{_sbindir}/named*
%attr(755,root,root) %{_sbindir}/ndc
%attr(755,root,root) %{_sbindir}/nsupdate

%{_mandir}/man8/named.8*
%{_mandir}/man8/ndc.8*
%{_mandir}/man8/named-xfer.8*
%{_mandir}/man8/named-bootconf.8*
%{_mandir}/man7/hostname.7*
%{_mandir}/man5/irs.conf.5*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man1/dnskeygen.1*
%{_mandir}/man8/nsupdate.8*

%attr(770,root,named) %dir /var/lib/named
%attr(750,root,named) %dir /var/lib/named/M
%attr(770,root,named) %dir /var/lib/named/S

/var/lib/named/M/*
/var/lib/named/root.*

%attr(660,named,named) %ghost /var/log/named

%files chroot
%defattr(644,root,root,755)
%doc {src/README,src/Version,src/CHANGES,EXAMPLE-CONFIG}.gz
%doc *.holelogd.gz

%ghost %attr(754,root,root) /etc/rc.d/init.d/named
%attr(754,root,root) /etc/rc.d/init.d/named-chroot
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,root) %ghost %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_chroot}%{_sysconfdir}/named.conf

%attr(755,root,root) %{_sbindir}/dnskeygen
%attr(755,root,root) %{_sbindir}/holelogd.named
%attr(755,root,root) %{_sbindir}/irpd
%attr(755,root,root) %{_sbindir}/named-bootconf
%attr(755,root,root) %{_sbindir}/ndc.chroot
%attr(755,root,root) %{_sbindir}/nsupdate

%{_mandir}/man8/named.8*
%{_mandir}/man8/ndc.8*
%{_mandir}/man8/named-xfer.8*
%{_mandir}/man8/named-bootconf.8*
%{_mandir}/man7/hostname.7*
%{_mandir}/man5/irs.conf.5*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man1/dnskeygen.1*
%{_mandir}/man8/nsupdate.8*

%attr(750,root,named) %dir /var/lib/named
%attr(750,root,named) %dir %{_chroot}
%attr(750,root,named) %dir %{_chroot}%{_sysconfdir}
%attr(750,root,named) %dir %{_chroot}/dev
%attr(750,root,named) %dir %{_chroot}%{_prefix}
%attr(750,root,named) %dir %{_chroot}%{_sbindir}
%attr(750,root,named) %dir %{_chroot}%{_datadir}
%attr(750,root,named) %dir %{_chroot}%{_datadir}/zoneinfo
%attr(750,root,named) %dir %{_chroot}/var
%attr(750,root,named) %dir %{_chroot}/var/lib
%attr(750,root,named) %dir %{_chroot}/var/lib/named
%attr(750,root,named) %dir %{_chroot}/var/lib/named/M
%attr(770,root,named) %dir %{_chroot}/var/lib/named/S
%attr(750,root,named) %dir %{_chroot}/var/log
%attr(770,root,named) %dir %{_chroot}/var/run
%attr(770,root,named) %dir %{_chroot}/var/tmp

%attr(660,named,named) %ghost %{_chroot}/var/log/named

%{_chroot}/var/lib/named/M/*
%{_chroot}/var/lib/named/root.*

%attr(755,root,root) %{_chroot}%{_sbindir}/*
%{_chroot}%{_datadir}/zoneinfo/*

%ghost %verify(not md5 size mtime) %{_chroot}%{_sysconfdir}/group
%ghost %verify(not md5 size mtime) %{_chroot}%{_sysconfdir}/localtime

%attr(10666,root,root) %ghost %{_chroot}/dev/log
%attr(20666,root,root) %ghost %{_chroot}/dev/null

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_datadir}/misc/nslookup.help

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
