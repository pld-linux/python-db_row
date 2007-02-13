
%define	module	db_row

Summary:	Database abstraction layer
Summary(pl.UTF-8):	Warstwa abstrakcji baz danych
Name:		python-%{module}
Version:	0.8
Release:	1
License:	distributable
Group:		Development/Languages/Python
Source0:	http://opensource.theopalgroup.com/files/%{module}-%{version}.tgz
# Source0-md5:	8a264dde00752bef9a5751c5382269c8
URL:		http://opensource.theopalgroup.com/
Patch0:		%{name}-setup.patch
%pyrequires_eq  python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The db_row module defines light-weight objects suitable for
many applications, though the primary goal of the
implementer is for storage of database query results.

%description -l pl.UTF-8
Moduł db_row definiuje zestaw lekkich obiektów odpowiednich
dla wielu aplikacji, jednak głównym zamierzeniem jest
przechowywanie wyników zapytań do baz danych.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.so
