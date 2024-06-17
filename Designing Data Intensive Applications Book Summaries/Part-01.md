سلام خدمت همه دوستان

من برگشتم با یکسری پست های جدید 

اخیرا شروع به خوندن کتاب `Designing Data-Intensive Applications` کردم و قصد دارم بعد از مطالعه هر فصل یک خلاصه ای از اون رو در قالب یک پست یا مقاله جا بدم 

یک اپلیکشن باید `requirement` های زیادی رو داشته باشه تا بتونه خوب عمل بکنه 

`functional requirements`  : به معنای کاری که باید انجام بشه مثل ذخیره دیتا ، برگردوندن دیتا ، سرچ کردن و ...

`nonfunctional requirements` : بیشتر منظور موارد کلی هست مثل امنیت ، توسعه‌پذیری ، سازگاری و نگهداری


داخل فصل اول ما بصورت کامل راجب `reliability`, `scalability`, `maintainability` صحبت میکنیم

## Reliability
یعنی ما سییستم رو به شکلی طراحی بکنیم  که بصورت درست کار کنه حتی وقتی که خطا (fualts) رخ بده 

اگر بخوام مفهوم خطا یا همون (fualts) رو شفاف تر توضیح بدم 

 خطا یک Error یا نقص در یک برنامه است که باعث ایجاد نتایج نادرست یا غیرمنتظره می شود.

سیستم‌هایی که خطاها را پیش‌بینی می‌کنند و می‌تونند با هاش  کنار بیان، مقاوم به خطا (fault-tolerant) یا انعطاف‌پذیر (resilient) نامیده می‌شند.

خطا ها یا اصطلاحا (Faults) داخل کتاب به چند دسته تقسیم میشن به صورت کلی

### اشکالات سخت‌افزاری
که معمولا رندوم هستن و ما خیلی کاری نمیتونیم راجبش انجام بدیم
### خطاهای نرم‌افزاری
که سمت خود سیستم هستن و حل کردنشون سخت تر از مشکلات نرم افزاری هست

### خطاهای انسانی
این هاهم مواردی هستن که همیشه وجود داره و هر از چندگاهی پیش میاد
    

## Scalability
یعنی داشتن استراتژی برای خوب نگه داشتن پرفرمنس سیستم وقتی که `load` افزایش پیدا میکنه 

#### Twitter example

Twitter main operations
- Post tweet: a user can publish a new message to their followers (4.6k req/sec, over 12k req/sec peak)
- Home timeline: a user can view tweets posted by the people they follow (300k req/sec)

Two ways of implementing those operations:
1. Posting a tweet simply inserts the new tweet into a global collection of tweets. When a user requests their home timeline, look up all the people they follow, find all the tweets for those users, and merge them (sorted by time). This could be done with a SQL `JOIN`.
2. Maintain a cache for each user's home timeline. When a user _posts a tweet_, look up all the people who follow that user, and insert the new tweet into each of their home timeline caches.

Approach 1, systems struggle to keep up with the load of home timeline queries. So the company switched to approach 2. The average rate of published tweets is almost two orders of magnitude lower than the rate of home timeline reads.

Downside of approach 2 is that posting a tweet now requires a lot of extra work. Some users have over 30 million followers. A single tweet may result in over 30 million writes to home timelines.

Twitter moved to an hybrid of both approaches. Tweets continue to be fanned out to home timelines but a small number of users with a very large number of followers are fetched separately and merged with that user's home timeline when it is read, like in approach 1.

---

#### Describing performance

What happens when the load increases:
* How is the performance affected?
* How much do you need to increase your resources?

In a batch processing system such as Hadoop, we usually care about _throughput_, or the number of records we can process per second.

> ##### Latency and response time
> The response time is what the client sees. Latency is the duration that a request is waiting to be handled.

It's common to see the _average_ response time of a service reported. However, the mean is not very good metric if you want to know your "typical" response time, it does not tell you how many users actually experienced that delay.

**Better to use percentiles.**
* _Median_ (_50th percentile_ or _p50_). Half of user requests are served in less than the median response time, and the other half take longer than the median
* Percentiles _95th_, _99th_ and _99.9th_ (_p95_, _p99_ and _p999_) are good to figure out how bad your outliners are.

Amazon describes response time requirements for internal services in terms of the 99.9th percentile because the customers with the slowest requests are often those who have the most data. The most valuable customers.

On the other hand, optimising for the 99.99th percentile would be too expensive.

_Service level objectives_ (SLOs) and _service level agreements_ (SLAs) are contracts that define the expected performance and availability of a service.
An SLA may state the median response time to be less than 200ms and a 99th percentile under 1s. **These metrics set expectations for clients of the service and allow customers to demand a refund if the SLA is not met.**

Queueing delays often account for large part of the response times at high percentiles. **It is important to measure times on the client side.**

When generating load artificially, the client needs to keep sending requests independently of the response time.

> ##### Percentiles in practice
> Calls in parallel, the end-user request still needs to wait for the slowest of the parallel calls to complete.
> The chance of getting a slow call increases if an end-user request requires multiple backend calls.

#### Approaches for coping with load

* _Scaling up_ or _vertical scaling_: Moving to a more powerful machine
* _Scaling out_ or _horizontal scaling_: Distributing the load across multiple smaller machines.
* _Elastic_ systems: Automatically add computing resources when detected load increase. Quite useful if load is unpredictable.

Distributing stateless services across multiple machines is fairly straightforward. Taking stateful data systems from a single node to a distributed setup can introduce a lot of complexity. Until recently it was common wisdom to keep your database on a single node.



## Maintainability 
این موضوع هم خودش فاکتور های خیلی زیادی داره ولی به صورت کلی به این معنا هست که شما زندگی رو واسه توسعه دهنده هایی که قراره در اینده و یا هرموقع با سیستم کار بکنن و توسعه بدند در کنار شما راحت بکنی 

نویسنده در ادامه سه اصل رو راجب این موضوع بیان میکنه 
که ترجیح میدم انگلیسی بنویسم ادامه اش رو چون ترجمه کردنش طول میکشه :)

### Operability: making life easy for operations
A good operations team is responsible for

- Monitoring and quickly restoring service if it goesinto bad state
- Tracking down the cause of problems
- Keeping software and platforms up to date
- Keeping tabs on how different systems affect each other
- Anticipating future problems
- Establishing good practices and tools for development
- Perform complex maintenance tasks, like platformmigration
- Maintaining the security of the system
- Defining processes that make operations predictable
- Preserving the organisation's knowledge about thesystem

Good operability means making routine tasks easy. allowing the operations team to focus their efforts on high-value activities. Data systems can do various things to make routine tasks easy, including:

- Providing visibility into the runtime behavior and internals of the system, with good monitoring
- Providing good support for automation and integration with standard tools
- Avoiding dependency on individual machines (allowing machines to be taken down for maintenance while the system as a whole continues running uninterrupted)
- Providing good documentation and an easy-to-understand operational model (“If I do X, Y will happen”)
- Providing good default behavior, but also giving administrators the freedom to
override defaults when needed
- Self-healing where appropriate, but also giving administrators manual control
over the system state when needed
- Exhibiting predictable behavior, minimizing surprises


### Simplicity: managing complexity
When complexity makes maintenance hard, budget and schedules are often overrun. There is a greater risk of introducing bugs.

Making a system simpler means removing accidental complexity, as non inherent in the problem that the software solves (as seen by users).

One of the best tools we have for removing accidental complexity is abstraction that hides the implementation details behind clean and simple to understand APIs and facades.

### Evolvability: making change easy
It’s extremely unlikely that your system’s requirements will remain unchanged for ever. They are much more likely to be in constant flux: you learn new facts, previously unanticipated use cases emerge, business priorities change, users request new features etc.

In terms of organizational processes, Agile working patterns provide a framework for adapting to change. The Agile community has also developed technical tools and pat
terns that are helpful when developing software in a frequently changing environment, such as test-driven development (TDD) and refactoring.

