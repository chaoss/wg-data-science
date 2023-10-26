This document has responses grouped into categories from the question, "What other challenges have you faced that weren’t in the above list or what else would you like to see us improve?"

Many comments fall into multiple categories, so you’ll see the same content multiple times. The full text for the responses can be found in the [repo](https://github.com/chaoss/wg-data-science/tree/main/challenges_survey/raw_data)

**Category: Taking action on data / generating insights from the data (8 Quotations)**
* ability to see and understand what other people are doing in real situation so I can leverage that work, and compare with my own
* Any new metric should have use cases associated where the usefulness of the metric becomes evident
* Overwhelming data.
* No CHAOSS tools make it easy to compare a large number of repos.
* Many CHAOSS metrics aren't quantitative, so evaluating them requires manual examination. CHAOSS metrics don't cover marketing metrics like social media mentions.
* The most challenging part is to communicate them to C level.
* Measuring the health and success of community (marketing) activities
* In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide.

**Category: CHAOSS Processes (4 Quotations)**
* It's hard to understand what is "official" CHAOSS software (like what is the relationship to compass?) or how things move from the metrics/models into the software.
* There also Augur meetings on the calendar but I'm not sure if they are actually happening, and I'm not sure if they are just for people doing development work on Augur, as opposed to users.
* The focus on OSPOs was a surprise to me as I got more involved in the project, it's understandable but makes it more difficult for people not in an OSPO to be seen as an audience for metrics/software, which is unfortunate because I think there is still a lot of value in CHAOSS metrics for people who are not part of an official OSPO.
* Overall I find it complex to understand what CHAOSS is actually about and how the tools relate to what is described

**Category: Metric Definitions (3 Quotations)**
* Any new metric should have use cases associated where the usefulness of the metric becomes evident
* Many CHAOSS metrics aren't quantitative, so evaluating them requires manual examination. CHAOSS metrics don't cover marketing metrics like social media mentions.
* Issues and PR backlog

**Category: Software: Augur (3 Quotations)**
* Both GrimoireLab and Augur don't really provide a UX that is fit for a product. Rather they are fairly complicated back-ends that require a significant amount of configuration to set up. For a well funded OSPO that has a clear list of the data sources they want to track, this may be useful, but for something like [REDACTED], this means that many of our needs are not met. In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide. Particularly with GrimoireLab we found that building on top of the current architecture was fairly difficult.
* I was excited by the prospect of Jupyter notebooks but then it turned out those also rely on Augur which could be fine but then some better instruction on getting just the Augur db running would be good. A simplified Augur install that is just the bare minimum for working with a data snapshot would be nice. Multiple instances of documentation also make working with Augur hard. There also Augur meetings on the calendar but I'm not sure if they are actually happening, and I'm not sure if they are just for people doing development work on Augur, as opposed to users.
* We find Augur easy to install and use.

**Category: Software: Contributing (2 Quotations)**
* Contributing has itself been a challenge, since documentation is woefully incomplete and (at times) inaccurate
* There also Augur meetings on the calendar but I'm not sure if they are actually happening, and I'm not sure if they are just for people doing development work on Augur, as opposed to users.

**Category: Software: GrimoireLab (9 Quotations)**
* More clarity/documentation in data model (for comparison against other data sources); OpenSearch backend is incompatible with other internal tooling so our implementation is a bit of an island :/
* Both GrimoireLab and Augur don't really provide a UX that is fit for a product. Rather they are fairly complicated back-ends that require a significant amount of configuration to set up. For a well funded OSPO that has a clear list of the data sources they want to track, this may be useful, but for something like [REDACTED], this means that many of our needs are not met. In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide. Particularly with GrimoireLab we found that building on top of the current architecture was fairly difficult.
* Integrating grimorelab with custom dashboards and frontend/backend software seemed tricky as far as ive heard from the team that was responsible for that. I dont know the details though, sounded like there was some architectural tech debt (not sure what that means) that made it hard to for the developers to integrate.
* This was more of a product issue (when I used Bitergia), but a few times we had infrastructure issues so that an up-to-date data wasn't available for an extended period. For corporate users (especially in technology companies), the main reason why they go with an outside vendor is so that they don't need to manage infrastructure/software.
* Creating production environments (security, set up backups, durability), updating, migrating to newer components (OpenSearch).
* I worked with Cauldron.io and thought it was a great tool but could not get GL running locally so my experimenting was limited to what was offered there. As a [REDACTED] I don't really have a budget to pay for metrics as a service just to experiment or to try and get other people involved, so I greatly appreciated the cauldron service.
* grimoire sigils should support opensearch / pivot away from kibiter asap
* Bitergia tools are quite complicated and take a lot of time to set up properly.
* Grimoirelab did not work well for the size of our OSPO.

**Category: Software: Software / Metrics Relationship (1 Quotation)**
* Understanding the relationship between the software and the metrics can be difficult, things aren't always named the same and the methods of calculation are not always transparent in the software so you can't tell if it is really doing what you think it is.

**Category: Technical: Compatibility / Tech Stack (7 Quotations)**
* More clarity/documentation in data model (for comparison against other data sources); OpenSearch backend is incompatible with other internal tooling so our implementation is a bit of an island :/
* From an OSPO perspective, I feel that OpenSSF Scorecard and Open Source Review Toolkit are quite valuable tools and resources ("easy" to set up and get a report). It would be great to see CHAOSS tools at the same level of maturity and value, or even integration with such tools, to get more adoption in the industry. On the other hand, the diversity of tools and setups related to open source development and contribution makes it so hard to find "the right" tools to 
* Both GrimoireLab and Augur don't really provide a UX that is fit for a product. Rather they are fairly complicated back-ends that require a significant amount of configuration to set up. For a well funded OSPO that has a clear list of the data sources they want to track, this may be useful, but for something like [REDACTED], this means that many of our needs are not met. In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide. Particularly with GrimoireLab we found that building on top of the current architecture was fairly difficult.
* Integrating grimorelab with custom dashboards and frontend/backend software seemed tricky as far as ive heard from the team that was responsible for that. I dont know the details though, sounded like there was some architectural tech debt (not sure what that means) that made it hard to for the developers to integrate.
* Creating production environments (security, set up backups, durability), updating, migrating to newer components (OpenSearch).
* grimoire sigils should support opensearch / pivot away from kibiter asap
* I was excited by the prospect of Jupyter notebooks but then it turned out those also rely on Augur which could be fine but then some better instruction on getting just the Augur db running would be good.

**Category: Technical: Documentation (3 Quotations)**
* Contributing has itself been a challenge, since documentation is woefully incomplete and (at times) inaccurate
* Documentation seems really good but there are a LOT of steps - I have such a limited amount of time that by the time I read through the documents to remember where I left off last time, I've already run out of time to do any experimentation.
* Multiple instances of documentation also make working with Augur hard.

**Category: Technical: Ease of Use / UX (9 Quotations)**
* Both GrimoireLab and Augur don't really provide a UX that is fit for a product. Rather they are fairly complicated back-ends that require a significant amount of configuration to set up. For a well funded OSPO that has a clear list of the data sources they want to track, this may be useful, but for something like [REDACTED], this means that many of our needs are not met. In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide. Particularly with GrimoireLab we found that building on top of the current architecture was fairly difficult.
* Documentation seems really good but there are a LOT of steps - I have such a limited amount of time that by the time I read through the documents to remember where I left off last time, I've already run out of time to do any experimentation.
* Estimating how much time and effort using tools would take, compared to ad hoc methods of assessing similar questions.
* Overall I find it complex to understand what CHAOSS is actually about and how the tools relate to what is described. They all seem quite complex and difficult to get started or require very special data analysis expertise. Maybe adding pre-requirements to usem them?
* Creating production environments (security, set up backups, durability), updating, migrating to newer components (OpenSearch).
* I would really like some lighter weight ways to play with the metrics. I was excited by the prospect of Jupyter notebooks but then it turned out those also rely on Augur which could be fine but then some better instruction on getting just the Augur db running would be good. A simplified Augur install that is just the bare minimum for working with a data snapshot would be nice.
* From an OSPO perspective, I feel that OpenSSF Scorecard and Open Source Review Toolkit are quite valuable tools and resources ("easy" to set up and get a report). It would be great to see CHAOSS tools at the same level of maturity and value,
* Overwhelming data.
* No CHAOSS tools make it easy to compare a large number of repos.

**Category: Technical: Installation (10 Quotations)**
* Both GrimoireLab and Augur don't really provide a UX that is fit for a product. Rather they are fairly complicated back-ends that require a significant amount of configuration to set up. For a well funded OSPO that has a clear list of the data sources they want to track, this may be useful, but for something like [REDACTED], this means that many of our needs are not met. In our case as [REDACTED], we need to provide an experience for [REDACTED] that encourages them to track the community health of projects they use and participate in. This requires a certain kind of UX as well as better integration with other data sources and services that we provide. Particularly with GrimoireLab we found that building on top of the current architecture was fairly difficult.
* Documentation seems really good but there are a LOT of steps - I have such a limited amount of time that by the time I read through the documents to remember where I left off last time, I've already run out of time to do any experimentation.
* Overall I find it complex to understand what CHAOSS is actually about and how the tools relate to what is described. They all seem quite complex and difficult to get started or require very special data analysis expertise. Maybe adding pre-requirements to usem them?
* Creating production environments (security, set up backups, durability), updating, migrating to newer components (OpenSearch).
* Getting either piece of software running locally proved impossible for me :)
* I worked with Cauldron.io and thought it was a great tool but could not get GL running locally so my experimenting was limited to what was offered there.
* From an OSPO perspective, I feel that OpenSSF Scorecard and Open Source Review Toolkit are quite valuable tools and resources ("easy" to set up and get a report). It would be great to see CHAOSS tools at the same level of maturity and value,
* Bitergia tools are quite complicated and take a lot of time to set up properly.
* self hosting is becoming really difficult, esp for remote only orgs
* Docker compose

**Category: Technical: Reliability (1 Quotation)**
* This was more of a product issue (when I used Bitergia), but a few times we had infrastructure issues so that an up-to-date data wasn't available for an extended period. For corporate users (especially in technology companies), the main reason why they go with an outside vendor is so that they don't need to manage infrastructure/software.

**Category: Technical: Relating to SaaS or need for SaaS solutions (3 Quotations)**
* This was more of a product issue (when I used Bitergia), but a few times we had infrastructure issues so that an up-to-date data wasn't available for an extended period. For corporate users (especially in technology companies), the main reason why they go with an outside vendor is so that they don't need to manage infrastructure/software.
* I worked with Cauldron.io and thought it was a great tool but could not get GL running locally so my experimenting was limited to what was offered there. As a [REDACTED] I don't really have a budget to pay for metrics as a service just to experiment or to try and get other people involved, so I greatly appreciated the cauldron service.
* self hosting is becoming really difficult, esp for remote only orgs

