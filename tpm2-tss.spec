%define major 0
%define libtss2_mu %mklibname tss2-mu %{major}
%define libtss2_sys %mklibname tss2-sys %{major}
%define libtss2_esys %mklibname tss2-esys %{major}
%define libtss2_rc %mklibname tss2-rc %{major}
%define libtss2_tctildr %mklibname tss2-tctildr %{major}
%define libtss2_tcti_d %mklibname tss2-tcti-device %{major}
%define libtss2_tcti_m %mklibname tss2-tcti-mssim %{major}
%define develname %mklibname %{name} -d

%define udevrules_prefix 60-

Name:		tpm2-tss
Version:	2.4.3
Release:	1
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
# The entire source code is under BSD except implementation.h and tpmb.h which
# is under TCGL(Trusted Computing Group License).
License:	BSD and TCGL
URL:		https://github.com/tpm2-software/tpm2-tss
Source0:	https://github.com/tpm2-software/tpm2-tss/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.conf

BuildRequires:	doxygen
BuildRequires:	autoconf-archive
BuildRequires:	libtool
BuildRequires:	systemd-macros
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libcurl)

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_mu}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_mu}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_sys}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_sys}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_esys}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_esys}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_rc}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_rc}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tctildr}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_tctildr}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_d}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_tcti_d}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_m}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_tcti_m}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libtss2_mu} = %{EVRD}
Requires:	%{libtss2_sys} = %{EVRD}
Requires:	%{libtss2_esys} = %{EVRD}
Requires:	%{libtss2_rc} = %{EVRD}
Requires:	%{libtss2_tctildr} = %{EVRD}
Requires:	%{libtss2_tcti_d} = %{EVRD}
Requires:	%{libtss2_tcti_m} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1

%build
# Use built-in tpm-udev.rules, with specified installation path and prefix.
%configure \
	--disable-static \
	--disable-silent-rules \
	--with-udevrulesdir=%{_udevrulesdir} \
	--with-udevrulesprefix=%{udevrules_prefix}

%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

# create tss user and group (mga#24457)
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_udevrulesdir}/%{udevrules_prefix}tpm-udev.rules
%{_sysusersdir}/%{name}.conf

%files -n %{libtss2_mu}
%{_libdir}/libtss2-mu.so.%{major}{,.*}

%files -n %{libtss2_sys}
%{_libdir}/libtss2-sys.so.%{major}{,.*}

%files -n %{libtss2_esys}
%{_libdir}/libtss2-esys.so.%{major}{,.*}

%files -n %{libtss2_rc}
%{_libdir}/libtss2-rc.so.%{major}{,.*}

%files -n %{libtss2_tctildr}
%{_libdir}/libtss2-tctildr.so.%{major}{,.*}

%files -n %{libtss2_tcti_d}
%{_libdir}/libtss2-tcti-device.so.%{major}{,.*}

%files -n %{libtss2_tcti_m}
%{_libdir}/libtss2-tcti-mssim.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/tss2/
%{_libdir}/libtss2-mu.so
%{_libdir}/libtss2-sys.so
%{_libdir}/libtss2-esys.so
%{_libdir}/libtss2-rc.so
%{_libdir}/libtss2-tctildr.so
%{_libdir}/libtss2-tcti-default.so
%{_libdir}/libtss2-tcti-device.so
%{_libdir}/libtss2-tcti-mssim.so
%{_libdir}/pkgconfig/tss2-mu.pc
%{_libdir}/pkgconfig/tss2-sys.pc
%{_libdir}/pkgconfig/tss2-esys.pc
%{_libdir}/pkgconfig/tss2-rc.pc
%{_libdir}/pkgconfig/tss2-tctildr.pc
%{_libdir}/pkgconfig/tss2-tcti-device.pc
%{_libdir}/pkgconfig/tss2-tcti-mssim.pc
%{_mandir}/man3/*.3.*
%{_mandir}/man7/tss2*.7.*
