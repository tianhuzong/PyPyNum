from setuptools import setup,find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import os
os.chdir("pypynum")
extensions = [
    Extension("pypynum.Array", ["Array.py"]),
    Extension("pypynum.chars", ["chars.py"]),
    Extension("pypynum.cipher", ["cipher.py"]),
    Extension("pypynum.constants", ["constants.py"]),
    Extension("pypynum.equations", ["equations.py"]),
    Extension("pypynum.errors", ["errors.py"]),
    Extension("pypynum.file", ["file.py"]),
    Extension("pypynum.FourierT", ["FourierT.py"]),
    Extension("pypynum.Geometry", ["Geometry.py"]),
    Extension("pypynum.Graph", ["Graph.py"]),
    Extension("pypynum.Group", ["Group.py"]),
    Extension("pypynum.image", ["image.py"]),
    Extension("pypynum.Logic", ["Logic.py"]),
    Extension("pypynum.maths", ["maths.py"]),
    Extension("pypynum.Matrix", ["Matrix.py"]),
    Extension("pypynum.NeuralN", ["NeuralN.py"]),
    Extension("pypynum.numbers", ["numbers.py"]),
    Extension("pypynum.plotting", ["plotting.py"]),
    Extension("pypynum.polynomial", ["polynomial.py"]),
    Extension("pypynum.probability", ["probability.py"]),
    Extension("pypynum.Quaternion", ["Quaternion.py"]),
    Extension("pypynum.random", ["random.py"]),
    Extension("pypynum.regression", ["regression.py"]),
    Extension("pypynum.sequence", ["sequence.py"]),
    Extension("pypynum.Symbolics", ["Symbolics.py"]),
    Extension("pypynum.Tensor", ["Tensor.py"]),
    Extension("pypynum.test", ["test.py"]),
    Extension("pypynum.this", ["this.py"]),
    Extension("pypynum.tools", ["tools.py"]),
    Extension("pypynum.Tree", ["Tree.py"]),
    Extension("pypynum.types", ["types.py"]),
    Extension("pypynum.ufuncs", ["ufuncs.py"]),
    Extension("pypynum.utils", ["utils.py"]),
    Extension("pypynum.Vector", ["Vector.py"]),

]
setup(name="pypynum",ext_modules=cythonize(extensions))
