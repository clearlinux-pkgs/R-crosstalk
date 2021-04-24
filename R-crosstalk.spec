#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-crosstalk
Version  : 1.1.1
Release  : 33
URL      : https://cran.r-project.org/src/contrib/crosstalk_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/crosstalk_1.1.1.tar.gz
Summary  : Inter-Widget Interactivity for HTML Widgets
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: R-R6
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-lazyeval
Requires: R-shiny
BuildRequires : R-R6
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
with each other, with Shiny or without (i.e. static .html files). Currently
    supports linked brushing and filtering.

%prep
%setup -q -c -n crosstalk
cd %{_builddir}/crosstalk

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610466578

%install
export SOURCE_DATE_EPOCH=1610466578
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crosstalk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crosstalk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crosstalk
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc crosstalk || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/crosstalk/DESCRIPTION
/usr/lib64/R/library/crosstalk/INDEX
/usr/lib64/R/library/crosstalk/LICENSE
/usr/lib64/R/library/crosstalk/Meta/Rd.rds
/usr/lib64/R/library/crosstalk/Meta/features.rds
/usr/lib64/R/library/crosstalk/Meta/hsearch.rds
/usr/lib64/R/library/crosstalk/Meta/links.rds
/usr/lib64/R/library/crosstalk/Meta/nsInfo.rds
/usr/lib64/R/library/crosstalk/Meta/package.rds
/usr/lib64/R/library/crosstalk/NAMESPACE
/usr/lib64/R/library/crosstalk/NEWS.md
/usr/lib64/R/library/crosstalk/R/crosstalk
/usr/lib64/R/library/crosstalk/R/crosstalk.rdb
/usr/lib64/R/library/crosstalk/R/crosstalk.rdx
/usr/lib64/R/library/crosstalk/help/AnIndex
/usr/lib64/R/library/crosstalk/help/aliases.rds
/usr/lib64/R/library/crosstalk/help/crosstalk.rdb
/usr/lib64/R/library/crosstalk/help/crosstalk.rdx
/usr/lib64/R/library/crosstalk/help/paths.rds
/usr/lib64/R/library/crosstalk/html/00Index.html
/usr/lib64/R/library/crosstalk/html/R.css
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap-theme.css
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap-theme.css.map
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap-theme.min.css
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap-theme.min.css.map
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap.css
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap.css.map
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap.min.css
/usr/lib64/R/library/crosstalk/lib/bootstrap/css/bootstrap.min.css.map
/usr/lib64/R/library/crosstalk/lib/bootstrap/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/crosstalk/lib/bootstrap/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/crosstalk/lib/bootstrap/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/crosstalk/lib/bootstrap/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/crosstalk/lib/bootstrap/fonts/glyphicons-halflings-regular.woff2
/usr/lib64/R/library/crosstalk/lib/bootstrap/js/bootstrap.js
/usr/lib64/R/library/crosstalk/lib/bootstrap/js/bootstrap.min.js
/usr/lib64/R/library/crosstalk/lib/bootstrap/js/npm.js
/usr/lib64/R/library/crosstalk/lib/bootstrap/shim/html5shiv.min.js
/usr/lib64/R/library/crosstalk/lib/bootstrap/shim/respond.min.js
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinFlat.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinHTML5.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinModern.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinNice.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinShiny.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/ion.rangeSlider.skinSimple.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/css/normalize.css
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/img/sprite-skin-flat.png
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/img/sprite-skin-modern.png
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/img/sprite-skin-nice.png
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/img/sprite-skin-simple.png
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/js/ion.rangeSlider.js
/usr/lib64/R/library/crosstalk/lib/ionrangeslider/js/ion.rangeSlider.min.js
/usr/lib64/R/library/crosstalk/lib/jquery/jquery-AUTHORS.txt
/usr/lib64/R/library/crosstalk/lib/jquery/jquery.js
/usr/lib64/R/library/crosstalk/lib/jquery/jquery.min.js
/usr/lib64/R/library/crosstalk/lib/jquery/jquery.min.map
/usr/lib64/R/library/crosstalk/lib/selectize/css/selectize.bootstrap3.css
/usr/lib64/R/library/crosstalk/lib/selectize/js/es5-shim.min.js
/usr/lib64/R/library/crosstalk/lib/selectize/js/selectize.min.js
/usr/lib64/R/library/crosstalk/lib/strftime/strftime-min.js
/usr/lib64/R/library/crosstalk/tests/testthat.R
/usr/lib64/R/library/crosstalk/tests/testthat/test-crosstalk.R
/usr/lib64/R/library/crosstalk/www/css/crosstalk.css
/usr/lib64/R/library/crosstalk/www/js/crosstalk.js
/usr/lib64/R/library/crosstalk/www/js/crosstalk.js.map
/usr/lib64/R/library/crosstalk/www/js/crosstalk.min.js
/usr/lib64/R/library/crosstalk/www/js/crosstalk.min.js.map
