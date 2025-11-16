"""
Convert Miles to Kilometres
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_CONVERSION = 1.60934


class ConvertMilesToKilometres(App):
    """Convert Miles to Kilometres App is an app which takes an input, miles and converts to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Convert Miles to Kilometres App."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = 'Result'
        return self.root

    def miles_to_kilometres(self):
        """Convert miles to kilometres."""
        try:
            self.message = str(float(self.root.ids.miles_value.text) * MILES_CONVERSION)
        except ValueError:
            self.message = '0.0'

    def handle_increment(self, i):
        """Increment the miles value by positive or negative one."""
        try:
            self.root.ids.miles_value.text = str(float(self.root.ids.miles_value.text) + i)
        except ValueError:
            self.root.ids.miles_value.text = str(0)
            self.root.ids.miles_value.text = str(float(self.root.ids.miles_value.text) + i)


ConvertMilesToKilometres().run()
