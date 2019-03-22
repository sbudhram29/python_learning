from company import Company


class TestClass(object):
    @classmethod
    def setup_class(cls):
        cls.company = Company('carlisle')

    def test_name(self):
        assert self.company.name == 'Carlisle'

    def test_email(self):
        assert self.company.email == 'ccmail@carlisle-etcetera.com'

    def test_id(self):
        assert self.company.id == 1
