Name:           sugar-logos
Version:        3
Release:        14%{?dist}
Summary:        Boot splash imagery for Sugar on a Stick

Group:          System Environment/Base
License:        GPLv2+
URL:            http://git.sugarlabs.org/projects/sugar-logos
Source0:        http://download.sugarlabs.org/sources/external/sugar-logos/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  plymouth-theme-charge
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

cp %{_datadir}/plymouth/themes/charge/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar


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
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 26 2010 Sebastian Dziallas <sebastian@when.com> 3-3
- include correct files for new release

* Mon Apr 26 2010 Sebastian Dziallas <sebastian@when.com> 3-2
- make sure to pull complete theme in

* Fri Apr  2 2010 Peter Robinson <pbrobinson@gmail.com> 3-1
- New upstream release for Mirabelle

* Fri Mar 19 2010 Sebastian Dziallas <sebastian@when.com> 2-3
- make sure to have correct config file naming

* Sat Feb 27 2010 Sebastian Dziallas <sebastian@when.com> 2-2
- activate the new theme too
- add authors file

* Wed Feb 17 2010 Sebastian Dziallas <sebastian@when.com> 2-1
- initial packaging
