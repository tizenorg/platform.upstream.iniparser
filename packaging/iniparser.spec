Name:           iniparser
Version:        2.17
Release:        3
License:        MIT
Summary:        Stand-alone ini file parsing library
Url:            http://ndevilla.free.fr/iniparser/
Group:          System/Libraries
Source:         http://ndevilla.free.fr/iniparser/iniparser-%{version}.tar.gz
Source1001:     %{name}.manifest

%description
iniparser is a free stand-alone ini file parsing library.
It is written in portable ANSI C and should compile anywhere.
iniparser is distributed under an MIT license.

%package devel
Summary:        Development tools for stand-alone ini file parsing library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.

%prep
%setup -q
cp %{SOURCE1001} .

%build
make prefix=%{_prefix}  %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"

%install

mkdir -p %{buildroot}/%{_libdir}
install -m 755 libiniparser.so.0 %{buildroot}/%{_libdir}
ln -s libiniparser.so.0 %{buildroot}/%{_libdir}/libiniparser.so
mkdir -p %{buildroot}/%{_includedir}
install -m 644 src/*.h %{buildroot}/%{_includedir}
install -m 644 src/*.h %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat > %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc <<EOF
prefix = %{_prefix}
exec_prefix = %{_exec_prefix}
libdir = %{_libdir}
includedir = %{_includedir}

Name : iniparser
Description : a free stand-alone ini file parsing library.
Version : %{version}
Libs : -L\${libdir} -liniparser
Cflags : -I\${includedir}

EOF
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
