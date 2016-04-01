% Nuclear Science and Engineering template
% by Jeremy Lloyd Conlin
%
% Usage: \documentclass{nse}

\NeedsTeXFormat{LaTeX2e}[1995/12/01]

\ProvidesClass{ansnse}[2008/01/14 v1.00 ANS Nuclear Science and Engineering class]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TYPE AND GEOMETRY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\LoadClass[10pt]{article}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INCLUDE PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%math without the times font %%%
%\RequirePackage{times}
%%%% if you want math to be in times: %%%%
\RequirePackage[T1]{fontenc}
%\RequirePackage{mathptmx}
%%%%%%%%%
%\RequirePackage{cuted} % for single column in a multicolumn doc
%\RequirePackage{ccaption}	% modify caption style

\RequirePackage{multicol}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Bibliography and Citations %%%%%%%%%%%%%%%%%
\usepackage[super, sort&compress]{natbib}
\citestyle{nature}
\bibliographystyle{unsrtnat}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ABSTRACT %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage[runin]{abstract}

\renewcommand{\abstracttextfont}{\normalfont\itshape}
\renewcommand{\abstractname}{Abstract ---}
\setlength{\absleftindent} {5.0em}
\setlength{\absrightindent}{5.0em}
\setlength{\abstitleskip}{-\absparindent}
%\setlength{\absparindent}{0em}

\newcommand{\ansabstract}[1]{
    \maketitle
    \begin{onecolabstract}#1 \end{onecolabstract}
    \vspace{3\parsep}
%   \saythanks
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SPACING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{setspace}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SECTIONING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand*\thesection{\Roman{section}}
\renewcommand*\thesubsection{\Roman{section}.\Alph{subsection}}
\renewcommand*\thesubsubsection{\Roman{section}.\Alph{subsection}.\arabic{subsubsection}}

\renewcommand\section{\@startsection{section}{1}{0pt}%		%name, level, indent
	{-\baselineskip}%		%beforeskip
	{.75\baselineskip}%		%afterskip
    {\centering\textsc}%
}

\renewcommand\subsection{\@startsection{subsection}{2}{0pt}%		%name, level, indent
	{-\baselineskip}%		%beforeskip
	{.75\baselineskip}%		%afterskip
    {\centering\textit}%
}

\renewcommand\subsubsection{\@startsection{subsubsection}{3}{-1em}%		%name, level, indent
	{-.75\baselineskip}%		%beforeskip
	{.5\baselineskip}%		%afterskip
	{\centering}%
}
