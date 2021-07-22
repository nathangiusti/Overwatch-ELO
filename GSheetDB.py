import gspread


class GSheetDB:

    def __init__(self, config_file_location, sheet_id):
        self.gc = gspread.service_account(config_file_location)
        self.sheet = self.gc.open_by_key(sheet_id)
        self.pages = {}
        page_list = self.sheet.worksheets()
        for page in page_list:
            self.pages[page.title] = GTable(page)


class GTable:

    def __init__(self, page):
        self.page = page
        self.table_name = page.title

    def get_row(self, row_number):
        return self.page.row_values(row_number)

    def add_row(self, values):
        self.page.append_row(values)

    def add_rows(self, values):
        self.page.append_rows(values)

    def get_all_values(self):
        return self.page.get_all_values()
