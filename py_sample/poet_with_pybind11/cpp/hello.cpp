#include <string>
#include <pybind11/pybind11.h>


std::string greeding(std::string name) {
    return "hello, " + name;
}

PYBIND11_MODULE(hello, m) {
    m.doc() = "hello, world";
    m.def("greeding", &greeding, "hello, message");
}
