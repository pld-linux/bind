Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan adý sunucusu
Name:		bind
Version:	9.1.3
Release:	1
Epoch:		5
License:	Distributable
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-conf.tar.gz
Source2:	named.init
Source3:	named.sysconfig
Source4:	named.logrotate
Source5:	nslookup.8
Source6:	resolver.5
Patch1:		%{name}-time.patch
BuildRequires:	sed
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	autoconf
Prereq:		rc-scripts >= 0.2.0
Prereq:		/sbin/chkconfig
Prereq:		%{name}-libs
Requires:	%{name}-libs = %{version}
Requires:	psmisc >= 20.1
#Requires(pre,post):	fileutils
#Requires(pre,postun):	shadow
#Requires(post,preun):	chkconfig
#Requires(post,preun):	rc-scripts
URL:		http://www.isc.org/products/BIND/bind9.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	caching-nameserver
Conflicts:	%{name}-chroot
Conflicts:	kernel < 2.2.18

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

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS araçlarý - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Requires:	%{name}-libs = %{version}

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

%package libs
Summary:	DNS libraries
Summary(pl):	Biblioteki DNS
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki

%description libs
The bind-libs package contains all libraries required for
running BIND and bind utils.

%description -l pl libs
Pakiet zawiera wszystkie biblioteki potrzebne do uruchomienia binda
lub programów z pakietu bind-utils.

%package devel
Summary:	DNS development includes
Summary(pl):	Pliki nag³ówkowe bibliotek DNS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
The bind-devel package contains all the include files and symlinks
required for DNS (Domain Name Service) development for BIND.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind-libs.

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe. Je¿eli bêdziesz pisa³ programy pod
binda, lub kompilowa³ kod ¼ród³owy oprogramowania korzystaj±cego
z tych plików nag³ówkowych czy biblioteki powiniene¶ zainstalowaæ ten
pakiet.

%package static
Summary:	DNS static libs
Summary(pl):	Biblioteki statyczne
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description static
Static bind libraries.

%description -l pl static
Statyczne biblioteki binda.

%prep
%setup -q -a1
%patch1 -p1

%build
autoconf
%configure \
	--with-openssl=%{_prefix} \
	--with-libtool \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_sbindir},%{_includedir}}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,logrotate.d,sysconfig}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8}
install -d $RPM_BUILD_ROOT%{_var}/{lib/named/{M,S,dev,etc},run,log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/man/bin/*.1			$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/lwres/*.3		$RPM_BUILD_ROOT%{_mandir}/man3
install doc/man/bin/*.5			$RPM_BUILD_ROOT%{_mandir}/man5
install %{SOURCE6}			$RPM_BUILD_ROOT%{_mandir}/man5
install doc/man/{bin/*.8,dnssec/*.8}	$RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE5}			$RPM_BUILD_ROOT%{_mandir}/man8

install conf-pld/*.zone			$RPM_BUILD_ROOT%{_var}/lib/named/M
install conf-pld/*.hint			$RPM_BUILD_ROOT%{_var}/lib/named
install conf-pld/*.conf			$RPM_BUILD_ROOT%{_var}/lib/named/etc
install bin/tests/named.conf		EXAMPLE-CONFIG-named
install bin/tests/ndc.conf		EXAMPLE-CONFIG-ndc
install %{SOURCE2}			$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/named
install %{SOURCE3}			$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/named
install %{SOURCE4}			$RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/named
ln -sf %{_var}/lib/named/etc/named.conf	$RPM_BUILD_ROOT%{_sysconfdir}/named.conf
ln -sf %{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
touch		$RPM_BUILD_ROOT%{_var}/lib/named/{named.log,dev/{random,null}}

gzip -9nf README EXAMPLE-CONFIG-* doc/misc/*

%pre
if [ -f %{_sysconfdir}/named.boot ]; then
	cp -f %{_sysconfdir}/named.boot /etc/named.boot.2conf
	mv -f %{_sysconfdir}/named.boot /etc/named.rpmsave
	echo "Warning:%{_sysconfdir}/named.boot saved as /etc/named.rpmsave" 1>&2
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
	%{_sysconfdir}/rc.d/init.d/named restart 1>&2
else
	echo "Type \"%{_sysconfdir}/rc.d/init.d/named start\" to start named" 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/named ]; then
		%{_sysconfdir}/rc.d/init.d/named stop 1>&2
	fi
	/sbin/chkconfig --del named
fi    

%postun
if [ "$1" = "0" ]; then
	%{_sbindir}/userdel named
	%{_sbindir}/groupdel named
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/misc/*.gz doc/arm/*

%attr(754,root,root)  %{_sysconfdir}/rc.d/init.d/named
%attr(640,root,root)  %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,root)  %config %verify(not size mtime md5) %{_sysconfdir}/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/nsupdate

%{_mandir}/man8/dns*
%{_mandir}/man8/lwres*
%{_mandir}/man8/named*
%{_mandir}/man8/rndc*
%{_mandir}/man5/rndc*
%{_mandir}/man8/nsupdate*

%attr(770,root,named) %dir %{_var}/lib/named
%attr(750,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(770,root,named) %dir %{_var}/lib/named/dev

%{_var}/lib/named/M/*
%{_var}/lib/named/root.*
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/etc/*

%ghost %{_var}/lib/named/dev/*
%attr(660,named,named) %ghost %{_var}/log/named

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/nslookup
%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
%{_mandir}/man8/nslookup.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.sh
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
