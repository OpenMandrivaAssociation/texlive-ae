# revision 15878
# category Package
# catalog-ctan /fonts/ae
# catalog-date 2009-06-30 11:37:01 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-ae
Version:	1.4
Release:	7
Summary:	Virtual fonts for T1 encoded CMR-fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ae
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ae.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ae.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ae.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package name, AE fonts, supposedly
stands for "Almost European". The main use of the package was
to produce PDF files using Adobe Type 1 versions of the CM
fonts instead of bitmapped EC fonts. Note that direct
substitutes for the bitmapped EC fonts are now available, via
the CM-super, Latin Modern and (in a restricted way) CM-LGC
font sets.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/ae/aeb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx5.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx6.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx7.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebx9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aebxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aecsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer17.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer5.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer6.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer7.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aer9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aesl10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aesl12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aesl8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aesl9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aesltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aess10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aess12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aess17.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aess8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aess9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessi10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessi12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessi17.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessi8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aessi9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aetcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeti10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeti12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeti7.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeti8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aeti9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aett10.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aett12.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aett8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/aett9.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/laess8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/laessb8.tfm
%{_texmfdistdir}/fonts/tfm/public/ae/laessi8.tfm
%{_texmfdistdir}/fonts/vf/public/ae/aeb10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx5.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx6.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx7.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebx9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebxsl10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aebxti10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aecsc10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeitt10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer17.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer5.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer6.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer7.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aer9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aesl10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aesl12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aesl8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aesl9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aesltt10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aess10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aess12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aess17.vf
%{_texmfdistdir}/fonts/vf/public/ae/aess8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aess9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessbx10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessdc10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessi10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessi12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessi17.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessi8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aessi9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aetcsc10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeti10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeti12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeti7.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeti8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aeti9.vf
%{_texmfdistdir}/fonts/vf/public/ae/aett10.vf
%{_texmfdistdir}/fonts/vf/public/ae/aett12.vf
%{_texmfdistdir}/fonts/vf/public/ae/aett8.vf
%{_texmfdistdir}/fonts/vf/public/ae/aett9.vf
%{_texmfdistdir}/fonts/vf/public/ae/laess8.vf
%{_texmfdistdir}/fonts/vf/public/ae/laessb8.vf
%{_texmfdistdir}/fonts/vf/public/ae/laessi8.vf
%{_texmfdistdir}/tex/latex/ae/ae.sty
%{_texmfdistdir}/tex/latex/ae/aecompl.sty
%{_texmfdistdir}/tex/latex/ae/omlaer.fd
%{_texmfdistdir}/tex/latex/ae/omsaer.fd
%{_texmfdistdir}/tex/latex/ae/ot1aer.fd
%{_texmfdistdir}/tex/latex/ae/ot1aess.fd
%{_texmfdistdir}/tex/latex/ae/ot1aett.fd
%{_texmfdistdir}/tex/latex/ae/ot1laess.fd
%{_texmfdistdir}/tex/latex/ae/ot1laett.fd
%{_texmfdistdir}/tex/latex/ae/t1aer.fd
%{_texmfdistdir}/tex/latex/ae/t1aess.fd
%{_texmfdistdir}/tex/latex/ae/t1aett.fd
%{_texmfdistdir}/tex/latex/ae/t1laess.fd
%{_texmfdistdir}/tex/latex/ae/t1laett.fd
%doc %{_texmfdistdir}/doc/fonts/ae/COPYING
%doc %{_texmfdistdir}/doc/fonts/ae/MANIFEST
%doc %{_texmfdistdir}/doc/fonts/ae/README
#- source
%doc %{_texmfdistdir}/source/fonts/ae/aefonts.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aefonts.tex
%doc %{_texmfdistdir}/source/fonts/ae/aehax5.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aehaxit.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aehaxrm.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aehaxsc.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aehaxsl.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aehaxss.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aelatin.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aelatint.mtx
%doc %{_texmfdistdir}/source/fonts/ae/aesample.tex
%doc %{_texmfdistdir}/source/fonts/ae/aet1.etx
%doc %{_texmfdistdir}/source/fonts/ae/bxittest.tex
%doc %{_texmfdistdir}/source/fonts/ae/clean
%doc %{_texmfdistdir}/source/fonts/ae/germtest.tex
%doc %{_texmfdistdir}/source/fonts/ae/go
%doc %{_texmfdistdir}/source/fonts/ae/install
%doc %{_texmfdistdir}/source/fonts/ae/makepl
%doc %{_texmfdistdir}/source/fonts/ae/ot1tt.etx
%doc %{_texmfdistdir}/source/fonts/ae/slitest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 749092
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 717800
- texlive-ae
- texlive-ae
- texlive-ae
- texlive-ae
- texlive-ae

