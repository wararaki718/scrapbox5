#include <string>
#include <nanobind/nanobind.h>


std::string greeding(std::string name) {
    return "hello, " + name;
}

NB_MODULE(hello, m) {
    m.doc() = "hello, world";
    m.def("greeding", &greeding, "hello, message");
}
