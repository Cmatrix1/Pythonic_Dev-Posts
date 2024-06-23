سلام خدمت همه عزیزان من برگشتم با پارت 2 از کتاب `Designing Data-Intensive Applications` 

توی این پارت قراره راجب خلاصه ای از فصل 2 کتاب صحبت کنیم 

در این فصل نویسنده راجب انواع دیتا مدل ها صحبت میکنه البته که دیتا مدل ها مبحث بسیار بزرگی هست ولی در این فصل ما نگاه سریعی نسبت به انواع اون ها میکنیم

شما صرفا با خوندن این فصل میتونید دید خوبی نسبت به دیتا مدل ها پیدا کنید و بتونید مدل مناسب اپلیکیشن خودتون رو پیدا کنید


اکثر برنامه ها با لایه بندی یک مدل داده بر روی مدل دیگر ساخته می شوند. هر لایه با ارائه یک مدل داده تمیز، پیچیدگی لایه های زیر را پنهان می کند. این abstraction به گروه های مختلف برنامه نویس ها اجازه می دهد تا به طور مؤثر کار کنند.

## Relational Model VS Document Model
در طول زمان که کامپیوتر ها قدرتمند تر میشدن و استفاده اشون هم در بیزینس های مختلف بیشتر میشد دیتابیس های رابطه ای به شکل خیلی خوبی generalize شدن برای usecase های خیلی زیادی اما خب از یه جایی به بعد requirements بیزینس ها بیشتر شد و با معرفی NOSQL و ویژگی های داشت باعث شد پذیرش اش راحت تر بشه

چنتا از این نیاز ها که باعث پذیرش راحت تر NOSQL شد

1. A need for greater scalability than relational databases can easily achieve, including very large datasets or very high write throughput

2. A widespread preference for free and open source software over commercial database products

3. Specialized query operations that are not well supported by the relational model

4. Frustration with the restrictiveness of relational schemas, and a desire for a more
dynamic and expressive data model


### The Object-Relational Mismatch
پیشنهاد شخصیم اینه راجب این مفهوم بیشتر تحقیق کنید چون مبحث یه مقدار پیچیده ای هست و اینجا نمیگنجه توضیح کاملش ولی خب من متن کتاب رو میارم


if data is stored in relational tables, an awkward translation layer is required between the objects in the application code and the database model of tables, rows, and columns. The disconnect between the models is sometimes called an impedance mismatch.

JSON model reduces the impedance mismatch and the lack of schema is often cited as an advantage.

- https://www.geeksforgeeks.org/impedance-mismatch-in-dbms/


### Many-to-One and Many-to-Many Relationships
در ادامه نویسنده راجب اهمیت و استفاده روابط داخل دیتابیس صحبت میکنه که نکات خوبی رو راجب نرمالایزیشن و دینرمالایزیشن میگه و راجب استفاده ها و usecase های اون که من خیلی راجبش صحبت نمیکنم چون خیلی مرتبط به بحث نیست و صرفا داره مقدمه میچینه برای مبحث بعدی 
شما دیگه واقعا این مباحث رو باید بدونید :)

### Are Document Databases Repeating History?
سرفصل جالبی رو داریم اینجا که نویسنده داره ارتباطی بین چالش امروزه دیتابیس های Document ای و دیتابیس های IBM میده که قدیمی تر هست 

در حالی که روابط و پیوندهای چند به چند به طور معمول در پایگاه های داده رابطه ای و document database استفاده می شود، document database  و NoSQL بحث را در مورد بهترین نحوه بازنمایی این روابط در یک دیتابیس دوباره باز کردند. 

و نویسنده اشاره میکنه این بحث از خیلی قبل تر وجود داشته و درواقع به اولین سیستم های پایگاه داده ای بر میگرده که شبیه دیتابیس های document قابلیت مناسبی برای روابط یک به چند داشتن ولی برای چند به چند خیلی مناسب نبودن

در اون زمان راه حل های زیادی برای حل این مشکل مطرح شد که دوتا از برجسته ترین هاش 

#### The network model
Standardised by a committee called the Conference on Data Systems Languages (CODASYL) model was a generalisation of the hierarchical model. In the tree structure of the hierarchical model, every record has exactly one parent, while in the network model, a record could have multiple parents.

The links between records are like pointers in a programming language. The only way of accessing a record was to follow a path from a root record called access path.

A query in CODASYL was performed by moving a cursor through the database by iterating over a list of records. If you didn't have a path to the data you wanted, you were in a difficult situation as it was difficult to make changes to an application's data model.

#### The relational model
By contrast, the relational model was a way to lay out all the data in the open" a relation (table) is simply a collection of tuples (rows), and that's it.

The query optimiser automatically decides which parts of the query to execute in which order, and which indexes to use (the access path).

The relational model thus made it much easier to add new features to applications.

#### Comparison to document databases

Document databases reverted back to the hierarchical model in one aspect: storing nested records (one-to-many relationships, like positions, education, and contact_info in Figure 2-1) within their parent record rather than in a separate table.

However, when it comes to representing many-to-one and many-to-many relationships, relational and document databases are not fundamentally different: in both cases, the related item is referenced by a unique identifier, which is called a foreign key in the relational model and a document reference in the document model

That identifier is resolved at read time by using a join or follow-up queries. To date, document databases have not followed the path of CODASYL.


## Relational Versus Document Databases Today
در ادامه سعی میکنم یه خلاصه کوتاهی راجب مقایسه ای که نویسنده بین دیتابیس های داکیومنت و رابطه ای کرده بنویسم

The main arguments in favour of the document data model are schema flexibility, better performance due to locality, and sometimes closer data structures to the ones used by the applications. The relation model counters by providing better support for joins, and many-to-one and many-to-many relationships.

If the data in your application has a document-like structure, then it's probably a good idea to use a document model. The relational technique of shredding can lead unnecessary complicated application code.

The poor support for joins in document databases may or may not be a problem.

If you application does use many-to-many relationships, the document model becomes less appealing. Joins can be emulated in application code by making multiple requests. Using the document model can lead to significantly more complex application code and worse performance.

#### Schema flexibility
Most document databases do not enforce any schema on the data in documents. Arbitrary keys and values can be added to a document, when reading, clients have no guarantees as to what fields the documents may contain.

Document databases are sometimes called schemaless, but maybe a more appropriate term is schema-on-read, in contrast to schema-on-write.

Schema-on-read is similar to dynamic (runtime) type checking, whereas schema-on-write is similar to static (compile-time) type checking.

The schema-on-read approach if the items on the collection don't have all the same structure (heterogeneous)

- Many different types of objects
- Data determined by external systems

#### Data locality for queries

If your application often needs to access the entire document, there is a performance advantage to this storage locality.

The database typically needs to load the entire document, even if you access only a small portion of it. On updates, the entire document usually needs to be rewritten, it is recommended that you keep documents fairly small.


#### Convergence of document and relational databases
PostgreSQL does support JSON documents. RethinkDB supports relational-like joins in its query language and some MongoDB drivers automatically resolve database references. Relational and document databases are becoming more similar over time.


## Relational Versus Document Databases Today


The main arguments in favour of the document data model are schema flexibility, better performance due to locality, and sometimes closer data structures to the ones used by the applications. The relation model counters by providing better support for joins, and many-to-one and many-to-many relationships.


#### Which data model leads to simpler application code?
If the data in your application has a document-like structure, then it's probably a good idea to use a document model. The relational technique of shredding can lead unnecessary complicated application code.

The poor support for joins in document databases may or may not be a problem.

If you application does use many-to-many relationships, the document model becomes less appealing. Joins can be emulated in application code by making multiple requests. Using the document model can lead to significantly more complex application code and worse performance.

It’s not possible to say in general which data model leads to simpler application code;
it depends on the kinds of relationships that exist between data items. 
For highly interconnected data, the document model is  awkward, the relational model is acceptable, and graph models are the most natural.


## Query Languages for Data

SQL is a declarative query language. In an imperative language, you tell the computer to perform certain operations in order.

In a declarative query language you just specify the pattern of the data you want, but not how to achieve that goal.

A declarative query language hides implementation details of the database engine, making it possible for the database system to introduce performance improvements without requiring any changes to queries.

Declarative languages often lend themselves to parallel execution while imperative code is very hard to parallelise across multiple cores because it specifies instructions that must be performed in a particular order. Declarative languages specify only the pattern of the results, not the algorithm that is used to determine results.

## Graph-like data models
اگر دیتای اپلیکیشن شما خیلی رابطه m2m زیادی داره منطقی تر هست که دیتا رو به صورت graph ذخیره کنید

A graph consists of vertices (nodes or entities) and edges (relationships or arcs).

Well-known algorithms can operate on these graphs, like the shortest path between two points, or popularity of a web page.

There are several ways of structuring and querying the data. The property graph model (implemented by Neo4j, Titan, and Infinite Graph) and the triple-store model (implemented by Datomic, AllegroGraph, and others). There are also three declarative query languages for graphs: Cypher, SPARQL, and Datalog.

### Property graphs
Each vertex consists of:

- Unique identifier
- Outgoing edges
- Incoming edges
- Collection of properties (key-value pairs)

Each edge consists of:

- Unique identifier
- Vertex at which the edge starts (tail vertex)
- Vertex at which the edge ends (head vertex)
- Label to describe the kind of relationship between the two vertices
- A collection of properties (key-value pairs)

Graphs provide a great deal of flexibility for data modelling. Graphs are good for evolvability.

## The Cypher Query Language

Cypher is a declarative query language for property graphs, created for the Neo4j graph database


Graph queries in SQL. In a relational database, you usually know in advance which joins you need in your query. In a graph query, the number if joins is not fixed in advance. In Cypher :WITHIN*0... expresses "follow a WITHIN edge, zero or more times" (like the * operator in a regular expression). This idea of variable-length traversal paths in a query can be expressed using something called recursive common table expressions (the WITH RECURSIVE syntax).

