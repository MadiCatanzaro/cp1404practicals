"""
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR = (0.5, 0.25, 0.75, 1)


class DynamicLabelsApp(App):
    """Dynamic Labels App is an app which generates dynamic labels using a provided list of names."""

    def __init__(self, **kwargs):
        """Initialise the Dynamic Labels App."""
        super().__init__(**kwargs)
        self.names = ['Bert', 'Moss', 'Rex']

    def build(self):
        """Build the Dynamic Labels App."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create the labels from the list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
