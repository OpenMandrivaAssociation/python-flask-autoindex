%global mod_name	Flask-AutoIndex

Name:		python-flask-autoindex
Version:	0.4.1
Release:	1
Summary:	A mod_autoindex for Flask
Group:		Development/Python
License:	BSD
URL:		http://github.com/sublee/flask-autoindex
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch
%py_requires -d
Requires:	python-flask
Requires:	python-flask-silk

%description
Flask-AutoIndex generates an index page for your Flask application
automatically. The result just like mod_autoindex, but the look is
more awesome!

%prep
%setup -q -n %{mod_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc PKG-INFO README
%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/*.py*
%{python_sitelib}/flaskext/autoindex