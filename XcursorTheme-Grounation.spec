%define		_name Grounation
Summary:	A cursor theme Grounation
Summary(pl.UTF-8):   Motyw kursorów Grounation
Name:		XcursorTheme-%{_name}
Version:	0.3
Release:	0.2
License:	GPL v2
Group:		Themes
Source0:	http://www.kde-look.org/content/files/14484-%{_name}-%{version}.tar.bz2
# Source0-md5:	2a448239a339ed3e87991d3ab621a24d
URL:		http://dvornik.uw.hu/
BuildRequires:	XFree86 >= 4.3
Requires:	XFree86 >= 4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cursor theme Grounation.

%description -l pl.UTF-8
Motyw kursorów Grounation.

%prep
%setup -q -n %{_name}-%{version}

%build
cd %{_name}/Source
./Build.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
install %{_name}/cursors/* $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
install %{_name}/index.theme $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
