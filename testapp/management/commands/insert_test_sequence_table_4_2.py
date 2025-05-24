import logging
from typing import Any, Self

from luckydonaldUtils.logger import logging

from django.core.management.base import BaseCommand
from django.db import connection, IntegrityError
from django.db.models.expressions import DatabaseDefault, Ref, Expression

logger = logging.getLogger(__name__)
logging.add_colored_handler(level=logging.DEBUG)

try:
    from testapp.models import TestSequenceTable4DjangoVersion
except ImportError:
    from ...models import TestSequenceTable4DjangoVersion
# end try



class WierdHackyExpressionThing(Expression):
    """ apparently some kind of expression with resolve_expression function is needed to use the DatabaseDefault expression ?!?"""
    def resolve_expression(self, *args, **kwargs) -> Self:
        return self
    # end def
# end class



class Command(BaseCommand):
    help = 'Insert a default row into MyModel'

    def handle(self, *args, **kwargs):
        # Insert DEFAULT values
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to VALUES (DEFAULT, DEFAULT);
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to INSERT INTO ... ("id", "self_reference") VALUES (DEFAULT, DEFAULT);
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to INSERT INTO ... ("id") VALUES (DEFAULT);
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to INSERT INTO ... ("self_reference") VALUES (DEFAULT);
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to DEFAULT VALUES

        # Insert with self_reference set to 1
        TestSequenceTable4DjangoVersion.objects.create(self_reference=TestSequenceTable4DjangoVersion.objects.get(pk=1))

        # Insert with specific id
        TestSequenceTable4DjangoVersion.objects.create(id=7)
        TestSequenceTable4DjangoVersion.objects.create(id=8)
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=7)
            raise AssertionError('Should have raised an IntegrityError')
        except IntegrityError:
            print('IntegrityError raised as expected')
        # end def

        # Set the sequence value to the max id
        with connection.cursor() as cursor:
            cursor.execute(
                '''SELECT SETVAL('testapp_testsequencetable4djangoversion_id_seq',
                                 (SELECT MAX("id") FROM "testapp_testsequencetable4djangoversion"))''',
                [],
            )

        # Insert with self_reference set to 9
        TestSequenceTable4DjangoVersion.objects.create(self_reference_id=9)

        # Try to find an equivalent to DEFAULT
        try:
            TestSequenceTable4DjangoVersion.objects.create()
            logger.success(f"Can use DEFAULT by ommiting `self_reference`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by ommiting `self_reference`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=None)
            logger.success(f"Can use DEFAULT by `self_reference=None`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=None`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=None)
            logger.success(f"Can use DEFAULT by `self_reference_id=None`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=None`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=DatabaseDefault())  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference=DatabaseDefault()`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=DatabaseDefault()`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=DatabaseDefault())  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference_id=DatabaseDefault()`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=DatabaseDefault()`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=DatabaseDefault(None))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference=DatabaseDefault(None)`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=DatabaseDefault(None)`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=DatabaseDefault(None))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference_id=DatabaseDefault(None)`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=DatabaseDefault(None)`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default)`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default)`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default)`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion.self_reference.db_default)`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion()))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion())`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=DatabaseDefault(TestSequenceTable4DjangoVersion())`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion()))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion())`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=DatabaseDefault(TestSequenceTable4DjangoVersion())`.\n{e}")
        # end try

        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference=DatabaseDefault(WierdHackyExpressionThing()))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference=DatabaseDefault(WierdHackyExpressionThing())`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference=DatabaseDefault(WierdHackyExpressionThing())`.\n{e}")
        # end try
        try:
            TestSequenceTable4DjangoVersion.objects.create(self_reference_id=DatabaseDefault(WierdHackyExpressionThing()))  # Equivalent to DEFAULT VALUES
            logger.success(f"Can use DEFAULT by `self_reference_id=DatabaseDefault(WierdHackyExpressionThing())`.")
        except Exception as e:
            logger.error(f"Can't use DEFAULT by `self_reference_id=DatabaseDefault(WierdHackyExpressionThing())`.\n{e}")
        # end try

        # Insert another DEFAULT value
        TestSequenceTable4DjangoVersion.objects.create()  # Equivalent to DEFAULT VALUES

        # Fetch and display all records
        all_records = TestSequenceTable4DjangoVersion.objects.all()
        for record in all_records:
            self.stdout.write(str(record))