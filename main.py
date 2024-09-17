from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from placecollection import PlaceCollection


class PlacesApp(App):
    status_text = StringProperty()

    def build(self):
        self.title = "Travel Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.place_collection = PlaceCollection()
        self.place_collection.load("places.csv")
        self.update_places()
        return self.root

    def update_places(self):
        self.root.ids.places_box.clear_widgets()
        for place in self.place_collection.places:
            temp_button = Button(text=place.name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            self.root.ids.places_box.add_widget(temp_button)
        self.status_text = f"To visit: {self.place_collection.get_number_unvisited()}"

    def press_entry(self, instance):
        place = instance.place
        if place.visited:
            place.mark_unvisited()
            self.status_text = f"You need to visit {place.name}."
        else:
            place.mark_visited()
            self.status_text = f"You visited {place.name}."
        if place.is_important():
            self.status_text += " Get going!"
        self.update_places()

    def clear_fields(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        self.status_text = ""

    def add_place(self):
        name = self.root.ids.name_input.text.strip()
        country = self.root.ids.country_input.text.strip()
        priority = self.root.ids.priority_input.text.strip()

        if not name or not country or not priority:
            self.status_text = "All fields must be completed"
            return

        try:
            priority = int(priority)
            if priority < 1:
                self.status_text = "Priority must be > 0"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        new_place = Place(name, country, priority)
        self.place_collection.add(new_place)
        self.clear_fields()
        self.update_places()

    def on_stop(self):
        self.place_collection.save("places.csv")


if __name__ == "__main__":
    PlacesApp().run()
