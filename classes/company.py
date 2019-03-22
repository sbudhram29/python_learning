class Company:

    def __init__(self, company):
        if company.lower() == 'carlisle':
            self.__name = 'Carlisle'
            self.__id = 1
            self.__email = 'ccmail@carlisle-etcetera.com'
        elif company.lower() == 'etcetera':
            self.__name = 'Etcetera'
            self.__id = 2
            self.__email = 'etmail@carlisle-etcetera.com'
        else:
            raise Exception(f"Company {company} isn't vaild")

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email


try:
    etcetera = Company('Etcetera')
    carlisle = Company('carlisle')
except Exception as e:
    print(f"{e}")


print(f"{etcetera.name}")
print(f"{etcetera.id}")
print(f"{etcetera.email}")

print("="*30)

print(f"{carlisle.name}")
print(f"{carlisle.id}")
print(f"{carlisle.email}")
