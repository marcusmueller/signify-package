Name:     signify
Version:  26
Release:  1%{?dist}
Summary:  Sign and encrypt files

License:  ISC
URL:      https://github.com/aperezdc/%{name}
Source0:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  libbsd-devel
BuildRequires:  gcc
BuildRequires:  make

%description
Sign and verify signatures on files, as used by the OpenBSD release maintainers.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build CFLAGS=-g

%install
%make_install PREFIX=/usr

%files
%doc CHANGELOG.md README.md
%{_bindir}/signify
%{_mandir}/man1/signify.*

%changelog
* Fri Nov 01 2019 Marcus Müller <marcus@hostalia.de> - 26-1
- Initial import
