سلام توی این پست میخوام راجب یه SQL Query صحبت کنم که چند روز پیش برای یک پروژه نوشتم بنظرم چالش جالبی بود واسه خودم و ارزش اینو داشت که یه پست کوتاه راجبش بنویسم

اول دیزاین دیتابیس رو توضیح  میدم و بعد میریم سراغ چالش
لطفا لطفا اول پست رو کامل بخونید بعد پیشنهاد یا انتقاد بدید چون یکسری از دلایل نحوه دیزاین در قسمت دوم پست مشخص میشه


خب تصور کنید یه تیبل  products داریم که فقط یک فیلد title داره به این شکل
```
 id |       title
----+------------------------
  1 | Sample Product 1
  2 | Sample Product 2
  3 | Sample Product 3
(3 rows)
```

و حالا هر کدوم از product های ما میتونه یکسری attribute و به قولی ویژگی داشته باشه مثلا وزن و طول و عرض و میخوایم برای این ها مقداری مشخص کنیم خب در مرحله اول احتمالن میگید خب بیایم یه تیبل دیگه بسازیم برای attributes به این شکل

```
 id |      title      | product_id | value
----+-----------------+------------+-------
  1 | Height          | 2          | 10.5
  2 | Length          | 3          | 20.0
  3 | Width           | 2          | 5.5
(3 rows)
```

ولی خب داخل تیبل مثل این مشکلی که وجود داره اینه که اگر ما attribute های زیادی داخل دیتابیس داشته باشیم و بین این attribute ها title های مشترک زیادی وجود داشته باشه و ما بخوایم برای هر attribute معادل فارسی یا فیلد های دیگه اضافه کنیم

باید فضای زیادی رو برای این دیتای تکراری داشته باشیم بنابراین در این مواقع راه حل پیشنهادی normalization هست (اگر نمیدونید چیه داخل چنل تلگرام راجبش چنتا پست نوشتم)

البته در کیس من یک دلیل دیگه هم برای normalization تایتل ها وجود داشت اونم فیلتر کردن بود که جلوتر بهش میرسیم

در این مورد به خصوص نرمالایزیشن نتیجه اش میشه یه تیبل دیگه به نام  attribute_title و اسم تیبلی که قراره با product رابطه داشته باشه  هم میشه attribute_value 
به این شکل

```
attribute_title:

 id |      title    |    title_fa
----+---------------|-------------------
  1 | Height        |   ارتفاع
  2 | Length        |   طول
  3 | Width         |   عرض
(3 rows)
```

و تیبل دیگه امون هم میشه این شکلی
```
attribute_value:
 id |       value        | attribute_id | product_id
----+--------------------+--------------+------------
 1  |  10.5              |            1 |          1
 2  |  20.0              |            2 |          1
 3  |  5.5               |            3 |          1
```

خب تا الان میتونیم خوشحال باشیم که یکمقدار ساختار رو بهتر کردیم
ولی داخل پروژه ما قراره value تکراری خیلی زیادی داشته باشیم یعنی مثلا طول و عرض 100 تا محصول ممکنه یکی باشه
برای همین باید یه بار دیگه نرمالایزیشن انجام بدیم و رابطه محصول و attribute_value رو از o2m به m2m تغییر بدیم
فیلد ایدی محصول رو از این تیبل حذف میکنیم
```
attribute_value:
 id |       value        | attribute_id |
----+--------------------+-------------
 1  |  10.5              |            1 |
 2  |  20.0              |            2 |
 3  |  5.5               |            3 |
```

و یک تیبل جدید به این شکل میسازیم
```
product_attributes
 id | product_id | attributevalue_id
----+------------+-------------------
 1  |          1 |               321
 2  |          1 |               322
 3  |          1 |               323
```
که بهمون میگه هر پروداکت جه attribute هایی داره و همینطور attribute ها مشترک هم هستن بین محصولات
اگر متوجه یک مشکل شدی اینجا صبر کن بهش میرسیم ;)


پست دوم: چالش اصلی که من رو به اون دیزاین رسوند

خب ما داخل پروژه یک فیلترینگ خاص برای محصول نیاز داریم
 به این صورت که محصولات داخل یک دسته بندی خاص یکسری ویژگی دارند مثلا محصولات دسته بندی میز همشون طول و عرض و ارتفاع دارند
و حالا داخل فیلترینگ محصولات میز ما باید همه ویژگی هارو ببینیم و از مقدار همه ویژگی ها قابلیت فیلتر کردن داشته باشیم به این شکل که فیلتر های دسته بندی میز اینشکلی میشه

```json
[
  {
    "attribute_id": 1,
    "attribute_title": "Height",
    "attribute_title_fa": "ارتفاع",
    "values": [
        {
            "id": 1,
            "value": "100"
        },
        {
            "id": 2,
            "value": "120"
        }
    ]
  },
    {
    "attribute_id": 2,
    "attribute_title": "Width",
    "attribute_title_fa": "عرض",
    "values": [
        {
            "id": 3,
            "value": "20"
        },
        {
            "id": 4,
            "value": "30"
        }
    ]
  }
]
```
و ما این دیتای values رو باید بر اساس دیتای attribute_value های همه محصولات اون دسته بندی بیاریم بیرون و بر اساس attribute هاشون مرتب کنیم که خروجیش بشه این
و همینطور باید کاملا داینامیک باشه مثلا اینجوری نمیشه که شما بیای یکبار اینارو در بیاری و بریزی داخل کش



---
خب پس تا اینجا ما 2 تا کوعری خفن نیاز داریم

یه کوعری که بهش ایدی دسته بندی بدیم و بهمون دیتای بخش فیلتر کردن رو برگردونه 

یه کوعری هم که چنتا ایدی attribute_value بدیم و اونم همه محصولاتی که اون چنتا رو دارن بهمون برگردونه تاکید میکنم که کوعری مون باید چنتا attribute_value بگیره



حالا واسه سنجش سطح SQL خودتون هم که شده قبل از اینکه برید ادامه رو بخونید سعی کنید بنویسید این Query هارو :)


واسه کوعری بخش اول ما با یک subquery میایم ایدی همه محصولات یک دسته بندی رو درمیاریم
بعد از اون میایم یک کوعری مینویسیم و از تیبل attribute_value مقدار value و id و با استفاده از join به تیبل attribute فیلد های attribute رو هم میگیریم
و خب از اونجایی که خروجی الانمون تمیز نیست میایم توی سطح کد خروجی کوعری رو بر اساس attribute_title گروه بندی میکنیم
بزارید واسه شفاف سازی کد sql و بخش کد پایتونش که با django orm نوشتم رو بهتون نشون بدم

```sql
SELECT
    "attributevalue"."id",
    "attributevalue"."value",
    "attributevalue"."attribute_id",
    "attribute"."title",
    "attribute"."title_fa"
FROM
    "attributevalue"
    INNER JOIN "attribute" ON (
        "attributevalue"."attribute_id" = "attribute"."id"
    )
WHERE
    "attributevalue"."id" IN (
        SELECT
            "product"."id"
        FROM
            "product" 
        WHERE
            "product"."category_id" = 1
    )
```
و اینم از کد پایتونش که در بخش دوم میبینید چطوری گروه بندی کردم

```python

def get_category_filters(category_id: int):
    products_ids = Product.objects.filter(category_id=category_id).values_list("pk", flat=True)
    result = (
        AttributeValue.objects.select_related("attribute")
        .filter(id__in=products_ids)
        .values(
            "id",
            "value",
            "attribute__id",
            "attribute__title",
            "attribute__title_fa",
        )
    )

    grouped_by_filters = defaultdict(list)
    for data in result:
        attribute_id = data.pop("attribute__id")
        attribute_title = data.pop("attribute__title")
        attribute_title_fa = data.pop("attribute__title_fa")
        grouped_by_filters[(attribute_id, attribute_title, attribute_title_fa)].append(
            data
        )
    data_dict = [
        {
            "id": filter_key[0],
            "title": filter_key[1],
            "title_fa": filter_key[2],
            "values": filter_values,
        }
        for filter_key, filter_values in grouped_by_filters.items()
    ]

    return data_dict

```
---

بریم سراغ کوعری دوم یعنی گرفتن محصولات بر اساس چنتا attribute_value.id که بنظرم اینجا اوج خلاقیتم بود
ما برای شروع ایدی دسته بندی و لیستی از attribute_value.id هارو داریم
و چیزی هم که باید برگردونیم محصولات یک دسته بندی هست با یکسری فیلتر خاص 
بنابر این ماهمون کوعری گرفتن محصولات بر اساس کتگوری رو نگه میداریم و بهش یکمی خلاقیت میزنیم

میایم یه تیبل products رو join میزنیم به تیبل attributevalue و برای اون دیتایی که از join قراره برگرده
یه شرط تعریف میکنیم میگیم چک کن ببین اون attributevalue ایدیش داخل این لیست ایدی هایی که از فرانت اومده هست یا نه
ولی خب اینجا ممکنه یک محصول فقط 1 attributevalue  داشته باشه که اونم ایدیش داخل لیست باشه پس اونم الان داخل خروجی ما هست
بله هست ولی ما اینجا زرنگ بازی در میاریم و میایم محصولات رو بر اساس id ایشون گروپ بای میکنیم داخل sql و همونطور که میدونید
واسه شرط نوشتن داخل Group By میام از HAVING استفاد میکنیم و میگیم اقا اون محصولاتی رو برگردون که تعداد attributevalue که براشون گرفتیم اندازه طول لیستی باشه که از فرانت اومده

میدونم هنگ کردید پس بیاید کدش رو ببینیم

```sql
SELECT
    "product"."id",
    "product"."title",
    COUNT(
        DISTINCT "product_attributes"."attributevalue_id"
    ) AS "num_attributes"
FROM
    "product"
    INNER JOIN "product_attributes" ON (
        "product"."id" = "product_attributes"."product_id"
    )
WHERE
    (
        "product"."category_id" = 1
        AND "product_attributes"."attributevalue_id" IN (1, 2, 3, 4)
    )
GROUP BY
    "product"."id"
HAVING
    COUNT(
        DISTINCT "product_attributes"."attributevalue_id"
    ) = 4
```

و همینطور کدش داخل django orm

```python
def get_product_list(category_id: int, get_parameters: ProductListParams = None):
    queryset = (
        Product.objects.defer(
            "base_url",
            "datasheet",
            "description",
            "is_active",
            "tags",
        )
        .select_related("manufacture")
        .prefetch_related(
            "images",
            "price_table",
        )
        .filter(is_active=True, category__id=category_id)
    )
    if get_parameters.attribute_filters:
        queryset = (
            queryset.filter(attributes__in=get_parameters.attribute_filters)
            .annotate(num_attributes=Count("attributes", distinct=True))
            .filter(num_attributes=len(get_parameters.attribute_filters))
        )
    return queryset
```


---
خب حالا که کوعری هارو هم نوشتیم بزارید یک نکته فوق العاده مهم هم بگم 
این دیزاین ما میشه گفت یک مشکل داره که البته میشه داخل سطح کد جلوش رو گرفت 
اونم اینکه اگر یک attribute_value رو تغییر بدیم یه جورایی ویژگی همه محصولاتی که با این ابجکت ارتباط دارن رو تغییر دادیم
واسه حل این مساله اگر بخوایم دیزاین رو عوض کنیم که خیلی مشکل پیش میاد 
مثلا اینکه باید یه عالمه دیتای تکراری ادد کنیم دیگه نمیتونیم انقدر راحت فیلتر کنیم و نمیتونیم انقدر راحت دیتای بخش فیلتر رو هم بگیریم

ولی راه حلش داخل کد خیلی راحته به این شکل که اگر خواستیم ویژگی محصول رو عوض کنیم 
دیتای جدید ویژگی رو میگیریم داخل تیبل attributevalue چک میکنیم اگر ویژگی با این value بود 
رابطه attributevalue قبلی رو با محصول پاک میکنیم و این جدیده رو یه رابطه میسازیم 
و اگر هم نبود یه attributevalue جدید میسازیم و به محصول رابطه اش میدیم
