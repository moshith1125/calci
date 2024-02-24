from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.expression = ''
        self.result = '0'

        layout = BoxLayout(orientation='vertical')
        self.display = Button(text=self.result, font_size=40, size_hint=(1, 0.75))
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            button_row = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                button_row.add_widget(button)
            layout.add_widget(button_row)

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result = str(eval(self.expression))
            except Exception as e:
                self.result = 'Error'
            self.expression = ''
        elif instance.text == 'C':
            self.expression = ''
            self.result = '0'
        else:
            self.expression += instance.text
            self.result = self.expression
        self.display.text = self.result


if __name__ == '__main__':
    CalculatorApp().run()
