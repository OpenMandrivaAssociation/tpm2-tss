%define major 0
%define oldlibtss2_mu %mklibname tss2-mu %{major}
%define oldlibtss2_sys %mklibname tss2-sys 1
%define oldlibtss2_esys %mklibname tss2-esys %{major}
%define oldlibtss2_fapi %mklibname tss2-fapi 1
%define oldlibtss2_rc %mklibname tss2-rc %{major}
%define oldlibtss2_tctildr %mklibname tss2-tctildr %{major}
%define oldlibtss2_tcti_d %mklibname tss2-tcti-device %{major}
%define oldlibtss2_tcti_m %mklibname tss2-tcti-mssim %{major}
%define oldlibtss2_tcti_c %mklibname tss2-tcti-cmd %{major}
%define oldlibtss2_tcti_p %mklibname tss2-tcti-pcap %{major}
%define oldlibtss2_tcti_s %mklibname tss2-tcti-swtpm %{major}
%define libtss2_mu %mklibname tss2-mu
%define libtss2_sys %mklibname tss2-sys
%define libtss2_esys %mklibname tss2-esys
%define libtss2_fapi %mklibname tss2-fapi
%define libtss2_rc %mklibname tss2-rc
%define libtss2_tctildr %mklibname tss2-tctildr
%define libtss2_tcti_d %mklibname tss2-tcti-device
%define libtss2_tcti_m %mklibname tss2-tcti-mssim
%define libtss2_tcti_c %mklibname tss2-tcti-cmd
%define libtss2_tcti_p %mklibname tss2-tcti-pcap
%define libtss2_tcti_s %mklibname tss2-tcti-swtpm
# (No old* bits for these libraries because they were added after
# versioning was fixed)
%define libtss2_policy %mklibname tss2-policy
%define libtss2_tcti_spi_helper %mklibname tss2-tcti-spi-helper

%define develname %mklibname %{name} -d

%define udevrules_prefix 60-

# Workaround for libtool thinking it has to inject an rpath
# at make install time (which clang doesn't like)
%if %{cross_compiling}
%define prefer_gcc 1
%endif

Name:		tpm2-tss
Version:	4.0.1
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
BuildRequires:	systemd-rpm-macros
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
%rename %{oldlibtss2_mu}

%description -n %{libtss2_mu}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_sys}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_sys}

%description -n %{libtss2_sys}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_esys}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_esys}

%description -n %{libtss2_esys}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_fapi}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_fapi}

%description -n %{libtss2_fapi}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.
#------------------------------------------------

%package -n %{libtss2_rc}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_rc}

%description -n %{libtss2_rc}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tctildr}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tctildr}

%description -n %{libtss2_tctildr}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_d}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tcti_d}

%description -n %{libtss2_tcti_d}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_m}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tcti_m}

%description -n %{libtss2_tcti_m}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_c}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tcti_c}

%description -n %{libtss2_tcti_c}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_p}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tcti_p}

%description -n %{libtss2_tcti_p}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_s}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}
%rename %{oldlibtss2_tcti_s}

%description -n %{libtss2_tcti_s}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_policy}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_policy}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

#------------------------------------------------

%package -n %{libtss2_tcti_spi_helper}
Summary:	TPM2.0 Software Stack
Group:		System/Libraries
Recommends:	%{name} >= %{EVRD}

%description -n %{libtss2_tcti_spi_helper}
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
Requires:	%{libtss2_fapi} = %{EVRD}
Requires:	%{libtss2_rc} = %{EVRD}
Requires:	%{libtss2_tctildr} = %{EVRD}
Requires:	%{libtss2_tcti_d} = %{EVRD}
Requires:	%{libtss2_tcti_m} = %{EVRD}
Requires:	%{libtss2_tcti_c} = %{EVRD}
Requires:	%{libtss2_tcti_p} = %{EVRD}
Requires:	%{libtss2_tcti_s} = %{EVRD}
Requires:	%{libtss2_policy} = %{EVRD}
Requires:	%{libtss2_tcti_spi_helper} = %{EVRD}
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
	--with-sysusersdir=%{_sysusersdir} \
	--with-tmpfilesdir=%{_tmpfilesdir} \
	--with-runstatedir=%{_rundir} \
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
%dir %{_sysconfdir}/tpm2-tss
%{_tmpfilesdir}/*.conf
%{_udevrulesdir}/%{udevrules_prefix}tpm-udev.rules
%{_sysconfdir}/tpm2-tss/*
%{_sysusersdir}/*.conf
%doc %{_mandir}/man5/fapi*.5.*

%files -n %{libtss2_mu}
%{_libdir}/libtss2-mu.so.%{major}{,.*}

%files -n %{libtss2_sys}
%{_libdir}/libtss2-sys.so.1{,.*}

%files -n %{libtss2_esys}
%{_libdir}/libtss2-esys.so.%{major}{,.*}

%files -n %{libtss2_fapi}
%{_libdir}/libtss2-fapi.so.1{,.*}

%files -n %{libtss2_rc}
%{_libdir}/libtss2-rc.so.%{major}{,.*}

%files -n %{libtss2_tctildr}
%{_libdir}/libtss2-tctildr.so.%{major}{,.*}

%files -n %{libtss2_tcti_d}
%{_libdir}/libtss2-tcti-device.so.%{major}{,.*}

%files -n %{libtss2_tcti_m}
%{_libdir}/libtss2-tcti-mssim.so.%{major}{,.*}

%files -n %{libtss2_tcti_c}
%{_libdir}/libtss2-tcti-cmd.so.%{major}{,.*}

%files -n %{libtss2_tcti_p}
%{_libdir}/libtss2-tcti-pcap.so.%{major}{,.*}

%files -n %{libtss2_tcti_s}
%{_libdir}/libtss2-tcti-swtpm.so.%{major}{,.*}

%files -n %{libtss2_policy}
%{_libdir}/libtss2-policy.so.%{major}{,.*}

%files -n %{libtss2_tcti_spi_helper}
%{_libdir}/libtss2-tcti-spi-helper.so.%{major}{,.*}

%files -n %{develname}
%dir %{_includedir}/tss2
%{_includedir}/tss2/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_mandir}/man3/*.3.*
%doc %{_mandir}/man7/tss2*.7.*
