from setuptools import setup

from pgimp.doc.GimpDocumentationGenerator import GimpDocumentationGenerator
from pgimp.doc.output.OutputPythonSkeleton import OutputPythonSkeleton
from pgimp.util import file
from pgimp import __version__, project


generate_python_skeleton = GimpDocumentationGenerator(OutputPythonSkeleton(
   file.relative_to(__file__, 'gimp'))
)
generate_python_skeleton()

setup(name=project,
      version=__version__,
      description='Call gimp routines from python3 code.',
      url='https://github.com/mabu-github/pgimp',
      author='Mathias Burger',
      author_email='mathias.burger@gmail.com',
      license='MIT',
      packages=[project, 'gimp', 'gimpenums', 'gimpfu'],
      zip_safe=False
)
