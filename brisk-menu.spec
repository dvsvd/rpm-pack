Name: brisk-menu 
Version: 0.6.2
Release:        1%{?dist}
Summary: Brisk-menu in RPM package

License: GPL-2.0 License
URL: https://github.com/getsolus/brisk-menu
Source0: %{_sourcedir}/brisk-menu-0.6.2.tar.xz

BuildRequires: meson >= 0.40
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: libnotify-devel >= 0.7.0
BuildRequires: mate-panel-devel >= 1.21.0
BuildRequires: mate-menus-devel >= 1.21.0
BuildRequires: gtk3-devel >= 3.18.0

Requires: libnotify >= 0.7.0
Requires: mate-panel
Requires: mate-menus
Requires: gtk3 >= 3.18

%description
brisk-menu is a modern and efficient menu designed to improve the MATE Desktop Environment with modern, first-class options.
The purpose of this project is to provide a usable menu as seen in other desktops without the bloat and performance issues.
brisk-menu is distro-agnostic and the reporting of portability issues is encouraged.

%description -l ru
brisk-menu - это современное и эффективное меню, созданное для улучшения MATE Desktop Environment современными и первоклассными опциями.
Цель этого проекта обеспечить удобное меню, похожее на то, чтоо можно видеть в других графических окружениях без проблем с раздуванием и производительностью.
brisk-menu нечувствительна к дистрибутиву. Также, мы будем рады всякой обратной связи о проблемах с совместимостью.

%prep
%setup -a 0

%build
%meson --buildtype=release
%meson_build


%install
%meson_install
find %{buildroot} -name ".debug" -delete


%files
%{_datadir}
%{_libexecdir}
%license LICENSE.CC-BY-SA-4.0
%doc README.md



%changelog
* Wed Feb 04 2026 Your Name <you@example.com>
- 
