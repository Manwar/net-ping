# Automatically generated by Net-Ping.spec.PL
%define perlmod Net-Ping
Summary:	%{perlmod} perl module
Name:		perl-%{perlmod}
Version:	2.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org./authors/id/B/BB/BBB/%{perlmod}-%{version}.tar.gz
Packager:	Rob Brown <rob@roobik.com>
BuildRequires:	perl
Requires:	perl
BuildRoot:	/var/tmp/%{name}-%{version}-root
Provides:	%{perlmod}

%description
%{perlmod} Perl Module

%prep
%setup -q -n %{perlmod}-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
# Just a hack to let this version override the default
eval `perl -V:installarchlib`
mkdir -p $RPM_BUILD_ROOT$installarchlib/Net
cp Ping.pm $RPM_BUILD_ROOT$installarchlib/Net/.
echo $installarchlib/Net/*.pm > %{name}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-filelist
%defattr(-,root,root)

%post

%changelog
* Thu Nov 15 2001 Rob Brown <rob@roobik.com>
- initial creation
