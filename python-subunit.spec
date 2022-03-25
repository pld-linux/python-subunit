#
# Conditional build:
%bcond_without	python2 # CPython 2.x module and tools
%bcond_without	python3 # CPython 3.x module and tools
%bcond_without	tests	# unit tests

Summary:	subunit - streaming protocol for test results
Summary(pl.UTF-8):	subunit - protokół strumieniowy do wyników testów
Name:		python-subunit
Version:	1.4.0
Release:	3
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-subunit/
Source0:	https://files.pythonhosted.org/packages/source/p/python-subunit/%{name}-%{version}.tar.gz
# Source0-md5:	30f1ab20651d94442dd9a7f8c9e8d633
Patch0:		%{name}-tests.patch
URL:		https://pypi.org/project/python-subunit/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-extras
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-testtools >= 0.9.34
%if %{with tests}
BuildRequires:	python-fixtures
BuildRequires:	python-hypothesis
BuildRequires:	python-testscenarios
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-extras
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-testtools >= 0.9.34
%if %{with tests}
BuildRequires:	python3-fixtures
BuildRequires:	python3-hypothesis
BuildRequires:	python3-testscenarios
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subunit is a streaming protocol for test results.

This package contains Python 2.x modules.

%description -l pl.UTF-8
Subunit to protokół strumieniowy przeznaczony do wyników testów.

Ten pakiet zawiera moduły Pythona 2.x.

%package -n subunit-python2
Summary:	Python 2 tools for subunit streaming protocol for test results
Summary(pl.UTF-8):	Narzędzia Pythona 2 dla protokołu strumieniowego do wyników testów subunit
Group:		Development/Tools
Requires:	python-subunit = %{version}-%{release}

%description -n subunit-python2
Python 2 tools for subunit streaming protocol for test results.

%description -n subunit-python2 -l pl.UTF-8
Narzędzia Pythona 2 dla protokołu strumieniowego do wyników testów
subunit.

%package -n python3-subunit
Summary:	subunit - streaming protocol for test results
Summary(pl.UTF-8):	subunit - protokół strumieniowy do wyników testów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-subunit
Subunit is a streaming protocol for test results.

This package contains Python 2.x modules.

%description -n python3-subunit -l pl.UTF-8
Subunit to protokół strumieniowy przeznaczony do wyników testów.

Ten pakiet zawiera moduły Pythona 2.x.

%package -n subunit-python3
Summary:	Python 3 tools for subunit streaming protocol for test results
Summary(pl.UTF-8):	Narzędzia Pythona 3 dla protokołu strumieniowego do wyników testów subunit
Group:		Development/Tools
Requires:	python3-subunit = %{version}-%{release}

%description -n subunit-python3
Python 3 tools for subunit streaming protocol for test results.

%description -n subunit-python3 -l pl.UTF-8
Narzędzia Pythona 3 dla protokołu strumieniowego do wyników testów
subunit.

%package -n subunit-python
Summary:	Python tools for subunit streaming protocol for test results
Summary(pl.UTF-8):	Pythonowe narzędzia dla protokołu strumieniowego do wyników testów subunit
Group:		Development/Tools
%if %{with python3}
Requires:	subunit-python3 = %{version}-%{release}
%else
Requires:	subunit-python2 = %{version}-%{release}
%endif

%description -n subunit-python
Python tools for subunit streaming protocol for test results.

%description -n subunit-python -l pl.UTF-8
Pythonowe narzędzia dla protokołu strumieniowego do wyników testów
subunit.

%prep
%setup -q
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/python \
%{__python} -m subunit.run subunit.tests.test_suite | PYTHONPATH=$(pwd)/python %{__python} filters/subunit2pyunit
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/python \
%{__python3} -m subunit.run subunit.tests.test_suite | PYTHONPATH=$(pwd)/python %{__python3} filters/subunit2pyunit
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/subunit/tests
%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	%{__mv} "$f" "${f}-2"
%if %{without python3}
	ln -sf $(basename $f)-2 "$f"
%endif
done
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/subunit/tests

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	if [ "${f%%-2}" = "$f" ]; then
		%{__mv} "$f" "${f}-3"
		ln -sf $(basename $f)-3 "$f"
	fi
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py_sitescriptdir}/subunit
%{py_sitescriptdir}/python_subunit-%{version}-py*.egg-info

%files -n subunit-python2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/subunit-1to2-2
%attr(755,root,root) %{_bindir}/subunit-2to1-2
%attr(755,root,root) %{_bindir}/subunit-filter-2
%attr(755,root,root) %{_bindir}/subunit-ls-2
%attr(755,root,root) %{_bindir}/subunit-notify-2
%attr(755,root,root) %{_bindir}/subunit-output-2
%attr(755,root,root) %{_bindir}/subunit-stats-2
%attr(755,root,root) %{_bindir}/subunit-tags-2
%attr(755,root,root) %{_bindir}/subunit2csv-2
%attr(755,root,root) %{_bindir}/subunit2disk-2
%attr(755,root,root) %{_bindir}/subunit2gtk-2
%attr(755,root,root) %{_bindir}/subunit2junitxml-2
%attr(755,root,root) %{_bindir}/subunit2pyunit-2
%attr(755,root,root) %{_bindir}/tap2subunit-2
%endif

%if %{with python3}
%files -n python3-subunit
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py3_sitescriptdir}/subunit
%{py3_sitescriptdir}/python_subunit-%{version}-py*.egg-info

%files -n subunit-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/subunit-1to2-3
%attr(755,root,root) %{_bindir}/subunit-2to1-3
%attr(755,root,root) %{_bindir}/subunit-filter-3
%attr(755,root,root) %{_bindir}/subunit-ls-3
%attr(755,root,root) %{_bindir}/subunit-notify-3
%attr(755,root,root) %{_bindir}/subunit-output-3
%attr(755,root,root) %{_bindir}/subunit-stats-3
%attr(755,root,root) %{_bindir}/subunit-tags-3
%attr(755,root,root) %{_bindir}/subunit2csv-3
%attr(755,root,root) %{_bindir}/subunit2disk-3
%attr(755,root,root) %{_bindir}/subunit2gtk-3
%attr(755,root,root) %{_bindir}/subunit2junitxml-3
%attr(755,root,root) %{_bindir}/subunit2pyunit-3
%attr(755,root,root) %{_bindir}/tap2subunit-3
%endif

%files -n subunit-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/subunit-1to2
%attr(755,root,root) %{_bindir}/subunit-2to1
%attr(755,root,root) %{_bindir}/subunit-filter
%attr(755,root,root) %{_bindir}/subunit-ls
%attr(755,root,root) %{_bindir}/subunit-notify
%attr(755,root,root) %{_bindir}/subunit-output
%attr(755,root,root) %{_bindir}/subunit-stats
%attr(755,root,root) %{_bindir}/subunit-tags
%attr(755,root,root) %{_bindir}/subunit2csv
%attr(755,root,root) %{_bindir}/subunit2disk
%attr(755,root,root) %{_bindir}/subunit2gtk
%attr(755,root,root) %{_bindir}/subunit2junitxml
%attr(755,root,root) %{_bindir}/subunit2pyunit
%attr(755,root,root) %{_bindir}/tap2subunit
