init python:
    class Notes():
        def __init__(self, items):
            self.items = items
        
        # Method adds an element 'item' to the items list of Notes
        # ...if the text of the new item doesn't exist already somewhere in this list
        def add_data(self, item):
            global phone_not_notes
            for it_item in self.items:
                if it_item.text == item.text:
                    return
            self.items.append(item)
            renpy.notify("Information added to your notebook.")
            phone_not_notes = True
        
        def remove_data(self, item):
            self.items.remove(item)

        def get_items_list(self):
            return self.items
    

    class NoteData():
        def __init__(self, text):
            self.text = text
        
init python:
    class Pictures():
        def __init__(self, items):
            self.items = items
        
        # Method adds an element 'item' to the items list of Notes
        # ...if the text of the new item doesn't exist already somewhere in this list
        def add_data(self, item, notification):
            global phone_not_gallery
            #for it_item in self.items:
                #if it_item.text == item.text:
                    #return
            self.items.append(item)
            if notification:
                renpy.notify("Picture added to your gallery.")
                phone_not_gallery = True

        
        def remove_data(self, item):
            self.items.remove(item)

        def get_items_list(self):
            return self.items

        def get_picture(self, index):
            return self.items[index]
