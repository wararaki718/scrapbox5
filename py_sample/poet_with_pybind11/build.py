from pybind11 import get_include
from pybind11.setup_helpers import Pybind11Extension, build_ext


def build(setup_kwargs: dict):
    ext_modules = [
        Pybind11Extension(
            "pybind11_extension",
            ["cpp/hello.cpp"],
            include_dirs=[
                get_include()
            ],
            languate="c++"
        )
    ]

    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmd_class": {"build_ext": build_ext},
        "zip_safe": False
    })
