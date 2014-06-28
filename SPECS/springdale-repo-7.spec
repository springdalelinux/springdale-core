%{!?repo:%define repo core}

Summary: yum %{repo} repository configuration file
Name: springdale-%{repo}
Version: 7
Release: 1.sdl7.1
Group: System Environment/Base 
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: yum springdale-release /etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
%if "%{repo}" != "core"
Requires: springdale-core
%if "%{repo}" != "addons" && "%{repo}" != "DevToolset"
Requires: springdale-addons
%endif
%define base %{nil}
%else
%define base _Base
%endif
%if  "%{repo}" == "DevToolset"
%define base _Base
%endif

%description
This rpm contains yum %{repo} repository configuration file.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/

%undefine base_repo
%undefine updates_repo
%undefine debuginfo_repo
%undefine debuginfoupdates_repo
%undefine source_repo
%undefine sourceupdates_repo
%define repo_name %{repo}


%if "%{repo_name}" == "core"
echo "core"
%define base_repo http://springdale.princeton.edu/data/springdale/\\$releasever/\\$basearch/os
%define updates_repo http://springdale.princeton.edu/data/springdale/updates/\\$releasever/en/os/\\$basearch
%define debuginfo_repo http://springdale.princeton.edu/data/springdale/\\$releasever/\\$basearch/debug/os
%define debuginfoupdates_repo http://springdale.princeton.edu/data/springdale/updates/\\$releasever/en/os/debug/\\$basearch
%define source_repo http://springdale.princeton.edu/data/springdale/\\$releasever/source/os
%define sourceupdates_repo http://springdale.princeton.edu/data/springdale/updates/\\$releasever/en/os/SRPMS
%undefine repo_name
%endif

%if "%{repo_name}" == "addons"
echo "addons"
%define base_repo http://springdale.princeton.edu/data/springdale/\\$releasever/\\$basearch/os/Addons
%define updates_repo http://springdale.princeton.edu/data/springdale/updates/\\$releasever/en/%{repo}/\\$basearch
%undefine repo_name
%endif

%if "%{repo_name}" == "buildsys"
echo "buildsys"
%define base_repo http://springdale.princeton.edu/data/springdale/%{repo}/\\$releasever/os/\\$basearch
%undefine repo_name
%endif

%if %{?repo_name:1}0
%define base_repo http://springdale.princeton.edu/data/springdale/%{repo}/\\$releasever/\\$basearch
echo "other %{repo}"
%endif


%if %{?base_repo:1}0
cat > $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}.repo <<ENDREPO
[Springdale_%{version}_%{repo}%{base}]
name=Springdale %{repo} Base \$releasever - \$basearch
mirrorlist=%{base_repo}/mirrorlist
#baseurl=%{base_repo}
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%if %{?updates_repo:1}0
cat >> $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}.repo <<ENDREPO

[Springdale_%{version}_%{repo}_Updates]
name=Springdale %{repo} Updates \$releasever - \$basearch
mirrorlist=%{updates_repo}/mirrorlist
#baseurl=%{updates_repo}
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%if %{?debuginfo_repo:1}0
cat > $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}-debug.repo <<ENDREPO
[Springdale_%{version}_%{repo}_Base-debuginfo]
name=Springdale %{repo} Base \$releasever Debuginfo - \$basearch
mirrorlist=%{debuginfo_repo}/mirrorlist
#baseurl=%{debuginfo_repo}
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%if %{?debuginfoupdates_repo:1}0
cat >> $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}-debug.repo <<ENDREPO

[Springdale_%{version}_%{repo}_Updates-debuginfo]
name=Springdale %{repo} Updates \$releasever Debuginfo - \$basearch
mirrorlist=%{debuginfoupdates_repo}/mirrorlist
#baseurl=%{debuginfoupdates_repo}
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%if %{?source_repo:1}0
cat > $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}-source.repo <<ENDREPO
[Springdale_%{version}_%{repo}_Base_Source]
name=Springdale %{repo} Base \$releasever SRPMS - \$basearch
mirrorlist=%{source_repo}/mirrorlist
#baseurl=%{source_repo}
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%if %{?sourceupdates_repo:1}0
cat >> $RPM_BUILD_ROOT/etc/yum.repos.d/springdale-%{version}-%{repo}-source.repo <<ENDREPO

[Springdale_%{version}_%{repo}_Updates_Source]
name=Springdale %{repo} Updates \$releasever SRPMS - \$basearch
mirrorlist=%{sourceupdates_repo}/mirrorlist
#baseurl=%{sourceupdates_repo}
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-springdale
ENDREPO
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/springdale*

%changelog
* Fri Jun 27 2014 Josko Plazonic <plazonic@princeton.edu>
- initial version for sdl7

* Tue May 27 2014 Josko Plazonic <plazonic@princeton.edu>
- change repoid of debuginfo repos which will make yum-utils happy

* Mon Feb 25 2013 Josko Plazonic <plazonic@math.princeton.edu>
- move to springdale

* Thu Mar 29 2012 Thomas Uphill <uphill@ias.edu>
- rewriting the if statements to make it more readable.
- adding buildsys

* Mon Nov 29 2010 Thomas Uphill <uphill@ias.edu>
- adding mirrorlist for all repos

* Tue Nov 16 2010 Josko Plazonic <plazonic@math.princeton.edu>
- initial build for PUIAS 6

* Tue Jul 17 2007 Josko Plazonic <plazonic@math.princeton.edu>
- variant for unsupported repo

* Mon Mar 26 2007 Josko Plazonic <plazonic@math.princeton.edu>
- first build
