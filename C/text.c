#include <windows.h>

// Function to handle button click events
void OnButtonClick(HWND hwnd) {
    MessageBox(hwnd, "Button Clicked!", "Message", MB_OK);
}

// Window procedure function
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        case WM_COMMAND:
            if (LOWORD(wParam) == 1) {
                OnButtonClick(hwnd);
            }
            return 0;
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
}

int main() {
    // Register the window class
    WNDCLASS wc = {0};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = "MyWindowClass";
    RegisterClass(&wc);

    // Create the window
    HWND hwnd = CreateWindowEx(
        0,
        "MyWindowClass",
        "Simple C GUI App",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 200,
        NULL, NULL, GetModuleHandle(NULL), NULL
    );

    // Create a button
    HWND button = CreateWindow(
        "BUTTON",  // predefined class
        "Click me",      // button text
        WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // styles
        150, 50, 80, 30,  // position and size
        hwnd, NULL, GetModuleHandle(NULL), NULL
    );

    // Set the button identifier
    SetWindowLongPtr(button, GWLP_ID, 1);

    // Show the window
    ShowWindow(hwnd, SW_SHOWNORMAL);

    // Enter the message loop
    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
