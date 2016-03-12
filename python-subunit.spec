#
# This is template for pure python modules (noarch)
# use template-specs/python-ext.spec for binary python packages
#
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# test target

%define 	module	template
Summary:	subunit - streaming protocol for test results
Summary(pl.UTF-8):	subunit - protokół strumieniowy do wyników testów
Name:		python-subunit
Version:	1.2.0
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/python-subunit/
Source0:	https://pypi.python.org/packages/source/p/python-subunit/%{name}-%{version}.tar.gz
# Source0-md5:	3305455dfe22e2b8666531909c026a2f
URL:		https://pypi.python.org/pypi/python-subunit
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-extras
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-testtools >= 0.9.34
%if %{with tests}
BuildRequires:	python-fixtures
BuildRequires:	python-hypothesis
BuildRequires:	python-testscenarios
%endif
%endif
%if %{with python3}
BuildRequires:	python3-extras
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-testtools >= 0.9.34
%if %{with tests}
BuildRequires:	python3-fixtures
BuildRequires:	python3-hypothesis
BuildRequires:	python3-testscenarios
%endif
%endif
Requires:	python-extras
Requires:	python-modules >= 1:2.6
Requires:	python-testtools >= 0.9.34
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subunit is a streaming protocol for test results.

%description -l pl.UTF-8
Subunit to protokół strumieniowy przeznaczony do wyników testów.

%package -n python3-subunit
Summary:	subunit - streaming protocol for test results
Summary(pl.UTF-8):	subunit - protokół strumieniowy do wyników testów
Group:		Libraries/Python
Requires:	python3-extras
Requires:	python3-modules >= 1:3.2
Requires:	python3-testtools >= 0.9.34

%description -n python3-subunit
Subunit is a streaming protocol for test results.

%description -n python3-subunit -l pl.UTF-8
Subunit to protokół strumieniowy przeznaczony do wyników testów.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/subunit/tests

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	%{__mv} "$f" "${f}-3"
done
%endif

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/subunit/tests
%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/*[!3] ; do
	%{__mv} "$f" "${f}-2"
	ln -sf $(basename $f)-2 "$f"
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%attr(755,root,root) %{_bindir}/subunit-1to2
%attr(755,root,root) %{_bindir}/subunit-2to1
%attr(755,root,root) %{_bindir}/subunit-filter
%attr(755,root,root) %{_bindir}/subunit-ls
%attr(755,root,root) %{_bindir}/subunit-notify
%attr(755,root,root) %{_bindir}/subunit-output
%attr(755,root,root) %{_bindir}/subunit-stats
%attr(755,root,root) %{_bindir}/subunit-tags
%attr(755,root,root) %{_bindir}/subunit2csv
%attr(755,root,root) %{_bindir}/subunit2gtk
%attr(755,root,root) %{_bindir}/subunit2junitxml
%attr(755,root,root) %{_bindir}/subunit2pyunit
%attr(755,root,root) %{_bindir}/tap2subunit
%attr(755,root,root) %{_bindir}/subunit-1to2-2
%attr(755,root,root) %{_bindir}/subunit-2to1-2
%attr(755,root,root) %{_bindir}/subunit-filter-2
%attr(755,root,root) %{_bindir}/subunit-ls-2
%attr(755,root,root) %{_bindir}/subunit-notify-2
%attr(755,root,root) %{_bindir}/subunit-output-2
%attr(755,root,root) %{_bindir}/subunit-stats-2
%attr(755,root,root) %{_bindir}/subunit-tags-2
%attr(755,root,root) %{_bindir}/subunit2csv-2
%attr(755,root,root) %{_bindir}/subunit2gtk-2
%attr(755,root,root) %{_bindir}/subunit2junitxml-2
%attr(755,root,root) %{_bindir}/subunit2pyunit-2
%attr(755,root,root) %{_bindir}/tap2subunit-2
%{py_sitescriptdir}/subunit
%{py_sitescriptdir}/python_subunit-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-subunit
%defattr(644,root,root,755)
%doc NEWS README.rst
%attr(755,root,root) %{_bindir}/subunit-1to2-3
%attr(755,root,root) %{_bindir}/subunit-2to1-3
%attr(755,root,root) %{_bindir}/subunit-filter-3
%attr(755,root,root) %{_bindir}/subunit-ls-3
%attr(755,root,root) %{_bindir}/subunit-notify-3
%attr(755,root,root) %{_bindir}/subunit-output-3
%attr(755,root,root) %{_bindir}/subunit-stats-3
%attr(755,root,root) %{_bindir}/subunit-tags-3
%attr(755,root,root) %{_bindir}/subunit2csv-3
%attr(755,root,root) %{_bindir}/subunit2gtk-3
%attr(755,root,root) %{_bindir}/subunit2junitxml-3
%attr(755,root,root) %{_bindir}/subunit2pyunit-3
%attr(755,root,root) %{_bindir}/tap2subunit-3
%{py3_sitescriptdir}/subunit
%{py3_sitescriptdir}/python_subunit-%{version}-py*.egg-info
%endif