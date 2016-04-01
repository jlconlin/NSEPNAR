
# Specify which files to compile
@default_files = ("MCPNAR.tex");

# Always make pdf
$pdf_mode = 1;

# Viewing PDF
$pdf_previewer = "open %S";
$pdf_update_method = 4;
# $pdf_update_command = "open %S";

# Redefine pdflatex to run xelatex instead and call splitindex
$pdflatex = 'xelatex %O %S';

