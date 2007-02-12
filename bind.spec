#
# Conditional build:
%bcond_without	ssl	# build without OpenSSL support
%bcond_without	ipv6	# build without IPv6 support
%bcond_without	ldap	# build without LDAP support
#
Summary:	BIND - DNS name server
Summary(de.UTF-8):   BIND - DNS-Namenserver
Summary(es.UTF-8):   BIND - Servidor de nombres DNS
Summary(fr.UTF-8):   BIND - serveur de noms DNS
Summary(pl.UTF-8):   BIND - serwer nazw DNS
Summary(pt_BR.UTF-8):   BIND - Servidor de nomes DNS
Summary(ru.UTF-8):   BIND - cервер системы доменных имен (DNS)
Summary(tr.UTF-8):   DNS alan adı sunucusu
Summary(uk.UTF-8):   BIND - cервер системи доменних імен (DNS)
Summary(zh_CN.UTF-8):   Internet 域名服务器
Name:		bind
Version:	9.3.0
Release:	0.2
Epoch:		5
License:	BSD-like
Group:		Networking/Daemons
Source0:	ftp://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fdb42fff7e345372ac52a4493b77b694
Source1:	%{name}-conf.tar.gz
# Source1-md5:	8ee77729f806fcd548fe0cceb34b4a06
Source2:	named.init
Source3:	named.sysconfig
Source4:	named.logrotate
Source5:	nslookup.8
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source6-md5:	35b1dfaa12615c9802126ee833e0e7f7
Source7:	http://www.venaas.no/ldap/bind-sdb/dnszone-schema.txt
# Source7-md5:	c9a17d8cf8c1a6d4fad6138a1c3f36c4
Patch0:		%{name}-time.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-includedir-libbind.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-pmake.patch
# from idnkit
Patch5:		%{name}-idn.patch
Patch6:		%{name}-sdb-ldap.patch
Patch7:		%{name}-noinet6.patch
URL:		http://www.isc.org/products/BIND/bind9.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	idnkit-devel
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	rpmbuild(macros) >= 1.159
PreReq:		%{name}-libs = %{epoch}:%{version}-%{release}
PreReq:		rc-scripts >= 0.2.0
Requires(pre):	fileutils
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires:	psmisc >= 20.1
Provides:	group(named)
Provides:	nameserver
Provides:	user(named)
Obsoletes:	caching-nameserver
Obsoletes:	nameserver
Conflicts:	%{name}-chroot
Conflicts:	kernel < 2.2.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l de.UTF-8
Enthält den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf Workstations als
caching Namen-Server verwendet werden, ist aber i.d.R. nur auf einem
Recher des Netzwerks erforderlich.

%description -l es.UTF-8
Incluye el servidor de nombres (DNS), que se usa para traducir nombres
para IP (y viceversa). Puede ser usado en estaciones de trabajo como
un servidor de nombres caché, pero generalmente sólo hace falta en una
máquina para toda la red.

%description -l fr.UTF-8
Contient le serveur de noms named, utilisé pour définir les
traductions nom d'hôte vers adresse IP (et vice versa). Il peut être
utilisé sur les stations de travail comme serveur de nom en cache mais
n'est souvent nécessaire que sur une machine pour un réseau entier.

%description -l pl.UTF-8
Pakiet ten zawiera demona named, który służy do zmieniania nazw
komputerów na numery IP i odwrotnie. Może być on używany na stacjach
roboczych jako bufor odwołań do serwisu nazw (caching name server),
ale generalnie wystarczy tylko jedna jednostka wyposażona w ten
program na fragment sieci.

%description -l pt_BR.UTF-8
Inclui o servidor de nomes (DNS), que é usado para traduzir nomes para
IP (e vice-versa). Pode ser usado em estações de trabalho como um
servidor de nomes cache, mas geralmente só é necessário em uma máquina
para toda a rede.

%description -l ru.UTF-8
BIND (Berkeley Internet Name Domain) является реализацией протоколов
DNS (Domain Name System). BIND включает DNS сервер (named) и
библиотеку "резолвера" (подпрограммы для приложений, через которые
происходят обращения к DNS). DNS сервер named может быть использован
на рабочих станциях как кеширующий сервер, но обычно запускается на
одной машине в локальной сети и используется остальными машинами (этим
достигается намного более эффективное кеширование).

Конфигурационные файлы, настраивающие BIND на работу в режиме простого
кеширующего сервера, включены в пакет caching-nameserver.

%description -l tr.UTF-8
Bu paket, makina adını IP numarasına (ya da tersi) çevirmek için
kullanılan alan adı sunucusunu içerir. İş istasyonlarında bir önbellek
isim sunucusu olarak da kullanılabilir ama genellikle bütün bir ağ
için sadece bir makina üzerinde kurulur.

%description -l uk.UTF-8
BIND (Berkeley Internet Name Domain) є реалізацією протоколів DNS
(Domain Name System). BIND включає DNS сервер (named) та бібліотеку
"резолвера" (підпрограми, що забезпечують інтерфейс до DNS). DNS
сервер named може бути використаний на робочих станціях як кешируючий
сервер, але звичайно запускається на одній машині в локальній мережі і
використовується іншими (цим досягається більша ефективність
використання кешу).

Конфігураційні файли, ща настроюють BIND на роботу в режимі простого
кешируючого серверу, включені в пакет caching-nameserver.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de.UTF-8):   DNS-Utils - Host, Dig, Dnsquery, Nslookup
Summary(es.UTF-8):   Utilitarios DNS - host, dig, dnsquery y nslookup
Summary(fr.UTF-8):   Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl.UTF-8):   Narzędzia DNS - host, dig, dnsquery, nslookup
Summary(pt_BR.UTF-8):   Utilitários DNS - host, dig, dnsquery e nslookup
Summary(ru.UTF-8):   Утилиты для посылки запросов к серверам DNS
Summary(tr.UTF-8):   DNS araçları - host, dig, dnsquery, nslookup
Summary(uk.UTF-8):   Утиліти для надсилання запитів до серверів DNS
Summary(zh_CN.UTF-8):   Internet 域名服务器实用工具
Group:		Networking/Utilities
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	iconv

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name Service) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install bind-utils if you need to get information from DNS
name servers.

%description utils -l de.UTF-8
Dienstprogrammsammlung zum Abfragen von Namen-Servern und Hosts. Diese
Tools bestimmen die IP-Adresse eines angegebenen Host-Namen und finden
Informationen über registrierte Domains und Netzwerk-Adressen.

%description utils -l es.UTF-8
Conjunto de utilitarios para consulta a servidores de nombres. Estas
herramientas permiten la determinación de direcciones IP para nombres
de máquinas informados y busca información sobre dominios registrados
y direcciones de red.

%description utils -l fr.UTF-8
Ensemble d'utilitaires pour interroger les serveurs de noms et
rechercher des hôtes. Ces outils vous permettent de déterminer les
adresses IP pour des noms d'hôtes donnés, et trouver des informations
sur les noms de domaine déclarés et les adresses réseau.

%description utils -l pl.UTF-8
Pakiet ten zawiera zbiór aplikacji umożliwiających odpytywanie
serwerów nazw z innych domen w celu uzyskania informacji o komputerach
i ich adresach IP.

%description utils -l pt_BR.UTF-8
Conjunto de utilitários para consulta a servidores DNS. Estas
ferramentas permitem a determinação de endereços IP para nomes de
máquinas informados e busca informações sobre domínios registrados e
endereços de rede. Você deveria instalar este pacote se necessitar
obter informações de servidores DNS.

%description utils -l ru.UTF-8
Набор утилит для генерации запросов к серверам имен (DNS) и поиска
адресов машин. Эти утилиты позволяют определить IP-адрес по известному
доменному имени (и наоборот) и другую информацию о зарегистрированных
доменах и сетевых адресах.

%description utils -l tr.UTF-8
Bu pakette isim sunucularını sorgulamak ve makina adreslerini çözmek
için kullanılan araçlar bulunmaktadır.

%description utils -l uk.UTF-8
Набір утиліт для генерації запитів до серверів імен (DNS) та пошуку
адрес машин. Ці утиліти дозволяють отримати IP-адресу за відомим
доменним іменем та навпаки, а також іншу інформацію про зареєстровані
домени та адреси.

%package libs
Summary:	DNS libraries
Summary(pl.UTF-8):   Biblioteki DNS
Summary(ru.UTF-8):   Библиотеки, необходимые для bind
Summary(uk.UTF-8):   Бібліотеки, необхідні для bind
Summary(zh_CN.UTF-8):   Internet 域名服务器开发库
Group:		Libraries

%description libs
The bind-libs package contains all libraries required for running BIND
and bind utils.

%description libs -l pl.UTF-8
Pakiet zawiera wszystkie biblioteki potrzebne do uruchomienia binda
lub programów z pakietu bind-utils.

%description libs -l ru.UTF-8
Библиотеки, необходимые для работы bind.

%description libs -l uk.UTF-8
Бібліотеки, необхідні для роботи bind.

%package devel
Summary:	DNS development includes
Summary(es.UTF-8):   Archivos de inclusión y bibliotecas para desarrollo DNS
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek DNS
Summary(pt_BR.UTF-8):   Todos os arquivos de cabeçalho e bibliotecas para desenvolvimento DNS
Summary(ru.UTF-8):   Хедеры и библиотеки разработчика для bind
Summary(uk.UTF-8):   Хедери та бібліотеки програміста для bind
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
The bind-devel package contains all the include files and symlinks
required for DNS (Domain Name Service) development for BIND.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind-libs.

%description devel -l es.UTF-8
Todos los archivos de inclusión y bibliotecas necesarios al desarrollo
DNS para el bind.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe. Jeżeli będziesz pisał programy pod
binda, lub kompilował kod źródłowy oprogramowania korzystającego z
tych plików nagłówkowych czy biblioteki powinieneś zainstalować ten
pakiet.

%description devel -l pt_BR.UTF-8
Todos os arquivos de cabeçalho e bibliotecas necessários para o
desenvolvimento com o bind.

%description devel -l ru.UTF-8
Все хедеры и библиотеки, необходимые для написания программ с
использованием BIND 9.x.x.

%description devel -l uk.UTF-8
Всі хедери та бібліотеки, необхідні для розробки програм з
використанням BIND 9.x.x.

%package static
Summary:	DNS static libs
Summary(pl.UTF-8):   Biblioteki statyczne DNS
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento DNS
Summary(ru.UTF-8):   Статические библиотеки разработчика для bind
Summary(uk.UTF-8):   Статичні бібліотеки програміста для bind
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static bind libraries.

%description static -l pl.UTF-8
Statyczne biblioteki binda.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento DNS.

%description static -l ru.UTF-8
Статические библиотеки, необходимые для написания программ с
использованием BIND.

%description static -l uk.UTF-8
Статичні бібліотеки, необхідні для розробки програм з використанням
BIND.

%prep
%setup -q -a1 -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%{?with_ldap:%patch6 -p1}
%patch7 -p1

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
	--with-idn \
	--with-libtool \
	%{?with_ssl:--with-openssl=%{_prefix}} \
	%{?with_ipv6:--enable-ipv6} \
	--enable-libbind \
	--enable-threads \
	--disable-getifaddrs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_sbindir},%{_includedir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3,5,8},%{_var}/{lib/named/{M,S,dev,etc},run,log}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/rfc/rfc*

install %{SOURCE5}			$RPM_BUILD_ROOT%{_mandir}/man8
bzip2 -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install conf-pld/*.zone			$RPM_BUILD_ROOT%{_var}/lib/named/M
install conf-pld/*.hint			$RPM_BUILD_ROOT%{_var}/lib/named
install conf-pld/*.conf			$RPM_BUILD_ROOT%{_var}/lib/named%{_sysconfdir}
install bin/tests/named.conf		EXAMPLE-CONFIG-named
install bin/tests/ndc.conf		EXAMPLE-CONFIG-ndc
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE4}			$RPM_BUILD_ROOT/etc/logrotate.d/named

ln -sf %{_var}/lib/named%{_sysconfdir}/named.conf $RPM_BUILD_ROOT/etc/named.conf
ln -sf %{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
ln -sf %{_var}/lib/named/named.stats	$RPM_BUILD_ROOT%{_var}/log/named.stats

touch $RPM_BUILD_ROOT%{_var}/lib/named/{named.{log,stats},dev/{random,null}}

%{?with_ldap:mkdir -p $RPM_BUILD_ROOT%{_datadir}/openldap/schema/}
%{?with_ldap:install %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/openldap/schema/dnszone.schema}

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
	/usr/sbin/useradd -u 58 -g 58 -d /tmp -s /bin/false -c "BIND user" named || exit 1
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
	%userremove named
	%groupremove named
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README EXAMPLE-CONFIG-* FAQ doc/misc/* doc/arm/*.html doc/rfc/index %{?with_ldap:doc/*.sdb-ldap}

%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*

%{?with_ldap:%{_datadir}/openldap/schema/*.schema}

%{_mandir}/man8/dns*
%{_mandir}/man8/lwres*
%{_mandir}/man8/named*
%{_mandir}/man8/rndc*
%{_mandir}/man5/rndc*
%lang(ja) %{_mandir}/ja/man8/named*

%attr(770,root,named) %dir %{_var}/lib/named
%attr(750,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(750,root,named) %dir %{_var}/lib/named%{_sysconfdir}
%attr(770,root,named) %dir %{_var}/lib/named/dev

%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/M/*
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/root.*
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_var}/lib/named%{_sysconfdir}/*

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
%attr(755,root,root) %{_libdir}/*.so.*.*

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
