# Practitioner Guide: Assessing Viability

If you haven’t already read the [Practitioner Guide: Introduction - Things to Think about When Interpreting Metrics](https://chaoss.community/practitioner-guide-introduction/), please pause now and read that guide.

# Audience / Scope

This guide is primarily for Open Source Program Offices (OSPOs) and other teams within organizations that need to understand the viability and risks associated with the open source software that they are consuming. 

# Introduction

Open source software can be found in 97% of codebases (Black Duck 2025), but like most software, the quality varies widely and some open source projects are more viable than others over the long term. Evaluating the viability and the risk that comes with engaging with specific open source projects is important to avoid disruptions to your work that hamper the ability to deliver products and services to customers, especially when a key dependency suddenly becomes unviable. It’s important to think about viability and risk as being on a continuum because projects will be more or less viable across a variety of categories, and whether you should embrace a project and accept the risk that comes with it is a strategic decision that depends on the needs of your organization and your use cases for associated technologies. Assessing the viability of open source projects, especially ones that have the potential to impact your business, is a good first step toward managing risk and reducing the chances of potential business disruptions.

Companies that use open source software (i.e., [all of them](https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf)) have been thinking more and more about bills of material, vulnerabilities, and license risks. This has especially been encouraged through recent [United States efforts](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) and the [EU’s Cyber Resilience Act (CRA)](https://www.cyberresilienceact.eu/faq-the-cyber-resilience-act/) regarding Software Bills of Material (SBOMs). This push is a good opportunity to observe and report on software supply chains. We can all learn from knowing what’s in our software dependencies! Proliferation of [SBOMs](https://en.wikipedia.org/wiki/Software_supply_chain), [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (Static Application Security Testing), and [SCA](https://en.wikipedia.org/wiki/Software_composition_analysis) (Software Composition Analysis) scanning tools allow for users and developers of software to better understand their risk portfolio. Most people find significant value by using these reports to surface critically important vulnerabilities, license information, and other issues that could impact the viability of an open source project that you’re consuming. 

Security can be an important factor in determining the viability of an open source project, but the security of any software component is only as good as the security of its dependencies, so assessing viability needs to look beyond an individual project. It’s important to note that popular packages are no more or less likely to follow good security practices (Imtiaz 2022). This goes beyond just thinking about dependency selection to considering plans for keeping those dependencies up to date, since you are four times as likely to have security issues when you use outdated dependencies (Cox et al. 2015).

While security may be top of mind when thinking about open source project viability, there are other factors that also need to be considered. How the project is governed and how the community collaborates to build the software are important to assess as well. We also have some strategy metrics for assessing the viability of a project. This guide provides advice for assessing viability across all four of these categories: compliance and security, governance, community, and strategy. 

# Challenges

Within many companies, there is no rigorous process for selecting dependencies that are most likely to be viable over time. Often product teams, or even individual software developers, select open source projects because they fill a particular technical need without any assessment of the viability of the project or the risks they might be taking by using it. Challenging questions include: 

* What else should we be looking for in our open source software choices? 
* What guidance can we give to encourage good decisions not just when maintaining software? 
* Should that guidance be different than when people decide on which software to use? 
* Could we provide tools and metrics to guide decisions? 
* How can we create less risk in our choices, providing more sustainable software infrastructure?

Often teams interested in steering technical discussion must rely on existing structures of security or licensing compliance. The main challenge for subject matter experts contending with these frameworks is a lack of metrics and systems to convey what else matters when selecting an open source dependency. Using viability, we can create measurements which allow for more thorough analysis of software dependencies.

# Lessons Learned

We’ve recently seen a wave of single vendor open source projects with Contributor License Agreements (CLAs) being relicensed to more restrictive licenses, and in some cases, relicensing has resulted in a hard fork of the original project. Examples include Elasticsearch / OpenSearch, Terraform / OpenTofu, and Redis / Valkey. These relicensing events and resulting forks can be disruptive to the companies and individuals using the original open source projects (Foster 2024). When this happens, companies often scramble to decide whether they can continue to use the project under the new license, and if they need to pay a license fee, or if they should switch to another technology (possibly the fork). 

In addition to relicensing, companies can make other business decisions that can result in no longer funding employees to work on an open source project, which can result in projects losing large numbers of maintainers at one time (Egbahl 2016), thus making them less viable. Avelino et al. (2019) found that even popular projects may become permanently abandoned, and if the majority of work is being performed by a single person or small number of people, it increases the risk that a project could become unsustainable if that person or people were no longer working on the project.

Over the past few years, we’ve had several high profile vulnerabilities that demonstrated how widely used projects can have viability concerns. In the case of OpenSSL, at the time of the Heartbleed security vulnerability many people learned that this widely used project was maintained by two overworked and underpaid people who were struggling to keep up with the work that OpenSSL required. A similar example a few years later with the XZ project showed what can happen when someone gets involved in the project and makes enough good contributions to convince one overworked maintainer to let them help maintain the project before eventually introducing malicious code. These two examples highlight the importance of assessing the viability of the open source projects that we consume. As such, we assess the Contributor Absence Factor to understand how many maintainers lead the majority of project code contributions as in the case of XZ. We can also understand the volume of changes, and how that trends over time, to understand when projects suffer from complexity and lack of contribution – as in the case of OpenSSL. 

These are just a few examples of what can happen to make projects riskier to use and less viable over time. By assessing viability in advance, an organization might decide not to use a particular open source project. In other cases, an organization might decide to use a less viable project, but work within the project to improve viability and thus mitigate some of the risks identified during the assessment.

# How to Take Action

It’s common to focus on security vulnerabilities and licensing when assessing risks associated with using an open source software project; however, there are many other areas that should also be considered. CHAOSS’ Viability Metrics Models break viability down into four key categories, with each category containing many metrics, but with some overlap of metrics appearing in more than one of these categories: **Compliance and Security, Governance, Community,** and **Strategy**. 

The rest of this section covers which metrics we’re using and why they fit together. We’ve summarized what metrics are in each category along with an overview of why they fit together. We’ll also cover the value proposition of metrics that cross between the categories and make suggestions for actions and mitigation.

## Compliance and Security

Compliance and Security assesses a project’s licensing fit, vulnerability risk, and ability to respond to their maintenance duties. It is important for users to comply with any responsibilities they may hold to an organization or to the creators of an OSS project.

**CHAOSS Metrics:**

[OpenSSF Best Practices](https://chaoss.community/?p=3939)

* This is a proxy metric to ensure that a project responds to security incidents and has enough protections in place to generally interpret a reliable Compliance and Security strategy. It also avoids using costly SCA / SAST scanning on every open source project.

[License Coverage](https://chaoss.community/?p=3961)

* License coverage is used to make decisions about the risk of using unlicensed software.

[Licenses Declared](https://chaoss.community/?p=3963)

* Licenses declared provides transparency on potential license conflicts present in software packages, and can be used to determine if the use case of the software is compatible with the license provided and in compliance with organizational license policies.

[OSI Approved Licenses](https://chaoss.community/?p=3962)

* The licenses that conform to the OSI standard provide confidence in how to use the software in compliance with those licenses.

[Defect Resolution Duration](https://chaoss.community/?p=4727)

* This metric provides a way to consider different response rates to defects when they occur between projects.

[Upstream Code Dependencies](https://chaoss.community/?p=3977)

* This ensures that dependencies of a project are also included in any viability evaluation by considering both the project being assessed along with its dependencies.

[Libyears](https://chaoss.community/?p=3976)

* This metric provides a measure of software dependency freshness that highlights the risk associated with using projects that might have a hidden maintenance cost or security vulnerabilities due to dependencies not being updated regularly.

**Additional Considerations:**

[Security Policy Documentation](https://chaoss.community/practitioner-guide-security/)

* This allows us to consider how the project responds to security vulnerabilities.
* The project’s security policy documents should have a process for allowing anyone to privately report vulnerabilities and for dealing with those reports quickly and efficiently. It should also include an embargo process for privately notifying the organizations who use the project to give these organizations time to apply security fixes before a vulnerability is made public.

### What compliance and security means for viability

This metrics model helps to gauge how well both the community and the maintainers of the application consider the security and compliance of their application. We expect to use these indicators to gauge risk. We have showstoppers like licensing, where a license can be incompatible with our intended use case, through security-centric badges and metrics, to how fast and regularly a team maintains the dependencies and defects reported to their application.

Additionally, like in other models, some metrics are challenging to trace or visualize. We leave flexibility in how we rank applications against tricky-to-gather metrics. For example: much like Defect Resolution Duration, the appetite for how many Libyears is appropriate for a project will always be up to maintainers. Depending on how or where an application may run, and how frequently it is updated, requires thinking about Libyears critically. 

## Governance

The governance category focuses heavily on the maintainers and their efforts, since open source project governance helps to define decision-making processes. Understanding “maintainership” is an important part of overall project viability, because a project's maintainers are the gatekeepers of incoming changes, new releases, and future project direction. 

**Metrics contained only in this category:**

[Issue Label Inclusivity](https://chaoss.community/?p=3533)

* Issue label inclusivity measures the accessibility and inclusiveness of project issues for contributors of various skill levels and backgrounds.

[Documentation Usability](https://chaoss.community/?p=3532)

* Document usability assesses how well an open source project’s documentation serves contributors by ensuring clarity, readability, inclusiveness, and accessibility.

[Time to Close](https://chaoss.community/?p=3446)

* This measures how long it takes for a contribution to make its way into the project

[Issue Age](https://chaoss.community/?p=3629)

* Issue age looks at how long questions, suggestions, and other issues generally stay in a project without being resolved or closed.

[Change Request Closure Ratio](https://chaoss.community/?p=4834)

* This helps to understand whether a project has enough maintainers to keep up with contributions to the project.

[Project Popularity](https://chaoss.community/?p=3573)

* This metric is an aggregate of other smaller metrics (e.g., likes, stars, badges, forks, clones) that provide indicators of usage and adoption (Vargas et. al., 2024). 

[Release Frequency](https://chaoss.community/?p=4765)

* Release frequency helps to understand how long it takes for a project to incorporate changes and security fixes into a release along with when to expect security patches, bug fixes, and new features.

[Libyears](https://chaoss.community/?p=3976)

* This metric provides a measure of software dependency freshness that highlights the risk associated with using projects that might have a hidden maintenance cost or security vulnerabilities due to dependencies not being updated regularly.

**Additional Considerations:**

[Governance Documentation](https://fastwonderblog.com/2025/08/03/governance-part-2-defining-governance/):

* Knowing how collaboration occurs and how decisions are made is important for viability because it provides clarity into how the project is governed and means that people are able to make contributions that are more likely to be accepted. 
* The processes for collaboration and decision-making should be clearly documented as part of the project governance. 
* There should be documentation about leadership within the project, including who those leaders are and how they are selected. Ideally, there should be a fair and transparent process for selecting leaders with leadership seats held by individuals with the right expertise and enough time available to lead the project.

[Foundation, Company, or Individual Ownership](https://fastwonderblog.com/2025/08/31/governance-part-5-overall-ownership-of-a-project/):

* The overall ownership structure often impacts how the project is governed on a day to day basis and how the project is perceived by others.
* Neutral foundations provide a level playing field where individual contributors can contribute as equals, which allows companies to collaborate together in a neutral environment where no single company is in control of the project.
* Projects owned by a company or individual may be less viable because they can make unilateral decisions than impact the users of the project (e.g., license change) or cease to continue development and maintenance (e.g., major life change or going out of business).

### What Governance Means for Viability

These metrics are useful to show the intention or lack of intention in the project’s governance. For example, if there’s a lack of inclusive labels on issues, it identifies a gap in welcoming new contributors and sifting existing contributors through workstreams. The ability to contribute, understand, or depend on a project is highly coupled to the effort behind governance.

This isn’t to say poor governance metrics indicate that a project is governed by fools. Low change request closure ratio, for example, may simply indicate that there are not as many maintainers to support a contributing community. A lack of new issues could be the result of a recent large release that addresses many recurring issues. These metrics are important to aggregate these reasons; not to cast professional doubt on maintainers of projects. The metrics help identify the governance capacity and effort across projects in a software portfolio.

If some of these metrics feel like they could be strong community metrics, they can be. Many of the shared metrics here are a combination of the effort a community has with a project, and the effort of the body governing a project. The overlap of shared metrics captures this relationship well, considering the responsibility contributors and maintainers share in creating open source software.

## Community

A key aspect of viability is community activity and adoption, because without an active community, an open source project is not likely to continue to evolve and grow. The idea is that an active community surrounding a project is more likely to drive better performance, vulnerability management, and feature-completeness to ease development downstream.

**CHAOSS Metrics:**

[Clones](https://chaoss.community/?p=3429)

* The number of clones measures how many times a project has been pulled from a repository into a local machine as an indicator of adoption.

[Technical Forks](https://chaoss.community/?p=3431)

* The number of forks indicates the interest in contributing to the project.

[Types of Contributions](https://chaoss.community/?p=3432)

* Open source projects are more than just code, and other types of contributions (e.g., strategy, issues, reviews, events, writing articles) indicate an ability to sustain a project.

[Change Requests](https://chaoss.community/?p=3610)

* The volume of regular requests can help to understand the strength, patterns, and sustainability of a project’s community.

[Committers](https://chaoss.community/?p=3945)

* The trends associated with the number of committers can provide insights into a project’s lifecycle and whether it has a growing, stable, or declining number of contributors.

[Change Request Closure Ratio](https://chaoss.community/?p=4834)

* This helps to understand whether a project has enough maintainers to keep up with contributions to the project.

[Project Popularity](https://chaoss.community/?p=3573)

* This metric is an aggregate of other smaller metrics (e.g., likes, stars, badges, forks, clones) that provide indicators of usage and adoption (Vargas et. al., 2024). 

[Libyears](https://chaoss.community/?p=3976)

* This metric provides a measure of software dependency freshness that highlights the risk associated with using projects that might have a hidden maintenance cost or security vulnerabilities due to dependencies not being updated regularly.

**Additional Considerations:**

Communication Inclusivity: 

* Projects with a culture of treating each other with respect and kindness are more viable because people will want to continue to contribute, so look carefully at how people treat each other in discussions, code reviews, Slack, and other communication channels. On the other hand, projects with toxic cultures put community members (including an organization’s employees) at risk.

### What community means for viability

With community, we seek to understand the “tinkering” that happens with a project, as well as being able to measure the contributions that are made. Clones and forks indicate how many users of software have pulled it to build from source, inspect the source code, submit a contribution, or take the project in a new direction. That flavor of popularity feels meaningful to trace community engagement in a project. One thing that can reduce the risk of embracing an open source project is if the project is adopted by a bunch of other organizations, since active projects with plenty of users are less likely to be abandoned. Having a strong user base reduces the risk that the project might be abandoned.

With committer trends, types of contributions, and change requests, we can see how a community is interacting. Maybe more markdown RFC’s are created than features, maybe vice-versa. With an understanding on what types of contributions are made, and how regular they are, we make a more informed judgment on project viability. For example, it’s reasonable to expect that a project which has shed 90% of its committers in a three month period is less viable than a stable (flat) committer trend. The inverse could indicate a growing or stable project gaining popularity around a particular technology trend. Where some “tinkering” metrics feel micro, other metrics take a macro lens.

By measuring some shared metrics, we give this model an opportunity to be viewed from the perspective of how the community maintains a project and how much interest there is generally. We find this distinct from the governance angle, even with significant overlap, as trends in these metrics are almost never entirely at fault of the community or the maintainers of a given project. The numbers could be meaningful for either space, so they exist in both models.

## Strategy

The strategy of a project may feel less numerically distinct than many of the other viability categories. The strategy will be measured by factors we can observe and by the influence that individuals and organizations might have on a project.

**CHAOSS Metrics:**

[Programming Language Distribution](https://chaoss.community/?p=3430)

* The programming languages used in a project can influence whether an organization has the skills to contribute upstream, which can impact viability if bug fixes cannot be incorporated.

[Contributor Absence Factor](https://chaoss.community/?p=3944) (sometimes called Bus Factor or Lottery Factor)

* A count of the fewest number of committers that comprise 50% of activity over a period to better understand the risk of using a particular project or set of projects regarding how much support the project would get if top contributors left.

[Elephant Factor](https://chaoss.community/?p=3940)

* Elephant factor counts the fewest organizations that comprise 50% of activity on a project and is used to infer the influence that specific organizations have on a project along with how detrimental it would be if that company shifted priority and stopped contributing.

[Organizational Influence](https://chaoss.community/?p=3560)

* Organizational Influence measures the amount of control an organization may have in a project. This is an estimate and an aggregation of several other metrics, including [organizational diversity](https://chaoss.community/?p=3464). 

[Release Frequency](https://chaoss.community/?p=4765)

* Release frequency helps to understand how long it takes for a project to incorporate changes and security fixes into a release along with when to expect security patches, bug fixes, and new features.

**Additional Considerations:**

Contributor License Agreements (CLAs)

* A Contributor License Agreement (CLA) signature required before contributing can decrease viability, since the CLA often gives the controlling organization the ability to relicense or perform other [rug pulls](https://thenewstack.io/clouds-code-and-control-the-new-open-source-power-struggle/).

### What strategy means for Viability

Metrics we trace in this model trace the strategy, or expected influence from individuals and organizations. For example, with a contributor absence factor of 1, it’s very possible that burnout or other factors could mean that the sole contributor stops maintaining the project. With a more resilient count of contributors, we are more likely to see a stable and viable maintenance strategy. 

We share release frequency between strategy and governance. This categorizes the overlap of how the maintainers of a project provide both a governance plan and a maintenance strategy.

## Actions and Mitigation

The previous four sections have covered categories with metrics that can be used to better understand many different aspects of viability, but organizations need to go beyond understanding and take action. 

### Contribution as a Risk Mitigation Strategy

One of the values of open source projects is that we can all work together to improve the viability of open source projects and reduce the risk of using those projects. The decision to use an open source project often comes down to tradeoffs between the risks and rewards as organizations decide whether a project is viable enough for their use case. 

The best way to understand, influence, and improve the future viability of a project is to allocate employee time to contribute to projects. Having your employees working within a project helps you understand the strengths and weaknesses of that project while also being able to influence the future direction of a project from within.

Organizations can also contribute funding and other resources to help sustain open source projects and improve their viability.

### Dependency Management

The application of these metrics operationalizes tasks for choosing and maintaining software. While evaluating dependencies, engineers have a better idea of what parts of an open source project excel, and what may fall short. Depending on the application intended, OSPOs, application teams, and operations teams can decide if the risk is worth taking on a project together. 

Assessing viability provides direction to what dependencies should be updated. Instead of lumping old dependencies into a ball of vague “technical debt”, we can estimate the fit of compliance and licensing, community, strategy, and governance against a particular project. We can also approximate the risk of not addressing projects in a way that is quantifiable to stakeholders and in review of priorities.

### Reassessment as Practice

Development teams regularly work under conditions that do not leave time to peruse codebases in search of optimizations. It’s critical to prioritize tasks that provide measurable value for whatever organization they work in. This viability framework allows for technical debt to be reframed as risk mitigation. In the same way we avoid vulnerabilities or licensing issues, we avoid unviable open source projects.

Having a tool and framework to practice assessment and re-assessment over a project’s life allows for metrics-based conversation about what are sometimes lofty goals for an engineer. We recommend having conversations about these metrics once a quarter, during conversations about prioritizing open source projects. By doing this, contributing to open source and upgrading major dependency versions (and consequently learning updated coding practices) are better justified as risk mitigation. Assessing viability is one way to drive a productive conversation with non-technical stakeholders on a regular basis.

# Conclusion

Depending on your use case, you may find different opportunities to use this viability assessment framework. It was originally developed for use in evaluating open source product usage within one specific company, so the thresholds for each model category will vary based on your organization’s assumption of risk.

For example:

* Organizations starting their journey into developing more formal open source software processes usually start with compliance and security, using licensing and vulnerability information to choose their software.
* Governance is crucial for organizations that intend to engage the open source community or contribute to a project to shape new functionality. If an organization is willing to commit time and resources to maintaining a project — the governance of that project becomes important to consider.
* Community is important for cutting-edge or newer implementations of technology. While older technology will likely have a less volatile community, where maintainers and flow of new contributions can be judged over time, a new project may need a stronger community with more vigilance on its competitors to ensure that a software stack isn’t abandoned.

Most business decisions boil down to an assessment of risk and making tradeoffs. Organizations should be thinking strategically about project risks in light of how they are using the projects. If it's a critical part of a technology stack, it should be as low of a risk as possible. On the other hand, if an open source project is used as a small part of some non-critical infrastructure, an organization can accept more risk. Assessing viability and thinking about it from the perspective of risk and which risks to accept is an important first step, but it's also important to think about which risks can be mitigated to improve viability. The best way to mitigate many of these risks is by paying employees to contribute to the projects that are most important to your organization. This provides an opportunity to improve viability and sustainability, but it also provides insight into where the project is heading and how things are going, so that if something changes in the project to further increase risk, it might be easier to anticipate those changes.

# Cautions and Considerations

* How you assess viability and your tolerance for risk is highly dependent on the needs of your particular organization and your particular use case, so there is no “one size fits all” approach. An acceptable risk for a technology startup might not be the same as for a financial services company. Similarly, using an open source infrastructure project as the basis for an organization’s revenue generating products will likely have a lower tolerance for risk and viability than if a project is being used by a small developer team.
* While some of what we have in this guide can be automated and assessed at scale, other metrics and additional considerations need a more manual assessment, so those might be better used only for projects where viability is critical to an organization.
* Not every risk can be anticipated, and a project might unexpectedly become unviable in ways that can’t be anticipated. This guide covers many aspects of viability that can be assessed, but the reality is that open source projects are run by people, and sometimes people will take unpredictable actions that impact others. 
* This guide can be a bit overwhelming for organizations who are new to assessing viability, so picking a few areas to focus on now and building on them later might be a good approach for many organizations. We recommend starting with one or two models, or even the general [Starter Model](https://chaoss.community/?p=5608) as a first step.

# Additional Reading

* 5 viability metrics models: [Starter](https://chaoss.community/?p=5608), [Compliance + Security](https://chaoss.community/?p=5407), [Governance](https://chaoss.community/?p=5411), [Community Engagement](https://chaoss.community/?p=5403), and [Strategy](https://chaoss.community/?p=5416) 
* [Viability: An Open Source CHAOSS Metric (Super)Model](https://chaoss.community/oss-viability-metric-supermodel/)
* [Metrics for OSS Viability](https://chaoss.community/viability-metrics-what-its-made-of/)
* [Guide for OSS Viability: A CHAOSS Metric Model](https://chaoss.community/chaoss-guide-oss-viability/)
* [CHAOSS Practitioner Guides](https://chaoss.community/about-chaoss-practitioner-guides/)
* [2024 Open Source Security and Risk Analysis Report](https://static.carahsoft.com/concrete/files/1617/1597/8665/2024_Open_Source_Security_and_Risk_Analysis_Report_WRAPPED.pdf)
* [Clouds, Code, and Control: The New Open Source Power Struggle](https://thenewstack.io/clouds-code-and-control-the-new-open-source-power-struggle/)

# Contributors

The following people contributed to this guide:

* Gary White
* Dawn Foster
* Matt Germonprez

# References

* Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. (2019, September). [On the abandonment and survival of open source projects: An empirical investigation](https://arxiv.org/pdf/1906.08058). In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)* (pp. 1-12). IEEE.
* Black Duck (2025). [2025 Open Source Security and Risk Analysis Report](https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf).
* Cox, J., Bouwers, E., Van Eekelen, M., & Visser, J. (2015, May). [Measuring dependency freshness in software systems](https://repository.ubn.ru.nl/bitstream/handle/2066/143749/143749.pdf?sequence=1). In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering* (Vol. 2, pp. 109-118). IEEE.
* Eghbal, N. (2016). [Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure](https://www.fordfoundation.org/work/learning/research-reports/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/). New York, NY: Ford Foundation.
* Foster, D., 2024, ‘The New Dynamics of Open Source: Relicensing, Forks, and Community Impact’, paper presented to OpenForum Academy Symposium, Boston,  Massachusetts, 13-14 November, Available at [https://doi.org/10.48550/arXiv.2411.04739](https://doi.org/10.48550/arXiv.2411.04739)
* Imtiaz, N., Khanom, A., & Williams, L. (2022). [Open or sneaky? fast or slow? light or heavy?: Investigating security releases of open source packages.](https://arxiv.org/pdf/2112.06804) *IEEE Transactions on Software Engineering*, *49*(4), 1540-1560.
* Vargas, S., Link, G., & Lee, J. (2024, April). [Estimating Usage Of Open Source Projects](https://dl.acm.org/doi/pdf/10.1145/3643991.3645066). In *Proceedings of the 21st International Conference on Mining Software Repositories *(pp. 652-653).

CHAOSS Practitioner Guides are MIT licensed, living documents, and we welcome your feedback and input. You can suggest edits to this document at [https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/viability.md](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/viability.md)