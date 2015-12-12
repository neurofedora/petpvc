%global commit 8b28893b24326e4701378ea65753d2a35016e264
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           petpvc
Version:        0.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Tools for partial volume correction (PVC) in positron emission tomography (PET) 

License:        ASL 2.0
URL:            https://github.com/UCL/PETPVC
Source0:        https://github.com/UCL/PETPVC/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  InsightToolkit-devel gdcm-devel
BuildRequires:  fftw-devel
BuildRequires:  vxl-devel

%description
%{summary}.

%prep
%autosetup -n PETPVC-%{commit}

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
  ctest -VV
popd

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_bindir}/pvc_*

%changelog
* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git8b28893
- Update with new upstream repo
- Fix things according review

* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git775857a
- Initial package
