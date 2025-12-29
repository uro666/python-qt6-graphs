%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define major %(echo %{version} |cut -d. -f1-2)
%define _debugsource_packages 0
%global _debugsource_template %{nil}

%define oname pyqt6_graphs
%define pypi_name PyQt6-Graphs

Name:		python-qt6-graphs
Version:	6.10.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{oname}-%{version}.tar.gz
Summary:	Python bindings for the Qt Graphs library
URL:		https://pypi.org/project/python-qt6-graphs/
License:	GPL-3.0-only
Group:		Development/Python

BuildRequires:	make
BuildRequires:	python-sip >= 5.1.0
BuildRequires:	python-sip-qt6
BuildRequires:	python-qt-builder
BuildRequires:	qmake-qt6
BuildRequires:	qt6-cmake
BuildRequires:	glibc-devel
BuildRequires:	sed
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python)
BuildRequires:	cmake(Qt6Bluetooth)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Nfc)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Graphs)
BuildRequires:	cmake(Qt6GraphsWidgets)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6RemoteObjects)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Quick3D)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6SerialPort)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libpcre2-16)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	cmake(double-conversion)
BuildRequires:	python-qt6
BuildRequires:	python-qt6-core
BuildRequires:	python-qt6-gui
BuildRequires:	python-qt6-network
BuildRequires:	python-qt6-webchannel
BuildRequires:	python-qt6-devel
BuildRequires:	python%{pyver}dist(pyqt-builder)
BuildRequires:	python%{pyver}dist(pyqt6-sip)
BuildRequires:	python%{pyver}dist(sip)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


%description
%{pypi_name} is a set of Python bindings for The Qt
Company's Qt Graphs library.

The bindings sit on top of PyQt6 and are implemented
as two separate modules corresponding to the different
libraries that make up the framework.

%prep
%autosetup -n %{oname}-%{version} -p1
export QTDIR=%{_qtdir}
export PATH=%{_qtdir}/bin/:$PATH
export LDFLAGS="%{ldflags} -lpython%{pyver}"

sip-build \
	--no-make \
	--qmake %{_qtdir}/bin/qmake
find . -name Makefile |xargs sed -i -e 's,-L/usr/lib64,,g;s,-L/usr/lib,,g;s,-flto,-fno-lto,g'

%build
%make_build -C build


%install
%make_install -C build INSTALL_ROOT=%{buildroot}

# ensure .so modules are executable for proper -debuginfo extraction
find %{buildroot}%{python_sitearch} -name "*.so" |xargs chmod a+rx

%files
%doc README.md
%license LICENSE
%{python_sitearch}/PyQt6/QtGraphs.abi3.so
%{python_sitearch}/PyQt6/QtGraphsWidgets.abi3.so
%{python_sitearch}/PyQt6/bindings/QtGraphs
%{python_sitearch}/PyQt6/bindings/QtGraphsWidgets
%{python_sitearch}/%{oname}-%{version}.dist-info
