#
# spec file for package envoy-proxy
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _dwz_low_mem_die_limit  20000000
%define _dwz_max_die_limit     100000000

%define src_install_dir /usr/src/%{name}

Name:           envoy
Version:        1.14.4
Release:        4%{?dist}
Summary:        L7 proxy and communication bus
License:        ASL 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://www.envoyproxy.io/
#Source0:       https://github.com/envoyproxy/envoy/archive/refs/tags/v%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
# Refer to https://github.com/kubic-project/obs-service-bazel_repositories/blob/master/README.md
# regarding how to generate the vendor source
# AUTOGENERATED BY obs-service-bazel_repositories
# vendor.tar.gz contains the following dependencies:
# - https://github.com/Cyan4973/xxHash/archive/v0.7.3.tar.gz
# - https://github.com/DataDog/dd-opentracing-cpp/archive/v1.1.3.tar.gz
# - https://github.com/LuaJIT/LuaJIT/archive/v2.1.0-beta3.tar.gz
# - https://github.com/Tencent/rapidjson/archive/dfbe1db9da455552f7a9ad5d2aea17dd9d832ac1.tar.gz
# - https://github.com/abseil/abseil-cpp/archive/06f0e767d13d4d68071c4fc51e25724e0fc8bc74.tar.gz
# - https://github.com/apache/kafka/archive/2.4.0.zip
# - https://github.com/bazelbuild/apple_support/releases/download/0.7.2/apple_support.0.7.2.tar.gz
# - https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.19.1/bazel-gazelle-v0.19.1.tar.gz
# - https://github.com/bazelbuild/bazel-skylib/releases/download/0.9.0/bazel_skylib-0.9.0.tar.gz
# - https://github.com/bazelbuild/bazel-toolchains/releases/download/2.2.0/bazel-toolchains-2.2.0.tar.gz
# - https://github.com/bazelbuild/platforms/archive/9ded0f9c3144258dad27ad84628845bcd7ca6fe6.zip
# - https://github.com/bazelbuild/rules_apple/releases/download/0.19.0/rules_apple.0.19.0.tar.gz
# - https://github.com/bazelbuild/rules_cc/archive/818289e5613731ae410efb54218a4077fb9dbb03.tar.gz
# - https://github.com/bazelbuild/rules_foreign_cc/archive/7bc4be735b0560289f6b86ab6136ee25d20b65b7.tar.gz
# - https://github.com/bazelbuild/rules_go/releases/download/v0.23.3/rules_go-v0.23.3.tar.gz
# - https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
# - https://github.com/bazelbuild/rules_proto/archive/2c0468366367d7ed97a1f702f9cd7155ab3f73c5.tar.gz
# - https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz
# - https://github.com/bazelbuild/rules_swift/releases/download/0.13.0/rules_swift.0.13.0.tar.gz
# - https://github.com/c-ares/c-ares/archive/d7e070e7283f822b1d2787903cce3615536c5610.tar.gz
# - https://github.com/census-instrumentation/opencensus-cpp/archive/04ed0211931f12b03c1a76b3907248ca4db7bc90.tar.gz
# - https://github.com/census-instrumentation/opencensus-proto/archive/be218fb6bd674af7519b1850cdf8410d8cbd48e8.tar.gz
# - https://github.com/circonus-labs/libcircllhist/archive/63a16dd6f2fc7bc841bb17ff92be8318df60e2e1.tar.gz
# - https://github.com/cncf/udpa/archive/e8cd3a4bb307e2c810cffff99f93e96e6d7fee85.tar.gz
# - https://github.com/envoyproxy/envoy-build-tools/archive/84ca08de00eedd0ba08e7d5551108d6f03f5d362.tar.gz
# - https://github.com/envoyproxy/protoc-gen-validate/archive/ab56c3dd1cf9b516b62c5087e1ec1471bd63631e.tar.gz
# - https://github.com/envoyproxy/sql-parser/archive/b14d010afd4313f2372a1cc96aa2327e674cc798.tar.gz
# - https://github.com/fmtlib/fmt/archive/6.0.0.tar.gz
# - https://github.com/gabime/spdlog/archive/v1.4.0.tar.gz
# - https://github.com/golang/protobuf/archive/v1.4.1.zip
# - https://github.com/golang/tools/archive/2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd.zip
# - https://github.com/google/cel-cpp/archive/80e1cca533190d537a780ad007e8db64164c582e.tar.gz
# - https://github.com/google/jwt_verify_lib/archive/40e2cc938f4bcd059a97dc6c73f59ecfa5a71bac.tar.gz
# - https://github.com/google/re2/archive/2020-03-03.tar.gz
# - https://github.com/googleapis/googleapis/archive/82944da21578a53b74e547774cf62ed31a05b841.tar.gz
# - https://github.com/gperftools/gperftools/archive/gperftools-2.7.90.tar.gz
# - https://github.com/grpc-ecosystem/grpc-httpjson-transcoding/archive/faf8af1e9788cd4385b94c8f85edab5ea5d4b2d6.tar.gz
# - https://github.com/grpc/grpc/archive/d8f4928fa779f6005a7fe55a176bdb373b0f910f.tar.gz
# - https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.3.tar.gz
# - https://github.com/libevent/libevent/archive/0d7d85c2083f7a4c9efe01c061486f332b576d28.tar.gz
# - https://github.com/lightstep/lightstep-tracer-cpp/archive/3efe2372ee3d7c2138d6b26e542d757494a7938d.tar.gz
# - https://github.com/mirror/tclap/archive/tclap-1-2-1-release-final.tar.gz
# - https://github.com/moonjit/moonjit/archive/2.2.0.tar.gz
# - https://github.com/msgpack/msgpack-c/releases/download/cpp-3.2.1/msgpack-3.2.1.tar.gz
# - https://github.com/nodejs/http-parser/archive/v2.9.3.tar.gz
# - https://github.com/opentracing/opentracing-cpp/archive/v1.5.1.tar.gz
# - https://github.com/openzipkin/zipkin-api/archive/0.2.2.tar.gz
# - https://github.com/pallets/jinja/archive/2.10.3.tar.gz
# - https://github.com/pallets/markupsafe/archive/1.1.1.tar.gz
# - https://github.com/prometheus/client_model/archive/99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c.tar.gz
# - https://github.com/protocolbuffers/protobuf-go/archive/v1.22.0.zip
# - https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protobuf-all-3.10.1.tar.gz
# - https://github.com/protocolbuffers/upb/archive/8a3ae1ef3e3e3f26b45dec735c5776737fc7247f.tar.gz
# - https://mirror.bazel.build/github.com/bazelbuild/platforms/archive/9ded0f9c3144258dad27ad84628845bcd7ca6fe6.zip
# - https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
# - https://mirror.bazel.build/github.com/golang/protobuf/archive/v1.4.1.zip
# - https://mirror.bazel.build/github.com/golang/tools/archive/2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd.zip
# - https://mirror.bazel.build/github.com/protocolbuffers/protobuf-go/archive/v1.22.0.zip
Source1:        %{name}-%{version}-vendor.tar.gz
# END obs-service-bazel_repositories
Source100:      %{name}-rpmlintrc
Patch0:         0001-build-Use-Go-from-host.patch
Patch1:         0002-build-update-several-go-dependencies-11581.patch
Patch2:         0003-build-Add-explicit-requirement-on-rules_cc.patch
Patch3:         0004-build-Use-new-bazel.patch
BuildRequires:  bazel
BuildRequires:  bazel-workspaces
BuildRequires:  boringssl-source
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  git
BuildRequires:  golang >= 1.12
BuildRequires:  golang-packaging
BuildRequires:  libcurl-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  nghttp2-devel
BuildRequires:  ninja-build
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  python3-jinja2
BuildRequires:  python3-markupsafe
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(openssl)
# AUTOGENERATED BY obs-service-bazel_repositories
Provides:       bundled(abseil-cpp) = 06f0e767d13d4d68071c4fc51e25724e0fc8bc74
Provides:       bundled(apple_support) = 0.7.2
Provides:       bundled(bazel-gazelle) = 0.19.1
Provides:       bundled(bazel-skylib) = 0.9.0
Provides:       bundled(bazel-toolchains) = 4.1.0
Provides:       bundled(c-ares) = d7e070e7283f822b1d2787903cce3615536c5610
Provides:       bundled(cel-cpp) = 80e1cca533190d537a780ad007e8db64164c582e
Provides:       bundled(client_model) = 99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c
Provides:       bundled(dd-opentracing-cpp) = 1.1.3
Provides:       bundled(envoy-build-tools) = 84ca08de00eedd0ba08e7d5551108d6f03f5d362
Provides:       bundled(fmt) = 6.0.0
Provides:       bundled(googleapis) = 82944da21578a53b74e547774cf62ed31a05b841
Provides:       bundled(gperftools) = 2.7.90
Provides:       bundled(grpc) = d8f4928fa779f6005a7fe55a176bdb373b0f910f
Provides:       bundled(grpc-httpjson-transcoding) = faf8af1e9788cd4385b94c8f85edab5ea5d4b2d6
Provides:       bundled(http-parser) = 2.9.3
Provides:       bundled(jinja) = 2.10.3
Provides:       bundled(jwt_verify_lib) = 40e2cc938f4bcd059a97dc6c73f59ecfa5a71bac
Provides:       bundled(kafka) = 2.4.0
Provides:       bundled(libcircllhist) = 63a16dd6f2fc7bc841bb17ff92be8318df60e2e1
Provides:       bundled(libevent) = 0d7d85c2083f7a4c9efe01c061486f332b576d28
Provides:       bundled(lightstep-tracer-cpp) = 3efe2372ee3d7c2138d6b26e542d757494a7938d
Provides:       bundled(luajit) = 2.1.0
Provides:       bundled(markupsafe) = 1.1.1
Provides:       bundled(moonjit) = 2.2.0
Provides:       bundled(msgpack-c) = 3.2.1
Provides:       bundled(opencensus-cpp) = 04ed0211931f12b03c1a76b3907248ca4db7bc90
Provides:       bundled(opencensus-proto) = be218fb6bd674af7519b1850cdf8410d8cbd48e8
Provides:       bundled(opentracing-cpp) = 1.5.1
Provides:       bundled(platforms) = 9ded0f9c3144258dad27ad84628845bcd7ca6fe6
Provides:       bundled(protobuf) = 1.4.1
Provides:       bundled(protobuf) = 3.10.1
Provides:       bundled(protobuf-go) = 1.22.0
Provides:       bundled(protoc-gen-validate) = ab56c3dd1cf9b516b62c5087e1ec1471bd63631e
Provides:       bundled(rapidjson) = dfbe1db9da455552f7a9ad5d2aea17dd9d832ac1
Provides:       bundled(re2)
Provides:       bundled(rules_apple) = 0.19.0
Provides:       bundled(rules_cc) = b1c40e1de81913a3c40e5948f78719c28152486d
Provides:       bundled(rules_foreign_cc) = d54c78ab86b40770ee19f0949db9d74a831ab9f0
Provides:       bundled(rules_go) = 0.23.3
Provides:       bundled(rules_java) = 7cf3cefd652008d0a64a419c34c13bdca6c8f178
Provides:       bundled(rules_proto) = 2c0468366367d7ed97a1f702f9cd7155ab3f73c5
Provides:       bundled(rules_python) = 0.0.1
Provides:       bundled(rules_swift) = 0.13.0
Provides:       bundled(spdlog) = 1.4.0
Provides:       bundled(sql-parser) = b14d010afd4313f2372a1cc96aa2327e674cc798
Provides:       bundled(tclap)
Provides:       bundled(tools) = 2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd
Provides:       bundled(udpa) = e8cd3a4bb307e2c810cffff99f93e96e6d7fee85
Provides:       bundled(upb) = 8a3ae1ef3e3e3f26b45dec735c5776737fc7247f
Provides:       bundled(xxhash) = 0.7.3
Provides:       bundled(yaml-cpp) = 0.6.3
Provides:       bundled(zipkin-api) = 0.2.2
# END obs-service-bazel_repositories
ExcludeArch:    %{ix86}

%description
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

%package source
Summary:        Source code of bazel-rules-cc

%description source
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

This package contains source code of Envoy.

%prep
%autosetup -p1

# Prevent bundling curl, nghttp2 and zlib, don't use foreign_cc on them.
sed -i \
    -e "s|@envoy//bazel/foreign_cc:curl|@com_github_curl//:curl|" \
    -e 's|patches = \["@envoy//bazel/foreign_cc:nghttp2.patch"\]|# patches = \["@envoy//bazel/foreign_cc:nghttp2.patch"\]|g' \
    -e "s|@envoy//bazel/foreign_cc:nghttp2|@com_github_nghttp2_nghttp2//:all|" \
    -e "s|@envoy//bazel/foreign_cc:zlib|@zlib//:zlib|" \
    bazel/repositories.bzl

# Remove the script which requires /usr/bin/bash.exe and is meant to work only
# on Windows.
rm ci/windows_ci_steps.sh

# AUTOGENERATED BY obs-service-bazel_repositories
%setup -q -T -D -a 1
# END obs-service-bazel_repositories

%build
git config --global user.email you@example.com
git config --global user.name "Your Name"
git init
git add .
GIT_AUTHOR_DATE=2000-01-01T01:01:01 GIT_COMMITTER_DATE=2000-01-01T01:01:01 \
git commit -m "Dummy commit just to satisfy bazel" &> /dev/null

# workaround for boo#1183836
CC=gcc CXX=g++ bazel --batch build \
    -c dbg \
    --color=no \
    --copt="-fsigned-char" \
    --cxxopt="-fsigned-char" \
    --copt="-Wno-error=old-style-cast" \
    --cxxopt="-Wno-error=old-style-cast" \
    --copt="-Wno-unused-parameter" \
    --cxxopt="-Wno-unused-parameter" \
    --copt="-Wno-implicit-fallthrough" \
    --cxxopt="-Wno-implicit-fallthrough"\
    --copt="-Wno-return-type" \
    --cxxopt="-Wno-return-type" \
    --curses=no \
    --host_force_python=PY3 \
    --repository_cache=BAZEL_CACHE \
    --strip=never \
    --override_repository="boringssl=%{_prefix}/src/boringssl/" \
    --override_repository="com_github_curl=%{_datadir}/bazel-workspaces/curl" \
    --override_repository="com_github_nghttp2_nghttp2=%{_datadir}/bazel-workspaces/nghttp2" \
    --override_repository="zlib=%{_datadir}/bazel-workspaces/zlib" \
    --verbose_failures \
%ifarch ppc64le
    --local_cpu_resources=HOST_CPUS*.5 \
%endif
    //source/exe:envoy
bazel shutdown

%install
install -D -m0755 bazel-bin/source/exe/envoy-static %{buildroot}%{_bindir}/envoy-proxy

# Install sources
rm -rf .git bazel-*
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
fdupes %{buildroot}%{src_install_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/envoy-proxy

%files source
%{src_install_dir}

%changelog
* Tue Sep 14 2021 Henry Li <lihl@microsoft.com> - 1.14.4-4
- Add patch to use newer version of bazel
- Update patch to use new version of external dependencies
- Update vendor source and file name

* Tue Jun 15 2021 Henry Li <lihl@microsoft.com> - 1.14.4-3.4
- Initial CBL-Mariner import from OpenSUSE Tumbleweed (license: same as "License" tag)
- License Verified
- Use gcc-c++ for BR
- Use ninja-build for BR
- Use golang for BR
- Change package name from envoy-proxy to envoy
- Use gcc instead of gcc10, which is not supported in CBL-Mariner
- Use bazel batch mode to build

* Wed May 19 2021 Martin Liška <mliska@suse.cz>
- Build it with GCC 10 for now (boo#1183836).

* Tue Mar 16 2021 Martin Liška <mliska@suse.cz>
- Double memory limits for dwz.

* Thu Sep 17 2020 Guillaume GARDET <guillaume.gardet@opensuse.org>
- Relax constraints on aarch64

* Tue Aug 25 2020 Michał Rostecki <mrostecki@suse.com>
- Update to 1.14.4
  * Release notes: https://www.envoyproxy.io/docs/envoy/v1.14.4/intro/version_history
- Remove patches which were either released upstream or are not
  relevant anymore:
  * 0001-server-add-getTransportSocketFactoryContext-to-Filte.patch
  * 0002-test-Fix-mocks.patch
  * 0003-test-Fix-format.patch
  * 0004-server-Add-comments-pointing-out-implementation-deta.patch
  * 0005-server-Move-setInitManager-to-TransportSocketFactory.patch
  * 0006-fix-format.patch
  * 0007-lua-Handle-the-default-case-in-scriptLog.patch
  * logger-Use-spdlog-memory_buf_t-instead-of-fmt-memory.patch
  * big-endian-support.patch
  * bazel-Fix-optional-dynamic-linking-of-OpenSSL.patch
  * compatibility-with-TLS-1.2-and-OpenSSL-1.1.0.patch
- Add patches which fix the offline build of the new version:
  * 0001-build-Use-Go-from-host.patch
  * 0002-build-update-several-go-dependencies-11581.patch
  * 0003-build-Add-explicit-requirement-on-rules_cc.patch

* Wed Jul  1 2020 Michał Rostecki <mrostecki@suse.com>
- Add patch which fixes the error occuring for spdlog 1.6.1:
  * 0007-lua-Handle-the-default-case-in-scriptLog.patch

* Wed May 20 2020 Michel Normand <normand@linux.vnet.ibm.com>
-  limit build resources for ppc64le to avoid Out of Memory error

* Wed May 20 2020 Michel Normand <normand@linux.vnet.ibm.com>
- Add ppc64/ppc64le in _constraints to use worker with max memory

* Thu Apr 16 2020 Dirk Mueller <dmueller@suse.com>
- add big-endian-support.patch to fix build on s390x:
  * backport of an already upstream patch at https://github.com/envoyproxy/envoy/pull/10250

* Mon Mar 16 2020 Michał Rostecki <mrostecki@opensuse.org>
- Fix the include dir of moonjit.

* Mon Mar  9 2020 Michał Rostecki <mrostecki@opensuse.org>
- Add bazel-rules-python as a build requirement.

* Tue Feb  4 2020 Michał Rostecki <mrostecki@opensuse.org>
- Remove nanopb from requirements.

* Thu Jan 16 2020 Michał Rostecki <mrostecki@opensuse.org>
- Add patches which allow an access to TransportSocketFactoryContext
  from a Filter context. Needed for cilium-proxy to work properly:
  * 0001-server-add-getTransportSocketFactoryContext-to-Filte.patch
  * 0002-test-Fix-mocks.patch
  * 0003-test-Fix-format.patch
  * 0004-server-Add-comments-pointing-out-implementation-deta.patch
  * 0005-server-Move-setInitManager-to-TransportSocketFactory.patch
  * 0006-fix-format.patch

* Tue Jan 14 2020 Michał Rostecki <mrostecki@opensuse.org>
- Update to version 1.12.2+git.20200109:
  * http: fixed CVE-2019-18801 by allocating sufficient memory for
    request headers.
  * http: fixed CVE-2019-18802 by implementing stricter validation
    of HTTP/1 headers.
  * http: trim LWS at the end of header keys, for correct HTTP/1.1
    header parsing.
  * http: added strict authority checking. This can be reversed
    temporarily by setting the runtime feature
    envoy.reloadable_features.strict_authority_validation to false.
  * route config: fixed CVE-2019-18838 by checking for presence of
    host/path headers.
  * listener: fixed CVE-2019-18836 by clearing accept filters
    before connection creation.
- Switch from Maistra to envoy-openssl as the way of replacing
  BoringSSL with OpenSSL.
- Add source package to build cilium-proxy separately, with
  envoy-proxy-source as a build depencency.
- Add patch which fixes dynamic linking of OpenSSL:
  * bazel-Fix-optional-dynamic-linking-of-OpenSSL.patch
- Add patch which adds backwards compatibility with TLS 1.2 and
  OpenSSL 1.1.0:
  * compatibility-with-TLS-1.2-and-OpenSSL-1.1.0.patch
- Add patch for compatibility with fmt 6.1.0 and spdlog 1.5.0:
  * logger-Use-spdlog-memory_buf_t-instead-of-fmt-memory.patch
- Remove patches which are not needed anymore:
  * 0001-bazel-Update-protobuf-and-other-needed-dependencies.patch
  * 0002-bazel-Update-grpc-to-1.23.0.patch
  * 0003-tracing-update-googleapis-use-SetName-for-operation-.patch

* Fri Dec 13 2019 Michał Rostecki <mrostecki@opensuse.org>
- Replace lua51-luajit with moonjit.

* Wed Nov  6 2019 Michał Rostecki <mrostecki@opensuse.org>
- Do not bundle any dependencies, move everything to separate
  packages.
- Add patch which makes envoy-proxy compatible with newer
  googleapis:
  * 0003-tracing-update-googleapis-use-SetName-for-operation-.patch

* Fri Nov  1 2019 Michał Rostecki <mrostecki@opensuse.org>
- Do not use global optflags (temporarily) - enabling them causes
  linker errors.

* Fri Oct 18 2019 Michał Rostecki <mrostecki@opensuse.org>
- Disable incompatible_bzl_disallow_load_after_statement check in
  Bazel - some dependencies still do not pass it.

* Thu Oct 17 2019 Richard Brown <rbrown@suse.com>
- Remove obsolete Groups tag (fate#326485)

* Wed Oct 16 2019 Michał Rostecki <mrostecki@opensuse.org>
- Remove duplicate tarball of golang-org-x-tools and unneeded
  tarballs of msgpack and http-parser.

* Tue Oct 15 2019 Michał Rostecki <mrostecki@opensuse.org>
- Update to version 1.11.1:
  * http: added mitigation of client initiated attacks that result
    in flooding of the downstream HTTP/2 connections. Those attacks
    can be logged at the “warning” level when the runtime feature
    http.connection_manager.log_flood_exception is enabled. The
    runtime setting defaults to disabled to avoid log spam when
    under attack.
  * http: added inbound_empty_frames_flood counter stat to the
    HTTP/2 codec stats, for tracking number of connections
    terminated for exceeding the limit on consecutive inbound
    frames with an empty payload and no end stream flag. The limit
    is configured by setting the
    max_consecutive_inbound_frames_with_empty_payload config
    setting.
  * http: added inbound_priority_frames_flood counter stat to the
    HTTP/2 codec stats, for tracking number of connections
    terminated for exceeding the limit on inbound PRIORITY frames.
    The limit is configured by setting the
    max_inbound_priority_frames_per_stream config setting.
  * http: added inbound_window_update_frames_flood counter stat
    to the HTTP/2 codec stats, for tracking number of connections
    terminated for exceeding the limit on inbound WINDOW_UPDATE
    frames.
  * http: added outbound_flood counter stat to the HTTP/2 codec
    stats, for tracking number of connections terminated for
    exceeding the outbound queue limit.
  * http: added outbound_control_flood counter stat to the HTTP/2
    codec stats, for tracking number of connections terminated
    for exceeding the outbound queue limit for PING, SETTINGS and
    RST_STREAM frames.
  * http: enabled strict validation of HTTP/2 messaging. Previous
    behavior can be restored using
    stream_error_on_invalid_http_messaging config setting.
- Add sources of envoy-openssl project which makes use of OpenSSL
  instead of BoringSSL.
- Add patches which makes Envoy compatible with versions of
  libraries available in openSUSE:
  * 0001-bazel-Update-protobuf-and-other-needed-dependencies.patch
  * 0002-bazel-Update-grpc-to-1.23.0.patch
- Remove patches which are not needed anymore:
  * 0001-Remove-deprecated-Blaze-PACKAGE_NAME-macro-5330.patch
  * 0001-Upgrade-gabime-spdlog-dependency-to-1.3.0-5604.patch
  * 0001-bazel-transport-sockets-Update-grpc-to-1.19.1.patch

* Thu Apr  4 2019 Jan Engelhardt <jengelh@inai.de>
- openssl-devel should be pkgconfig(openssl)

* Tue Mar 19 2019 Michal Rostecki <mrostecki@opensuse.org>
- Add patch which allows to use grpc 1.19.x.
  * 0001-bazel-transport-sockets-Update-grpc-to-1.19.1.patch
- Use source packages of grpc-httpjson-transcoding, opentracing-cpp
  and lightstep-tracer-cpp. (boo#1129568)

* Tue Mar 12 2019 Bernhard Wiedemann <bwiedemann@suse.com>
- Use fixed date for reproducible builds (boo#1047218)

* Tue Feb 26 2019 Michał Rostecki <mrostecki@opensuse.org>
- Add upstream patch which allows to use spdlog 1.3.x.
  * 0001-Upgrade-gabime-spdlog-dependency-to-1.3.0-5604.patch

* Wed Feb 20 2019 Michał Rostecki <mrostecki@opensuse.org>
- Add upstream patch which fixes build with Bazel 0.22.0.
  * 0001-Remove-deprecated-Blaze-PACKAGE_NAME-macro-5330.patch
- Fix build with the newest bazel-rules-go.

* Thu Feb 14 2019 Michał Rostecki <mrostecki@opensuse.org>
- Stop bundling libraries and dependencies, use shared libraries
  and *-source packages instead.

* Wed Oct 31 2018 Michał Rostecki <mrostecki@suse.de>
- Initial version 1.8.0+git20181105
