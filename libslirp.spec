%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		libslirp
Version:	4.4.0
Release:	1
Summary:	A general purpose TCP-IP emulator
Group:		System/Libraries
# check the SPDX tags in source files for details
License:	BSD and MIT
URL:		https://gitlab.freedesktop.org/slirp/%{name}
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  glib2-devel

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

#---------------------------------------------------------------------
%package -n %{libname}
Summary:	A general purpose TCP-IP emulator
Group:		System/Libraries

%description -n %{libname}
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

#---------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Provides:	slirp-devel = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{devname}
%dir %{_includedir}/slirp/
%{_includedir}/slirp/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/slirp.pc

#---------------------------------------------------------------------

%prep
%autosetup -S git_am

%build
%meson
%meson_build

%install
%meson_install
