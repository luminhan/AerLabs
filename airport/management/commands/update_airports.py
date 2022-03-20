from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
from airport.models import Airport


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        engine = create_engine('sqlite:///db.sqlite3')
        url = 'https://davidmegginson.github.io/ourairports-data/airports.csv'
        csv = pd.read_csv(url)

        # create new db from certain columns

        updated_csv = csv.filter(['id', 'type', 'name', 'latitude_deg',
                                  'longitude_deg', 'gps_code', 'iata_code'],
                                 axis=1)
        # rename id

        updated_csv = updated_csv.rename(columns={'id': 'Id'})

        number_of_rows_affected = updated_csv.to_sql(
            Airport._meta.db_table,
            con=engine,
            index=False,
            if_exists='replace')

        print(f'{number_of_rows_affected} rows updated.')

