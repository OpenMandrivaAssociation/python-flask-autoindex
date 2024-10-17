%global mod_name	Flask-AutoIndex

Name:		python-flask-autoindex
Version:	0.4.1
Release:	4
Summary:	A mod_autoindex for Flask
Group:		Development/Python
License:	BSD
URL:		https://github.com/sublee/flask-autoindex
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-flask
BuildRequires:	python2-flask
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
Requires:	python-flask
Requires:	python-flask-silk

%description
Flask-AutoIndex generates an index page for your Flask application
automatically. The result just like mod_autoindex, but the look is
more awesome!

%package -n python2-flask-autoindex
Summary:        A mod_autoindex for Flask

%description -n python2-flask-autoindex
Flask-AutoIndex generates an index page for your Flask application
automatically. The result just like mod_autoindex, but the look is
more awesome!

%prep
%setup -q -n %{mod_name}-%{version}

cp -a . %py2dir

%build
%{__python} setup.py build

pushd %py2dir
%{__python2} setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

pushd %py2dir
%{__python2} setup.py install --root %{buildroot}

%files
%doc PKG-INFO README
%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/*.py*
%{python_sitelib}/flaskext/autoindex

%files -n python2-flask-autoindex
%doc PKG-INFO README
%{python2_sitelib}/*-nspkg.pth
%{python2_sitelib}/*.egg-info/
%{python2_sitelib}/flaskext/*.py*
%{python2_sitelib}/flaskext/autoindex

