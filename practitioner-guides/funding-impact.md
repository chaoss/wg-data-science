# Practitioner Guide: Funding Impact Measurement

If you haven’t already read the [Practitioner Guide: Introduction - Things to Think about When Interpreting Metrics](https://chaoss.community/practitioner-guide-introduction/), please pause now and read that guide.

# Audience / Scope

The audience for this guide is organizations who seek to demonstrate and/or justify the impact of the funding that they provide to open source projects / maintainers. This includes public funding and grant-making organizations, government agencies, companies, philanthropic foundations, and other organizations providing funding to open source projects / maintainers. Demonstrating the impact of internal open source initiatives within an organization is out of scope, but is covered in the [Practitioner Guide: Demonstrating Organizational Value](https://chaoss.community/practitioner-guide-demonstrating-org-value). The return on investment for commercial open source companies is also out of scope, but can be found in the [LF State of Commercial Open Source report](https://www.linuxfoundation.org/research/2025-state-of-commercial-open-source).

# Introduction

Open source software has become ubiquitous and can be found in almost every codebase, but sustaining those open source projects and communities over the long-term can be a challenge. Historically, much of the funding provided to open source projects has been for development of new projects and/or new features with the goal of fostering novel innovation. However, only funding innovation is not enough to ensure the sustainability of open source projects (Osborne, 2024).  Several high profile, widely spread security vulnerabilities in open source projects (e.g., Log4Shell, Heartbleed) have also highlighted the need to fund maintenance and security and maintenance work in critical projects. With the push toward digital sovereignty and the recognition of the role that open source software can play, governments are now funding the maintenance of popular open source projects (e.g., [Sovereign Tech Agency in Germany](https://www.bundeswirtschaftsministerium.de/Redaktion/EN/Pressemitteilungen/2022/10/20221018-the-sovereign-tech-fund-launches-funding-an-investment-in-europes-digital-sovereignty.html), the work toward an [EU Sovereign Tech Fund](https://eu-stf.openforumeurope.org/)). Similarly, many companies are also seeking to support the open source projects that they rely on and use in their business operations. The role of open source software for supply chain security is also becoming increasingly important as governments, corporate procurement teams, and other groups start to create Software Bill of Materials (SBOMs) mandates.

Much of the critical infrastructure that we all rely on is made up of open source projects that lack the resources to be properly maintained over the long term. Companies, public institutions, and philanthropic organizations are beginning to fill this gap, but measuring the impact of this funding is an ongoing challenge (Osborne et al., 2024). Funders need to be able to understand the impacts of past funding in order to secure buy-in for future funding as well as to adapting and/or innovating [funding approaches](https://recommendations.implicit-development.org/) whilst mitigating ineffective or even harmful approaches. We all benefit from more public institutions, philanthropic organizations, and companies giving money to open source; when done in a way that positive impact is the ultimate goal and objective. 

# Challenges

Interest in open source funding is increasing, but there is little consensus on how to measure them in a meaningful way. Not only is the measurement of the impacts of open source funding challenging, but it is complicated by the fact that introducing funding into open source projects may change contributor incentives and the balance of voluntary and paid participation when some contributors become funded for project work. Funding may or may not be the right solution for all projects, and funders need to think about the best way to achieve their goals when funding projects. For example, general funding may not improve the security posture of open source projects as well as targeted support designed to strengthen security (Brackett, et. al., 2025) By better understanding the impacts of funding (or lack of), funders can learn more about what works well for different types of open source projects so that the funding provided can have the greatest benefit for fundees and more widely across the entire ecosystem.

Developing standardized funding impact measurement frameworks also presents challenges because the goals and objectives for the funding varies widely by funding organization and open source project, and how impact is measured depends on those goals and objectives. For example, providing funding for new feature development vs. funding for security fixes and maintenance require different funding impact measurement approaches. 

# Lessons Learned

Funders have a wide variety of goals and objectives for their funding, and every open source project being funded operates a bit differently, so there is no one size fits all approach to measuring the impact of funding. Funding impact measurement requires a customized approach that takes the goals of the funder and the unique needs of the open source project being funded into account.

Using the goals and objectives for the funding provides a starting point for selecting the metrics, but metrics and other quantitative measurements don’t provide the details needed to fully understand the funding impact. Qualitative measurements can help to understand how the funding impacted project dynamics, motivations, and other intangible outcomes. Using a mixed methods approach provides a way to get the best of both worlds with scalable quantitative measures along with contextual depth from qualitative data gathered in collaboration with the open source projects (Casari et al., 2023).

It is worth noting that the impacts of funding for open source projects and / or maintainers are not necessarily always positive. Some projects struggle to use the funding when they don’t already have a mechanism for distributing funds, and funding can create internal strife within a project when some people become paid to work on the project and others are not.

# How to Take Action

## Start by Understanding the Context

Accounting for funding objectives, project life stage and social structure, and regional and organizational cost factors is an important first step in measuring funding impact, since it provides important context. Each of these areas is covered in more detail below.

### Start with the Funding Objectives

Different funding instruments and procurement – whether milestone-based contracts with deliverables, bug bounty programmes, or general project support – have varying purposes, from innovation to maintenance, and in turn can have varying impacts. Understanding the specific objectives of the funding helps to align the impact measurements with the expected outcomes. For example, projects are often funded based on a set of milestones that are mutually agreed upon by the funder and the project. As a result, each project works toward different milestones with different goals and objectives, so there is no one-size-fits-all measurement to determine the impacts of funding programs. One approach is to assess impacts against each project's agreed milestones, but this may measure compliance rather than impact. Later in this guide, the impacts section includes a range of possible economic, social, and technological impacts, which can be both positive and negative, direct and indirect, internal (project) and external (ecosystem), and manifest over varying time horizons, which provide a broader perspective beyond funding objectives.

### Consider Project Life Stages and Social Structures

The impacts of funding vary depending on both a project's life stage and its social structure. For example, a new prototype project will have very different needs and potential outcomes compared to a mature project with an established community. While the prototype might need funding to build initial features and attract contributors, the mature project might require support for security improvements or maintenance work. 

Similarly, considering the social structure of a project is crucial for understanding funding impacts. For instance, Nadia Asparouhova (was Eghbal) (2020) identifies four distinct models of open source projects based on their contributor and user ratios: federations, clubs, stadiums, and toys. Funding for a federation-type project might need to account for complex governance processes and multiple working groups, while funding for a stadium-type project might focus on supporting its small core of maintainers who serve a large user base. These structural differences affect not only how funding should be allocated but also how its impact should be measured.

### Account for Salary Structures and Cost Factors

Salary structures and cost factors across regions and organizations should also be considered. When similar budgets are allocated to different organisations or regions, they can support different numbers of developers due to varying salary levels. Even with access to salary and cost data, compensation can vary wildly with a senior developer in one organization earning less than a junior developer in another organization.

## Economic, Social, and Technological Impacts 

Funding can have many different types of impacts, which funders might want to consider (see also the [Superbloom toolkit](https://buildingblocks.superbloom.design/about/)). The potential social, economic, and technological impacts can be both positive and negative, direct and indirect, internal (i.e. within a project) and external (i.e. among a project’s ecosystem of dependents and users), and manifest over various time horizons.

When assessing the impacts of open source funding, there may be a tendency to focus on technological impacts, which may in part be due to the technological nature of open source development or the relative ease of measuring technological impacts due to data availability from repositories. However, the potential impacts of funding extend beyond the code itself, and it is crucial to consider economic and social impacts on projects and their wider ecosystems of dependents and users. It is also important to note that impacts are not linear or unidirectional; funding can lead to both improvements and degradations across different metrics. This multidirectional nature of impacts means that measurement frameworks need to be flexible to capture both positive and negative changes, rather than assuming funding inherently leads to improvements or that metrics only move in one direction. Illustrative examples of various impacts can be found in the table below. 

**Examples of Social, Economic, Technological Impact Areas of Open Source Funding**

<table>
  <tr>
   <td>
   </td>
   <td><strong>Internal Impacts (Project-level)</strong>
   </td>
   <td><strong>External Impacts (Ecosystem-level)</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Direct</strong>
<p>
<strong>Impacts</strong>
   </td>
   <td>
<ul>

<li><em>Social:</em> <a href="https://chaoss.community/?p=3630">Contributor</a> retention, <a href="https://chaoss.community/?p=3432">community engagement</a>, <a href="https://chaoss.community/?p=3507">community events</a>, <a href="https://chaoss.community/?p=4889">contributor diversity</a>, work-life balance, reduced <a href="https://chaoss.community/?p=3537">burnout</a>, <a href="https://chaoss.community/?p=3524">mentorship</a></li>

<li><em>Economic:</em> <a href="https://chaoss.community/?p=3559">Paid developer time</a> / support roles, infrastructure coverage, conference sponsorship, project-related revenue via various channels</li>

<li><em>Technological:</em> <a href="https://chaoss.community/?p=3448">Maintainer responsiveness</a>, commit <a href="https://chaoss.community/?p=3572">velocity</a>, code <a href="https://chaoss.community/?p=3939">security</a>, <a href="https://chaoss.community/?p=3976">dependency management</a>, <a href="https://chaoss.community/?p=3532">documentation quality</a>, <a href="https://chaoss.community/?p=4765">consistent releases</a></li>
</ul>
   </td>
   <td>
<ul>

<li><em>Social:</em> User trust, ecosystem community, ecosystem events</li>

<li><em>Economic:</em> Cost savings for adopters, integration/support costs, shared maintenance burden</li>

<li><em>Technological:</em> Stability of APIs, ecosystem-wide security updates, interoperability</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Indirect</strong>
<p>
<strong>Impacts</strong>
   </td>
   <td>
<ul>

<li><em>Social:</em> <a href="https://chaoss.community/?p=3522">Leadership development</a>, <a href="https://chaoss.community/?p=3516">governance</a> and decision-making processes, knowledge preservation, <a href="https://chaoss.community/?p=5430">conflict resolution/prevention mechanisms</a></li>

<li><em>Economic: </em><a href="https://chaoss.community/?p=3567">Job</a> market value for developers, partnership opportunities, <a href="https://chaoss.community/?p=3583">academic</a> collaborations, consulting opportunities, funding diversity</li>

<li><em>Technological: </em>Standardisation, interoperability</li>
</ul>
   </td>
   <td>
<ul>

<li><em>Social:</em> Cross-project collaboration, training & education resources, ecosystem engagement</li>

<li><em>Economic: </em>Market growth, job creation, industry cost reduction, start-up creation</li>

<li><em>Technological: </em>Standardisation, research papers, patents, ecosystem-wide security improvements</li>
</ul>
   </td>
  </tr>
</table>


When measuring the impact of funding on open source development, it is crucial to consider the effects across different time horizons. The influence of funding can manifest differently in the **short, medium, and long term**, which is essential for a comprehensive understanding of funding impacts.

1. Short term (&lt;1 year): These are the immediate effects of funding, which may be easier to observe and attribute to the funding received. Short-term impacts might include immediate increases in [development activity](https://chaoss.community/?p=3444), improvements in code quality, or rapid growth in [community size](https://chaoss.community/?p=3484).
2. Medium term (1-3 years): Medium-term impacts may reveal how the project adapts and grows with the resources provided. This period might show the development of new features, expansion of the project’s reach, or evolution of the project’s governance structures.
3. Long term (>3 years): Long-term impacts are the enduring effects of funding that manifest over an extended period, which can be the most challenging to measure and attribute directly to funding.

## Methods

When it comes to measuring the impacts, funders can consider a breadth of methods for impact measurement. We recommend using a mixed methods approach, which provides a way to combine scalable quantitative measures along with contextual depth from qualitative data to better understand the funding impact.

**Quantitative methods** offer a structured, scalable approach for measuring relationships between funding and outcomes in open source projects and their ecosystems. Starting with the funding objectives provides a focus for metric selection, rather than trying to cast a wide net that includes metrics that aren’t as relevant. These quantitative metrics can be gathered from repositories, surveys, and other sources, but there are also challenges. Some data isn’t often available for open source projects (e.g., [usage](https://chaoss.community/?p=3573), non-code contributions), and open source projects have different ways of working (e.g., commit strategies, [code review](https://chaoss.community/?p=4712) processes) that make analysis more difficult. 

**Qualitative** **methods**, such as case studies, interviews, and participant observation, are useful strategies for collecting contextual data about the history, role, and impacts of funding on open source projects. A major strength of interviews lies in their ability to provide rich, contextual understandings by gaining insights into the perspective of the funding recipients, revealing why funding was needed and how it has influenced project dynamics, individual motivations, and community structures. Qualitative methods are useful for capturing intangible outcomes and hard-to-quantify impacts, such as changes in project culture or enhancements in the overall sustainability of the project, which often play a crucial role in the long-term success of open source projects but can be challenging to measure through quantitative means alone. Challenges can include securing the right people for interviews, ensuring representation, and the time required to conduct and analyze qualitative data.

**[Mixed-Methods](https://arxiv.org/pdf/2411.06027)** approaches that combine qualitative and quantitative techniques offer the best of both words: scalability and contextual depth. Mixed-methods approaches are particularly useful for examining complex open source ecosystems, where development spans multiple channels and goes beyond repositories. There are several ways to conduct mixed methods approaches. By starting with quantitative data the subsequent qualitative phase can be used to better explain the earlier data, which can be especially useful when looking at a large number of projects. On the other hand, starting with qualitative data offers a more exploratory approach that can be used to decide which quantitative measures to use, which may offer a better way to discover unanticipated impacts. They can also be collected and analyzed concurrently using a maturity model approach to create a holistic view of the development of an open source project, but this can be time-consuming and challenging to get agreement on what constitutes maturity.

A much more detailed assessment of the strengths and weaknesses of qualitative, quantitative, and mixed methods approaches can be found in Section 3.4 of Osborne et al., (2024) with a summary in Table 3 on page 10.

# Conclusion

While measuring the impact of funding open source projects can be challenging, this guide provides a framework for ways that impact(s) can be measured based on lessons learned from organizations already doing this work. By starting with the organization’s funding objectives, understanding the open source projects being funded, and accounting for cost factors, the funding initiatives can be put in the proper context before starting to measure the impact. This can be followed by an assessment of the economic, social and technological impacts that consider direct / indirect impacts along with project-level / ecosystem level impact to think about the metrics and timelines that might be important in your context. The final step is to consider how using a mixed-methods approach can combine scalable quantitative measures along with contextual depth from qualitative data to better understand the funding impact. The case studies section includes examples of organizations who are already doing this work.

Funders need to be able to understand the impacts of past funding in order to secure buy-in for future funding as well as to adapting and/or innovating funding approaches whilst mitigating ineffective or even harmful approaches. We all benefit from more public institutions, philanthropic organizations, and companies giving money to open source; when done in a way that positive impact is the ultimate goal and objective. We hope that this guide helps organizations measure the impact of their funding initiatives so that we can increase the funding to open source projects to drive future improvements and allow these projects, and the people working on them, to become healthier and more sustainable over time.

# Cautions and Considerations

* There is no one-size-fits-all approach to measuring impact. Measuring the impact(s) of open source project funding is something that we’re all figuring out as we go along, so we expect this space to evolve over time as we learn more about the best ways to measure impact.
* Funding may or may not be the right solution for all projects and can result in both positive and negative impacts for projects. Funding can introduce unanticipated challenges for open source projects, especially the first time they receive funding, and some projects struggle to use their funding. 
* Open source projects are made up of people, and money can create complications. Funding into open source projects can change contributor incentives and the balance of voluntary and paid participation, which should be considered when measuring impact.

# Additional Resources

* [A Toolkit for Measuring the Impacts of Public Funding on Open Source Software Development](https://arxiv.org/abs/2411.06027) - this paper was the starting point for this guide, and it provides many more details on the subject.
* [CHAOSS Funding Impact Measurement Working Group](https://github.com/chaoss/wg-funding-impact) - join us!
* [Roadwork ahead: Evaluating the needs of FOSS communities working on digital infrastructure in the public interest](https://recommendations.implicit-development.org/)
* [Podcast: Funding Impact Measurement Working Group on CHAOSScast](https://podcast.chaoss.community/106) in March 2025.
* [Toolkit for Measuring the Impacts of Public Funding for OSS](https://25.foss-backstage.de/schedule/#session/7UJYUR/) at FOSS Backstage in Berlin in March 2025 ([video](https://25.foss-backstage.de/session/toolkit-for-measuring-the-impacts-of-public-funding-for-foss/)).
* [Panel: The Impact of Funding for Sustainable Open Source Projects](https://sched.co/1zfhR) with Georg Link, Andrew Nesbitt, and Alyssa Wright at the Open Source Summit NA in Denver in June 2025 ([video](https://www.youtube.com/watch?v=8sD81Dqw0Os)).
* [FOSS Funders](https://fossfunders.com/)
* [OSS Research-Software: Incentivizing Investment in and Adoption of Open Infrastructure for Research through Community Health Assessments](https://infrastructureinsights.fund/projects/oss-research-software/)
* [Building bridges: How trust and community health frameworks can strengthen open infrastructure decision-making](https://investinopen.org/blog/building-bridges-how-trust-and-community-health-frameworks-can-strengthen-open-infrastructure-decision-making/)
* [Building Blocks: Digital Infrastructure Funding Toolkit](https://buildingblocks.superbloom.design/about/)

# Contributors

The following people contributed to this guide:

* Dawn Foster
* Cailean Osborne
* Paul Sharratt
* Mirko Boehm
* Serkan Holat
* Katharina Meyer

# References

* Brackett, S. A., Scott, S., and Chen, C. (2025). [Buying Security: Open Source Software Funding and Security Posture](https://infrastructureinsights.fund/wp-content/uploads/2025/12/CSINTPolicyPaperNo22025BrackettScottandCheng.pdf). CSINT Policy Paper Series. Fall 2025.
* Casari, A., Ferraioli, J., & Lovato, J. (2023). [Beyond the Repository](https://dl.acm.org/doi/pdf/10.1145/3605160). *Communications of the ACM*, *66*(10), 50-55.
* Asparouhova, N. (2020). *Working in public: the making and maintenance of open source software*. Stripe Press.
* Osborne, C., Sharratt, P., Foster, D., & Boehm, M. (2024). [A Toolkit for Measuring the Impacts of Public Funding on Open Source Software Development](https://arxiv.org/abs/2411.06027). *arXiv preprint arXiv:2411.06027*.
* Osborne, C. (2024). [Open Source Software Developers' Views on Public and Private Funding: A Case Study on scikit-learn](https://dl.acm.org/doi/abs/10.1145/3678884.3681844). In Companion Publication of the 2024 Conference on Computer-Supported Cooperative Work and Social Computing (CSCW Companion '24). Association for Computing Machinery, New York, NY, USA, 154–161. https://doi.org/10.1145/3678884.3681844

CHAOSS Practitioner Guides are MIT licensed, living documents, and we welcome your feedback and input. You can suggest edits to this document at https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/funding-impact.md
