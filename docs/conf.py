# -*- coding: utf-8 -*-
#
# F5 WAF Autoscale AWS Guide documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 17 17:29:37 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# BEGIN CONFIG
# ------------
#
# REQUIRED: Your class/lab name
classname = "F5 WAF AWS AWS Guide"

# OPTIONAL: The URL to the GitHub Repository for this class
github_repo = "https://github.com/tkam8/f5waf_autoscale_aws_guide"

# OPTIONAL: Google Analytics
# googleanalytics_id = 'UA-85156643-4'

#
# END CONFIG
# ----------


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
import time
import re
import pkgutil
import string
sys.path.insert(0, os.path.abspath('.'))
import f5_sphinx_theme

year = time.strftime("%Y")
eventname = "F5 WAF Autoscale AWS Guide %s" % (year)

rst_prolog = """
.. |classname| replace:: %s
.. |classbold| replace:: **%s**
.. |classitalic| replace:: *%s*
.. |ltm| replace:: Local Traffic Manager
.. |adc| replace:: Application Delivery Controller
.. |gtm| replace:: Global Traffic Manager
.. |dns| replace:: DNS
.. |asm| replace:: Application Security Manager
.. |afm| replace:: Advanced Firewall Manager
.. |apm| replace:: Access Policy Manager
.. |pem| replace:: Policy Enforcement Manager
.. |ipi| replace:: IP Intelligence
.. |iwf| replace:: iWorkflow
.. |biq| replace:: BIG-IQ
.. |bip| replace:: BIG-IP
.. |aiq| replace:: APP-IQ
.. |ve|  replace:: Virtual Edition
.. |icr| replace:: iControl REST API
.. |ics| replace:: iControl SOAP API
.. |f5|  replace:: F5 Networks
.. |f5i| replace:: F5 Networks, Inc.
.. |year| replace:: %s
""" % (classname,
       classname,
       classname,
       year)

if 'github_repo' in locals() and len(github_repo) > 0:
    rst_prolog += """
.. |repoinfo| replace:: このガイドのコンテンツは、完全な
　　　　　　　　　　　DevOps CI /CDパイプラインを活用しており、以下のGitHubリポジトリから取得可能です。 
　　　　　　　　　　　%s
""" % (github_repo)
else:
    rst_prolog += """
.. |repoinfo| replace:: \ \n"
"""

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_snops = os.environ.get('SNOPS_ISALIVE', None) == 'True'

print "on_rtd = %s" % on_rtd
print "on_snops = %s" % on_snops

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 WAF Autoscale AWS Guide'
copyright = u'2017, Terence Kam (F5)'
author = u'Terence Kam (F5)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'f5_sphinx_theme'
html_theme_path = f5_sphinx_theme.get_html_theme_path()
html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html','relations.html']}
html_theme_options = {
                        'site_name': 'F5 WAF Autoscale AWS Guide',
                        'next_prev_link': True
                     }

def setup(app):
    app.add_stylesheet('css/f5_agility_theme.css')

if on_rtd:
    templates_path = ['_templates']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

cleanname = re.sub('\W+','',classname)

# Output file base name for HTML help builder.
htmlhelp_basename =  cleanname + 'doc'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'platex'

front_cover_image = 'front_cover'
back_cover_image = 'back_cover'

front_cover_image_path = os.path.join('_static', front_cover_image + '.png')
back_cover_image_path = os.path.join('_static', back_cover_image + '.png')

latex_additional_files = [front_cover_image_path, back_cover_image_path]

template = string.Template(open('preamble.tex').read())

latex_contents = r"""
\frontcoverpage
\contentspage
"""

backcover_latex_contents = r"""
\backcoverpage
"""

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'preamble': template.substitute(eventname=eventname,
                                    project=project,
                                    author=author,
                                    frontcoverimage=front_cover_image,
                                    backcoverimage=back_cover_image),

    'tableofcontents': latex_contents,
    'printindex': backcover_latex_contents,
	'classoptions': ',dvipdfmx',
	'babel': '\usepackage[japanese]{babel}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '%s.tex' % cleanname, u'%s Documentation' % classname,
     u'F5 Networks, Inc.', 'manual', True),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, cleanname.lower(), u'%s Documentation' % classname,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, classname, u'%s Documentation' % classname,
     author, classname, classname,
     'Training'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

