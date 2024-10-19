from django.core.management.base import BaseCommand
from category.models import SubCategory

class Command(BaseCommand):
    help = 'Will remove all the null subcategories'

    def handle(self, *args, **kwargs):
        user_input = input('Do you want to delete all the null subcategories? [y/N]: ').strip().lower()

        if user_input == 'y':
            try:
                get_null_sub_category = SubCategory.objects.filter(category__isnull=True)
                
                if not get_null_sub_category.exists():
                    self.stdout.write('No NULL subcategories found.')
                    return
                
                for sub_category in get_null_sub_category:
                    self.stdout.write(f'NULL subcategory found: {sub_category.name}')
                
                last_user_input = input('Do you want to delete all the [NULL] subcategories? [y/N]: ').strip().lower()

                if last_user_input == 'y':
                    deleted_count, _ = get_null_sub_category.delete()
                    self.stdout.write(f'{deleted_count} NULL subcategory(ies) deleted successfully.')
                elif last_user_input == 'n':
                    self.stdout.write('Command Aborted.')
                else:
                    self.stdout.write('Invalid command.')
                    
            except Exception as e:
                self.stdout.write(f'Something went wrong: {e}')
        elif user_input == 'n':
            self.stdout.write('Command Aborted.')
        else:
            self.stdout.write('Invalid command.')