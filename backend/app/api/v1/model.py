from ...db_con import database_setup

class Manga():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def get_chapters(self):
        # https://drive.google.com/file/d/1ZTAzTcO5dtYDdZ_h24BVT-7rNmx31n71/view
        pass
