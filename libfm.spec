#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : libfm
Version  : 1.3.2
Release  : 14
URL      : https://github.com/lxde/libfm/archive/1.3.2/libfm-1.3.2.tar.gz
Source0  : https://github.com/lxde/libfm/archive/1.3.2/libfm-1.3.2.tar.gz
Summary  : A glib/gio-based lib used to develop file managers providing some file management utilities.
Group    : Development/Tools
License  : GPL-2.0
Requires: libfm-bin = %{version}-%{release}
Requires: libfm-data = %{version}-%{release}
Requires: libfm-lib = %{version}-%{release}
Requires: libfm-license = %{version}-%{release}
Requires: libfm-locales = %{version}-%{release}
Requires: libfm-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : cairo-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk+-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libxslt-bin
BuildRequires : pango-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libmenu-cache)
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Notes for compilation:
1. This library requires:
- Libtool.
- Intltool 0.40.0 or newer.
- GLib 2.22.0 or newer.
- GTK+ 2.18.0 or newer.
- Libmenu-cache 0.3.2 or newer.

%package bin
Summary: bin components for the libfm package.
Group: Binaries
Requires: libfm-data = %{version}-%{release}
Requires: libfm-license = %{version}-%{release}

%description bin
bin components for the libfm package.


%package data
Summary: data components for the libfm package.
Group: Data

%description data
data components for the libfm package.


%package dev
Summary: dev components for the libfm package.
Group: Development
Requires: libfm-lib = %{version}-%{release}
Requires: libfm-bin = %{version}-%{release}
Requires: libfm-data = %{version}-%{release}
Provides: libfm-devel = %{version}-%{release}
Requires: libfm = %{version}-%{release}

%description dev
dev components for the libfm package.


%package lib
Summary: lib components for the libfm package.
Group: Libraries
Requires: libfm-data = %{version}-%{release}
Requires: libfm-license = %{version}-%{release}

%description lib
lib components for the libfm package.


%package license
Summary: license components for the libfm package.
Group: Default

%description license
license components for the libfm package.


%package locales
Summary: locales components for the libfm package.
Group: Default

%description locales
locales components for the libfm package.


%package man
Summary: man components for the libfm package.
Group: Default

%description man
man components for the libfm package.


%prep
%setup -q -n libfm-1.3.2
cd %{_builddir}/libfm-1.3.2
pushd ..
cp -a libfm-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683042931
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1683042931
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libfm
cp %{_builddir}/libfm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libfm/db95910cb27890d60e596e4c622fc3eeba6693fa || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang libfm
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/libfm-pref-apps
/V3/usr/bin/lxshortcut
/usr/bin/libfm-pref-apps
/usr/bin/lxshortcut

%files data
%defattr(-,root,root,-)
/usr/share/applications/libfm-pref-apps.desktop
/usr/share/applications/lxshortcut.desktop
/usr/share/libfm/archivers.list
/usr/share/libfm/images/folder.png
/usr/share/libfm/images/unknown.png
/usr/share/libfm/terminals.list
/usr/share/libfm/ui/app-chooser.ui
/usr/share/libfm/ui/ask-rename.ui
/usr/share/libfm/ui/choose-icon.ui
/usr/share/libfm/ui/exec-file.ui
/usr/share/libfm/ui/file-prop.ui
/usr/share/libfm/ui/filesearch.ui
/usr/share/libfm/ui/preferred-apps.ui
/usr/share/libfm/ui/progress.ui
/usr/share/mime-packages/libfm.xml

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libfm-extra.so
/V3/usr/lib64/libfm-gtk.so
/V3/usr/lib64/libfm.so
/usr/include/libfm
/usr/include/libfm-1.0/fm-action.h
/usr/include/libfm-1.0/fm-actions.h
/usr/include/libfm-1.0/fm-app-chooser-combo-box.h
/usr/include/libfm-1.0/fm-app-chooser-dlg.h
/usr/include/libfm-1.0/fm-app-info.h
/usr/include/libfm-1.0/fm-app-menu-view.h
/usr/include/libfm-1.0/fm-archiver.h
/usr/include/libfm-1.0/fm-bookmarks.h
/usr/include/libfm-1.0/fm-cell-renderer-pixbuf.h
/usr/include/libfm-1.0/fm-cell-renderer-text.h
/usr/include/libfm-1.0/fm-clipboard.h
/usr/include/libfm-1.0/fm-config.h
/usr/include/libfm-1.0/fm-deep-count-job.h
/usr/include/libfm-1.0/fm-dir-list-job.h
/usr/include/libfm-1.0/fm-dir-tree-model.h
/usr/include/libfm-1.0/fm-dir-tree-view.h
/usr/include/libfm-1.0/fm-dnd-auto-scroll.h
/usr/include/libfm-1.0/fm-dnd-dest.h
/usr/include/libfm-1.0/fm-dnd-src.h
/usr/include/libfm-1.0/fm-dummy-monitor.h
/usr/include/libfm-1.0/fm-extra.h
/usr/include/libfm-1.0/fm-file-info-job.h
/usr/include/libfm-1.0/fm-file-info.h
/usr/include/libfm-1.0/fm-file-launcher.h
/usr/include/libfm-1.0/fm-file-menu.h
/usr/include/libfm-1.0/fm-file-ops-job-change-attr.h
/usr/include/libfm-1.0/fm-file-ops-job-delete.h
/usr/include/libfm-1.0/fm-file-ops-job-xfer.h
/usr/include/libfm-1.0/fm-file-ops-job.h
/usr/include/libfm-1.0/fm-file-properties.h
/usr/include/libfm-1.0/fm-file.h
/usr/include/libfm-1.0/fm-folder-config.h
/usr/include/libfm-1.0/fm-folder-model.h
/usr/include/libfm-1.0/fm-folder-view.h
/usr/include/libfm-1.0/fm-folder.h
/usr/include/libfm-1.0/fm-gtk-file-launcher.h
/usr/include/libfm-1.0/fm-gtk-marshal.h
/usr/include/libfm-1.0/fm-gtk-utils.h
/usr/include/libfm-1.0/fm-gtk.h
/usr/include/libfm-1.0/fm-icon-pixbuf.h
/usr/include/libfm-1.0/fm-icon.h
/usr/include/libfm-1.0/fm-job.h
/usr/include/libfm-1.0/fm-list.h
/usr/include/libfm-1.0/fm-marshal.h
/usr/include/libfm-1.0/fm-menu-tool-item.h
/usr/include/libfm-1.0/fm-mime-type.h
/usr/include/libfm-1.0/fm-module.h
/usr/include/libfm-1.0/fm-monitor.h
/usr/include/libfm-1.0/fm-nav-history.h
/usr/include/libfm-1.0/fm-path-bar.h
/usr/include/libfm-1.0/fm-path-entry.h
/usr/include/libfm-1.0/fm-path.h
/usr/include/libfm-1.0/fm-places-model.h
/usr/include/libfm-1.0/fm-places-view.h
/usr/include/libfm-1.0/fm-progress-dlg.h
/usr/include/libfm-1.0/fm-seal.h
/usr/include/libfm-1.0/fm-side-pane.h
/usr/include/libfm-1.0/fm-simple-job.h
/usr/include/libfm-1.0/fm-sortable.h
/usr/include/libfm-1.0/fm-standard-view.h
/usr/include/libfm-1.0/fm-tab-label.h
/usr/include/libfm-1.0/fm-templates.h
/usr/include/libfm-1.0/fm-terminal.h
/usr/include/libfm-1.0/fm-thumbnail-loader.h
/usr/include/libfm-1.0/fm-thumbnail.h
/usr/include/libfm-1.0/fm-thumbnailer.h
/usr/include/libfm-1.0/fm-utils.h
/usr/include/libfm-1.0/fm-version.h
/usr/include/libfm-1.0/fm-xml-file.h
/usr/include/libfm-1.0/fm.h
/usr/lib64/libfm-extra.so
/usr/lib64/libfm-gtk.so
/usr/lib64/libfm.so
/usr/lib64/pkgconfig/libfm-extra.pc
/usr/lib64/pkgconfig/libfm-gtk.pc
/usr/lib64/pkgconfig/libfm.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libfm-extra.so.4
/V3/usr/lib64/libfm-extra.so.4.1.3
/V3/usr/lib64/libfm-gtk.so.4
/V3/usr/lib64/libfm-gtk.so.4.1.3
/V3/usr/lib64/libfm.so.4
/V3/usr/lib64/libfm.so.4.1.3
/V3/usr/lib64/libfm/modules/gtk-fileprop-x-desktop.so
/V3/usr/lib64/libfm/modules/gtk-fileprop-x-shortcut.so
/V3/usr/lib64/libfm/modules/gtk-menu-actions.so
/V3/usr/lib64/libfm/modules/gtk-menu-trash.so
/V3/usr/lib64/libfm/modules/vfs-menu.so
/V3/usr/lib64/libfm/modules/vfs-search.so
/usr/lib64/libfm-extra.so.4
/usr/lib64/libfm-extra.so.4.1.3
/usr/lib64/libfm-gtk.so.4
/usr/lib64/libfm-gtk.so.4.1.3
/usr/lib64/libfm.so.4
/usr/lib64/libfm.so.4.1.3
/usr/lib64/libfm/modules/gtk-fileprop-x-desktop.so
/usr/lib64/libfm/modules/gtk-fileprop-x-shortcut.so
/usr/lib64/libfm/modules/gtk-menu-actions.so
/usr/lib64/libfm/modules/gtk-menu-trash.so
/usr/lib64/libfm/modules/vfs-menu.so
/usr/lib64/libfm/modules/vfs-search.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libfm/db95910cb27890d60e596e4c622fc3eeba6693fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libfm-pref-apps.1
/usr/share/man/man1/lxshortcut.1

%files locales -f libfm.lang
%defattr(-,root,root,-)

