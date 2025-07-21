# Practitioner Guide: Demonstrating Organizational Value

If you haven’t already read the [Practitioner Guide: Introduction - Things to Think about When Interpreting Metrics](https://chaoss.community/practitioner-guide-introduction/), please pause now and read that guide.

# Audience / Scope

The audience for this guide is open source teams and Open Source Program Offices working within organizations where there is a need to demonstrate the value of the work and justify the resources being used for open source initiatives. 

# Introduction

Many people contribute to open source projects as part of their employment. In a [2023 survey of open source maintainers](https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en), the Linux Foundation found that 62.5% were employed to work full time on their projects, and [another study by Sophia Vargas (2023) at Google](https://opensource.google/static/documentation/publications/WhatBringsYouToOpenSource_2023.pdf) found that 30% of the developers in their sample contributed in their professional time only and 52% contributed in both personal and professional time. This participation from within organizations can help sustain open source projects over time by employing people to work on the open source projects that they use or by contributing other resources to those projects (Egbahl 2016). However, it remains a challenge for many organizations to justify the value of this work so that it can continue over the long periods of time needed to sustain open source projects.

**A few notes about terminology:**

* This guide uses the term "**organization**" deliberately because demonstrating organizational value is important for a wide variety of different types of organizations (e.g., university / government OSPOs, research groups, corporations).
* Throughout this guide, the term “**goals**” is being used to describe what the organization is planning to achieve. Depending on the organization, the goals might be described as part of the vision, mission, or strategy. In the context of a company business unit, the goals might be part of a product line strategy or plan. These goals are a key component of demonstrating **value** to your organization because organizational leadership is more likely to see the value in work that is clearly aligned with the goals of the organization.  

# Challenges

The open source teams in many organizations experience pressure from leadership to drop and / or reduce their open source contributions to focus on internal initiatives that deliver more “value” to the organization. This puts open source teams in the position of needing to justify their work in open source to demonstrate that it has as much or more value than other initiatives that employees could be working on. However, it can be difficult to frame the justification in ways that resonate with leadership and clearly articulate how the organization benefits from continued contributions to an open source project.

Open source teams often default to justifying their work by talking about contributions to open source in ways that sound like charity by talking about how it’s for the good of the community, which doesn’t resonate with leadership because it doesn’t show a return on investment of employee time.

In other cases, open source teams provide an overview of what they use internally with data about the work done in an open source project (e.g., numbers of contributions, maintainers, commits, features); however, what this indicates to leadership is that while an employee is spending effort, there still isn't a demonstrated return on the time spent by employees on open source efforts.

Another challenge for many organizations is that they have no overall open source strategy for their contributions. Employees are frequently encouraged to contribute to open source directly or indirectly without proper guidance about how to demonstrate the value of these efforts, and this can create a negative feedback loop:

* Employees are encouraged to contribute.
* The value is not understood, so leadership asks: “Why are we spending time on something that doesn’t help us?”
* Employees are told to spend less time on open source, creating the feeling of being unrecognized and undervalued, which leads to burnout.
* Both the open source project AND the organization begin to suffer.

This negative feedback loop can be even more pronounced in organizations where there is no official open source team, and demonstrating the value of this work falls to unofficial teams made up of individual contributors who may not be in a position or have the time to justify this work. In some cases, these individuals might be contributing because an open source project needs bug fixes or features that would help with their job duties, but this isn’t seen as part of their official role.

# Lessons Learned

Leadership wants answers to the following questions:

* What is the criticality of the open source projects the organization is helping maintain?
* What is the organization getting out of contributing to open source projects?
* How much software engineering time is being spent on maintaining open source projects? 

Creating an open source contribution strategy can help organizations frame their discussions with leadership to demonstrate the value of their open source efforts in ways that resonate with leadership. At a minimum, the open source strategy should contain details in the following areas, which are each addressed in the “How to Take Action” sections below:

* Supporting your organization’s **goals**
* Determining which open source projects are the most **critical** for your organization 
* Assessing open source project **health risk**
* **Prioritizing** within your organization’s limited resources
* Measuring & framing **value** 

# How to Take Action

By creating a robust open source strategy that demonstrates the value of your organization’s open source efforts, these efforts and outcomes can be described in ways that resonate with leadership by clearly articulating how the work in open source helps your organization achieve its goals. This helps to frame the rest of the strategy that describes the influence of open source project health, how your organization’s resources are being used, and finally how the value is being measured. 

## Supporting your organization’s *goals*

Taking some time and effort to make sure that your open source strategy supports the overall organization’s goals makes it much easier to justify continuing organizationally-relevant open source projects. Explaining how open source contributions support the goals of the organization can help the executive team understand the strategic importance of this work.

Having a solid open source strategy is important because successful participation in open source requires a long-term commitment. Individuals and organizations spend months and years building trust and reputations within specific open source communities, and all of that hard work is wasted if those people keep getting pulled off of open source projects to work on internal efforts. Keeping people working on the open source projects that are critical to your organization requires planning and strategic thinking to prioritize these open source efforts and align them with the overall goals for your organization. 

However, every organization has a limited number of people and other finite resources, so ***prioritizing*** your open source efforts can help you focus on the activities that demonstrate the most value to your organization and most directly help the organization achieve its goals. This prioritization helps to facilitate efficient use of limited resources. For this guide, priority is defined as a formula made up of criticality multiplied by health risk.

![Priority = Criticality X Health Risk](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/priority-formula.png "Priority = Criticality X Health Risk")

***Criticality*** is where these efforts align with the goals of your organization. By showcasing the criticality of certain open source projects for your organization, these critical projects can be used to frame the strategies in a way that leadership will understand how important it is to continue this work over the long-term to ensure that the company can achieve its goals.

***Project health risk*** is important in this equation because some open source projects are healthier and more sustainable than others, so some projects are riskier and need more help. A healthy open source project that is critical to your organization is likely to be a lower priority than an equally critical, but more risky project that needs your organization’s help to become healthy and reduce the risk of using it. 

Thus, the priority for investment (allocating staff or other resources) is a combination of criticality and project health risk that is unique to your organization. 

## Determining which open source projects are the most **critical** for your organization

For all of the important open source projects used, it’s important to determine the criticality of each project, which also means that it’s important to have a software inventory that helps to identify those projects. Many organizations are already performing these inventories to evaluate their supply chain risk, so criticality dovetails nicely with existing supply chain assessment initiatives.

To better illustrate this concept, here are some example categories with descriptions and questions that might help determine criticality.

**Dependency**: Determine how your organization depends on this open source project. 

* Is it a core component to the function of your organization?
* Does it have high usage rates across the organization?
* What are downstream impacts to your organization’s projects, products, services, or teams?
* How difficult would it be to switch to something else? Or fork and maintain internally? And what would that cost be?
* What would the impact of an unplanned security event be?

**Opportunities:** There are opportunities to drive or influence the open source project to better suit your organization’s needs.

* Does it currently have features or initiatives on the roadmap that would be beneficial? If yes, how so? 
* If it went in another direction, how would it affect your organization?
* What opportunities make it worth investing resources in?
* Could development create a competitive advantage?
* Does your organization want to be seen as a leader in this space? Or be strongly associated with it?

**Supportability**: Determine your organization’s ability to support using the open source project.

* How easy is it to support? Is it well documented?
* How difficult is it to skill-up employees or backfill on expertise?
* Does it help reduce or manage costs (e.g. right-sizing pods)? If so, by what factor? 
* Would using and committing resources to it be a better option than a vendored option?
* Does using it enable picking from multiple solutions and avoid vendor lock-in?

The answers to these questions can help you map each open source project on a criticality scale. Here are some examples that can be used as a starting point to assign criticality using a 1 (low) to 10 (high) scale, which you’ll see again in the prioritization section later in this guide:

<table>
  <tr>
   <td colspan="2" ><strong>Example Criticality Scale</strong>
   </td>
  </tr>
  <tr>
   <td><strong>High (8 - 10)</strong>
   </td>
   <td>
<ul>

<li>Critical to core functions</li>

<li>High usage rates across the organization</li>

<li>Extremely difficult to swap or maintain internally</li>

<li>Difficult to backfill expertise</li>

<li>Roadmap has features that would be very beneficial to organization</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Moderate (4 - 7)</strong>
   </td>
   <td>
<ul>

<li>Software that supports core functionality</li>

<li>Could be swapped out with reasonable effort </li>

<li>Easy to backfill expertise</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Low (1 - 3)</strong>
   </td>
   <td>
<ul>

<li>Non-essential tools/apps with minimal organizational impact</li>

<li>Could be swapped out with minimal effort (API compatible)</li>
</ul>
   </td>
  </tr>
</table>

## Assessing open source project **health risk**

Now that the criticality has been determined, it’s time to think about the other part of the equation, open source project health risk (Priority = Criticality x Health Risk). 

There are many ways to think about open source project health risk, but it can help to start with a few things:

* [Quality codebase](https://chaoss.community/kbtopic/software/): Sound architectural design, static code analysis, sufficient testing
* [Responsive](https://chaoss.community/practitioner-guide-responsiveness/) to issues / PRs:  Time to first response / review
* Healthy [organizational participation](https://chaoss.community/practitioner-guide-organizational-participation/): No single vendor drives the whole project
* Has future plans and a roadmap: They are planning and have a design review process
* [Quality documentation](https://chaoss.community/?p=3532) for [both users & contributors](https://chaoss.community/?p=3534): Docs are critical for both adoption and [contributor sustainability]( https://chaoss.community/practitioner-guide-contributor-sustainability/) and growth
* Good [security](https://chaoss.community/practitioner-guide-security/) and releasing controls: Do they have a history of triaging and resolving security issues, are they using/investigating supply chain security best practices

Similarly to criticality, the health risk of a project can be scored while also potentially looking even deeper at core areas that matter the most to your organization. If a project is unhealthy and it’s critical, it’s likely worth allocating resources to improve the project to bring it into a healthier state. 

As an example, when the CNCF Helm project was found to have several project health concerns due to having a single maintainer, the risk was escalated to the CNCF. Jorge Castro, a CNCF staff member, got involved and helped the project to realign on a target ([the launch of helm v4](https://helm.sh/blog/the-road-to-helm-4/)), as a focal point for contributor growth. This led to building a better contributor ladder, engagement with other projects, organizations, and vendors to invest and make the open source project more sustainable. 

## **Prioritizing** within your organization’s limited resources

With insight on how to score both criticality and health, the following example combines them to set priority. The example uses two made up open source projects “Foo” and “Bar” with some information about their status, a rough scoring, and how that would map to establishing a priority. Assuming each section is worth 10 points, they’re scored with comments in each, and then the criticality score is multiplied by the health risk score. Some important notes:

* The three components of criticality (Dependency, Opportunity, and Supportability) are averaged to create a single criticality score, but using a weighted average might be a better solution depending on your organization’s needs. A higher score means that the project is more critical.
* Health is scored as health risk, which means that lower numbers are better, since a healthy project would have a low risk score.

Example:

<table>
  <tr>
   <td><strong>Project</strong>
   </td>
   <td><strong>Dependency</strong>
   </td>
   <td><strong>Opportunity</strong>
   </td>
   <td><strong>Supportability</strong>
   </td>
   <td><strong>Health Risk</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="2" ><strong>Foo (50)</strong>
   </td>
   <td colspan="3" >
    <strong>Criticality: 8.3 (average of 10, 7, and 8)</strong>
   </td>
   <td>
    <strong>Health Risk: 6</strong>
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><strong>Score: </strong>10</li>

<li>Critical to core functions</li>

<li>Migrating to an alternative would be extremely difficult</li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score:  </strong>7</li>

<li>Roadmap has very useful features</li>

<li>High barrier of entry to contribute and will require more time to engage</li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score:  </strong>8</li>

<li>Extremely difficult to backfill expertise</li>

<li>Not well documented internally</li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score: 6</strong></li>

<li>Project has a large contributor base, but few senior maintainers and contributor ladder needs work</li>

<li>Time to first response is too long</li>
</ul>
   </td>
  </tr>
  <tr>
   <td rowspan="2" ><strong>Bar (21)</strong>
   </td>
   <td colspan="3" >
    <strong>Criticality: 7 (average of 6, 9, and 6)</strong>
   </td>
   <td>
    <strong>Health Risk: 3</strong>
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><strong>Score: </strong>6</li>

<li>Not critical to core function</li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score:</strong> 9</li>

<li>Project is a better option than &lt;Baz> and easy to drive features</li>

<li>Popular, strong branding opportunity to be associated with it</li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score: </strong>6</li>

<li>Easy to backfill expertise</li>

<li>Could be swapped out with reasonable effort </li>
</ul>
   </td>
   <td>
<ul>

<li><strong>Score:  3</strong></li>

<li>Project has enough maintainers and a decent contributor pipeline.</li>

<li>Codebase has solid quality processes</li>

<li>Documentation could be improved.</li>
</ul>
   </td>
  </tr>
</table>

The final step in determining priority is mapping the resources your organization has to the open source projects that have just been assessed for criticality. The example in the table above shows that Foo has a priority score of 50, making it a higher priority than Bar with a priority score of 21. In this case, more resources should be allocated to Foo, but it might make sense to allocate some resources to both.

It can help to think about this in terms of software engineers and software engineering hours, but if your organization can’t commit people, donating funds or hiring contractors to help in these areas might be helpful.

![Priority = Criticality X Health Risk](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/putting-together-formula.png "Resources you have available")

## Measuring & Framing the **Value**

Now that the most critical open source projects have been identified, this information can be  measured and framed in ways that resonate with the leadership team. One of the most common pitfalls is that organizations tend to bias towards easy to measure metrics such as total contributions, but these do not hold up under scrutiny. Metrics should support the goals and be able to be tied back to “value” and the types of resources being invested in the open source project:

* Are the features we’re interested in progressing?
* Are the issues we’re concerned about being addressed?
* Is stability being improved and bugs being fixed?
* Is the project itself healthy?

Ultimately, your organization needs to decide if it is this worth the resource investment vs. maintaining internally or accepting the risk, and it can help think about these across three focus areas:

* **Classifying Features & Initiatives**: How to determine and prioritize what features & initiatives to track
* **Issues & Change Requests**: Tracking the value of contributions to organizational goals
* **Overall Project Health**: Tracking overall open source project health and how it can benefit your organization

### Classifying Features and Initiatives

When investing or contributing to an open source project and that project has a roadmap, it can help to start with the features in a project and evaluate them to determine alignment with your organization’s needs. These classifications are useful when reporting about where people are allocated and why.

* **Invest**: Direct benefit to your organization that warrants allocating more staff to drive the feature or initiative. Frequently these are important features to organization implementation or initiatives deemed important to overall health of the open source project. 
* **Watch**:Feature or initiative that has the potential to either be disruptive or beneficial depending on implementation.
* **Ignore**: No features or initiatives that are expected to benefit or impact how the project is used by your organization.

### Issues and Change Requests

Bugs, security, and issues are useful because most people understand them without having to know a lot about the details of the open source project itself. These are a few example metrics that are not too difficult to get from GitHub and other code platforms. Note that within the CHAOSS project, we use the term Change Request (CR) to include pull requests (GitHub), merge requests (GitLab), patches, and similar processes for merging changes into a repository, since the different tools have different names for this.

<table>
  <tr>
   <td><strong>Type</strong>
   </td>
   <td>
    <strong>Metric</strong>
   </td>
   <td><strong>Source</strong>
   </td>
  </tr>
  <tr>
   <td>Bugs
   </td>
   <td>
<ul>

<li><a href="https://chaoss.community/?p=3633">Bugs reported vs resolved</a></li>

<li><a href="https://chaoss.community/?p=3630">Time to resolution</a></li>

<li>What % are resolved by your org vs others</li>
</ul>
   </td>
   <td>Bugs closed this year (GitHub Query):
<p>
<strong>is:issue closed:2024-01-01..2024-11-01 label:kind/bug</strong>
   </td>
  </tr>
  <tr>
   <td>Security
   </td>
   <td>
<ul>

<li><a href="https://chaoss.community/?p=3633">Security issues reported vs resolved</a></li>

<li><a href="https://chaoss.community/?p=3630">Time to resolution</a></li>
</ul>
   </td>
   <td>Time to resolve security issues (GitHub cli tool):<strong> \
gh issue list –search “is:closed label:security” –json “id,openedAt, closedAt”</strong>
   </td>
  </tr>
  <tr>
   <td>Issue / Change Request
   </td>
   <td>
<ul>

<li><a href="https://chaoss.community/?p=3587">Time to resolution</a></li>

<li>What % are resolved by your org vs others</li>
</ul>
   </td>
   <td>GitHub queries can be tailored with <strong>author:</strong> keyword look at organization created items to track own items vs. project as a whole. \
 \
Issues/PR queries can be tailored to track initiatives
   </td>
  </tr>
</table>

### Overall Project Health

Improving the project health for your organization’s critical open source projects is crucial for reducing the risk associated with using those projects. Within the CHAOSS project, we have [Practitioner Guides](https://chaoss.community/about-chaoss-practitioner-guides/) and [metrics](https://chaoss.community/kbtopic/all-metrics/) that can help identify areas within those open source projects that aren’t as healthy as they could be and take steps to improve in those areas. This is not an exhaustive list, but it should provide a good starting point. 

* [Organizational Participation](https://chaoss.community/practitioner-guide-organizational-participation/)
* [Contributor Sustainability](https://chaoss.community/practitioner-guide-contributor-sustainability/)
* [Responsiveness](https://chaoss.community/practitioner-guide-responsiveness/)
* [Security](https://chaoss.community/practitioner-guide-security/)
* [Adoption](https://chaoss.community/?p=3573)
* [Documentation Usability]( https://chaoss.community/?p=3532)

There are also a number of other important roles in open source projects that can provide value to your organization and improve the health of a project. These are covered in more detail in the Appendix and include, but aren’t limited to:

* Triage and program management
* Documentation
* Communications and marketing
* Events

# Conclusion

To tie all of this back together, here is an example report for the 2 open source projects, Foo and Bar described earlier that can be delivered as a quarterly report. This report highlights the percentage of bugs and security issues fixed by others along with the average time to fix them. Below the table shows a breakdown of Software Engineer (SWE) investment, along with the notes related to the categories that were identified as important. 

Telling the story and communicating to leadership might include examples like these:

* For Bar, we have allocated 1 SWE per quarter, and have seen a good improvement in overall security with bugs trending down and the bugs we filed are all being fixed.
* For Foo, feature baz is set to release next month, and it should drastically improve our developer productivity. We estimate a lag of 2 weeks from release before we can roll it out internally. We made a strategic hire, and they are helping drive that feature upstream and are also spending time upskilling our own team to better engage the project.

![Summary of a report communicating the value of contributions to Foo and Bar](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/conclusion-communication.png "Report Summary")

One guide can’t possibly cover everything about demonstrating the value of your organization’s  open source efforts, so this is just a fraction of the potential ways that open source investments can be tracked and tied back to goals while effectively describing the value of the contributions. It requires the right framing and ensuring that resources are allocated where they may have the most value; however, the framing and resource allocation will be different in almost every situation, since it depends on your organization’s unique needs.

# Cautions and Considerations

* Demonstrating organizational value is highly dependent on your organization’s needs, so these activities should be interpreted in light of your organization’s goals.
* Return on Investment (ROI) is notoriously difficult to measure, but it’s even more difficult to measure when talking about investments in open source software. Coming up with a single ROI number is unlikely, so telling stories and giving examples will be an important part of helping your organization understand the value of your open source efforts.

# Additional Reading

* KubeCon talk by Bob Killen: [Why is this so hard? Conveying the Business Value of Open Source](https://kccnceu2024.sched.com/event/1YeQH/why-is-this-so-hard-conveying-the-business-value-of-open-source-bob-killen-google) (slides and video) and the [White Whale](https://static.sched.com/hosted_files/lfms24/f9/Chasing%20the%20White%20Whale%20of%20Open%20Source%20-%20ROI.pdf) talk from the Linux Foundation Member Summit.
* [CHAOSS Practitioner Guides](https://chaoss.community/about-chaoss-practitioner-guides/) on topics that include improving responsiveness, contributor sustainability, organizational participation, and security.

# Contributors

The following people contributed to this guide:

* Bob Killen
* Dawn Foster
* Justin Gosses
* Ria Schalnat
* Matt Germonprez
* Mike Gifford


# References

* Eghbal, N. (2016). [Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure](https://www.fordfoundation.org/work/learning/research-reports/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/). New York, NY: Ford Foundation.
* Foster, D. (2018). Understanding Collaboration in Fluid Organizations, a Proximity Approach [Doctoral Dissertation, University of Greenwich].
* Linåker, J., Link, G., & Lumbard, K. (2024, October). Sustaining Maintenance Labor for Healthy Open Source Software Projects through Human Infrastructure: A Maintainer Perspective. In *Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement* (pp. 37-48).
* Linux Foundation (2023). [Open Source Maintainers](https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf): Exploring the people, practices, and constraints facing the world’s most critical open source software projects.
* Vargas, Sophia (2023). [What brings you to open source?](https://opensource.google/static/documentation/publications/WhatBringsYouToOpenSource_2023.pdf) How can projects encourage sustainable open source participation? Google Open Source.

# Appendix

There are a number of important roles in open source projects that can provide value to your organization and improve the health of a project. These include, but aren’t limited to:

* Triage and program management
* Documentation
* Communications and marketing
* Events

**Triage and Program Management**

Having a product manager or program manager can help cut down on engineering time spent on things that aren’t really engineering efforts and that engineers might not be able to as efficiently as someone with expertise managing products and programs. Doing triage can provide awareness of open source project activities and issues that are important to your organization much earlier than if you were not involved. By reviewing incoming issues, assigning labels and priorities, and aiding in roadmap planning, your organization gets a number of benefits:

* Prioritized triage of issues & bugs
* Decreased time to resolve
* Early awareness of potential breaking changes & security issues
* De-risk usage of project by improving overall project health
* Introduces better data to answer questions & track trends.

Key Metrics:

* Decreased [time to first response](https://chaoss.community/?p=3448) on issues and change requests
* Decreased time to assignment
* Decreased [issue resolution duration](https://chaoss.community/?p=3630) / [change request duration](https://chaoss.community/?p=3587)

Long Term Health Metrics:

* Increased contributor engagement and sustainability across a variety of metrics (e.g., [number of contributors](https://chaoss.community/?p=3630), [project velocity](https://chaoss.community/?p=3572), frequency of contributions, retention)
* Positive sentiment on issues / change requests and other communication channels

**Documentation**

Many people rely on an open source project’s documentation when getting started, and good documentation can help reduce support requests for common questions or issues that can be headed off with good documentation. In particular, a well documented contributor guide can help with onboarding new people and creating a good start for a contributor funnel. They can increase adoption and general overall positive sentiment with improved site traffic, search engine findability, and other web statistics. Contributors rarely want to do the big initial heavy lift to create documentation from scratch, but if a project has good docs to start, folks are much more open to keeping them updated. **“Having good docs leads to better docs.”** Well-documented open source projects are easier for users to understand and utilize, thus aiding in contributor sustainability, and your organization gets the following benefits:

* Better developer experience
* Increases ability to self-service / decreased engineering time 
* De-risk usage of project by improving overall project health

Metrics:

* Decreased support questions opened
* Increased site traffic & accompanying site metrics

Long Term Health Metrics:

* Increased [new contributor](https://chaoss.community/?p=3613) engagement & retention
* Positive sentiment on issues and change requests

**Communications and Marketing**

Open source projects often lack both the knowledge and skills regarding communication & marketing best practices. Maintainers and engineers do not always have the skills required to craft the right message to get attention, and they often appreciate help with marketing and outreach, which allows them to focus on the technical aspects that are more comfortable for them (Linåker et al., 2024). As an example of unclear and overcomplicated messaging, the description for an enhancement proposal was originally, “This KEP proposes to allow mutating spec.completions for Indexed job if spec.completions equals to spec.parallelism before and after the update, meaning that spec.completions is mutable only in tandem with spec.parallelism.” It was rewritten as, “Enables autoscaling for Indexed Jobs.” By providing resources for communications and marketing, your organization can see the following benefits:

* Improved brand awareness & association
* De-risk usage of project by driving more adoption and conversion to contributors
* Early awareness of potential breaking changes

Metrics

* Increased traffic to website and accompanying site metrics
* Increased social engagement
* Increased share of voice

Long Term Health Metrics

* Growth in [adoption](https://chaoss.community/?p=3573) (e.g., downloads, stars / forks, share of voice)
* Positive sentiment on communication channels

**Events**

Events serve many purposes, from new contributor workshops to help with onboarding, to summits with many high-bandwidth conversations that can unblock development. Many open source projects resolve blockers and bigger issues at events (Foster, 2018), and being in the room can be a huge advantage to make sure your organization’s needs are considered. They’re also useful for workshops and training new contributors. Events are often underestimated, but they help with creating a healthy project, and are important. Your organization benefits in several ways:

* Workshops can serve as onboarding or additional skill-up opportunities
* Being “in-the-room” can ensure organizational needs are addressed
* De-risk usage of project by improving overall project health

Metrics:

* Tracking contributions from attendees
* Conversions from attendees / contributors to maintainers
* Unblocked issues/features

Long Term Health Metrics:

* Increased contributor engagement and sustainability across a variety of metrics (e.g., [number of contributors](https://chaoss.community/?p=3630), [project velocity](https://chaoss.community/?p=3572), frequency of contributions, retention)
* Increase in conversion from contributors to maintainers