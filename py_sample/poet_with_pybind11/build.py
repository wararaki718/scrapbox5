from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = "0.0.1"

def build(setup_kwargs: dict):
    ext_modules = [
        Pybind11Extension(
            "hello",
            ["cpp/hello.cpp"],
            define_macros = [('VERSION_INFO', __version__)],
            languate="c++"
        )
    ]

    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmdclass": {"build_ext": build_ext},
        "zip_safe": False
    })
