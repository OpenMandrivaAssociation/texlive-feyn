Name:		texlive-feyn
Version:	63945
Release:	2
Summary:	A font for in-text Feynman diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/feyn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feyn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Feyn may be used to produce relatively simple Feynman diagrams
within equations in a LaTeX document. While the feynmf package
is good at drawing large diagrams for figures, the present
package and its fonts allow diagrams within equations or text,
at a matching size. The fonts are distributed as MetaFont
source, and macros for their use are also provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/feyn
%{_texmfdistdir}/fonts/tfm/public/feyn
%{_texmfdistdir}/tex/latex/feyn
%doc %{_texmfdistdir}/doc/fonts/feyn
#- source
%doc %{_texmfdistdir}/source/fonts/feyn

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
