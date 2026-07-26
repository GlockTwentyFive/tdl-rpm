Name: tdl
Version: 0.20.3
Release: 1%{?dist}
Summary: A telegram toolkit written in Golang

License: AGPL-3.0-only
URL: https://github.com/iyear/tdl

%ifarch x86_64
%global archive Linux_64bit
%endif

%ifarch i686
%global archive Linux_32bit
%endif

%ifarch aarch64
%global archive Linux_arm64
%endif

ExclusiveArch: x86_64 i686 aarch64

Source0: https://github.com/iyear/tdl/releases/download/v%{version}/tdl_%{archive}.tar.gz

%description
tdl is a Telegram toolkit written in Go that can download media, upload files,
forward messages, and perform various Telegram automation tasks.

%prep
%setup -q -c -T
%{__tar} -xzf %{SOURCE0}

%build
# Nothing to build

%install
install -Dpm755 tdl %{buildroot}%{_bindir}/tdl
install -Dpm644 LICENSE %{buildroot}%{_licensedir}/LICENSE

%files
%license %{_licensedir}/LICENSE
%{_bindir}/tdl

%changelog
* Sun Jul 26 2026 GlockTwentyFive <redninjaxbt@gmail.com> - 0.20.3-1
- Initial build
