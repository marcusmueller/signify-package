Name:     signify
Version:  27
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
# remove upstream bundled optional library libwaive from source
%autosetup
rm -rf libwaive

%build
%set_build_flags
%make_build

# enabling checks as soon as upstream releases the next release (after v27)
# which should include regression testing
# %check
# %{__make} check


%install
%make_install PREFIX=%{_prefix}


%files
%doc CHANGELOG.md README.md
%{_bindir}/signify
%{_mandir}/man1/signify.*

%changelog
* Sat Jan 11 2020 Marcus Müller <marcus@hostalia.de> - 27-2
- removed bundled library libwaive from source
* Fri Jan 10 2020 Marcus Müller <marcus@hostalia.de> - 27-1
- updated to release v27
- prepared `%check` for as soon as regression tests are released
- fixed `%set_build_flags` (thanks Antonio <anto.trande@gmail.com>)
- proper _prefix (thanks Vít Ondruch <vondruch@redhat.com>)
* Fri Nov 01 2019 Marcus Müller <marcus@hostalia.de> - 26-1
- Initial import
