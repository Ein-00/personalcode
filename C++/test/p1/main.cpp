#include <iostream>
#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

int main() {
    fs::path p(".");

    if (fs::exists(p) && fs::is_directory(p)) {
        for (auto& entry : fs::directory_iterator(p)) {
            std::cout << entry.path().string() << std::endl;
        }
    } else {
        std::cout << "Path does not exist or is not a directory" << std::endl;
    }

    return 0;
}
