Summary:	BIND - DNS name server
Summary(de):	BIND - DNS-Namenserver  
Summary(fr):	BIND - serveur de noms DNS
Summary(pl):	BIND - serwer nazw DNS
Summary(tr):	DNS alan ad� sunucusu
Name:		bind
Version:	8.2.1
Release:	1
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}-src.tar.gz
Source1:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}-doc.tar.gz
Source2:	ftp://ftp.isc.org/isc/bind/%{version}/%{name}-%{version}-contrib.tar.gz
Source3:	named.init
Source4:	named.sysconfig
Source5:	named.logrotate
Source6:	named.conf
Patch1:		bind-pselect.patch
Patch2:		bind-fds.patch
Patch3:		bind-nonlist.patch
Patch5:		bind-host.patch
Patch6:		bind-glibc21.patch
Patch8:		bind-mkdep.patch
Prereq:		/sbin/chkconfig
Obsoletes:      caching-nameserver
URL:		http://www.isc.org/bind.html
Buildroot:	/tmp/%{name}-%{version}-root

%define		_datadir	%{_prefix}/share/misc
%define		_sysconfdir	/etc

%description
Includes the named name server, which is used to define host name
to IP address translations (and vice versa).  It can be used on
workstations as a caching name server, but is generally only needed
on one machine for an entire network.

%description -l de
Enth�lt den Namen-Server, der zum Umwandeln von Host-Namen in
IP-Adressen und umgekehrt verwendet wird. Er kann auf
Workstations als caching Namen-Server verwendet werden, ist aber
i.d.R. nur auf einem Recher des Netzwerks erforderlich.

%description -l fr
Contient le serveur de noms named, utilis� pour d�finir les traductions
nom d'h�te vers adresse IP (et vice versa). Il peut �tre utilis� sur
les stations de travail comme serveur de nom en cache mais n'est souvent
n�cessaire que sur une machine pour un r�seau entier.

%description -l pl
Pakiet ten zawiera demona named, kt�ry s�u�y do zmieniania nazw
komputer�w na numery IP i odwrotnie. Mo�e by� on u�ywany na stacjach
roboczych jako bufor odwo�a� do serwisu nazw (caching name server), ale
generalnie wystarczy tylko jedna jednostka wyposa�ona w ten program na
fragment sieci.

%description -l tr
Bu paket, makina ad�n� IP numaras�na (ya da tersi) �evirmek i�in kullan�lan
alan ad� sunucusunu i�erir. �� istasyonlar�nda bir �nbellek isim sunucusu
olarak da kullan�labilir ama genellikle b�t�n bir a� i�in sadece bir makina
�zerinde kurulur.

%package	utils
Summary:	DNS utils - host, dig, dnsquery, nslookup
Summary(de):	DNS-Utils - Host, Dig, Dnsquery, Nslookup 
Summary(fr):	Utilitaires DNS - host, dig, dnsquery, nslookup
Summary(pl):	Narz�dzia DNS - host, dig, dnsquery, nslookup
Summary(tr):	DNS ara�lar� - host, dig, dnsquery, nslookup
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia

%description utils
Collection of utilities for querying name servers and looking up hosts.
These tools let you determine the IP addresses for given host names,
and find information about registered domains and network addresses.

%description -l de utils
Dienstprogrammsammlung zum Abfragen von Namen-Servern und Hosts.
Diese Tools bestimmen die IP-Adresse eines angegebenen Host-Namen
und finden Informationen �ber registrierte Domains und Netzwerk-Adressen.

%description -l fr utils
Ensemble d'utilitaires pour interroger les serveurs de noms et rechercher
des h�tes. Ces outils vous permettent de d�terminer les adresses IP pour
des noms d'h�tes donn�s, et trouver des informations sur les noms de
domaine d�clar�s et les adresses r�seau.

%description -l pl utils
Pakiet ten zawiera zbi�r aplikacji umo�liwiaj�cych odpytywanie serwer�w
nazw z innych domen w celu uzyskania informacji o komupterach i ich
adresach IP.

%description -l tr utils
Bu pakette isim sunucular�n� sorgulamak ve makina adreslerini ��zmek i�in
kullan�lan ara�lar bulunmaktad�r.

%package	devel
Summary:	DNS development includes and libs
Summary(pl):	Pliki nag��wkowe i biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
All the include files and the library required for DNS development for
bind 8.x.x

%description -l pl devel
Pakiet zawiera pliki nag��wkowe i bibliotek� statyczn�. Je�eli b�dziesz
pisa� programy pod binda, lub kompilowa� kod �r�d�owy oprogramowania
korzystaj�cego z tych plik�w nag��wkowych czy biblioteki powiniene�
zainstalowa� ten pakiet.

%package	doc
Summary:	Bind documentation
Summary(pl):	Dokumentacja programu bind
Group:		Documentation
Group(pl):	Dokumentacja

%description doc
Bind documentations

%decscription doc -l pl
Dokumentacja programu bind

%prep
%setup -q -n src -a 1 -a 2

%patch1 -p1
%patch2 -p2
%patch3 -p1
%patch5 -p2
%patch6 -p2
%patch8 -p1

%build
rm -f compat/include/sys/cdefs.h
make \
	clean \
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
	$RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},%{_mandir}/man{1,3,5,7,8}}

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

install bin/named/test/127.*    $RPM_BUILD_ROOT/var/state/named/M
install bin/named/test/loca*    $RPM_BUILD_ROOT/var/state/named/M
install conf/workstation/root.* $RPM_BUILD_ROOT/var/state/named/root.hint
install %{SOURCE6}              $RPM_BUILD_ROOT/etc

cp bin/named/named.conf EXAMPLE-CONFIG

install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/named
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/named
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/named
touch $RPM_BUILD_ROOT/var/log/named

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[13578]/* \
	README Version CHANGES EXAMPLE-CONFIG 

%pre
if [ -f /etc/named.boot ]
	cp /etc/named.boot /etc/named.boot.2conf
	mv -f /etc/named.boot /etc/named.rpmsave
	echo "Warrnig: /etc/named.boot saved as /etc/named.rpmsave" 1>&2
fi

%post
/sbin/chkconfig --add named

if [ -f /var/run/named.pid ]; then
	/etc/rc.d/init.d/named restart >&2
else
	echo "Type \'/etc/rc.d/init.d/named  start\' to start named" 1>&2
fi

if [ -f /etc/named.boot.2conf ]
	/usr/sbin/named-bootconf </etc/named.boot.2conf >/etc/named.conf
	rm /etc/named.boot.2conf
fi

umask 137
/bin/touch /var/log/named

%preun
if [ $1 = 0 ]; then
	/etc/rc.d/init.d/named stop >&2
	/sbin/chkconfig --del named
fi    

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Version,CHANGES,EXAMPLE-CONFIG}.gz

%attr(755,root,root) /etc/rc.d/init.d/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/named
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/named.conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/logrotate.d/named

%attr(755,root,root) %{_sbindir}/named
%attr(755,root,root) %{_sbindir}/named-xfer
%attr(755,root,root) %{_sbindir}/ndc
%attr(755,root,root) %{_sbindir}/irpd
%attr(755,root,root) %{_sbindir}/dnskeygen
%attr(755,root,root) %{_sbindir}/named-bootconf
%attr(755,root,root) %{_bindir}/nsupdate

%{_mandir}/man8/named.8.gz
%{_mandir}/man8/ndc.8.gz
%{_mandir}/man8/named-xfer.8.gz
%{_mandir}/man8/named-bootconf.8.gz
%{_mandir}/man7/hostname.7.gz
%{_mandir}/man5/irs.conf.5.gz
%{_mandir}/man5/named.conf.5.gz
%{_mandir}/man1/dnskeygen.1.gz

%attr(750,root,root) %dir /var/state/named
%attr(750,root,root) %dir /var/state/named/M
%attr(750,root,root) %dir /var/state/named/S

/var/state/named/M/*
/var/state/named/root.*

%attr(640,root,root) %ghost /var/log/named

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dig
%attr(755,root,root) %{_bindir}/host
%attr(755,root,root) %{_bindir}/dnsquery
%attr(755,root,root) %{_bindir}/nslookup

%attr(644,root,root) %{_datadir}/nslookup.help

%{_mandir}/man1/dig.1.gz
%{_mandir}/man1/host.1.gz
%{_mandir}/man1/dnsquery.1.gz
%{_mandir}/man8/nslookup.8.gz
%{_mandir}/man5/resolver.5.gz

%files devel
%defattr(644,root,root,755)

%{_includedir}/bind
%{_libdir}/*.a
%{_mandir}/man3/*

%files doc
%defattr(644,root,root,755)
%doc doc/html doc/rfc doc/misc doc/notes

%changelog
* Mon May 31 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- FHS 2.0 -- build prepare for Ra 

* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
  [8.2-7]
- upgrade to 8.2
- fixed group for devel subpackage
- removed named-bootconf.pl (non exist)
- symplifikation in %files

* Wed Jan 13 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [8.1.2-3d]
- removed Requires: %{name} = %{version} from utils sub-package,
- compressed man pages,
- added Group(pl),
- minor changes.

* Tue Sep  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.1.2-2d]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using $RPM_OPT_FLAGS during compile (modified bind-makefile.patch),

* Wed Aug 26 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [8.1.2-1d]
- translation modified for pl,
- major changes -- needed for Linux PLD,
- start at RH spec file.
