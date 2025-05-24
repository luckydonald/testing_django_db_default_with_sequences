from django.db import models



from django.db.models import Func
from django.db.models.expressions import RawSQL


class CurrVal(Func):
    function = 'currval'
    template = '%(function)s(%(expressions)s)'

    def __init__(self, sequence_name, **extra):
        super().__init__(sequence_name, **extra)
    # end def
# end class


class TestSequenceTable4DjangoVersion(models.Model):
    # DB TABLE NAME: "testapp_testsequencetable4djangoversion"
    self_reference = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=False,
        # db_default=CurrVal('test_sequece_table_4_id_seq')
        db_default=RawSQL("currval('testapp_testsequencetable4djangoversion_id_seq')", ())
    )

    def __str__(self):
        return f"TestSequenceTable4(id={self.id}, self_reference={self.self_reference})"
    # end def
# end class

