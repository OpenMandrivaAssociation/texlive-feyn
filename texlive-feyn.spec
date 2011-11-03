# revision 15878
# category Package
# catalog-ctan /fonts/feyn
# catalog-date 2009-10-08 14:27:31 +0200
# catalog-license gpl
# catalog-version 0.3.3
Name:		texlive-feyn
Version:	0.3.3
Release:	1
Summary:	A font for in-text Feynman diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/feyn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Feyn may be used to produce relatively simple Feynman diagrams
within equations in a LaTeX document. While the feynmf package
is good at drawing large diagrams for figures, the present
package and its fonts allow diagrams within equations or text,
at a matching size. The fonts are distributed as MetaFont
source, and macros for their use are also provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/feyn/feyn.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyn10.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyn11.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyn12.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyn18.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyn24.mf
%{_texmfdistdir}/fonts/source/public/feyn/feynmac.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyntext10.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyntext11.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyntext12.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyntext18.mf
%{_texmfdistdir}/fonts/source/public/feyn/feyntext24.mf
%{_texmfdistdir}/fonts/tfm/public/feyn/feyn10.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyn11.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyn12.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyn18.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyn24.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyntext10.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyntext11.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyntext12.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyntext18.tfm
%{_texmfdistdir}/fonts/tfm/public/feyn/feyntext24.tfm
%{_texmfdistdir}/tex/latex/feyn/feyn.sty
%doc %{_texmfdistdir}/doc/fonts/feyn/LICENCE
%doc %{_texmfdistdir}/doc/fonts/feyn/README
%doc %{_texmfdistdir}/doc/fonts/feyn/VERSION
%doc %{_texmfdistdir}/doc/fonts/feyn/exercise-font.pdf
%doc %{_texmfdistdir}/doc/fonts/feyn/exercise-font.tex
%doc %{_texmfdistdir}/doc/fonts/feyn/feyn.pdf
%doc %{_texmfdistdir}/doc/fonts/feyn/overheads.pdf
%doc %{_texmfdistdir}/doc/fonts/feyn/overheads.tex
#- source
%doc %{_texmfdistdir}/source/fonts/feyn/feyn.drv
%doc %{_texmfdistdir}/source/fonts/feyn/feyn.dtx
%doc %{_texmfdistdir}/source/fonts/feyn/feyn.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
