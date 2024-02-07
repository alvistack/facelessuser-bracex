# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-bracex
Epoch: 100
Version: 2.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Bash style brace expansion for Python
License: MIT
URL: https://github.com/facelessuser/bracex/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Bracex is a brace expanding library for Python. Brace expanding is used
to generate arbitrary strings.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-bracex
Summary: Bash style brace expansion for Python
Requires: python3
Provides: python3-bracex = %{epoch}:%{version}-%{release}
Provides: python3dist(bracex) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-bracex = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(bracex) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-bracex = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(bracex) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-bracex
Bracex is a brace expanding library for Python. Brace expanding is used
to generate arbitrary strings.

%files -n python%{python3_version_nodots}-bracex
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-bracex
Summary: Bash style brace expansion for Python
Requires: python3
Provides: python3-bracex = %{epoch}:%{version}-%{release}
Provides: python3dist(bracex) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-bracex = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(bracex) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-bracex = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(bracex) = %{epoch}:%{version}-%{release}

%description -n python3-bracex
Bracex is a brace expanding library for Python. Brace expanding is used
to generate arbitrary strings.

%files -n python3-bracex
%license LICENSE.md
%{python3_sitelib}/*
%endif

%changelog
