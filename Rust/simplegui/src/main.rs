use iced::{
    button, Align, Column, Command, Container, Element, Length, Settings, Text, Application, Button,
};

pub fn main() -> iced::Result {
    SimpleGui::run(Settings::default())
}

struct SimpleGui {
    // State for the button
    button_state: button::State,
}

impl Application for SimpleGui {
    type Message = ();
    type Executor = iced::executor::Default;
    type Flags = ();

    fn new(_flags: Self::Flags) -> (Self, Command<Self::Message>) {
        (
            SimpleGui {
                button_state: button::State::new(),
            },
            Command::none(),
        )
    }

    fn title(&self) -> String {
        String::from("Simple GUI with Iced")
    }

    fn update(&mut self, _message: Self::Message) -> Command<Self::Message> {
        Command::none()
    }

    fn view(&mut self) -> Element<Self::Message> {
        // Create a simple layout with a blank screen and a button
        let content = Column::new()
            .align_items(Align::Center)
            .padding(20)
            .spacing(20)
            .push(Text::new("This is a simple GUI with a blank screen."))
            .push(
                Button::new(&mut self.button_state, Text::new("Click Me"))
                    .on_press(()), // You can handle button clicks here
            );

        Container::new(content)
            .width(Length::Fill)
            .height(Length::Fill)
            .center_x()
            .center_y()
            .into()
    }
}
