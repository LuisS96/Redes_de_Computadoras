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
  
### DNS Server
#### Theory

#### Installation Guide

### Web Server
#### Theory

#### Installation Guide

### Email Server
#### Theory

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

If an error appears, do not worry and run the following command lines:
```
cd /tmp
wget https://git.ispconfig.org/ispconfig/ispconfig3/raw/stable-3.1/helper_scripts/ubuntu-amavisd-new-2.11.patch
cd /usr/sbin
cp -pf amavisd-new amavisd-new_bak
patch < /tmp/ubuntu-amavisd-new-2.11.patch
```

The mail server installation and configuration is completed!

### DBS Server
#### Theory

#### Installation Guide

### FTP Server
#### Theory

#### Installation Guide

### Video Streaming Server
#### Theory

#### Installation Guide
