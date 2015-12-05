%global commit 775857a079f11f6dcfc8f6b536a8d5c597be1bad
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           petpvc
Version:        0.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Toolbox for partial volume correction (PVC) in positron emission tomography (PET) 

License:        ASL 2.0
URL:            https://github.com/bathomas/PETPVC
Source0:        https://github.com/bathomas/PETPVC/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  InsightToolkit

%description
%{summary}.

%prep
%autosetup -n PETPVC-%{commit}

rm -rf build
mkdir build

%build
pushd build
  export ITK_DIR=%{_libdir}/cmake/InsightToolkit
  %cmake ../
  %make_build
popd

%install
pushd build
  %make_install
popd

%check
pushd build
  # https://github.com/bathomas/PETPVC/issues/1
  ctest -VV || :
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/pvc_*

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git775857a
- Initial package
