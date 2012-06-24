Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(es):	BIND - Servidor de nombres DNS
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(pt_BR):	BIND - Servidor de nomes DNS
Summary(tr):	DNS alan ad� sunucusu
Name:		bind
Version:	9.2.0
Release:	4
Epoch:		5
License:	BSD Like
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-conf.tar.gz
Source2:	named.init
Source3:	named.sysconfig
Source4:	named.logrotate
Source5:	nslookup.8
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch1:		%{name}-time.patch
Patch2:		%{name}-autoconf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	openssl-devel 
BuildRequires:	sed
Prereq:		rc-scripts >= 0.2.0
Prereq:		/sbin/chkconfig
Prereq:		%{name}-libs
Requires:	%{name}-libs = %{version}
Requires:	psmisc >= 20.1
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
Enth�lt den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf Workstations als
caching Namen-Server verwendet werden, ist aber i.d.R. nur auf einem
Recher des Netzwerks erforderlich.

%description -l es
Incluye el servidor de nombres (DNS), que se usa para traducir nombres
para IP (y viceversa). Puede ser usado en estaciones de trabajo como
un servidor de nombres cach�, pero generalmente s�lo hace falta en una
m�quina para toda la red.

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

%description -l pt_BR
Inclui o servidor de nomes (DNS), que � usado para traduzir nomes para
IP (e vice-versa). Pode ser usado em esta��es de trabalho como um
servidor de nomes cache, mas geralmente s� � necess�rio em uma m�quina
para toda a rede.

%description -l tr
Bu paket, makina ad�n� IP numaras�na (ya da tersi) �evirmek i�in
kullan�lan alan ad� sunucusunu i�erir. �� istasyonlar�nda bir �nbellek
isim sunucusu olarak da kullan�labilir ama genellikle b�t�n bir a�
i�in sadece bir makina �zerinde kurulur.

%package utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(es):	Utilitarios DNS - host, dig, dnsquery y nslookup
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narz�dzia DNS - host, dig, dnsquery, nslookup
Summary(pt_BR):	Utilit�rios DNS - host, dig, dnsquery e nslookup
Summary(tr):	DNS ara�lar� - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
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
Informationen �ber registrierte Domains und Netzwerk-Adressen.

%description -l es utils
Conjunto de utilitarios para consulta a servidores de nombres. Estas
herramientas permiten la determinaci�n de direcciones IP para nombres
de m�quinas informados y busca informaci�n sobre dominios registrados
y direcciones de red.

%description -l fr utils
Ensemble d'utilitaires pour interroger les serveurs de noms et
rechercher des h�tes. Ces outils vous permettent de d�terminer les
adresses IP pour des noms d'h�tes donn�s, et trouver des informations
sur les noms de domaine d�clar�s et les adresses r�seau.

%description -l pl utils
Pakiet ten zawiera zbi�r aplikacji umo�liwiaj�cych odpytywanie
serwer�w nazw z innych domen w celu uzyskania informacji o komputerach
i ich adresach IP.

%description -l pt_BR utils
Conjunto de utilit�rios para consulta a servidores DNS. Estas
ferramentas permitem a determina��o de endere�os IP para nomes de
m�quinas informados e busca informa��es sobre dom�nios registrados e
endere�os de rede. Voc� deveria instalar este pacote se necessitar
obter informa��es de servidores DNS.

%description -l tr utils
Bu pakette isim sunucular�n� sorgulamak ve makina adreslerini ��zmek
i�in kullan�lan ara�lar bulunmaktad�r.

%package libs
Summary:	DNS libraries
Summary(pl):	Biblioteki DNS
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����

%description libs
The bind-libs package contains all libraries required for running BIND
and bind utils.

%description -l pl libs
Pakiet zawiera wszystkie biblioteki potrzebne do uruchomienia binda
lub program�w z pakietu bind-utils.

%package devel
Summary:	DNS development includes
Summary(es):	Archivos de inclusi�n y bibliotecas para desarrollo DNS
Summary(pl):	Pliki nag��wkowe bibliotek DNS
Summary(pt_BR):	Todos os arquivos de cabe�alho e bibliotecas para desenvolvimento DNS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}

%description devel
The bind-devel package contains all the include files and symlinks
required for DNS (Domain Name Service) development for BIND.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll also need to install
bind-libs.

%description -l es devel
Todos los archivos de inclusi�n y bibliotecas necesarios al desarrollo
DNS para el bind.

%description -l pl devel
Pakiet zawiera pliki nag��wkowe. Je�eli b�dziesz pisa� programy pod
binda, lub kompilowa� kod �r�d�owy oprogramowania korzystaj�cego z
tych plik�w nag��wkowych czy biblioteki powiniene� zainstalowa� ten
pakiet.

%description -l pt_BR devel
Todos os arquivos de cabe�alho e bibliotecas necess�rios para o
desenvolvimento com o bind.

%package static
Summary:	DNS static libs
Summary(pl):	Biblioteki statyczne DNS
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento DNS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static bind libraries.

%description -l pl static
Statyczne biblioteki binda.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento DNS.

%prep
%setup -q -a1
%patch1 -p1
%patch2 -p1

%build
libtoolize --copy --force
aclocal
autoconf
cd lib/bind
libtoolize --copy --force
aclocal
autoconf
cd ../..
%configure \
	--with-openssl=%{_prefix} \
	--with-libtool \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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
install conf-pld/*.conf			$RPM_BUILD_ROOT%{_var}/lib/named/etc
install bin/tests/named.conf		EXAMPLE-CONFIG-named
install bin/tests/ndc.conf		EXAMPLE-CONFIG-ndc
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE4}			$RPM_BUILD_ROOT/etc/logrotate.d/named
ln -sf %{_var}/lib/named/etc/named.conf $RPM_BUILD_ROOT%{_sysconfdir}/named.conf
ln -sf %{_var}/lib/named/named.log	$RPM_BUILD_ROOT%{_var}/log/named
ln -sf %{_var}/lib/named/named.stats	$RPM_BUILD_ROOT%{_var}/log/named.stats
touch		$RPM_BUILD_ROOT%{_var}/lib/named/{named.{log,stats},dev/{random,null}}

gzip -9nf README EXAMPLE-CONFIG-* FAQ doc/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

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
	/etc/rc.d/init.d/named restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/named start\" to start named" 1>&2
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
	%{_sbindir}/userdel named
	%{_sbindir}/groupdel named
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/misc/*.gz doc/arm/*.html

%attr(754,root,root)  /etc/rc.d/init.d/named
%attr(640,root,root)  %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/named.conf
%attr(640,root,root)  %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/nsupdate

%{_mandir}/man8/dns*
%{_mandir}/man8/lwres*
%{_mandir}/man8/named*
%{_mandir}/man8/rndc*
%{_mandir}/man5/rndc*
%{_mandir}/man8/nsupdate*
%lang(ja) %{_mandir}/ja/man8/named*

%attr(770,root,named) %dir %{_var}/lib/named
%attr(750,root,named) %dir %{_var}/lib/named/M
%attr(770,root,named) %dir %{_var}/lib/named/S
%attr(770,root,named) %dir %{_var}/lib/named/dev

%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/M/*
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/root.*
%attr(640,root,named) %config(noreplace) %verify(not size mtime md5) %{_var}/lib/named/etc/*

%ghost %{_var}/lib/named/dev/*
%attr(660,named,named) %ghost %{_var}/log/named*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/nslookup
%{_mandir}/man1/dig.1*
%{_mandir}/man1/host.1*
%{_mandir}/man8/nslookup.8*

%lang(fi) %{_mandir}/fi/man1/host.1*

%lang(fr) %{_mandir}/fr/man1/host.1*

%lang(hu) %{_mandir}/hu/man1/host.1*

%lang(ja) %{_mandir}/ja/man1/dig.1*
%lang(ja) %{_mandir}/ja/man1/host.1*
%lang(ja) %{_mandir}/ja/man8/nslookup.8*

%lang(pl) %{_mandir}/pl/man1/host.1*

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
