package main

import (
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/container"
    "fyne.io/fyne/v2/widget"
    "fyne.io/fyne/v2"
)

func main() {
    // Create a new application
    myApp := app.New()
    myWindow := myApp.NewWindow("Hello Fyne")

    // Create a button
    button := widget.NewButton("Say Hello", func() {
        fyne.LogInfo("Button pressed", "Hello, World!")
    })

    // Set the content of the window
    myWindow.SetContent(container.NewVBox(button))

    // Show and run the application
    myWindow.ShowAndRun()
}
