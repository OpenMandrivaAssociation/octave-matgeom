%define octpkg matgeom

Summary:	Library for geometric computing extending MatGeom functions
Name:		octave-%{octpkg}
Version:	1.2.3
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD and Boost Software License
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildRequires:	octave-devel

Requires:	octave(api) = %{octave_api}

BuildArch:	noarch

Requires(post): octave
Requires(postun): octave

%description
MatGeom is a library for geometric computing with Matlab in 2D and 3D. It
contains several hundreds of functions for the creation and manipulation of
2D and 3D shapes such as point sets, lines, polygons, 3D meshes, ellipses...

This package is part of external Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

