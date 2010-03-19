Name:           sugar-logos
Version:        2
Release:        3%{?dist}
Summary:        Boot splash imagery for Sugar on a Stick

Group:          System Environment/Base
License:        GPLv2+
URL:            http://git.sugarlabs.org/projects/sugar-logos
Source0:        http://download.sugarlabs.org/sources/external/sugar-logos/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       plymouth
Requires:       plymouth-plugin-two-step

%description
A boot splash screen for Sugar using Plymouth.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
for i in src/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
done


%clean
rm -rf $RPM_BUILD_ROOT


%post
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme sugar
else
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme sugar
    fi
fi


%postun
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "sugar" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/plymouth/themes/sugar/


%changelog
* Fri Mar 19 2010 Sebastian Dziallas <sebastian@when.com> 2-3
- make sure to have correct config file naming

* Sat Feb 27 2010 Sebastian Dziallas <sebastian@when.com> 2-2
- activate the new theme too
- add authors file

* Wed Feb 17 2010 Sebastian Dziallas <sebastian@when.com> 2-1
- initial packaging
