from django.db import connection
from loader.celery import celery_app


def parse_prices(prices):
    new_prices = list()
    for price in prices:
        splitted_price = price.split('£')
        if len(splitted_price) > 1:
            try:
                new_prices.append(float(splitted_price[1]))
            except:
                new_prices.append(0)    
        else:
            new_prices.append(0)
    return new_prices


@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 2, 'countdown': 2},
)
def insert_items(self, items):
    names = list()
    categories = list()
    prices = list()
    for item in items:
        names.append(item['name'].strip()[:255])
        categories.append(item['category'].strip()[:255])
        prices.append(item['price'].strip()[:255])

    prices = parse_prices(prices)

    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO items_item (
                name,
                category,
                price
            )
            SELECT 
                unnest(%s), 
                unnest(%s), 
                unnest(%s);
            """,
            (names, categories, prices)
        )
