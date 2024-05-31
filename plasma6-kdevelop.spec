%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

# We cannot do it when debug is set to nil like in 2012.1
%if %unstable
#define dont_strip 1
%endif

%define libname_orig libkdevplatform4
%define major   5
%define libname %mklibname kdevplatform %{major}
%define old_major 2
%define old_libname %mklibname kdevplatform4 %{old_major}
%define dev_clang_major 60
%define __requires_exclude /bin/zsh

%define git 20240530
%define gitbranch work/apol/kf6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Integrated Development Environment for C++/C
Name:		plasma6-kdevelop
Version:	24.05.0
Release:	1
Group:		Development/C++
License:	GPLv2
Url:		http://www.kdevelop.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/kdevelop/kdevelop/-/archive/%{gitbranch}/kdevelop-%{gitbranchd}.tar.bz2#/kdevelop-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)/release-service/%{version}/src/kdevelop-%{version}.tar.xz
%endif
Patch1:		kdevplatform-5.0.3-bsdtar.patch
Patch2:		kdevelop-23.03.90-clang16.patch
BuildRequires:	qt5-assistant
BuildRequires:	boost-devel
BuildRequires:	bash-completion
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Runner)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(Okteta3Kasten5Controllers)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Help)
BuildRequires:	cmake(KDevelop-PG-Qt)
BuildRequires:	cmake(KSysGuard) >= 6.0.0
BuildRequires:	cmake(KompareDiff2) >= 6.0.0
BuildRequires:	cmake(KDEExperimentalPurpose)
BuildRequires:	llvm-devel
BuildRequires:	llvm-static-devel
BuildRequires:	spirv-llvm-translator
BuildRequires:	llvm-bolt
BuildRequires:	libclc-amdgcn
BuildRequires:	libclc-nvptx
BuildRequires:	clang-devel
BuildRequires:	shared-mime-info
BuildRequires:	subversion-devel
BuildRequires:	astyle-devel
BuildRequires:	meson
BuildRequires:	clazy
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(libxml-2.0)
%if %{compile_apidox}
BuildRequires:	doxygen
%endif
Requires:	cmake
Requires:	git
Requires:	gdb
Requires:	kdevplatform >= %{EVRD}
Recommends:	meson
Recommends:	clazy
BuildSystem:	cmake
BuildOption:	-DBUILD_TESTING=OFF
BuildOption:	-DBSDTAR=1
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
The KDevelop Integrated Development Environment provides many features that
developers need as well as providing a unified interface to programs like gdb,
the C/C++ compiler, and make.

KDevelop manages or provides:
   * All development tools needed for C++ programming like Compiler, Linker,
     automake and autoconf
   * KAppWizard, which generates complete, ready-to-go sample applications
   * Classgenerator, for creating new classes and integrating them into the
     current project
   * File management for sources, headers, documentation etc. to be included in
     the project
   * The creation of User-Handbooks written with SGML and the automatic
     generation of HTML-output with the KDE look and feel
   * Automatic HTML-based API-documentation for your project's classes with
     cross-references to the used libraries; Internationalization support for
     your application, allowing translators to easily add their target language
     to a project
   * WYSIWYG (What you see is what you get) creation of user interfaces with a
     built-in dialog editor
   * Debugging your application by integrating KDbg
   * Editing of project-specific pixmaps with KIconEdit
   * The inclusion of any other program you need for development by adding it
     to the "Tools" menu according to your individual needs.

%files -f %{name}.lang
%{_bindir}/kdevelop*
%{_bindir}/kdev_includepathsconverter
%{_datadir}/applications/*.desktop
%{_datadir}/qlogging-categories6/kdevelop.categories
%{_datadir}/mime/packages/kdev*.xml
%{_libdir}/libKDevCMakeCommon.so.%{dev_clang_major}
%{_libdir}/libKDevClangPrivate.so.%{dev_clang_major}
%{_libdir}/libKDevCompileAnalyzerCommon.so.%{dev_clang_major}
%{_libdir}/qt6/plugins/kdevplatform
%{_datadir}/icons/hicolor/*/apps/kdevelop.png
%{_datadir}/icons/hicolor/*/apps/kdevgh.png
%{_datadir}/icons/hicolor/*/apps/cmake.png
%{_datadir}/icons/hicolor/*/apps/cppcheck.png
%{_datadir}/icons/hicolor/*/apps/github-*.png
%{_datadir}/icons/hicolor/*/apps/clazy.png
%{_datadir}/icons/hicolor/*/apps/qtlogo.svg
%{_datadir}/icons/hicolor/scalable/apps/kdevelop.svg
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevcodegen
%{_datadir}/kdevgdb
%{_datadir}/kdevlldb
%{_datadir}/kdevappwizard
%{_datadir}/kdevmanpage
%{_datadir}/kdevclangsupport
%{_datadir}/knotifications6/kdevelop.notifyrc
%{_datadir}/metainfo/org.kde.kdevelop.appdata.xml
%{_datadir}/knsrcfiles/kdevappwizard.knsrc
%{_datadir}/knsrcfiles/kdevelop-qthelp.knsrc
%{_datadir}/knsrcfiles/kdevfiletemplates.knsrc
%{_datadir}/bash-completion/completions/kdevelop
# Exclude kdevplatform folders
%exclude %{_datadir}/kdevplatform/
%exclude %{_datadir}/kdevcodegen/
%exclude %{_datadir}/kdevcodeutils/

#------------------------------------------------
%package devel
Summary:	Development files for kdevelop
Group:		Development/KDE and Qt

%description devel
Development files for kdevelop.

%files devel
%{_libdir}/cmake/KDevelop
%{_includedir}/kdevelop

#------------------------------------------------
%package -n kdevplatform
Summary:	Files for kdevplatform
Group:		Development/KDE and Qt

%description -n kdevplatform
Kdevelop platform tools.

%files -n kdevplatform 
%{_bindir}/kdev_dbus_socket_transformer
%{_bindir}/kdev_format_source
%{_bindir}/kdevplatform_shell_environment.sh
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_datadir}/kdevplatform
%{_datadir}/qlogging-categories6/kdevplatform.categories
%{_iconsdir}/hicolor/*/apps/subversion.*
%{_iconsdir}/hicolor/*/apps/bazaar.png
%{_iconsdir}/hicolor/*/apps/git.*
%{_iconsdir}/hicolor/*/actions/breakpoint.*
%{_qtdir}/plugins/kf6/ktexttemplate/kdev_filters.so
%{_qtdir}/qml/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so
%{_qtdir}/qml/org/kde/kdevplatform/qmldir
%dir %{_qtdir}/plugins/kdevplatform
%{_libdir}/libKDevPlatformInterfaces.so.*
%{_libdir}/libKDevPlatformLanguage.so.*
%{_libdir}/libKDevPlatformOutputView.so.*
%{_libdir}/libKDevPlatformProject.so.*
%{_libdir}/libKDevPlatformShell.so.*
%{_libdir}/libKDevPlatformUtil.so.*
%{_libdir}/libKDevPlatformVcs.so.*
%{_libdir}/libKDevPlatformSublime.so.*
%{_libdir}/libKDevPlatformDebugger.so.*
%{_libdir}/libKDevPlatformDocumentation.so.*
%{_libdir}/libKDevPlatformSerialization.so.*

#-----------------------------------------------------------------------------

%package -n %{libname}-devel
Summary:        Development files for kdevplatform
Group:          Development/KDE and Qt
Provides:       kdevplatform-devel = %{EVRD}
Requires:       kdevplatform = %{EVRD}

%description -n %{libname}-devel
Development files for kdevplatform.

%files -n %{libname}-devel
%{_libdir}/cmake/KDevPlatform
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so

#-----------------------------------------------------------------------------

%install -a
%find_lang %{name} --all-name --with-html
