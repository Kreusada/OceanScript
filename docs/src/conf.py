exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv"]
html_css_files = ["literals.css"]
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
]
templates_path = ["_templates"]
master_doc = "index"
html_theme = "furo"
html_static_path = ["static"]
source_suffix = ".rst"
master_doc = "index"
project = "Kreusada-Cogs"
copyright = "2021 - 2022 | Kreusada"
author = "Kreusada"
html_logo = "image_cog-creators-logo.png"
html_context = {
    "display_github": True,
    "github_user": "Kreusada",
    "github_repo": "OceanScript",
    "github_version": "master/docs/",
}

from oceanscript import __version__ as release

version = ".".join(release.split(".")[:2])
