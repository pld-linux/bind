# TODO
# - apply http://www.caraytech.com/geodns/
#
# Conditional build:
%bcond_with	dnstap		# dnstap replication support
%bcond_without	geoip		# GeoIP support
%bcond_without	kerberos5	# GSS-API support
%bcond_without	ssl		# OpenSSL support
%bcond_without	lmdb		# LMDB storage support for addzone zones
%bcond_without	doh		# DNS over HTTPS support
%bcond_with	static_libs	# static libraries
%bcond_with	system_tests	# system tests (require root to configure localhost IPs)
%bcond_with	tests		# unit tests
%bcond_with	edns_cli	# ability to use edns-client-subnet in dig
%bcond_with	hip		# HIP RR support

%if "%{pld_release}" == "ac"
%bcond_with	epoll		# enable epoll support
# there didn't exist x86_64 2.4 kernel in PLD, so can safely enable epoll
%ifarch %{x8664}
%define		with_epoll	1
%endif
%else
%bcond_without	epoll		# disable epoll support
%endif

Summary:	BIND - DNS name server
Summary(de.UTF-8):	BIND - DNS-Namenserver
Summary(es.UTF-8):	BIND - Servidor de nombres DNS
Summary(fr.UTF-8):	BIND - serveur de noms DNS
Summary(pl.UTF-8):	BIND - serwer nazw DNS
Summary(pt_BR.UTF-8):	BIND - Servidor de nomes DNS
Summary(ru.UTF-8):	BIND - cервер системы доменных имен (DNS)
Summary(tr.UTF-8):	DNS alan adı sunucusu
Summary(uk.UTF-8):	BIND - cервер системи доменних імен (DNS)
Summary(zh_CN.UTF-8):	Internet 域名服务器
Name:		bind
Version:	9.20.11
Release:	1
Epoch:		7
License:	MPL 2.0
Group:		Networking/Daemons
Source0:	https://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	84b6a72244271f0d79bc6922cf7e7ed9
Source1:	named.init
Source2:	named.sysconfig
Source3:	named.logrotate
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	35b1dfaa12615c9802126ee833e0e7f7
Source6:	%{name}-hip.tar.gz
# Source6-md5:	62a8a67f51ff8db9fe815205416a1f62
Source7:	https://www.internic.net/domain/named.root
# Source7-md5:	65c48192c7ee264a34dd469f88c6c160
Source8:	%{name}-127.0.0.zone
Source9:	%{name}-localhost.zone
Source10:	%{name}-named.conf
Source11:	%{name}.tmpfiles
Source12:	named.service

Patch3:		jemalloc.patch
Patch4:		%{name}-ac-libs.patch
Patch5:		%{name}-edns-client-subnet.patch
URL:		https://www.isc.org/software/bind
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bison
%{?with_tests:BuildRequires:	cmocka-devel >= 1.1.3}
BuildRequires:	flex
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	jemalloc-devel
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	libatomic-devel
BuildRequires:	libcap-devel
BuildRequires:	libidn2-devel
# note, there is no kyua in PLD yet (work in progress)
%{?with_tests:%{!?with_system_tests:BuildRequires:	kyua}}
BuildRequires:	libtool
BuildRequires:	libuv-devel >= 1.40.0
# any version for hi2dns (if with_hip), 2.6.0 for XML stats
BuildRequires:	libxml2-devel >= 1:2.6.0
%{?with_lmdb:BuildRequires:	lmdb-devel}
%{?with_geoip:BuildRequires:	libmaxminddb-devel}
%{?with_doh:BuildRequires:	nghttp2-devel >= 1.6.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 1.0.0}
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	readline-devel
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	userspace-rcu-devel >= 0.13.0
BuildRequires:	xz
BuildRequires:	zlib-devel
%if %{with dnstap}
BuildRequires:	fstrm-devel
BuildRequires:	protobuf-c-devel
%endif
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	fileutils
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	psmisc >= 20.1
Requires:	rc-scripts >= 0.2.0
Requires:	systemd-units >= 38
Requires:	uname(release) >= 2.2.18
Provides:	group(named)
Provides:	nameserver
Provides:	user(named)
Obsoletes:	caching-nameserver
Obsoletes:	openldap-schema-bind < 7:9.18.0
Obsoletes:	python3-isc < 7:9.18.0
Conflicts:	bind-chroot
Conflicts:	logrotate < 3.8.0
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

%package plugins
Summary:	Plugins for Bind DNS name server
Summary(pl.UTF-8):	Wtyczki dla serwera nazw DNS Bind
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugins
Plugins for extending of query processing functionality of Bind DNS name
server.

%description plugins -l pl.UTF-8
Wtyczki rozszerzające funkcjonalność przetwarzania zapytań przez serwer
nazw DNS Bind.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de.UTF-8):	DNS-Utils - Host, Dig, Dnsquery, Nslookup
Summary(es.UTF-8):	Utilitarios DNS - host, dig, dnsquery y nslookup
Summary(fr.UTF-8):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl.UTF-8):	Narzędzia DNS - host, dig, dnsquery, nslookup
Summary(pt_BR.UTF-8):	Utilitários DNS - host, dig, dnsquery e nslookup
Summary(ru.UTF-8):	Утилиты для посылки запросов к серверам DNS
Summary(tr.UTF-8):	DNS araçları - host, dig, dnsquery, nslookup
Summary(uk.UTF-8):	Утиліти для надсилання запитів до серверів DNS
Summary(zh_CN.UTF-8):	Internet 域名服务器实用工具
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
Summary(pl.UTF-8):	Biblioteki DNS
Summary(ru.UTF-8):	Библиотеки, необходимые для bind
Summary(uk.UTF-8):	Бібліотеки, необхідні для bind
Summary(zh_CN.UTF-8):	Internet 域名服务器开发库
Group:		Libraries
Requires:	json-c >= 0.11
Requires:	libuv >= 1.40.0
Requires:	libxml2 >= 1:2.6.0
%{?with_doh:Requires:	nghttp2-libs >= 1.6.0}

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
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para desarrollo DNS
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek DNS
Summary(pt_BR.UTF-8):	Todos os arquivos de cabeçalho e bibliotecas para desenvolvimento DNS
Summary(ru.UTF-8):	Хедеры и библиотеки разработчика для bind
Summary(uk.UTF-8):	Хедери та бібліотеки програміста для bind
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
The bind-devel package contains all the include files and symlinks
required for DNS (Domain Name Service) development for BIND.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind-libs.

%description devel -l es.UTF-8
Los archivos de inclusión y bibliotecas necesarios al desarrollo DNS
para el bind.

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
Summary(pl.UTF-8):	Biblioteki statyczne DNS
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento DNS
Summary(ru.UTF-8):	Статические библиотеки разработчика для bind
Summary(uk.UTF-8):	Статичні бібліотеки програміста для bind
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
%setup -q %{?with_hip:-a6}

%patch -P3 -p1
%patch -P4 -p1
%{?with_hip:%{__mv} bind-hip/hip_55.[ch] lib/dns/rdata/generic}
%{?with_edns_cli:%patch -P5 -p0}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CFLAGS="-D_GNU_SOURCE=1 %{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	%{?with_dnstap:--enable-dnstap} \
	--enable-dnsrps \
	%{!?with_doh:--disable-doh} \
	%{!?with_epoll:--disable-epoll --disable-devpoll} \
	--enable-full-report \
	--enable-largefile \
	%{?with_static_libs:--enable-static} \
	%{?with_kerberos5:--with-gssapi} \
	--with-jemalloc=yes \
	--with-libidn2 \
	--with-libxml2 \
	%{?with_ssl:--with-openssl} \
	%{?with_geoip:--with-maxminddb} \
	--with-lmdb%{!?with_lmdb:=no} \
	--disable-silent-rules

%{__make}
%{__make} -C doc/arm html

%{?with_hip:%{__make} -C bind-hip}

%if %{with tests}
%if %{with system_tests}
%{__make} test-force
%else
sh unit/unittest.sh
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_sbindir},%{_includedir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3,5,8},%{_var}/{lib/named/{M,D,S,dev,etc},run/named,log}} \
	$RPM_BUILD_ROOT{%{systemdunitdir},%{systemdtmpfilesdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bind/filter-*.la

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.named-non-english-man-pages
%{__mv} $RPM_BUILD_ROOT%{_mandir}/ja/man8/nslookup.8 $RPM_BUILD_ROOT%{_mandir}/ja/man1/nslookup.1
%{__sed} -i -e 's/NSLOOKUP 8/NSLOOKUP 1/' $RPM_BUILD_ROOT%{_mandir}/ja/man1/nslookup.1

install -p %{SOURCE1}			$RPM_BUILD_ROOT/etc/rc.d/init.d/named
cp -p %{SOURCE2}			$RPM_BUILD_ROOT/etc/sysconfig/named
cp -p %{SOURCE3}			$RPM_BUILD_ROOT/etc/logrotate.d/named
cp -p %{SOURCE7}			$RPM_BUILD_ROOT%{_var}/lib/named/root.hint
cp -p %{SOURCE8}			$RPM_BUILD_ROOT%{_var}/lib/named/M/127.0.0.zone
cp -p %{SOURCE9}			$RPM_BUILD_ROOT%{_var}/lib/named/M/localhost.zone
cp -p %{SOURCE10}			$RPM_BUILD_ROOT%{_var}/lib/named%{_sysconfdir}/named.conf

ln -sf --relative $RPM_BUILD_ROOT%{_var}/lib/named%{_sysconfdir}/named.conf $RPM_BUILD_ROOT/etc/named.conf
ln -sf --relative $RPM_BUILD_ROOT%{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
ln -sf --relative $RPM_BUILD_ROOT%{_var}/lib/named/named.stats	$RPM_BUILD_ROOT%{_var}/log/named.stats

touch $RPM_BUILD_ROOT%{_var}/lib/named/named.{log,stats}

install %{SOURCE12} $RPM_BUILD_ROOT%{systemdunitdir}/named.service
install %{SOURCE11} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

%{?with_hip:install -p bind-hip/hi2dns $RPM_BUILD_ROOT%{_bindir}}

# we don't want Makefiles in documentation...
rm -rf _doc
cp -a doc _doc
%{__rm} _doc/misc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -f %{_sysconfdir}/named.boot ]; then
	cp -f %{_sysconfdir}/named.boot /etc/named.boot.2conf
	mv -f %{_sysconfdir}/named.boot /etc/named.rpmsave
	echo >&2 "Warning: %{_sysconfdir}/named.boot saved as /etc/named.rpmsave."
fi
%groupadd -g 58 named
%useradd -u 58 -g 58 -d /tmp -s /bin/false -c "BIND user" named

%post
/sbin/chkconfig --add named
%service named restart
%systemd_post named.service

%preun
if [ "$1" = "0" ]; then
	%service named stop
	/sbin/chkconfig --del named
fi
%systemd_preun named.service

%postun
if [ "$1" = "0" ]; then
	%userremove named
	%groupremove named
fi
%systemd_reload

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%triggerpostun -- %{name} < 7:9.9.2.P2-2
%systemd_trigger named.service

%files
%defattr(644,root,root,755)
%doc README.md %{?with_hip:bind-hip/COPYRIGHT-HIP-RR}
%doc _doc/misc/* _doc/arm/_build/html/*.html

%{systemdunitdir}/named.service
%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/named
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/named
%{_sysconfdir}/named.conf

%attr(755,root,root) %{_bindir}/dnssec-*
%attr(755,root,root) %{_bindir}/named-*
%attr(755,root,root) %{_bindir}/nsec3hash
%attr(755,root,root) %{_sbindir}/ddns-confgen
%attr(755,root,root) %{_sbindir}/named
%attr(755,root,root) %{_sbindir}/rndc
%attr(755,root,root) %{_sbindir}/rndc-confgen
%attr(755,root,root) %{_sbindir}/tsig-keygen

%{_mandir}/man1/dnssec-*.1*
%{_mandir}/man1/named-*.1*
%{_mandir}/man1/nsec3hash.1*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man8/ddns-confgen.8*
%{_mandir}/man8/named.8*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/rndc-confgen.8*
%{_mandir}/man8/tsig-keygen.8*
%lang(ja) %{_mandir}/ja/man8/named*

%{systemdtmpfilesdir}/%{name}.conf

%attr(770,root,named) %dir %{_var}/lib/named
%attr(770,root,named) %dir %{_var}/lib/named/D
%attr(770,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(770,root,named) %dir %{_var}/lib/named/dev
%dev(c,1,9) %attr(644,root,root) %{_var}/lib/named/dev/urandom
%attr(750,root,named) %dir %{_var}/lib/named/etc
%attr(640,root,named) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named/etc/named.conf
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named/M/*.zone
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named/root.hint
%attr(660,named,named) %ghost %{_var}/lib/named/named.log
%attr(660,named,named) %ghost %{_var}/lib/named/named.stats

%config(noreplace,missingok) %{_var}/log/named
%config(noreplace,missingok) %{_var}/log/named.stats

%attr(770,root,named) %dir %{_var}/run/named

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/bind
%attr(755,root,root) %{_libdir}/bind/filter-a.so
%attr(755,root,root) %{_libdir}/bind/filter-aaaa.so
%{_mandir}/man8/filter-a.8*
%{_mandir}/man8/filter-aaaa.8*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arpaname
%attr(755,root,root) %{_bindir}/delv
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/named-rrchecker
%attr(755,root,root) %{_bindir}/mdig
%attr(755,root,root) %{_bindir}/nslookup
%attr(755,root,root) %{_bindir}/nsupdate
%{?with_hip:%attr(755,root,root) %{_bindir}/hi2dns}
%{_mandir}/man1/arpaname.1*
%{_mandir}/man1/delv.1*
%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
%{_mandir}/man1/mdig.1*
%{_mandir}/man1/named-rrchecker.1*
%{_mandir}/man1/nslookup.1*
%{_mandir}/man1/nsupdate.1*

%lang(fi) %{_mandir}/fi/man1/host.1*

%lang(fr) %{_mandir}/fr/man1/host.1*

%lang(hu) %{_mandir}/hu/man1/host.1*

%lang(ja) %{_mandir}/ja/man1/dig.1*
%lang(ja) %{_mandir}/ja/man1/host.1*
%lang(ja) %{_mandir}/ja/man1/nslookup.1*
%lang(ja) %{_mandir}/ja/man8/nsupdate.8*

%lang(pl) %{_mandir}/pl/man1/host.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns-%{version}.so
%attr(755,root,root) %{_libdir}/libisc-%{version}.so
%attr(755,root,root) %{_libdir}/libisccc-%{version}.so
%attr(755,root,root) %{_libdir}/libisccfg-%{version}.so
%attr(755,root,root) %{_libdir}/libns-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns.so
%attr(755,root,root) %{_libdir}/libisc.so
%attr(755,root,root) %{_libdir}/libisccc.so
%attr(755,root,root) %{_libdir}/libisccfg.so
%attr(755,root,root) %{_libdir}/libns.so
%{_libdir}/libdns.la
%{_libdir}/libisc.la
%{_libdir}/libisccc.la
%{_libdir}/libisccfg.la
%{_libdir}/libns.la
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/irs
%{_includedir}/isc
%{_includedir}/isccc
%{_includedir}/isccfg
%{_includedir}/ns

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdns.a
%{_libdir}/libisc.a
%{_libdir}/libisccc.a
%{_libdir}/libisccfg.a
%{_libdir}/libns.a
%endif
