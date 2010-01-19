# TODO
# - apply http://www.caraytech.com/geodns/
#
# Conditional build:
%bcond_without	ssl		# build without OpenSSL support
%bcond_without	ipv6		# build without IPv6 support
%bcond_without	ldap		# build without LDAP support
%bcond_without	kerberos5	# build without kerneros5 support
%bcond_without	sql		# build without SQL support
%bcond_without	static_libs	# build without static libraries
%bcond_without	tests		# perform tests
%bcond_with	hip		# build with HIP RR support
#
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
%define	ver		9.6.1
%define	plev	P3
Name:		bind
Version:	%{ver}.%{plev}
Release:	1
Epoch:		7
License:	BSD-like
Group:		Networking/Daemons
Source0:	ftp://ftp.isc.org/isc/bind9/%{ver}-%{plev}/%{name}-%{ver}-%{plev}.tar.gz
# Source0-md5:	a0952d589b3051538033387be4c983f9
Source1:	named.init
Source2:	named.sysconfig
Source3:	named.logrotate
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	35b1dfaa12615c9802126ee833e0e7f7
Source5:	http://www.venaas.no/ldap/bind-sdb/dnszone-schema.txt
# Source5-md5:	49fe799c6eca54ae227b22d57ebc1145
Source6:	%{name}-hip.tar.gz
# Source6-md5:	62a8a67f51ff8db9fe815205416a1f62
Source7:	ftp://rs.internic.net/domain/named.root
# Source7-md5:	a94e29ac677846f3d4d618c50b7d34f1
Source8:	%{name}-127.0.0.zone
Source9:	%{name}-localhost.zone
Source10:	%{name}-named.conf
Patch0:		%{name}-time.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-pmake.patch
Patch3:		%{name}-sdb-ldap.patch
URL:		https://www.isc.org/software/bind
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	idnkit-devel
%{?with_kerberos5:BuildRequires:	heimdal-devel}
%{?with_hip:BuildRequires:	libxml2-devel}
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_sql:BuildRequires:	mysql-devel}
%{?with_sql:BuildRequires:	postgresql-devel}
%{?with_sql:BuildRequires:	unixODBC-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
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
Provides:	group(named)
Provides:	nameserver
Provides:	user(named)
Obsoletes:	caching-nameserver
Conflicts:	%{name}-chroot
Conflicts:	kernel < 2.2.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		schemadir	/usr/share/openldap/schema

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

%package -n openldap-schema-bind
Summary:	BIND schema for openldap
Summary(pl.UTF-8):	Schemat BIND dla openldap
Group:		Development/Libraries
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers
Requires:	sed >= 4.0

%description -n openldap-schema-bind
BIND schema for openldap.

%description -n openldap-schema-bind -l pl.UTF-8
Schemat BIND dla openldap.

%prep
%setup -q %{?with_hip:-a6} -n %{name}-%{ver}-%{plev}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_ldap:%patch3 -p1}
%{?with_hip:mv bind-hip/hip_55.[ch] lib/dns/rdata/generic}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	CFLAGS="-D_GNU_SOURCE=1" \
	--with-idn \
	--with-libtool \
	%{?with_ssl:--with-openssl=%{_prefix}} \
	%{?with_ipv6:--enable-ipv6} \
	%{?with_kerberos5:--with-gssapi} \
	%{?with_sql:--with-dlz-postgres=yes} \
	%{?with_sql:--with-dlz-mysql=yes} \
	--with-dlz-bdb=no \
	--with-dlz-filesystem=yes \
	%{?with_ldap:--with-dlz-ldap=yes} \
	--with-dlz-odbc=no \
	--with-dlz-stub=yes \
	--enable-largefile \
	%{!?with_static_libs:--enable-static=no} \
	--enable-threads \
	--enable-getifaddrs

%{__make}
%{?with_hip:cd bind-hip/; %{__make}}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_sbindir},%{_includedir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3,5,8},%{_var}/{lib/named/{M,D,S,dev,etc},run/{named,lwresd},log}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_mandir}/ja/man8/nslookup.8 $RPM_BUILD_ROOT%{_mandir}/ja/man1/nslookup.1
%{__perl} -pi -e 's/NSLOOKUP 8/NSLOOKUP 1/' $RPM_BUILD_ROOT%{_mandir}/ja/man1/nslookup.1

install bin/tests/named.conf		EXAMPLE-CONFIG-named
install bin/tests/ndc.conf		EXAMPLE-CONFIG-ndc
install %{SOURCE1}			$RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/logrotate.d/named
install %{SOURCE7}			$RPM_BUILD_ROOT%{_var}/lib/named/root.hint
install %{SOURCE8}			$RPM_BUILD_ROOT%{_var}/lib/named/M/127.0.0.zone
install %{SOURCE9}			$RPM_BUILD_ROOT%{_var}/lib/named/M/localhost.zone
install %{SOURCE10}			$RPM_BUILD_ROOT%{_var}/lib/named%{_sysconfdir}/named.conf

ln -sf %{_var}/lib/named%{_sysconfdir}/named.conf $RPM_BUILD_ROOT/etc/named.conf
ln -sf %{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
ln -sf %{_var}/lib/named/named.stats	$RPM_BUILD_ROOT%{_var}/log/named.stats

touch $RPM_BUILD_ROOT%{_var}/lib/named/named.{log,stats}

%if %{with ldap}
install -d $RPM_BUILD_ROOT%{schemadir}
install %{SOURCE5} $RPM_BUILD_ROOT%{schemadir}/dnszone.schema
%endif

%{?with_hip:install bind-hip/hi2dns $RPM_BUILD_ROOT%{_bindir}}

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/named-compilezone.8
echo ".so man8/named-checkzone.8" > $RPM_BUILD_ROOT%{_mandir}/man8/named-compilezone.8

# let rpm generate deps (workaround -m644 used for libs installation)
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*.*

# we don't want Makefiles in documentation...
rm -rf _doc
cp -a doc _doc
rm -f _doc/rfc/rfc*
rm -f _doc/misc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -f %{_sysconfdir}/named.boot ]; then
	cp -f %{_sysconfdir}/named.boot /etc/named.boot.2conf
	mv -f %{_sysconfdir}/named.boot /etc/named.rpmsave
	echo "Warning: %{_sysconfdir}/named.boot saved as /etc/named.rpmsave." 1>&2
fi
%groupadd -g 58 named
%useradd -u 58 -g 58 -d /tmp -s /bin/false -c "BIND user" named

%post
/sbin/chkconfig --add named
%service named restart

%preun
if [ "$1" = "0" ]; then
	%service named stop
	/sbin/chkconfig --del named
fi

%postun
if [ "$1" = "0" ]; then
	%userremove named
	%groupremove named
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post -n openldap-schema-bind
%openldap_schema_register %{schemadir}/dnszone.schema
%service -q ldap restart

%postun -n openldap-schema-bind
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/dnszone.schema
	%service -q ldap restart
fi

%triggerpostun -- %{name} < 7:9.4.2-2
/sbin/chkconfig named reset
#triggerpostun -- %{name} < 6:9.4.1
sed -i -e 's#^\([ \t]*category[ \t]\+cname[ \t]\+.*\)$#// \1#g' /var/lib/named/etc/named.conf
sed -i -e 's#^\([ \t]*category[ \t]\+response-checks[ \t]\+.*\)$#// \1#g' /var/lib/named/etc/named.conf
sed -i -e 's#^\([ \t]*category[ \t]\+load[ \t]\+.*\)$#// \1#g' /var/lib/named/etc/named.conf

%files
%defattr(644,root,root,755)
%doc README EXAMPLE-CONFIG-* FAQ %{?with_hip:bind-hip/COPYRIGHT-HIP-RR}
%doc _doc/misc/* _doc/arm/*.html _doc/rfc/index %{?with_ldap:_doc/*.sdb-ldap}

%attr(754,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/named.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man8/dns*
%{_mandir}/man8/lwres*
%{_mandir}/man8/named*
%{_mandir}/man8/rndc*
%{_mandir}/man5/rndc*
%{_mandir}/man5/named.conf*
%lang(ja) %{_mandir}/ja/man8/named*

%attr(770,root,named) %dir %{_var}/lib/named
%attr(770,root,named) %dir %{_var}/lib/named/D
%attr(750,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(750,root,named) %dir %{_var}/lib/named%{_sysconfdir}

%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named/M/*
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named/root.*
%attr(640,root,named) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/named%{_sysconfdir}/*
%attr(660,named,named) %config(noreplace,missingok) %verify(not md5 mtime size) %{_var}/log/named*
%attr(660,named,named) %ghost  %{_var}/lib/named/named.log
%attr(660,named,named) %ghost  %{_var}/lib/named/named.stats

%attr(770,root,named) %dir %{_var}/run/named
%attr(770,root,named) %dir %{_var}/run/lwresd

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/nslookup
%attr(755,root,root) %{_bindir}/nsupdate
%{?with_hip:%attr(755,root,root) %{_bindir}/hi2dns}
%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
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
%attr(755,root,root) %{_libdir}/libbind9.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbind9.so.[0-9][0-9]
%attr(755,root,root) %{_libdir}/libdns.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdns.so.[0-9][0-9]
%attr(755,root,root) %{_libdir}/libisc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisc.so.[0-9][0-9]
%attr(755,root,root) %{_libdir}/libisccc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisccc.so.[0-9][0-9]
%attr(755,root,root) %{_libdir}/libisccfg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisccfg.so.[0-9][0-9]
%attr(755,root,root) %{_libdir}/liblwres.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblwres.so.[0-9][0-9]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isc-config.sh
%attr(755,root,root) %{_libdir}/libbind9.so
%attr(755,root,root) %{_libdir}/libdns.so
%attr(755,root,root) %{_libdir}/libisc.so
%attr(755,root,root) %{_libdir}/libisccc.so
%attr(755,root,root) %{_libdir}/libisccfg.so
%attr(755,root,root) %{_libdir}/liblwres.so
%{_libdir}/libbind9.la
%{_libdir}/libdns.la
%{_libdir}/libisc.la
%{_libdir}/libisccc.la
%{_libdir}/libisccfg.la
%{_libdir}/liblwres.la
%{_includedir}/bind9
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/isc
%{_includedir}/isccc
%{_includedir}/isccfg
%{_includedir}/lwres
%{_mandir}/man1/isc-config.sh.1*
%{_mandir}/man3/lwres*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbind9.a
%{_libdir}/libdns.a
%{_libdir}/libisc.a
%{_libdir}/libisccc.a
%{_libdir}/libisccfg.a
%{_libdir}/liblwres.a
%endif

%if %{with ldap}
%files -n openldap-schema-bind
%defattr(644,root,root,755)
%{_datadir}/openldap/schema/dnszone.schema
%endif
