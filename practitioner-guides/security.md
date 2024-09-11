# Practitioner Guide: Security

Primary metrics:

* [OpenSSF Best Practices Badge](https://chaoss.community/?p=3939)  
* [Libyears](https://chaoss.community/?p=3976)  
* [Release Frequency](https://chaoss.community/?p=4765)

If you haven’t already read the [Practitioner Guide: Introduction \- Things to Think about When Interpreting Metrics](https://chaoss.community/practitioner-guide-introduction/), please pause now and read that guide.

Security is only as strong as its weakest link. Open source software packages can be found in almost all of the software that we use (Synopsis 2024), so the security of our open source projects can have wide-reaching implications for other projects, our users, and the broader ecosystem. 

Security can be an important factor in open source project selection, but the security of any software component is only as good as the security of its dependencies (Imtiaz 2022). Security is an important consideration both for selecting open source components that your project depends on as well as influencing why others might choose to use (or not use) your open source project. In this selection, it’s important to note that popular packages are no more or less likely to follow good security practices (Imtiaz 2022).

The 2024 Synopsys Open Source Security and Risk Analysis report found that 96% of the codebases they scanned contained open source software, and unfortunately, 84% of those had vulnerabilities (74% with a high severity rating). Because open source is everywhere, open source project security impacts the health and sustainability for our projects, which ripples out across the entire software ecosystem. However, keep in mind that security risk can often be thought of as a function of likelihood together with impact. Likelihood is the potential for exploitability, and impact is the damage that could be caused as a result of the exploit in the context of software deployment, so the risk is something that each adopter of open source needs to determine for their particular context, situation, and environment. 

Because security is a complex and critical topic, this guide is designed only to **get you started** on your path toward improving the security of your project. It is **not a comprehensive guide** to everything you need to know about open source project security. The goal of the Practitioner Guide Series is to get people through the overwhelming phase that many feel when faced with a lot of new metrics that help them find some ways to start understanding and improving the health of their projects. After getting started with this Practitioner Guide, you can learn more from links to the comprehensive guides in the Additional Reading section below and linked throughout this guide.

# Step 1: Identify Trends

Security is a complex topic, but you can start by looking at a few key metrics. First, the [OpenSSF Best Practices Badging](https://chaoss.community/?p=3939) criteria creates a good engineering foundation that incoporates basic security practices. Second, when you use outdated dependencies, you are four times as likely to have security issues (Cox et al. 2015), so using the [Libyears](https://chaoss.community/?p=3976) metric can help you understand if you are keeping your dependencies up to date. Third, [Release Frequency](https://chaoss.community/?p=4765) helps gauge whether your security fixes and other updates are landing in a release in a timely manner so that your users can benefit from your security updates.

## OpenSSF Best Practices

The [Open Source Security Foundation](https://openssf.org/) (OpenSSF) provides ways to assess your open source project across a number of different dimensions to get a summary of where your project’s practices can be improved. While security practices are an important component, the [OpenSSF Best Practices Badge](https://chaoss.community/?p=3939) goes beyond just security to suggest a range of best practices for your project. It’s a good way to not only assess your security practices and improve on them to meet the badge criteria, but it also signals to your users that you follow OpenSSF best practices. The criteria found in the reporting, security, and analysis sections are the ones that are most applicable to understanding and improving the security of your project.  

![Open SSF Badge example of gold badge from the curl project](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/ossf-badge-curl.png)

Image Source: [https://www.bestpractices.dev/en/projects/63](https://www.bestpractices.dev/en/projects/63) 

## Libyears

The [Libyears](https://chaoss.community/kb/metric-libyears/) metric explains the age of dependencies that you rely on, compared to the current stable releases of those dependencies. It was first proposed in “Measuring Dependency Freshness in Software Systems” (Cox et al. 2015). In general, a lower Libyear number is better because it indicates that you are keeping your dependencies up to date. 

![Libyear example of a project that is 103.78 years behind](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/libyears.png)

Image Source: [https://github.com/nasirhjafri/libyear](https://github.com/nasirhjafri/libyear)  

By comparing the current version of a dependency used in your project with the latest version available for each dependency, you can better understand where you might need to be more diligent about updating your dependencies. However, the technical lag in updating dependencies is commonly created by the tension between using the most recent version and not breaking a solution that already works well, so in some cases, developers may deliberately choose to use an older version instead of the latest version due to incompatibilities or other technical issues (Zerouali et al. 2019).

## Release Frequency

It’s critical that security updates, bug fixes, and new features are released in a timely fashion. When looking at release frequency, it’s important to include not just the big releases, but also all of the tiny point releases, since urgent security fixes are usually released outside of the major releases. 

![Release Frequency of a project with frequent releases][https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/releases.png]

Keep in mind that interpreting this metric can be challenging because different types of projects and different situations can impact whether the project needs to have a more frequent or less frequent release cadence. Having a consistent release frequency can indicate a more stable or mature project.

# Step 2: Diagnosis

A good place to start diagnosing potential issues with your project’s security practices is to begin working through the OpenSSF Project Badging Criteria. While it is in progress, it will likely look something like this example:  

![OSSF Badging list of categories for a project that is working toward a badge, but has more work to do](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/ossf-badge-categories.png)  

Image Source: [https://www.bestpractices.dev/en/projects/40](https://www.bestpractices.dev/en/projects/40) 

As mentioned earlier, this includes security best practices, but also more general software engineering best practices to improve your project in a variety of ways. Under each of these suggestions, you’ll find questions that you need to answer with the criteria required to receive the badge. 

For example, here are a few of the questions under the security section:  

![OSSF Badging criteria from the security section for MITM attacks and vulnerabilities fixed](https://github.com/chaoss/wg-data-science/blob/main/practitioner-guides/images/ossf-badge-criteria-example.png)

Whether you decide to pursue the badge or not, the [criteria](https://www.bestpractices.dev/en/criteria?details=true&rationale=true) used, especially in the security and reporting sections, are a good way to think about how you might understand and improve the security of your project. There are also other options to perform security self-assessments for your projects, including the [self-assessment that the CNCF](https://github.com/cncf/tag-security/blob/main/community/assessments/guide/self-assessment.md) uses for their projects.

The next step in diagnosis might be to look at your Libyears report with a focus on the dependencies that are most out of date. When you use outdated dependencies, you are four times as likely to have security issues (Cox et al. 2015), so keeping your dependencies up to date is an important factor in improving the security of your project. As mentioned earlier, there are sometimes good reasons for a dependency to be behind the current version: breaking changes, incompatibilities with your software / other dependencies, or other technical issues. Diagnosis in this case requires a thoughtful and thorough look at whether there is a good reason for not updating a dependency.

For diagnosing whether you are making timely releases, you should look at the security patches you’ve created over the past year. If you’ve done a release around the time that you’ve released each security patch, then you are probably in pretty good shape. If the security patches have piled up and not gone out in a release, then you should probably look at why this happened and see if you can improve your release process to make more frequent releases when you fix vulnerabilities.

# Step 3: Gather Additional Data if Needed

The examples used in Steps 1 and 2 provide a starting point that can be expanded by using additional tools and metrics. A good next step in the diagnostic process would be to also run the [OpenSSF Scorecard](https://scorecard.dev/), which goes into great detail with checks that help you find areas where your project might be vulnerable across source code, build, dependencies, testing, and project maintenance categories.

You may notice that there is no metric in this guide focused on time to resolve security vulnerabilities. It’s very important, but challenging to measure because you need to be able to separate out the security issues from bugs and other issues while also tying the initial report of the vulnerability to the change requests where the fix was made. There are many ways to do this, but how you do it depends on your tooling. While it may not be the best metric to get started, it is something you should consider measuring as one of your next steps. The additional metrics below provide a good start toward measuring this.

Additional Metrics: 

* [OpenSSF Scorecard](https://scorecard.dev/) (not a CHAOSS metric, but a tool that collects many security metrics)  
* [Change Requests](https://chaoss.community/?p=3610)  
* [Defect Resolution Duration](https://chaoss.community/?p=4727)  
* [SPDX Document](https://chaoss.community/?p=3968)  
* [Upstream Code Dependencies](https://chaoss.community/?p=3977)

# Step 4: Make Improvements

One of the best places to start when improving your security practices is by securing your code repository. This includes managing access, branch protection, managing contributions, and more. The [OpenSSF Source Code Management Platform Configuration Best Practices](https://best.openssf.org/SCM-BestPractices/) guide has a list of suggestions with links to implementing them for both GitHub and GitLab. 

Another good starting point is creating a detailed security policy document for your project. This is usually found in a [SECURITY.md](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository) file at the root of your repository. The purpose of this document is to provide instructions for reporting security vulnerabilities along with documenting how you respond to those reports, including managing [embargoes](https://aliceevebob.com/2018/01/09/meltdown-and-spectre-thinking-about-embargoes-and-disclosures/). This document will help you meet the requirements for the reporting criteria in the OpenSSF Best Practices Badge. There are many places to find detailed instructions for creating security policies, so we won’t duplicate those details here. For example, the [OpenSSF’s OSS Vulnerability Guide](https://github.com/ossf/oss-vulnerability-guide/tree/main) contains more details about what this file should include along with templates and instructions for implementing a security policy, which goes beyond just creating the document and includes details about infrastructure and other requirements for managing the security process.

As mentioned, when you use outdated dependencies, you are four times as likely to have security issues (Cox et al. 2015), so keeping your dependencies up to date is an important factor in improving the security of your project. Dependencies require a thoughtful and thorough look at whether there is a good reason for not updating a dependency along with testing of more recent versions to make sure that you aren’t breaking something else when updating a dependency. While there are good reasons to avoid updating certain dependencies, in most cases, dependencies aren’t updated because it can be difficult to keep track of when they should be updated. A tool like [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) or [Renovatebot](https://docs.renovatebot.com/) can help identify and automatically update certain dependencies.

Good documentation of security fixes can help increase awareness of available security fixes (Imtiaz et al. 2022), and it’s important to make sure that those fixes land in a release in a timely fashion. If you make security patches often but don’t get them into a release quickly, then you should probably look at why this happens and see if you can improve your release process to make more frequent releases when you fix vulnerabilities. It’s also important that your release notes or other documentation contains details about the security fixes to highlight the importance of updating for the people using your software.

As mentioned earlier, working your way through the OpenSSF Best Practices badge criteria is a good way to make security improvements. The [detailed view of the criteria page for all levels](https://www.bestpractices.dev/en/criteria?details=true&rationale=true) contains explanations and links with more details that can help you improve in each of those areas.

# Step 5: Monitor Results

Because security is such a complex topic, it can be difficult to monitor. However, there are a few things that you can monitor over time to see if the actions you’ve taken to improve your security are having an impact. Here are a few suggestions for monitoring your progress:

* [OpenSSF Scorecard](https://scorecard.dev/): Has your overall score improved? Have you improved your score on some of the individual areas that you identified for improvement?  
* Libyears: Has your libyear number improved?  
* Releases: Are you making a release every time you create a security patch?

# Cautions and Considerations

* Because security is a critical topic, this guide is designed only to **get you started** on your path toward improving the security of your project. It is **not a comprehensive guide** to everything you need to know about open source project security. You can learn more from the links in the Additional Reading section below.  
* You may notice that there is no metric in this guide focused on time to resolve security vulnerabilities. It’s very important, but challenging to measure, so we recommend including this metric as one of your first next steps. See Step 3 for more details.

# Additional Reading

* [OpenSSF’s website](https://openssf.org/) contains a wide variety of very detailed guides, training, and other resources.  
* The [CNCF Security Guidelines](https://contribute.cncf.io/maintainers/security/security-guidelines/) document is much less comprehensive than the OpenSSF guides, but it might be more helpful if you are just starting to improve your security.  
* [OpenSSF’s OSS Vulnerability Guide](https://github.com/ossf/oss-vulnerability-guide/tree/main) contains a guide along with templates and a runbook focused on developing and implementing a security policy.

# Contributors

The following people contributed to this guide:

* Dawn Foster  
* Matt Germonprez   
* Emily Fox

# References

* Cox, J., Bouwers, E., Van Eekelen, M., & Visser, J. (2015, May). [Measuring dependency freshness in software systems](https://repository.ubn.ru.nl/bitstream/handle/2066/143749/143749.pdf?sequence=1). In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering* (Vol. 2, pp. 109-118). IEEE.  
* Imtiaz, N., Khanom, A., & Williams, L. (2022). [Open or sneaky? fast or slow? light or heavy?: Investigating security releases of open source packages](https://arxiv.org/pdf/2112.06804). *IEEE Transactions on Software Engineering*, *49*(4), 1540-1560.  
* Synopsys (2024). [Open Source Security and Risk Analysis Report](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html#introMenu).  
* Zerouali, A., Mens, T., Gonzalez‐Barahona, J., Decan, A., Constantinou, E., & Robles, G. (2019). [A formal framework for measuring technical lag in component repositories—and its application to npm](https://www.academia.edu/download/101718334/jsep-2019.pdf). *Journal of Software: Evolution and Process*, *31*(8), e2157.
