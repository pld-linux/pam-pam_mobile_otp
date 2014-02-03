%define		modulename pam_mobile_otp
Summary:	Mobile-OTP PAM module
Summary(pl.UTF-8):	Moduł PAM Mobile-OTP
Name:		pam-%{modulename}
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://motp.sourceforge.net/%{modulename}-%{version}.tgz
# Source0-md5:	972e6fdd2f785b6f779dd9823118f5f2
Patch0:		%{modulename}-DESTDIR.patch
URL:		http://motp.sourceforge.net/
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mobile One Time Passwords - strong, two-factor authentication with
mobile phones.

%prep
%setup -qc
mv %{modulename}/* .
%patch0 -p1

%{__sed} -i -e 's,gcc,$(CC),' Makefile

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib}/security,/etc/security,/var/cache/motp}
%{__make} install \
	LIB=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

cp -p motp.conf $RPM_BUILD_ROOT/etc/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README MOTP.html
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/motp.conf
%attr(755,root,root) /%{_lib}/security/pam_mobile_otp.so
%attr(750,root,root) %dir /var/cache/motp
