Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan ad� sunucusu
Name:		bind
Version:	9.0.0
Release:	1
Copyright:	distributable
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-conf.tar.gz
Source2:	ftp://ftp.nikhef.nl/pub/network/host_991529.tar.Z
Source3:	named.init
Source4:	named.sysconfig
Source5:	named.logrotate
Patch0:		ftp://ftp.6bone.pl/pub/ipv6/set-glibc-2.1.new/host_991529+.diff
BuildRequires:	flex
Prereq:		/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Obsoletes:	caching-nameserver
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
Enth�lt den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf Workstations als
caching Namen-Server verwendet werden, ist aber i.d.R. nur auf einem
Recher des Netzwerks erforderlich.

%description -l fr
Contient le serveur de noms named, utilis� pour d�finir les
traductions nom d'h�te vers adresse IP (et vice versa). Il peut �tre
utilis� sur les stations de travail comme serveur de nom en cache mais
n'est souvent n�cessaire que sur une machine pour un r�seau entier.

%description -l pl
Pakiet ten zawiera demona named, kt�ry s�u�y do zmieniania nazw
komputer�w na numery IP i odwrotnie. Mo�e by� on u�ywany na stacjach
roboczych jako bufor odwo�a� do serwisu nazw (caching name server),
ale generalnie wystarczy tylko jedna jednostka wyposa�ona w ten
program na fragment sieci.

%description -l tr
Bu paket, makina ad�n� IP numaras�na (ya da tersi) �evirmek i�in
kullan�lan alan ad� sunucusunu i�erir. �� istasyonlar�nda bir �nbellek
isim sunucusu olarak da kullan�labilir ama genellikle b�t�n bir a�
i�in sadece bir makina �zerinde kurulur.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narz�dzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS ara�lar� - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia

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
Informationen �ber registrierte Domains und Netzwerk-Adressen.

%description -l fr utils
Ensemble d'utilitaires pour interroger les serveurs de noms et
rechercher des h�tes. Ces outils vous permettent de d�terminer les
adresses IP pour des noms d'h�tes donn�s, et trouver des informations
sur les noms de domaine d�clar�s et les adresses r�seau.

%description -l pl utils
Pakiet ten zawiera zbi�r aplikacji umo�liwiaj�cych odpytywanie
serwer�w nazw z innych domen w celu uzyskania informacji o komupterach
i ich adresach IP.

%description -l tr utils
Bu pakette isim sunucular�n� sorgulamak ve makina adreslerini ��zmek
i�in kullan�lan ara�lar bulunmaktad�r.

%package devel
Summary:	DNS development includes and libs
Summary(pl):	Pliki nag��wkowe i biblioteka statyczna
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
Pakiet zawiera pliki nag��wkowe i bibliotek� statyczn�. Je�eli
b�dziesz pisa� programy pod binda, lub kompilowa� kod �r�d�owy
oprogramowania korzystaj�cego z tych plik�w nag��wkowych czy
biblioteki powiniene� zainstalowa� ten pakiet.

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
%setup -q -a1
mkdir host && cd host && %{__gzip} -dc %{SOURCE2} | tar -xf -
%patch0 -p1

%build
%configure \
	--enable-ipv6

%{__make}
%{__make} -C host COPTS="$RPM_OPT_FLAGS -DIPV6"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig,logrotate.d,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5,8}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install host/host $RPM_BUILD_ROOT%{_bindir}/host6
install contrib/named-bootconf/named-bootconf.sh $RPM_BUILD_ROOT%{_sbindir}/named-bootconf
mv -f $RPM_BUILD_ROOT%{_bindir}/nsupdate $RPM_BUILD_ROOT%{_sbindir}

install doc/man/bin/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/bin/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install doc/man/bin/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install doc/man/dnssec/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

install -d $RPM_BUILD_ROOT/var/{log,lib/named/{M,S,dev}}

install conf-pld/127.* $RPM_BUILD_ROOT/var/lib/named/M
install conf-pld/loca* $RPM_BUILD_ROOT/var/lib/named/M
install conf-pld/root.* $RPM_BUILD_ROOT/var/lib/named/root.hint
install conf-pld/named.conf $RPM_BUILD_ROOT/var/lib/named

ln -s /var/lib/named/named.conf $RPM_BUILD_ROOT/etc/named.conf

cp bin/tests/named.conf EXAMPLE-CONFIG

install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/named

touch $RPM_BUILD_ROOT/var/lib/named/{named.log,dev/{random,null}}
ln -s /var/lib/named/named.log $RPM_BUILD_ROOT/var/log/named

gzip -9nf README CHANGES EXAMPLE-CONFIG \
	doc/rfc/* doc/misc/* doc/draft/*

%pre
if [ -f /etc/named.conf ]; then
	if [ ! -e /var/lib/named/named.conf ]; then
		mv -f /etc/named.conf /var/lib/named/named.conf
		ln -sf  /var/lib/named/named.conf /etc/named.conf
	else
		mv -f /var/lib/named/named.conf /var/lib/named/named.conf.rpmsave
		mv -f /etc/named.conf /var/lib/named/named.conf
		ln -sf /var/lib/named/named.conf /etc/named.conf
	fi
fi

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
%{_bindir}/update-db

%post
/sbin/chkconfig --add named

if [ -f /var/lock/subsys/named ]; then
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named" 1>&2
fi

if [ -f /etc/named.boot.2conf ]; then
	mv -f /var/lib/named/named.conf /var/lib/named/named.conf.rpmsave
	/usr/sbin/named-bootconf </etc/named.boot.2conf >/var/lib/named/named.conf
	rm -f /etc/named.boot.2conf
fi

umask 117
/bin/touch /var/lib/named/named.log
chown named.named /var/lib/named/named.log
ln -s /var/lib/named/named.log /var/log/named

umask 022
mknod -m u+rw,go+r /var/lib/named/dev/random c 1 8
mknod -m a+rw /var/lib/named/dev/null c 1 3

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
	%{_bindir}/update-db
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,EXAMPLE-CONFIG}.gz

%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) /var/lib/named/named.conf

%attr(755,root,root) %{_sbindir}/dnssec*
%attr(755,root,root) %{_sbindir}/lwresd
%attr(755,root,root) %{_sbindir}/named*
%attr(755,root,root) %{_sbindir}/nsupdate
%attr(755,root,root) %{_sbindir}/rndc

%{_mandir}/man8/*
%{_mandir}/man5/*

%attr(770,root,named) %dir /var/lib/named
%attr(750,root,named) %dir /var/lib/named/M
%attr(770,root,named) %dir /var/lib/named/S
%attr(770,root,named) %dir /var/lib/named/dev

/var/lib/named/M/*
/var/lib/named/root.*

%attr(660,named,named) %ghost /var/log/named
%ghost /var/lib/named/dev/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host*
%attr(755,root,root) %{_bindir}/nslookup
%{_mandir}/man1/host.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isc-config.sh
%{_includedir}/*
%{_libdir}/*.a

%files doc
%defattr(644,root,root,755)
%doc doc/arm doc/rfc doc/misc doc/draft
