#
# Conditional build:
# _without_ssl	- don't build with OpenSSL support
# _without_ipv6	- don't build IPv6 support
#
Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver
Summary(es):	BIND - Servidor de nombres DNS
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(pt_BR):	BIND - Servidor de nomes DNS
Summary(ru):	BIND - cÅÒ×ÅÒ ÓÉÓÔÅÍÙ ÄÏÍÅÎÎÙÈ ÉÍÅÎ (DNS)
Summary(tr):	DNS alan adý sunucusu
Summary(uk):	BIND - cÅÒ×ÅÒ ÓÉÓÔÅÍÉ ÄÏÍÅÎÎÉÈ ¦ÍÅÎ (DNS)
Summary(zh_CN):	Internet ÓòÃû·þÎñÆ÷
Name:		bind
Version:	9.2.2
Release:	1
Epoch:		5
License:	BSD-like
Group:		Networking/Daemons
Source0:	ftp://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-conf.tar.gz
Source2:	named.init
Source3:	named.sysconfig
Source4:	named.logrotate
Source5:	nslookup.8
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-time.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-includedir-libbind.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-pmake.patch
URL:		http://www.isc.org/products/BIND/bind9.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.6i}
PreReq:		%{name}-libs = %{version}
PreReq:		rc-scripts >= 0.2.0
Requires(pre):	fileutils
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires:	psmisc >= 20.1
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

%description -l es
Incluye el servidor de nombres (DNS), que se usa para traducir nombres
para IP (y viceversa). Puede ser usado en estaciones de trabajo como
un servidor de nombres caché, pero generalmente sólo hace falta en una
máquina para toda la red.

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

%description -l pt_BR
Inclui o servidor de nomes (DNS), que é usado para traduzir nomes para
IP (e vice-versa). Pode ser usado em estações de trabalho como um
servidor de nomes cache, mas geralmente só é necessário em uma máquina
para toda a rede.

%description -l ru
BIND (Berkeley Internet Name Domain) Ñ×ÌÑÅÔÓÑ ÒÅÁÌÉÚÁÃÉÅÊ ÐÒÏÔÏËÏÌÏ×
DNS (Domain Name System). BIND ×ËÌÀÞÁÅÔ DNS ÓÅÒ×ÅÒ (named) É
ÂÉÂÌÉÏÔÅËÕ "ÒÅÚÏÌ×ÅÒÁ" (ÐÏÄÐÒÏÇÒÁÍÍÙ ÄÌÑ ÐÒÉÌÏÖÅÎÉÊ, ÞÅÒÅÚ ËÏÔÏÒÙÅ
ÐÒÏÉÓÈÏÄÑÔ ÏÂÒÁÝÅÎÉÑ Ë DNS). DNS ÓÅÒ×ÅÒ named ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎ
ÎÁ ÒÁÂÏÞÉÈ ÓÔÁÎÃÉÑÈ ËÁË ËÅÛÉÒÕÀÝÉÊ ÓÅÒ×ÅÒ, ÎÏ ÏÂÙÞÎÏ ÚÁÐÕÓËÁÅÔÓÑ ÎÁ
ÏÄÎÏÊ ÍÁÛÉÎÅ × ÌÏËÁÌØÎÏÊ ÓÅÔÉ É ÉÓÐÏÌØÚÕÅÔÓÑ ÏÓÔÁÌØÎÙÍÉ ÍÁÛÉÎÁÍÉ (ÜÔÉÍ
ÄÏÓÔÉÇÁÅÔÓÑ ÎÁÍÎÏÇÏ ÂÏÌÅÅ ÜÆÆÅËÔÉ×ÎÏÅ ËÅÛÉÒÏ×ÁÎÉÅ).

ëÏÎÆÉÇÕÒÁÃÉÏÎÎÙÅ ÆÁÊÌÙ, ÎÁÓÔÒÁÉ×ÁÀÝÉÅ BIND ÎÁ ÒÁÂÏÔÕ × ÒÅÖÉÍÅ ÐÒÏÓÔÏÇÏ
ËÅÛÉÒÕÀÝÅÇÏ ÓÅÒ×ÅÒÁ, ×ËÌÀÞÅÎÙ × ÐÁËÅÔ caching-nameserver.

%description -l tr
Bu paket, makina adýný IP numarasýna (ya da tersi) çevirmek için
kullanýlan alan adý sunucusunu içerir. Ýþ istasyonlarýnda bir önbellek
isim sunucusu olarak da kullanýlabilir ama genellikle bütün bir að
için sadece bir makina üzerinde kurulur.

%description -l uk
BIND (Berkeley Internet Name Domain) ¤ ÒÅÁÌ¦ÚÁÃ¦¤À ÐÒÏÔÏËÏÌ¦× DNS
(Domain Name System). BIND ×ËÌÀÞÁ¤ DNS ÓÅÒ×ÅÒ (named) ÔÁ Â¦ÂÌ¦ÏÔÅËÕ
"ÒÅÚÏÌ×ÅÒÁ" (Ð¦ÄÐÒÏÇÒÁÍÉ, ÝÏ ÚÁÂÅÚÐÅÞÕÀÔØ ¦ÎÔÅÒÆÅÊÓ ÄÏ DNS). DNS
ÓÅÒ×ÅÒ named ÍÏÖÅ ÂÕÔÉ ×ÉËÏÒÉÓÔÁÎÉÊ ÎÁ ÒÏÂÏÞÉÈ ÓÔÁÎÃ¦ÑÈ ÑË ËÅÛÉÒÕÀÞÉÊ
ÓÅÒ×ÅÒ, ÁÌÅ Ú×ÉÞÁÊÎÏ ÚÁÐÕÓËÁ¤ÔØÓÑ ÎÁ ÏÄÎ¦Ê ÍÁÛÉÎ¦ × ÌÏËÁÌØÎ¦Ê ÍÅÒÅÖ¦ ¦
×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ¦ÎÛÉÍÉ (ÃÉÍ ÄÏÓÑÇÁ¤ÔØÓÑ Â¦ÌØÛÁ ÅÆÅËÔÉ×Î¦ÓÔØ
×ÉËÏÒÉÓÔÁÎÎÑ ËÅÛÕ).

ëÏÎÆ¦ÇÕÒÁÃ¦ÊÎ¦ ÆÁÊÌÉ, ÝÁ ÎÁÓÔÒÏÀÀÔØ BIND ÎÁ ÒÏÂÏÔÕ × ÒÅÖÉÍ¦ ÐÒÏÓÔÏÇÏ
ËÅÛÉÒÕÀÞÏÇÏ ÓÅÒ×ÅÒÕ, ×ËÌÀÞÅÎ¦ × ÐÁËÅÔ caching-nameserver.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup
Summary(es):	Utilitarios DNS - host, dig, dnsquery y nslookup
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narzêdzia DNS - host, dig, dnsquery, nslookup
Summary(pt_BR):	Utilitários DNS - host, dig, dnsquery e nslookup
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ ÐÏÓÙÌËÉ ÚÁÐÒÏÓÏ× Ë ÓÅÒ×ÅÒÁÍ DNS
Summary(tr):	DNS araçlarý - host, dig, dnsquery, nslookup
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ÎÁÄÓÉÌÁÎÎÑ ÚÁÐÉÔ¦× ÄÏ ÓÅÒ×ÅÒ¦× DNS
Summary(zh_CN):	Internet ÓòÃû·þÎñÆ÷ÊµÓÃ¹¤¾ß
Group:		Networking/Utilities
Requires:	%{name}-libs = %{version}

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name Service) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install bind-utils if you need to get information from DNS
name servers.

%description utils -l de
Dienstprogrammsammlung zum Abfragen von Namen-Servern und Hosts. Diese
Tools bestimmen die IP-Adresse eines angegebenen Host-Namen und finden
Informationen über registrierte Domains und Netzwerk-Adressen.

%description utils -l es
Conjunto de utilitarios para consulta a servidores de nombres. Estas
herramientas permiten la determinación de direcciones IP para nombres
de máquinas informados y busca información sobre dominios registrados
y direcciones de red.

%description utils -l fr
Ensemble d'utilitaires pour interroger les serveurs de noms et
rechercher des hôtes. Ces outils vous permettent de déterminer les
adresses IP pour des noms d'hôtes donnés, et trouver des informations
sur les noms de domaine déclarés et les adresses réseau.

%description utils -l pl
Pakiet ten zawiera zbiór aplikacji umo¿liwiaj±cych odpytywanie
serwerów nazw z innych domen w celu uzyskania informacji o komputerach
i ich adresach IP.

%description utils -l pt_BR
Conjunto de utilitários para consulta a servidores DNS. Estas
ferramentas permitem a determinação de endereços IP para nomes de
máquinas informados e busca informações sobre domínios registrados e
endereços de rede. Você deveria instalar este pacote se necessitar
obter informações de servidores DNS.

%description utils -l ru
îÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÇÅÎÅÒÁÃÉÉ ÚÁÐÒÏÓÏ× Ë ÓÅÒ×ÅÒÁÍ ÉÍÅÎ (DNS) É ÐÏÉÓËÁ
ÁÄÒÅÓÏ× ÍÁÛÉÎ. üÔÉ ÕÔÉÌÉÔÙ ÐÏÚ×ÏÌÑÀÔ ÏÐÒÅÄÅÌÉÔØ IP-ÁÄÒÅÓ ÐÏ ÉÚ×ÅÓÔÎÏÍÕ
ÄÏÍÅÎÎÏÍÕ ÉÍÅÎÉ (É ÎÁÏÂÏÒÏÔ) É ÄÒÕÇÕÀ ÉÎÆÏÒÍÁÃÉÀ Ï ÚÁÒÅÇÉÓÔÒÉÒÏ×ÁÎÎÙÈ
ÄÏÍÅÎÁÈ É ÓÅÔÅ×ÙÈ ÁÄÒÅÓÁÈ.

%description utils -l tr
Bu pakette isim sunucularýný sorgulamak ve makina adreslerini çözmek
için kullanýlan araçlar bulunmaktadýr.

%description utils -l uk
îÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÇÅÎÅÒÁÃ¦§ ÚÁÐÉÔ¦× ÄÏ ÓÅÒ×ÅÒ¦× ¦ÍÅÎ (DNS) ÔÁ ÐÏÛÕËÕ
ÁÄÒÅÓ ÍÁÛÉÎ. ã¦ ÕÔÉÌ¦ÔÉ ÄÏÚ×ÏÌÑÀÔØ ÏÔÒÉÍÁÔÉ IP-ÁÄÒÅÓÕ ÚÁ ×¦ÄÏÍÉÍ
ÄÏÍÅÎÎÉÍ ¦ÍÅÎÅÍ ÔÁ ÎÁ×ÐÁËÉ, Á ÔÁËÏÖ ¦ÎÛÕ ¦ÎÆÏÒÍÁÃ¦À ÐÒÏ ÚÁÒÅ¤ÓÔÒÏ×ÁÎ¦
ÄÏÍÅÎÉ ÔÁ ÁÄÒÅÓÉ.

%package libs
Summary:	DNS libraries
Summary(pl):	Biblioteki DNS
Summary(ru):	âÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ bind
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ bind
Summary(zh_CN):	Internet ÓòÃû·þÎñÆ÷¿ª·¢¿â
Group:		Libraries

%description libs
The bind-libs package contains all libraries required for running BIND
and bind utils.

%description libs -l pl
Pakiet zawiera wszystkie biblioteki potrzebne do uruchomienia binda
lub programów z pakietu bind-utils.

%description libs -l ru
âÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÂÏÔÙ bind.

%description libs -l uk
â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÂÏÔÉ bind.

%package devel
Summary:	DNS development includes
Summary(es):	Archivos de inclusión y bibliotecas para desarrollo DNS
Summary(pl):	Pliki nag³ówkowe bibliotek DNS
Summary(pt_BR):	Todos os arquivos de cabeçalho e bibliotecas para desenvolvimento DNS
Summary(ru):	èÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ bind
Summary(uk):	èÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ bind
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
The bind-devel package contains all the include files and symlinks
required for DNS (Domain Name Service) development for BIND.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind-libs.

%description devel -l es
Todos los archivos de inclusión y bibliotecas necesarios al desarrollo
DNS para el bind.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe. Je¿eli bêdziesz pisa³ programy pod
binda, lub kompilowa³ kod ¼ród³owy oprogramowania korzystaj±cego z
tych plików nag³ówkowych czy biblioteki powiniene¶ zainstalowaæ ten
pakiet.

%description devel -l pt_BR
Todos os arquivos de cabeçalho e bibliotecas necessários para o
desenvolvimento com o bind.

%description devel -l ru
÷ÓÅ ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÎÁÐÉÓÁÎÉÑ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ BIND 9.x.x.

%description devel -l uk
÷Ó¦ ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú
×ÉËÏÒÉÓÔÁÎÎÑÍ BIND 9.x.x.

%package static
Summary:	DNS static libs
Summary(pl):	Biblioteki statyczne DNS
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento DNS
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ bind
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ bind
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static bind libraries.

%description static -l pl
Statyczne biblioteki binda.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento DNS.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÎÁÐÉÓÁÎÉÑ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ BIND.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ
BIND.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd lib/bind
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd ../..
%configure \
	%{!?_without_ssl:--with-openssl=%{_prefix}} \
	--with-libtool \
	--enable-threads \
	%{!?_without_ipv6:--enable-ipv6} \
	--enable-libbind
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

rm -f doc/rfc/rfc*

install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_sbindir},%{_includedir}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8}
install -d $RPM_BUILD_ROOT%{_var}/{lib/named/{M,S,dev,etc},run,log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE5}			$RPM_BUILD_ROOT%{_mandir}/man8
bzip2 -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install conf-pld/*.zone			$RPM_BUILD_ROOT%{_var}/lib/named/M
install conf-pld/*.hint			$RPM_BUILD_ROOT%{_var}/lib/named
install conf-pld/*.conf			$RPM_BUILD_ROOT%{_var}/lib/named/%{_sysconfdir}
install bin/tests/named.conf		EXAMPLE-CONFIG-named
install bin/tests/ndc.conf		EXAMPLE-CONFIG-ndc
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE4}			$RPM_BUILD_ROOT/etc/logrotate.d/named

ln -sf %{_var}/lib/named/%{_sysconfdir}/named.conf $RPM_BUILD_ROOT/etc/named.conf
ln -sf %{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
ln -sf %{_var}/lib/named/named.stats	$RPM_BUILD_ROOT%{_var}/log/named.stats

touch $RPM_BUILD_ROOT%{_var}/lib/named/{named.{log,stats},dev/{random,null}}

# we don't want Makefiles in documentation...
rm -f doc/misc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -f %{_sysconfdir}/named.boot ]; then
	cp -f %{_sysconfdir}/named.boot /etc/named.boot.2conf
	mv -f %{_sysconfdir}/named.boot /etc/named.rpmsave
	echo "Warning: %{_sysconfdir}/named.boot saved as /etc/named.rpmsave." 1>&2
fi
if [ -n "`getgid named`" ]; then
	if [ "`getgid named`" != "58" ]; then
		echo "Error: group named doesn't have gid=58. Correct this before installing bind." 1>&2
		exit 1
	fi
else
	echo "Adding group named GID=58."
	/usr/sbin/groupadd -g 58 named || exit 1
fi
if [ -n "`id -u named 2>/dev/null`" ]; then
	if [ "`id -u named`" != "58" ]; then
		echo "Error: user named doesn't have uid=58. Correct this before installing bind." 1>&2
		exit 1
	fi
else
	echo "Adding user named UID=58."
	/usr/sbin/useradd -u 58 -g 58 -d /dev/null -s /bin/false -c "BIND user" named || exit 1
fi

%post
/sbin/chkconfig --add named
if [ -f /var/lock/subsys/named ]; then
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named." 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/named ]; then
		/etc/rc.d/init.d/named stop 1>&2
	fi
	/sbin/chkconfig --del named
fi

%postun
if [ "$1" = "0" ]; then
	echo "Removing user named."
	%{_sbindir}/userdel named
	echo "Removing group named."
	%{_sbindir}/groupdel named
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README EXAMPLE-CONFIG-* FAQ doc/misc/* doc/arm/*.html doc/rfc/index

%attr(754,root,root)  /etc/rc.d/init.d/named
%attr(640,root,root)  %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,root)  %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man8/dns*
%{_mandir}/man8/lwres*
%{_mandir}/man8/named*
%{_mandir}/man8/rndc*
%{_mandir}/man5/rndc*
%lang(ja) %{_mandir}/ja/man8/named*

%attr(770,root,named) %dir %{_var}/lib/named
%attr(750,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(770,root,named) %dir %{_var}/lib/named/dev

%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/M/*
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/root.*
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/%{_sysconfdir}/*

#%ghost %{_var}/lib/named/dev/*
%attr(770,root,named) %{_var}/lib/named/dev/*
%attr(660,named,named) %ghost %{_var}/log/named*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/nslookup
%attr(755,root,root) %{_bindir}/nsupdate
%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
%{_mandir}/man8/nslookup.8*
%{_mandir}/man8/nsupdate*

%lang(fi) %{_mandir}/fi/man1/host.1*

%lang(fr) %{_mandir}/fr/man1/host.1*

%lang(hu) %{_mandir}/hu/man1/host.1*

%lang(ja) %{_mandir}/ja/man1/dig.1*
%lang(ja) %{_mandir}/ja/man1/host.1*
%lang(ja) %{_mandir}/ja/man8/nslookup.8*
%lang(ja) %{_mandir}/ja/man8/nsupdate.8*

%lang(pl) %{_mandir}/pl/man1/host.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.sh
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
