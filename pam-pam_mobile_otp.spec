%define		modulename pam_mobile_otp
Summary:	Mobile-OTP PAM module
Summary(pl.UTF-8):	Moduł PAM Mobile-OTP
Name:		pam-%{modulename}
Version:	0.6.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://motp.sourceforge.net/%{modulename}-%{version}.tgz
# Source0-md5:	28a2239d5b7afdec8437c4cbca4b7417
Patch0:		%{modulename}-DESTDIR.patch
URL:		http://motp.sourceforge.net/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mobile One Time Passwords - strong, two-factor authentication with
mobile phones.

%prep
%setup -q -n %{modulename}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/lib/security/,/etc/security,/var/cache/motp}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install motp.conf $RPM_BUILD_ROOT/etc/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README MOTP.html

%attr(755,root,root) /lib/security/pam_mobile_otp.so
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/motp.conf
%attr(750,root,root) %dir /var/cache/motp
