
package main

import (
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/container"
    "fyne.io/fyne/v2/widget"
)

func main() {
    myApp := app.New()
    myWindow := myApp.NewWindow("Hello Fyne")

    label := widget.NewLabel("Hello, World!")
    button := widget.NewButton("Click Me", func() {
        label.SetText("Button Clicked!")
    })

    myWindow.SetContent(container.NewVBox(label, button))
    myWindow.ShowAndRun()
}
