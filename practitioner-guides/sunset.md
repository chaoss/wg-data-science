# Practitioner Guide: Getting Started with Sunsetting an Open Source Project

Primary metrics:

* [Change Requests](https://chaoss.community/?p=3610)
* [Issues New](https://chaoss.community/?p=3634)
* [Technical Forks](https://chaoss.community/?p=3431)

If you haven’t already read the [Insight Guide: Introduction - Things to Think about When Interpreting Metrics](https://chaoss.community/practitioner-guide-introduction/), please pause now and read that guide.

Many open source projects, even widely used ones, become abandoned for a variety of reasons (e.g., evolving interests, family situations, employment changes), but abandonment can be done in a responsible way by proactively sunsetting the project (Miller et al. 2025). Sunsetting is an important consideration for corporate environments where it can be easy to lose track of projects that were created by employees who later walked away from the project and left if abandoned. You don’t want abandoned open source projects with security vulnerabilities sitting in your organization’s source code repositories where someone might trust that project simply because they trust your organization. Finding inactive projects and responsibly sunsetting them is a good business decision and something that many open source teams / Open Source Program Offices (OSPOs) do on a regular basis.

It’s important to remember that not every open source project can or should exist forever: technologies evolve, corporate priorities change, and people’s interests change. Part of the beauty of open source is that we work in the open as we innovate, and some of those innovative projects will stand the test of time, while others should be responsibly deprecated via a sunset process. Sunsetting an open source project should take your user’s needs into account, and where possible, offer users time to migrate to a replacement technology. At a minimum, it’s important to signal that the project will no longer be maintained, updated, or have security patches so that users know that they should no longer be using the project.

The most important step you can take when sunsetting a project is to be transparent at every step of the way. Thus, being open about your intentions and ensuring trust for future open source work.

# Step 1: Identify Trends

There are several metrics that can help you identify whether there is any activity or usage for a project to make decisions about responsibly sunsetting a project. Looking at [Change Requests](https://chaoss.community/?p=3610) (aka Pull Requests / Merge Requests) and [New Issues](https://chaoss.community/?p=3634) can be a good start when looking at whether there are still people using and contributing to a project. Another good metric is [Technical Forks](https://chaoss.community/?p=3431), which tend to be an indication of usage and potential contribution.


## Change Requests

The Change Requests metric can help you understand whether people are trying to contribute to your project, which signals whether there is interest in your project. It helps to look at both closed and open requests, since closed change requests indicate that a project might still be maintained, while open change requests that are not being resolved can indicate that a project might be abandoned. If there are no recently merged change requests, then it’s also likely that there have not been any security updates.

![Abandoned project - change requests](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/change_requests_abandoned.png "Example of project change requests decreasing to almost nothing over time. These might be from an abandoned project")

## New Issues

Many new issues are created when a user finds a bug, has a question, or wants a new feature, so new issues may be filed because people are using your project or are otherwise interested in your project. When there are few to no issues created over a period of some time, then it might indicate that the project has been abandoned.

![Abandoned project - new issues](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/issues_abandoned.png "Example of new issues decreasing to almost nothing over time. These might be from an abandoned project")

## Technical Forks

These are the forks that people create when they are using your project or planning to contribute to it, but it can help to look beyond the numbers of forks to see who has forked your project and whether they are continuing to update their fork. Recently updated forks can indicate usage, and by gathering data about who has forked your project, you might also be able to reach out to some of these people to ask if they are still using it before you decide whether, or how, to sunset it. 

# Step 2: Diagnosis

If you are part of an organization who is auditing their repositories to find projects that seem to be abandoned, you should start by talking to the people who were involved in the project so that you can better understand whether the project is truly abandoned, and if so, why. This will likely require looking at the most recent change requests to see who made the last few changes to the project so that you can reach out to them. In some cases, a project might not need to be updated regularly and might seem to be abandoned when it has simply stabilized and might still be widely used. For example, a small library that performs some complex mathematical function might not need to be updated after it is written, assuming that it doesn’t have dependencies that need to be updated. If the project is primarily distributed via package managers, usage metrics from those sources should also be considered.

If the project has truly been abandoned, then it can help to understand why it was abandoned and whether anyone might still be using it before you decide to sunset it. This is where the technical fork data can be useful to see if other people have forked your project and are continuing to update their fork, which might indicate usage of your project. [Criticality Score](https://github.com/ossf/criticality_score), an OpenSSF project, can also shed light on usage, since it also calculates the number of projects that depend on your project. There is a [Python script](https://github.com/geekygirldawn/project-api-metrics/blob/main/scripts/sunset.py) called that uses criticality score and the GitHub API fork data that can be used to gather and analyze this data.

# Step 3: Gather Additional Data if Needed

CHAOSS has other metrics to understand project activity and usage that can be helpful when deciding whether to sunset a project.

Additional Metrics: 

* [Collaboration Platform Activity](https://chaoss.community/?p=3484)
* [Clones](https://chaoss.community/?p=3429)
* [Code Changes Commits](https://chaoss.community/?p=4707)
* [Release Frequency](https://chaoss.community/?p=4765)
* [Project Popularity](https://chaoss.community/?p=3573)
* [Criticality Score](https://github.com/ossf/criticality_score) (an OpenSSF tool, not a CHAOSS metric)
* Package Manager usage metrics

# Step 4: Make the Change

After you have completed your diagnosis and have decided to sunset a project, there are several things you can do to ensure that you are sunsetting the project in a responsible manner.

**Communication**

Communication should start with any existing contributors to make sure that they agree with this decision. In some cases, there may be contributors who would like to continue the project, instead of sunsetting it.

When you have agreement to sunset the project, then this needs to be communicated to any existing users, including any other internal teams who may be using the project. This communication should be done in a transparent manner by being clear about the reasons for sunsetting it. There are quite a few places that this should be communicated and documented:

* README: Clearly state at the top the README that the project has been deprecated and will no longer be updated. If possible, suggest alternate projects that provide similar functionality.
* Project communication channels: This may include Slack, mailing lists, forums, social media, and any other channels used for communication within the project.
* Documentation: Project documentation should also be updated. This may include wikis, websites, and other project documentation.
* Package managers / distribution channels: Since most projects are distributed via package managers (e.g., npm, PyPI, RubyGems), those should also be updated with a deprecation warning that clearly states that the project is no longer being maintained or updated.
* Additional channels: If this is a corporate project, marketing and other internal teams should also be notified.
* Users: Known users of the project should also be notified.

**Archival**

The project should be officially archived using something like GitHub’s archival method. It might also be a good idea to keep these projects in a separate location to make it clear that these projects have reached the end of their life. For example, VMware has a separate ‘vmware-archive’ organization, and Apache has something similar called the ‘Apache Attic’.

Taking the additional step of adding your code to the [Software Heritage](https://www.softwareheritage.org/) archive can help preserve it over time. This is especially true if you are self-hosting your source code repositories, but it can also help archived code outlive potential platform changes and make it easier for people to find in the future. 

Keep in mind that projects can always be unarchived if you change your mind later. Stressing this fact can often make it easier to get people to agree to the sunset process.

**Special Case: Sunsetting Active Projects**

Unfortunately, even active projects may need to be sunsetted, which can be much more difficult. This can happen when a project is being maintained entirely by a company, and that company has a shift in strategy and decides that they no longer wish to staff or maintain a project that is being widely used. There are a number of additional considerations in this case that should happen before the project is archived:

* Public Relations (PR): Archiving an active project can be a tricky situation that might result in negative press as soon as you start talking to people about your desire to sunset the project, so before talking to anyone outside of your company, you want to get your PR team involved so that they can be ready to handle any queries.
* Option to continue under new ownership: Determine if there are other contributors or other organizations who would be willing and able to take over new development and / or maintenance of the project.
* Sunset plan: It can help to create a detailed plan that outlines all of the steps that need to be taken along with a timeframe for when the project will be sunsetted.
* Timing: A responsible sunset plan will give users time to migrate to another solution before you stop making security updates and releases. 6 months is a good starting point.
* Customers, users, and communication: Careful communication is required to communicate this decision along with the timing to any existing customers and users.

# Cautions and Considerations

* It is worth taking some extra time to talk to contributors and make sure that the decision to sunset a project is the right decision before you do it.
* Be as transparent as possible about the decision to sunset a project and why you made that decision.
* Sunsetting a project is not an indication of failure and should not be positioned as such. Projects have life cycles; they endure for as long as they are needed and then they should be responsibly deprecated when they are no longer needed.
* Consider providing transition details, and if possible, tooling that helps your existing users transition to an alternative solution if a reasonable one is available. 
* As with all of the CHAOSS Practitioner Getting Started Guides, these materials are designed to help you get started when sunsetting a project, but it is not a comprehensive guide with everything you might need to know for every situation.

# Additional Reading

* Stefka Dimitrova on When and How to Deprecate an Open Source Project ([Part 1](https://blogs.vmware.com/opensource/2022/09/29/when-and-how-to-deprecate-an-open-source-project/) and [Part 2](https://blogs.vmware.com/opensource/2023/05/17/deprecating-an-open-source-project-part-2/)) along with a video from the Open Source Summit in Europe in 2022 about [Simple Steps for a Calm “Sunset”](https://www.youtube.com/watch?v=OdpkMkoKtDY). Much of the content for this guide is based on these materials.
* [GitHub’s Do’s and Don'ts When Sunsetting Open Source Projects](https://github.blog/open-source/maintainers/dos-and-donts-when-sunsetting-open-source-projects/)
* [TODO Group Guide: Shutting Down an Open Source Project](https://todogroup.org/resources/guides/shutting-down-an-open-source-project/)
* [Allen Friedman on End of Life and End of Support Across the Ecosystem](https://www.youtube.com/watch?v=ZgWwiKLB6hE) (video)
* [10 Quick tips for making software outlive your job (white paper)](https://arxiv.org/abs/2505.06484)

# Contributors

The following people contributed to this guide:

* Dawn Foster
* Ria Schalnat
* Damián Vicino
* Matt Germonprez
* Elizabeth Barron
* Tara Tarakiyee

# References

* Miller, C., Jahanshahi, M., Mockus, A., Vasilescu, B., & Kästner, C. (2025). [Understanding the response to open-source dependency abandonment in the npm ecosystem](http://www.cs.cmu.edu/~ckaestne/pdf/icse25_abandonment.pdf). In *Int’l Conf. Software Engineering (ICSE), IEEE/ACM*.

