from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from placecollection import PlaceCollection

class PlacesApp(App):
    status_text = StringProperty()

    def build(self):
        self.title = 'Travel Tracker 2.0'
        self.root = Builder.load_file('app.kv')
        self.place_collection = PlaceCollection()
        self.place_collection.load('places.csv')
        self.update_places() 
        return self.root

    def update_places(self):
        self.root.ids.places_box.

    #press entry
    def places
    #clear fields
    #add places

if __name__ == '__main__':
    PlacesApp().run()
