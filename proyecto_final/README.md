# Multi-Server Setup
A DNS, Web, Email, FTP, Database, and Video Streaming server. An all-in-one server.

## Prerequisites
  - Ubuntu 18.04 (Bionic Beaver)
  
## Preinstallation
Be sure to have the latest OS update by writing the following command lines
```
sudo apt-get install update -y
sudo apt-get install upgrade -y
reboot
```

In order to successfully setup a multi-server, some changes need to be made
1. Run as root
```
sudo -s
```
Add the root's credentials.

2. Stop using dash as the default system shell
Run `dpkg-reconfigure dash` and respond the next question `Use dash as the default system shell (/bin/sh)?` by writing `No`.

3. Disable AppArmor
This is an extended security which is not needed, therefore run the next code block:
```
service apparmor stop
update-rc.d -f apparmor remove
apt-get remove apparmor apparmor-utils
```


## Theory and Installation Guide
  - DNS Server
  - Web Server
  - Email Server
  - DBS Server
  - FTP Server
  - Video Streaming Server
  - ISPConfig 3.1 (Only Installation Guide)
  
### DNS Server
#### Theory
The DNS (Domain Name System) main objective is to create a link between the human readable network address name and its machine numerical address. The DNS is managed by the ICANN (Internet Corporation for Assigned Names and Numbers), which uses a hierarchical addressing system to prevent confusion between sites.In theory, the Internet is divided into +250 top-level domains, and each one of those is partitioned into more subdomains.

In this project, the open source software BIND will be implemented in order to our own Domain Name System.  BIND provides the software and protocols necessary to answer name service questions.

#### Installation Guide
BIND needs to installed as follows:
```
apt-get -y install bind9 dnsutils haveged
```

Enable and start the haveged Daemon:
```
systemctl enable haveged
systemctl start haveged
```

The DNS server installation and configuration is complete!


### Web Server
#### Theory
When the term “Web Server” is brought up, it often refers to a physical machine that is interconnected to an architectural framework that correlates millions of machines all over the world. This framework is called the World Wide Web, it consists of a vast collection of content, mostly in the form of Web Pages, that make use of the HyperText Transfer Protocol (HTTP) to convey graphical information to the user. This are the bases of the Internet, allowing the interconnection of any given machine to the rest of the web. The concept of Web Server can be interpreted as the hardware or the software.

Referring to the hardware, a Web Server is a computer that’s connected to the Internet. It stores the software and the respective website information and files. 

On the other hand, the Web Server software includes the actual system of the website. It must be able to understand web addresses and protocols such as HTTP. It can be accessed via domain names, and it delivers their content to the end user. 

The Web Servers can be classified into two categories, static and dynamic. A static web server just sends its files to every client uniformly. However, a dynamic server can differentiate between users and updates the files before sending them to the end user.

Every web server performs the following main loop when accessed by a client:
- Accept a TCP connection from a client.
- Retrieve the name file requested, which is dictated by the path.
- Retrieve the actual file from disk.
- Send the contents of the file to the client (this may change depending on the web server type).
- Release the TCP connection.

An important feature of a web server is that it can only serve a single request at a time, this is solved via multithreading. This feature allows several clients to be connected to the same server.

#### Installation Guide
The install of Apache, PHP, PHPMyAdmin, FCGI, SuExec, Pear, and mcrypt is needed, therefore run the following code bliock:
```
apt-get -y install apache2 apache2-doc apache2-utils libapache2-mod-php php7.2 php7.2-common php7.2-gd php7.2-mysql php7.2-imap phpmyadmin php7.2-cli php7.2-cgi libapache2-mod-fcgid apache2-suexec-pristine php-pear mcrypt  imagemagick libruby libapache2-mod-python php7.2-curl php7.2-intl php7.2-pspell php7.2-recode php7.2-sqlite3 php7.2-tidy php7.2-xmlrpc php7.2-xsl memcached php-memcache php-imagick php-gettext php7.2-zip php7.2-mbstring php-soap php7.2-soap
```
Apache 2.4, Php7.2 and the latest versions of the others packages were installed.

Answer the following questions as shown:
```
Web server to reconfigure automatically: apache2 (To select apache2 press Space and then Enter)
Configure database for phpmyadmin with dbconfig-common? Yes
MySQL application password for phpmyadmin: (Press Enter)
```

The modules suexec, rewrite, ssl, actions, and include need to be enabled:
```
a2enmod suexec rewrite ssl actions include cgi
```
```
a2enmod dav_fs dav auth_digest headers
```

In the effort to ensure no vulnerabilities, the HTTP_PROXY header needs to be disabled and to do so, run the following command lines:
The httpoxy.conf file needs to be created
```
nano /etc/apache2/conf-available/httpoxy.conf
```

Add this content in the file:
```
<IfModule mod_headers.c>
  RequestHeader unset Proxy early
</IfModule>
```

Enable the config file by running:
```
a2enconf httpoxy
```

Than restart apache:
```
service restart apache2
```

PHP-FPM needs to be installed as follows:
```
apt-get -y install php7.2-fpm
```

And enabled:
```
a2enmod actions proxy_fcgi alias
service restart apache2
```

To add some features to the website, install Let's Encrypt and Mailman:
To install Let's Encrypt:
```
apt-get -y install certbot
```

To install Mailman:
```
apt-get -y install mailman
```

Answer the following questions as shown:
```
Languages to support: en (English)
Missing site list: Ok
```

Before starting Mailman, the mailing list _mailman_ needs to be created:
```
newlist mailman
```

And do as follows:
```
Enter the email of ht person runnin the list: admin@yourdomain.com
Initial mailman password: (Admin password)
Hit enter to notify mailman owner... (Press Enter)
```

Open the file `/etc/aliases` by running the following command line:
```
nano /etc/aliases
```

And add the following code block:
```
...
## mailman mailing list
mailman:              "|/var/lib/mailman/mail/mailman post mailman"
mailman-admin:        "|/var/lib/mailman/mail/mailman admin mailman"
mailman-bounces:      "|/var/lib/mailman/mail/mailman bounces mailman"
mailman-confirm:      "|/var/lib/mailman/mail/mailman confirm mailman"
mailman-join:         "|/var/lib/mailman/mail/mailman join mailman"
mailman-leave:        "|/var/lib/mailman/mail/mailman leave mailman"
mailman-owner:        "|/var/lib/mailman/mail/mailman owner mailman"
mailman-request:      "|/var/lib/mailman/mail/mailman request mailman"
mailman-subscribe:    "|/var/lib/mailman/mail/mailman subscribe mailman"
mailman-unsubscribe:  "|/var/lib/mailman/mail/mailman unsubscribe mailman"
```

Run
```
newaliases
```

And restart Postfix:
```
service restart postfix
```

Afterward Mailman configuration needs to be enabled:
```
ln -s /etc/mailman/apache.conf /etc/apache2/conf-available/mailman.conf
```

The configuration needs to be activated:
```
a2enconf mailman
```

Restart Apache:
```
service restart apache2
```

Start the Mailman daemon:
```
service mailman start
```

### Email Server
#### Theory
The term “Email Server” refers to a computer dedicated to handle and distribute incoming mail to it’s local users, and send outgoing messages. This type of server uses the Simple Mail Transfer Protocol (SMTP) to create a client-server application model. This model consists of two kinds of subsystems, the user agents and the message transfer agents. The user agents allow the user to send and read email, and the message transfer agents move the messages throughout the web from source to destination. 

The process of handling an outgoing email can be divided into six steps:
- Once the mail is composed, the email client connects to the SMTP server.
- The SMTP server receives the client’s email; address, the recipient's email address, the body of the message, and any files attached to the mail.
- The SMTP server communicates to the recipient's email address corresponding Domain Name Server.
- The Domain Name Server takes the recipient's email domain name and translates it into an IP address and sends it to the sender’s SMTP server.
- Now, the SMTP server connects to the recipient's SMTP server and sends the actual message.
- The recipient's SMTP server reads the message and directs it to the corresponding user. At this point, the message can be viewed by the recipient.


#### Installation Guide
The install of Postfix, Dovecot, MariaDB, rkhunter, and binutils is needed, therefore run the following code bliock:
```
apt-get -y install postfix postfix-mysql postfix-doc mariadb-client mariadb-server openssl getmail4 rkhunter binutils dovecot-imapd dovecot-pop3d dovecot-mysql dovecot-sieve dovecot-lmtpd
```

The following questions need to be answered as shown:
When asked for a subdomain as 'system mail name' use your domain (e.g., ns1.yourdomain.com) and not as an email domain (e.g., mail.domain.com):
```
General type of mail configuration: Internet Site
System mail name: ns1.domain.com
```

Open the next file by running this command:
```
nano /etc/postfix/master.cf
```

Now, uncomment the _sumbission_ and _smtps_ sections as shown in the code block:
```
...
submission inet n       -       y       -       -       smtpd
  -o syslog_name=postfix/submission
  -o smtpd_tls_security_level=encrypt
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_client_restrictions=permit_sasl_authenticated,reject
#  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
#  -o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
#  -o milter_macro_daemon_name=ORIGINATING
smtps     inet  n       -       y       -       -       smtpd
  -o syslog_name=postfix/smtps
  -o smtpd_tls_wrappermode=yes
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_client_restrictions=permit_sasl_authenticated,reject
#  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
#  -o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
#  -o milter_macro_daemon_name=ORIGINATING
...
```

Now restart Postfix:
```
service restart postfix
```

Roundube Webmail will be installed for a better user interface, run the following code block:
```
apt-get -y install roundcube roundcube-core roundcube-mysql roundcube-plugins javascript-common libjs-jquery-mousewheel php-net-sieve tinymc
```

Answer the question as follows:
```
Configure database for roundcube with dbconfig-common? Yes
MySQL application password for roundcube: (Press Enter)
```

Opem the RoundCube configuration file:
```
nano /etc/apache2/conf-enabled/roundcube.conf
```

Edit the file by removing the '#' in front of the Alias line and add the the next lines as follows:
```
# Those aliases do not work properly with several hosts on your apache server
# Uncomment them to use it or adapt them to your configuration
Alias /roundcube /var/lib/roundcube
Alias /webmail /var/lib/roundcube
...
<Directory /var/lib/roundcube>
AddType application/x-httpd-php .php
...
```

Restart Apache:
```
service restart apache2
```

Edit the RoundCube config.inc.php configuration file:
```
nano /etc/roundcube/config.inc.php
```

And change the default host to localhost:
```
$config['default_host'] = 'localhost';
```

The mail server installation and configuration is complete!


### DBS Server
#### Theory

#### Installation Guide
MySQL was previously installed with Postfix, we will now continue from that point.

To make MySQL listen all interfaces and not only 'localhost', it is needed to run the folowwing:
```
nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

And comment the line `bind-address = 127.0.0.1` shown as next:
```
...
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
#bind-address           = 127.0.0.1

...
```

A root password is needed for MySQL
```
mysql_secure_installation
```

The following answers need to be answered as next
```
Enter current password for root (enter for none: (Press Enter)
Set root password? [Y/n]: y
New password: (Enter the new password for root)
Re-enter new password: (Repeat the password)
Remove anonymous users? [Y/n]: y
Disallow root login remotely? [Y/n]: y
Reload privilage tables now? [Y/n]: y
````

Set the password authentication to use PHPMyAdmin to connect as root:
```
echo "update mysql.user set plugin = 'mysql_native_password' where user='root';" | mysql -u root
```

Also, run the follow command line to set the password for root shown in the next code block
```
nano /etc/mysql/debian.cnf
```
```
# Automatically generated for Debian scripts. DO NOT TOUCH!
[client]
host = localhost
user = root
password = (password)
socket = /var/run/mysqld/mysqld.sock
[mysql_upgrade]
host = localhost
user = root
password = (password)
socket = /var/run/mysqld/mysqld.sock
basedir = /usr
```

MySQL service needs to be restarted:
```
service restart mysql
```

To install Amavisd-new, SpamAssassin, and Clamav run the following command line:
```
apt-get -y install amavisd-new spamassassin clamav clamav-daemon unzip bzip2 arj nomarch lzop cabextract apt-listchanges libnet-ldap-perl libauthen-sasl-perl clamav-docs daemon libio-string-perl libio-socket-ssl-perl libnet-ident-perl zip libnet-dns-perl postgrey
```

Although SpamAssassin has just been installed, momentarily SpamAssasin can be stopped as next:
```
service stop spamassassin
update-rc.d -f spamassassin remove
```

To start ClamAV, run:
```
freshclam
service start clamav-daemon
```

If an error appears, do not worry, run the following command lines:
```
cd /tmp
wget https://git.ispconfig.org/ispconfig/ispconfig3/raw/stable-3.1/helper_scripts/ubuntu-amavisd-new-2.11.patch
cd /usr/sbin
cp -pf amavisd-new amavisd-new_bak
patch < /tmp/ubuntu-amavisd-new-2.11.patch
```

The database server installation and configuration is complete!


### FTP Server
#### Theory
The File Transfer Protocol (FTP) is a set of rules that machines use to transfer files over a TCP/IP network. These kind of servers are machines dedicated to receiving an FTP connection from FTP clients. In order to access the files of a FTP server, most of the time, a username and a password must be provided to the server, ensuring a somewhat secure server. Once the access is granted, the client can ask for a certain file in the server’s memory, or it request permission for uploading a local file.

Most of FTP servers provides us with a user friendly graphic interface, instead of a command-line interface. This allowed the improvement of the general access to information on the Web.  

#### Installation Guide
PureFTPd and Quota needs to be installed, run the following code block:
```
apt-get -y install pure-ftpd-common pure-ftpd-mysql quota quotatool
```

Ensure the start mode is set correctly when editing the file `/etc/default/pure-ftpd-common`, to do it run the next command line:
```
nano /etc/default/pure-ftpd-common
```
```
...
STANDALONE_OR_INETD=standalone
...
VIRTUALCHROOT=true
...
```

To allow FTP and TLS sessions, run the next command line:
```
echo 1 > /etc/pure-ftpd/conf/TLS
```

Yet, an SSL certificate is needed to use TLS.
```
mkdir -p /etc/ssl/private/
```
```
openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -keyout /etc/ssl/private/pure-ftpd.pem -out /etc/ssl/private/pure-ftpd.pem
```

And answer as shown the next questions:
```
Country Name (2 letter code) [AU]: (Enter Country Name)
State or Province Name (full name) [Some-State]: (Enter State or Province Name)
Locality Name (eg, city) []: (Enter City)
Organization Name (eg, company) [Internet Widgits Pty Ltd]: (Enter Organization Name)
Organization Unit Name (eg, section) []: (Enter Organizational Unit Name)
Common Name (eg, YOUR name) []: (Enter the FullyQualifiedDomainName (FQDN) (eg, "ns1.yourdomain.com"))
Email Address []: (Enter Email Address)
```

Change the SSL certificate permissions:
```
chmod 600 /etc/ssl/private/pure-ftpd.pem
```

Restart PureFTPd:
```
service restart pure-ftpd-mysql
```

To establish quota, be sure to add the command lines needed as shown:
```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point> <type> <options> <dump> <pass>
/dev/mapper/server1--vg-root / ext4 errors=remount-ro,usrjquota=quota.user,grpjquota=quota.group,jqfmt=vfsv0 0 1
/dev/mapper/server1--vg-swap_1 none swap sw 0 0
/dev/fd0 /media/floppy0 auto rw,user,noauto,exec,utf8 0 0
```

Run as follows to enable quota:
```
mount -o remount /
```

Be sure that no errors appear by running the next command lines:
```
quotacheck -avugm
quotaon -avug
```

The output should be as follows:
```
root@ns1:/opt/metronome# quotacheck -avugm
quotacheck: Scanning /dev/mapper/server1--vg-root [/] done
quotacheck: Cannot stat old user quota file //quota.user: No such file or directory. Usage will not be subtracted.
quotacheck: Cannot stat old group quota file //quota.group: No such file or directory. Usage will not be subtracted.
quotacheck: Cannot stat old user quota file //quota.user: No such file or directory. Usage will not be subtracted.
quotacheck: Cannot stat old group quota file //quota.group: No such file or directory. Usage will not be subtracted.
quotacheck: Checked 13602 directories and 96597 files
quotacheck: Old file not found.
quotacheck: Old file not found.
root@ns1:/opt/metronome# quotaon -avug
/dev/mapper/ns1--vg-root [/]: group quotas turned on
/dev/mapper/ns1--vg-root [/]: user quotas turned on
```

The FTP server installation and configuration is complete!

### Video Streaming Server
#### Theory
As the name implies, a Video Streaming Server creates a regular state of delivering video packets over the Internet to a certain user. 

#### Installation Guide
Plex Media Server will be installed, to do so, go to your browser and copy/paste at the URL this link
```
https://www.plex.tv/media-server-downloads/
```

Next, choose your right operating system - **`linux`**

Choose your right distribution - **`Ubuntu 14.04 or newer`**

Download the file and execute it after downloading, the video streaming server will get installed.

Afterwards, create a Plex Account at this link [Plex Media Server/Sign Up](https://app.plex.tv/auth#?forwardUrl=https%3A%2F%2Fwww.plex.tv%2Fsign-up%2F%3Ffa%3D1%26fasignup%3D1&clientID=6d9fc410-90bb-373d-f685-60bf2d98b9e7&&context%5Bdevice%5D%5Bproduct%5D=www.plex.tv&context%5Bdevice%5D%5Bplatform%5D=Firefox&context%5Bdevice%5D%5BplatformVersion%5D=63.0&context%5Bdevice%5D%5Bdevice%5D=OS%20X&signUp=1) and be sure at the settings section that you have a remote access to it.

The Video Streaming Server installation and configuration is complete!

### ISPConfig3.1
#### Installation Guide
To install ISPConfig3.1, run the following:
```
cd /tmp
wget -O ispconfig.tar.gz https://git.ispconfig.org/ispconfig/ispconfig3/repository/archive.tar.gz?ref=stable-3.1
tar xfz ispconfig.tar.gz
cd ispconfig3*/install/
```

Run ISPConfig3.1 to setup all the services that already installed, like Email, Web, etc.:
```
php -q install.php
```
Remember, do NOT press `Ctrl + C`, tap in `quit` to stop installer.

Answer as follows to setup Postgrey and Postfix:
```
Select language (en, de) [en]: (Press Enter)
Installation mode (standard, expert) [standard]: (Press Enter)
Full qualified hostname (FQDN) of the server, eg server1.domain.tld [server1.canomi.com]: (Press Enter)
MySQL server hostname [localhost]: (Press Enter)
MySQL server port [3306]: (Press Enter)
MySQL root username [root]: (Press Enter)
MySQL root password []: (Enter MySQL root password)
MySQL database to create [dbispconfig]: (Press Enter)
MySQL charset [utf8]: (Press Enter)
```

Answer as follows to setup Mailman, Dovecot, Amavisd, Getmail, BIND, PureFTPd, and Apache:
```
Country Name (2 letter code) [AU]: (Enter Country Code)
State or Province Name (full name) [Some-state]: (Enter State or Province Name)
Locality Name (eg, city) []: (Enter City Name)
Organization Name (eg, company) [Internet Widgits Pty Ltd]: (Enter Company Name)
Organizational Unit Name (eg, section) []: (Press Enter if none)
Common Name (e.g. server FQDN or YOUR name) []: (Enter your domain, e.g., ns1.yourdomain.com)
Email Address []: (Enter Email Address)
```

Answer as follows to setup Fail2Ban and ISPConfig:
```
Country Name (2 letter code) [AU]: (Enter Country Code)
Locality Name (eg, city) []: (Enter City Name)
Organization Name (eg, company) [Internet Widgits Pty Ltd]: (Enter Company Name)
Organizational Unit Name (eg, section) []: (Press Enter if none)
Common Name (e.g. server FQDN or YOUR name) []: (Enter your domain, e.g., ns1.yourdomain.com)
Email Address []: (Enter Email Address)
...
Do you want a secure (SSL) connection to the ISPConfig web interface (y,n) [Y]: (Press Enter)
```

Answer as follows to setup DBServer:
```
Country Name (2 letter code) [AU]: (Enter Country Code)
State or Province Name (full name) [Some-state]: (Enter State or Province Name)
Locality Name (eg, city) []: (Enter City Name)
Organization Name (eg, company) [Internet Widgits Pty Ltd]: (Enter Company Name)
Organizational Unit Name (eg, section) []: (Press Enter if none)
Common Name (e.g. server FQDN or YOUR name) []: (Enter your domain, e.g., ns1.yourdomain.com)
Email Address []: (Enter Email Address)

Please enter the following 'extra' attributes to be sent with your certificate request
A challenge password []: (Press Enter)
An optional company name []: (Press Enter)
```

ISPConfig3.1 install is complete. By logging in at the next URL https://ns1.yourdomain.com:8080/, one can access ISPConfig 3.
