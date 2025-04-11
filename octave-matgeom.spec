%global octpkg matgeom

Summary:	Geometry toolbox for 2D/3D geometric computing extending MatGeom
Name:		octave-matgeom
Version:	1.2.4
Release:	3
License:	GPLv3+ and BSD and Boost Software License
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/matgeom/
Source0:	https://downloads.sourceforge.net/octave/matgeom-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
MatGeom is a library for geometric computing with Matlab in 2D and 3D. It
contains several hundreds of functions for the creation and manipulation of
2D and 3D shapes such as point sets, lines, polygons, 3D meshes, ellipses...

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

