class CompanyDefault:
    def __init__(self, company_number, library, web_library, image_alias):
        self.company_number = company_number
        self.library = library
        self.web_library = web_library
        self.image_alias = image_alias


etcetera = CompanyDefault(2, 'etlib', 'weblibet', 'etimages')
carlisle = CompanyDefault(1, 'acsdbase', 'weblibcc', 'simages')

print(etcetera.image_alias)
print(f'the images for carlisle are located at https://www.carlisle-etcetera.com/{carlisle.image_alias}')


companyData = tuple([1, 2, 3, 4])

print(f"{companyData[0]}")
