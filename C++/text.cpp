
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class TextEditor {
public:
    void run() {
        std::string command;
        while (true) {
            std::cout << "Enter command (new, open, save, edit, exit): ";
            std::cin >> command;

            if (command == "new") {
                createNewFile();
            } else if (command == "open") {
                openFile();
            } else if (command == "save") {
                saveFile();
            } else if (command == "edit") {
                editFile();
            } else if (command == "exit") {
                break;
            } else {
                std::cout << "Unknown command. Please try again." << std::endl;
            }
        }
    }

private:
    std::string filename;
    std::vector<std::string> lines;

    void createNewFile() {
        std::cout << "Enter filename: ";
        std::cin >> filename;
        lines.clear();
        std::cout << "New file created: " << filename << std::endl;
    }

    void openFile() {
        std::cout << "Enter filename to open: ";
        std::cin >> filename;
        std::ifstream file(filename);
        if (!file) {
            std::cout << "Could not open file: " << filename << std::endl;
            return;
        }
        lines.clear();
        std::string line;
        while (std::getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
        std::cout << "File opened: " << filename << std::endl;
    }

    void saveFile() {
        if (filename.empty()) {
            std::cout << "No file to save. Please create or open a file first." << std::endl;
            return;
        }
        std::ofstream file(filename);
        for (const auto& line : lines) {
            file << line << std::endl;
        }
        file.close();
        std::cout << "File saved: " << filename << std::endl;
    }

    void editFile() {
        std::cout << "Editing file. Type 'done' to finish editing." << std::endl;
        std::string line;
        while (true) {
            std::cout << "> ";
            std::cin.ignore(); // Clear the newline character from the input buffer
            std::getline(std::cin, line);
            if (line == "done") {
                break;
            }
            lines.push_back(line);
        }
    }
};

int main() {
    TextEditor editor;
    editor.run();
    return 0;
}
