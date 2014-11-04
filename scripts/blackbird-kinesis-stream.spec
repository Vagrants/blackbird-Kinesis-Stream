%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name blackbird-kinesis-stream
%define version 0.1.0
%define unmangled_version %{version}
%define release 1%{dist}
%define include_dir /etc/blackbird/conf.d
%define plugins_dir /opt/blackbird/plugins

Summary: Blackbird plugin Kinesis Stream
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: WTFPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vagrants <vagrants@gmail.com>
Packager: Vagrants <vagrants@gmail.com>
Requires: blackbird python-boto
Url: https://github.com/Vagrants/blackbird-kinesis-stream
BuildRequires:  python-setuptools

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install -dm 0755 $RPM_BUILD_ROOT%{include_dir}
install -dm 0755 $RPM_BUILD_ROOT%{plugins_dir}
install -p -m 0644 scripts/kinesis-stream.cfg $RPM_BUILD_ROOT%{include_dir}/kinesis-stream.cfg
install -p -m 0644 kinesis_stream.py $RPM_BUILD_ROOT%{plugins_dir}/kinesis_stream.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%config(noreplace) %{include_dir}/kinesis-stream.cfg
%{plugins_dir}/kinesis_stream.*

%changelog
* Tue Nov 4 2014 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.1.0-1
- Initial package
