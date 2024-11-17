#include <wx/wx.h>
#include <wx/stc/stc.h>
#include <fstream>

class TextEditor : public wxFrame {
public:
    TextEditor(const wxString& title);

private:
    wxStyledTextCtrl* textCtrl;
    
    void OnOpen(wxCommandEvent& event);
    void OnSave(wxCommandEvent& event);
    void OnQuit(wxCommandEvent& event);

    wxDECLARE_EVENT_TABLE();
};

enum {
    ID_Open = 1,
    ID_Save
};

wxBEGIN_EVENT_TABLE(TextEditor, wxFrame)
    EVT_MENU(ID_Open, TextEditor::OnOpen)
    EVT_MENU(ID_Save, TextEditor::OnSave)
    EVT_MENU(wxID_EXIT, TextEditor::OnQuit)
wxEND_EVENT_TABLE()

TextEditor::TextEditor(const wxString& title) : wxFrame(nullptr, wxID_ANY, title, wxDefaultPosition, wxSize(800, 600)) {
    // Create Menu
    wxMenuBar* menuBar = new wxMenuBar;
    wxMenu* fileMenu = new wxMenu;
    fileMenu->Append(ID_Open, "&Open...\tCtrl+O");
    fileMenu->Append(ID_Save, "&Save...\tCtrl+S");
    fileMenu->Append(wxID_EXIT, "&Quit\tCtrl+Q");
    menuBar->Append(fileMenu, "&File");
    SetMenuBar(menuBar);

    // Create the text control (editor)
    textCtrl = new wxStyledTextCtrl(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE);
}

void TextEditor::OnOpen(wxCommandEvent& event) {
    wxFileDialog openFileDialog(this, _("Open Text file"), "", "",
                                "Text files (*.txt)|*.txt", wxFD_OPEN | wxFD_FILE_MUST_EXIST);

    if (openFileDialog.ShowModal() == wxID_CANCEL) return;

    std::ifstream file(openFileDialog.GetPath().ToStdString());
    if (file.is_open()) {
        std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        textCtrl->SetText(content);
        file.close();
    }
}

void TextEditor::OnSave(wxCommandEvent& event) {
    wxFileDialog saveFileDialog(this, _("Save Text file"), "", "",
                                "Text files (*.txt)|*.txt", wxFD_SAVE | wxFD_OVERWRITE_PROMPT);

    if (saveFileDialog.ShowModal() == wxID_CANCEL) return;

    std::ofstream file(saveFileDialog.GetPath().ToStdString());
    if (file.is_open()) {
        file << textCtrl->GetText().ToStdString();
        file.close();
    }
}

void TextEditor::OnQuit(wxCommandEvent& event) {
    Close(true);
}

class MyApp : public wxApp {
public:
    virtual bool OnInit();
};

wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit() {
    TextEditor* editor = new TextEditor("Simple wxWidgets Text Editor");
    editor->Show(true);
    return true;
}
