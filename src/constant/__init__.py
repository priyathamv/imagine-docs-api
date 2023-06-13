NETWORK_IDLE = 'networkidle'
BODY = 'body'
RESOURCE_EXCLUSIONS = ['image']
# RESOURCE_EXCLUSIONS = ['image', 'stylesheet', 'media', 'font', 'script', 'other']

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']

# Supabase
SUPABASE_URL = 'SUPABASE_URL'
SUPABASE_KEY = 'SUPABASE_KEY'

# Azure OpenAI
OPENAI_API_TYPE = 'OPENAI_API_TYPE'
OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_LOCATION = 'OPENAI_LOCATION'
OPENAI_ENDPOINT = 'OPENAI_ENDPOINT'
OPENAI_EMBEDDING_ENGINE = 'OPENAI_EMBEDDING_ENGINE'
OPENAI_EMBEDDING_MODEL = 'OPENAI_EMBEDDING_MODEL'
OPENAI_API_VERSION = 'OPENAI_API_VERSION'
OPENAI_COMPLETION_MODEL = 'OPENAI_COMPLETION_MODEL'
OPENAI_COMPLETION_ENGINE = 'OPENAI_COMPLETION_ENGINE'

# Exception messages
RESOURCE_NOT_FOUND = 'Resource not found'
INVALID_REQUEST = 'Invalid request'
INTERNAL_SERVER_ERROR = 'Internal Server Error'

TEMP_FOLDER = '/tmp/'

MAX_WORKERS = 4

LINK_TO_PAGE_CONTENT_DICT = {
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/337e1ac15eba1bd8583d816dfe0628fd9c46f0cc8d3116c882753125284c3de6": """"
    Walmart Cloud Native Platform (WCNP)

    Everything you need to know about the largest and fastest growing Walmart-specific Cloud Platform is here.
    Begin your journey with Getting Started, which takes you from zero to hero.
    
    Whether you have used or have never heard of it, we will help you to navigate building and deploying your app with KITT.
    
    Meanwhile, make sure you are familiar with the WCNP Capabilities to dive further.
    
    After the latest news and updates? Visit What's New.
    
    Still stumped? You may also find it helpful to become acquainted with a few Common Terms. We are here to answer your questions!
    
    So, grab your team and let us go on a quick tour of WCNP.
    
    Overview
    The Walmart Cloud Native Platform (WCNP) is a Kubernetes based platform that securely and efficiently runs Walmart's cloud native, containerized workloads across the edge (Stores, Distribution Centers), private data centers, and public cloud (Azure, Google) deployments.
    
    At the heart of WCNP is Kubernetes (K8s), an open-source platform for managing containerized workloads. However, the WCNP encompasses a much broader set of ecosystem technologies necessary for being successful with K8s. This includes tools for build/deploy, observability, service mesh, and transparent integration with existing Walmart services such as Torbit GSLB.
    
    WCNP lays the foundation for many long-term benefits including:
    
    Improved developer and operations productivity
    Reduced infrastructure costs
    Improved systems reliability
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/50e5604aca0442e005e691dd5c7fb013fdbeb52223583f61207f75a6db58de11": """
    When to Use WCNP
    Today, there are more ways than ever to run your service or application.
    In the following sections we seek to illustrate the differences the value proposition WCNP brings and compare it to some of the common runtime orchestration platforms available from commercial vendors and other projects.
    
    If you are interested in learning about KITT and how it compares to alternatives, please see the KITT comparison page.
    
    Azure Kubernetes Services (AKS) Google Kubernetes Engine (GKE)
    WCNP is not a competitor to AKS, GKE or other managed Kubernetes offerings. While AKS and GKE have networking and security limitations preventing it's usage today, the WCNP is intended to be layered on top of these services once they are available. Usage of a single offering directly results in vendor lock-in and hence uncontrollable costs. WCNP usage avoids this and adds additional value.
    
    WCNP Offerings
    Multi-tenant
    Single-tenant
    Multi-tenant
    WCNP's multi-tenant offeirng provides users options to place their workloads on following cloud provider
    
    Public Cloud - Azure and GCP(GKE): If your application's scale fluctuates throughout the day based on various metrics like incoming requests, traffic patterns, and others, then choose Azure or GCP (or both) to host your application.
    Private Cloud (Data centers): When workloads are static (scale does not vary drastically based on traffic or incoming request patterns), choose to use private cloud to host your workloads.
    Users have the opportunity to either make use of any or all three of the above options.
    
    Single-tenant
    WCNP's single tenant offering provides an entire AKS or GKE cluster to customers offering greater control over workloads and VM types. The single tenant offering is only available on an exceptional basis and customers are required to have developer level expertise with Kubernetes.
    
    Integration w/ Walmart's Ecosystem of Tools**
    WCNP provides built-in integration with many Walmart systems to improve security, connectivity, and telemetry. This is particularly helpful when migrating existing VM-based or other legacy workloads. It allows teams to leverage the same great tools during the transition phase and hence avoids rework and existing skills and configurations can continue to be valuable.
    
    InfoSec Integrations
    
    Akeyless (Secrets) - Easily inject secrets into your pods via integration with the InfoSec approved Akeyless solution
    Certificate Management - Full integration with InfoSec's CWS service for automatically requesting ingress certificates
    Routing and Connectivity Integrations
    
    Torbit - Auto provision Torbit GSLBs and Vanity URLs and easily split traffic across WCNP and non-WCNP deployments
    Service Registry / Service Mesh - Automated registration and access to Walmart's service mesh
    Telemetry Integration
    
    Splunk, automatic integration with Managed Log Service for Splunk log aggregation
    Dynatrace, automatic Dynatrace instrumentation for all deployed workloads
    Prometheus / Centralized TSDB, automatic Prometheus instrumentation for container and ingress metrics
    Performance and Usage
    
    Pod Profiler - Custom tooling to profile your workload in Kubernetes and right size resource requests
    
    Cost Management - Automatic instrumentation for cost charge-backs and reporting, coming soon
    
    Compliance
    
    ServiceNow - Integrates with Walmart's Service Now environment to automatically create comprehensive change records for production deployments.
    WARN - Integration with Walmart's WARN tool to block deployments during site outages.
    Kubernetes In The Trenches (KITT)
    Kubernetes In The Trenches (KITT) is a GitOps build and deployment tool for Kubernetes workloads. It is built on top of Looper and Concord, which natively integrates with Walmart's Github. It provides the following value over comparable commercial and open-source systems:
    
    Natively integrated with Walmart Github for accelerated on-boarding
    Strati-maintained base docker images and helm chart blueprints for accelerated on-boarding
    GitOps flow encourages CI/CD best practices and improves developer productivity
    Visibility into deployments defined as immutable, declarative configuration
    Reduced Security and Compliance Burden
    Managed Kubernetes offerings only solve a small part of the overall security and compliance requirements. GKE and AKS both offer direct SSH access to the worker VMs which means that the surface area is similar to that of IaaS VMs in the a public cloud. WCNP layers on the following:
    
    Cluster authentication, integration with Walmart AD for authentication
    Cluster access control, integration with Walmart AD groups for role-based access control
    Locked down VM access, limited, or blocked, SSH access to underlying worker VMs
    Secure cluster configuration - Pod Security Policies that prevent running containers in privileged modes
    Ensuring secure multi-tenancy by deployment time policies - Cluster Policies
    Secrets - Integration with Walmart's Akeyless Vault Platform
    Certificate automation, integration w/ Walmart's CWS service for secure cert requests and renewals
    Because WCNP layers on these critical controls, it greatly reduces the security and compliance burden as teams can leverage:
    
    WCNP Framework SRCR - 37899779
    WCNP SOX Audit - Coming soon
    Security Responsibilities Comparison between WCNP and Vanilla AKS & GKE:
    Improved Cloud & Edge Portability
    By maintaining consistent Kubernetes configurations and integrations across all of our public cloud and edge environments, WCNP further improves portability for customers' workloads. Specifically, it enables increased portability:
    
    between public cloud providers, for example from Microsoft Azure to Google GCP
    between public cloud and edge deployments
    across multiple edge hardware and virtualization technologies
    Higher Resource Utilization via Multi-Tenancy
    WCNP layers on critical policies and controls that allow multiple tenants to use the same Kubernetes cluster safely. These controls include namespaces, cluster policies and AD-driven RBAC controls. By safely allowing multi-tenancy, teams can share the burden of common infrastructure costs like control plane nodes, and common operational costs such as cluster administration.
    
    OneOps or VM-Based Scheduling Solutions
    Kubernetes is an open-source scheduling platform for containerized workloads. It offers many advantages compared to a VM-based scheduling system such as OneOps on top of OpenStack or commercial cloud provider IaaS or PaaS systems:
    
    Scalability
    
    Kubernetes offers both cluster and pod auto-scaling capabilities
    Containerized workloads deploy faster and are more reliable to replicate compared to virtual machines
    Reliability
    
    Kubernetes declarative infrastructure allows for self-healing systems if pods or VMs enter a failed state
    Kubernetes is a mature, battle-tested orchestration platform
    Flexibility
    
    Kubernetes supports usage of side cars which enable specialized deployments beyond what would be possible with single containers. Kubernetes has a large ecosystem of plug-ins allowing many workloads types including Functions, GPUs, and others, not all of which are available through WCNP yet.
    
    Portability
    
    Containers offer portability across various infrastructure and virtual machine configurations, including for local development
    Kubernetes offers portability of scheduling configuration across different infrastructure and cloud providers
    These features and system principles ultimately lead to a number of significant benefits:
    
    Improved developer and operations productivity
    Reduced infrastructure costs
    Improved systems reliability
    It's important to note that Kubernetes is built to run cloud native containerized workloads. There are certain workloads that might be a better fit for a VM-based scheduling system:
    
    Non-containerized workloads
    Legacy workloads that require a local GUI
    Stateful workloads
    Apps that can't follow a GitOps model for build/deploy/ops
    Check out our WCNP Checklist and our KITT prerequisites for more details.
    
    Managed Servlet
    Managed Servlet (MS) provides Java Servlet-based applications an abstraction over the infrastructure lifecycle management of OneOps. This allows application teams the ability to focus more on the application lifecycle, without having to manage the integration and support of platform services such as logging and alerting. However, the limitations of OneOps are transferred to MS, including VM build and startup time and limited dynamic scaling.
    
    Managed Servlet, while catering to a large number of our developers in Walmart, is still limited to stateless Java workloads that run with the Servlet Specification in mind. This limits the ability of MS to provide additional environments to teams needing different technology to realize solutions for our Company. Managed Servlet is also very opinionated about how workloads are deployed: this reduces the operational TCO but can lead to solutions who haven't thought about 12factor and Cloud Native (CN) having a hard time adhering to the platform offering.
    
    Azure App Services / App Service Environment
    Managed ASE Azure App Services allow you to run a variety of workloads (both containerized and non-containerized) within Azure. GTP's current guidance is to use this for non-containerized, non-JAVA workloads.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/3afa501ffc5c90875e29677c6e22d6a2f916da305e493d07033e57bb0ad5bb1f": """
    The WCNP documentation covers a variety of topics and has information for users with different roles and responsibilities within Walmart.

    Regardless if your role is listed below, leverage the search functionality within the WCNP documentation to find what you're looking for.
    
    This guide is intended for the following audience:
    
    Application Developers - Developers deploying stateless containerized applications.
    Application Architects - Architects looking for additional information on how WCNP operates and the funtionality it provides.
    DevOps / SRE's - Engineers supporting the deployed application.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/4f3c2ebf1d04d2aea0ad88bc496d1230b1f8491d57034abc702a923e01ac74a9": """
    KITT Introduction
    KITT is the only approved deployment tool for deploying to cloud, multi-tenant WCNP clusters.
    
    KITT is the codename for our most developer friendly way of getting your application into a production-ready cloud environment, part of the WCNP ecosystem.
    
    KITT could stand for Kubernetes In The Trenches, since it is built upon real Kubernetes learnings and experience. But you could also consider it a hint to a really cool car that assists in getting your application into the cloud. Or it maybe it is just a cool name - KITT.
    
    KITT provides a Walmart-specific implementation of a GitOps process combined with ChatOps notifications and interactions. It starts with simple, automated onboarding and is capable of getting your application all the way to a production deployment.
    
    KITT is powered by the tools created, supported and operated by Strati.
    
    Concord
    Looper
    Artifactory
    It also integrates with, and relies on other enterprise tools.
    
    GitHub
    Slack
    Microsoft Teams
    ServiceNow
    Features of the KITT application build and deployment flow include:
    
    git-based auto-releases for every main commit
    builds temporary deployments for every branch commit
    a concord-yml-less approach (a shared concord project handles the pipeline heavy lifting)
    integrated Helm-based k8s deployments and app configurations
    messaging-app-based pipeline communications
    built-in review and audit trail using standard pull-requests with required approvals
    support for test container builds and in-pipeline test execution
    By providing a very small bit of initial configuration, KITT enables a PR-friendly workflow, automatically deploying and testing your application with every commit:
    While we very much believe in Kubernetes, Helm, Concord, and Looper as technologies, KITT endeavors to minimally expose these technologies in the KITT model and flows.

    Give KITT a spin and let us know what you think!
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/4116b6f4e62fae890f34c7702500bf3ae209d462c565cea686b50b0fe342e828": """
    Prerequisites
    Before jumping in, we recommend first checking off a few boxes which will help to make your KITT experience a better one.

    AD security group
    ServiceNow group
    Messaging channel
    Git repository
    For more advanced KITT use cases, there may be additional considerations, such as:
    
    Operating system
    Application Stack
    Software architecture
    DevOps readiness and processes
    If in doubt on any of these, reach out to us on Slack! Once you feel you're ready, you can jump straight in with the quick start guide, or feel free to learn more about the first steps of KITT pipelines with our CI Guide.
    
    
    AD Security Group
    KITT uses Active Directory security groups to determine ownership of the created k8s namespaces. You therefore need to have such a security group with the relevant people from your application team in it available. Distribution lists are not suitable. You can use the Azure Active Directory tool to discover the AD groups you are in, but be warned that only security groups may be used to establish ownership of a namespace. A list of AD groups is also available with sledge. Currently, all members of the group have to be in the homeoffice domain or part of one of the following domains:
    
    These are the domains that are configured to support:
    
    ar.wal-mart.com
    br.wal-mart.com
    ca.wal-mart.com
    cam.wal-mart.com
    cl.wal-mart.com
    cloud.wal-mart.com
    cn.wal-mart.com
    emea.wal-mart.com
    in.wal-mart.com
    jp.wal-mart.com
    mx.wal-mart.com
    pr.wal-mart.com
    uk.wal-mart.com
    us.wal-mart.com
    wmct.wal-mart.com
    wmsc.wal-mart.com
    People who are not in homeoffice need to use userid@<domain>.wal-mart.com as the user name. If you are not already a part of an Active Directory group that represents your development team, you have to submit a request for the creation and addition.
    
    Ensure that all required users are added to the new group. This should also include the requester/owner of the group, as well all committers to the code base in GitHub. By default, the requester/owner is not automatically added to the new group.
    
    If you would like to expedite this request, ensure your manager is available to approve it. Once you have the group determined, you simply configure it as owner in your kitt.yml file.
    
    
    ServiceNow Group
    Info Sec team will use ServiceNow Assignment Group (ITIL) to track vulnerability remediation ownership by namespace. You can use ServiceNow Groups FAQ and click on this link to review this ServiceNow Knowledge Article and read through the available notifications options (For example, e-mail notification, slack integration, and others.) You can also view the details of a ServiceNow group including the ownership of the group, the configuration of the group, and the members of the group you are part of.
    Messaging Channel
    KITT requires either a Slack or MSTeams channel for pipeline event notifications. The channel has to be public. All users have access to create channels. Private channel usage is not supported. Typical names use a team or application name and append -alerts or -ops or similar terms.
    
       In it's current iteration, when making use of an MSTeams channel for pipeline event notifications, a Slack channel also needs to be provided in the notify section of the KITT file. Please refer to the documentation for more information.
    
    
    Git Repository
    KITT requires your code to be managed in a git repository on git.walmart.com.
    
    Find out more git and GitHub from our documentation and training.
    
    The repository has to be located within a GitHub organization. Personal repositories are not supported. Repositories may be either public or private within the GitHub organization. The organization name as well as the repository name are used by KITT, so we recommend usage of simple, short names. Any GitHub committer on an application's repository must also be in the AD security group.
    
    
    Operating System
    WCNP runs Kubernetes/Docker on top of Linux hosts. Therefore your application needs to be able to run on a Linux kernel based operating system. Since KITT provides Dockerfiles to create your container, by default it makes the operating system choice for you due to your profile selection. Preferred Linux distributions are first Alpine as a dedicated small distro, and then Ubuntu. Both are supported with backing repositories on ARK.
    
    Alpine / APK
    
    Ubuntu / APT
    
    ARK Overview
    
    
    Application Stack
    KITT includes a number of Dockerfiles that support different build systems and application stacks. For example, a Java-based application built with Apache Maven running as a standalone JAR or on Apache Tomcat is supported. The list of available options is expanding. Find out more by looking into KITT profiles. As an alternative you can create your own Dockerfile and take ownership of the Looper build so that your own Docker container is used as an advanced user.
    
    
    Software Architecture
    WCNP provides a Cloud Native runtime environment for Docker containers on Kubernetes. This implies that you are using a microservices architecture. At a minimum your application needs to be able to run in a Docker container within the available size limits. More information is available from a number of sources:
    
    WCNP checklist
    Cloud Computing and Cloud Native Fundamentals training
    12 factor app
    Micro services
    
    DevOps Readiness and Processes
    KITT is an opinionated system that implements DevOps best practices such as usage of trunk-based development, continuous integration and continuous deployment. Your team culture, communication and composition as well as your project management practices need to be able to adapt to the relevant patterns. Reach out to our DevOps Dojo for more help.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/30a7eca2bed3ef33cc009b020168bcb0dd4ec3191d6704c334faf3b5942f694e": """
    KITT Quick Start
    Last updated 15/04/2023
     Before mashing that turbo button, be sure to check out KITT prerequisites.
    
    Do you have an existing repo, and want to get your first deployment up and going ASAP?
    Follow these steps:
    
    Pick from one of the below platforms that best match your kind of repository
    Copy the sample yaml into a file named kitt.yml at the root of your repository
    Substitute a couple important user-specific values (commented with <-- your ...)
    Commit, and wait for messaging notifications to start rolling in. KITT will take it from there!
    No repo to start with? No problem! Getting started is even easier. Just clone one of our example repos and give KITT a spin.
    
    Platforms
    Java
    Tomcat
    Spring Boot
    Generic Jar File
    Golang
    Nodejs
    Nodejs + Nginx
    dotnet
    aspnetcore
    Python
    Other
    Java
    Tomcat
    Performs a Maven build and deploys a single war file hosted on tomcat9 / jre8.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - tomcat9-jre8-centos
      - default-lab  #deploys to our default lab cluster
    build:
      buildType: maven
    deploy:
      releaseType:
        deployTimeout: 360  #app should deploy & boot up within 6 mins
      helm:
        values:
          livenessProbe:
            wait: 360
          readinessProbe:
            path: "/"  #your app should return a '200/OK' at the root.. else change this to something valid!!
            wait: 360
    Spring Boot
    Performs a maven build and deploys a single jar file hosted on java 8 using configs common to springboot web apps.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - springboot-web
      - default-lab  #deploys to our default lab cluster
    deploy:
      releaseType:
        deployTimeout: 300  #app should deploy & boot up within 5 mins. increase as needed.
      helm:
        values:
            #values for min/max be adjusted as needed
            min:  
              cpu: 100m     
              memory: 256Mi
            max:
              cpu: 400m
              memory: 1024Mi  
            livenessProbe:
              wait: 120   #your app should be booted & ready within 2 mins
            readinessProbe:
              wait: 120
    SpringBoot JDK8
    Builds a standard java8 jar via maven, and includes runtime configurations common with springboot apps, such as probe configurations pointed to actuator endpoints. Includes the JDK for troubleshooting purposes, but increases size of image.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - springboot-jdk8-web
      - default-lab  #deploys to our default lab cluster
    deploy:
      releaseType:
        deployTimeout: 300  #app should deploy & boot up within 5 mins. increase as needed.
      helm:
        values:
            #values for min/max be adjusted as needed
            min:  
              cpu: 100m     
              memory: 256Mi
            max:
              cpu: 400m
              memory: 1024Mi  
            livenessProbe:
              wait: 120   #your app should be booted & ready within 2 mins
            readinessProbe:
              wait: 120
    Generic Jar File
    Builds and deploys a single jar file running on java 8.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - springboot-web
      - default-lab  #deploys to our default lab cluster
    ### Remaining sample TBD ###
    Golang
    Generates a fully executable binary utilizing multi-stage builds. Runtime target will default to a recent golang version, but ultimately it can be overridden with buildArg goVersion for any specific version requirements.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - golang
    ### Remaining sample TBD ###
    NodeJs
    Generates a fully executable binary utilizing multi-stage builds. Runtime target defaults to version 8.15.0 but can be overridden with buildArg nodeVersion.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - node
      - default-lab  #deploys to our default lab cluster
    ### Remaining sample TBD ###
    nodejs-nginx
    Utilizes nginx as a reverse proxy server to the backing NodeJs application. Runtime targets NodeJs 8.15.0 and Nginx 1.15 by default, but overridden with buildArgs nodeVersion and nginxVersion.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - node-nginx
      - default-lab  #deploys to our default lab cluster
    ### Remaining sample TBD ###
    DotNet
    aspnetcore
    Generates a fully executable .dll utilizing multi-stage builds. Runtime targets version 2.0 of ASP .Net Core.
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - aspnetcore
      - default-lab  #deploys to our default lab cluster
    ### Remaining sample TBD ###
    python
    Builds a docker image with your python code, all python libraries required to run the application. Runtime targets version 3.10 by default, but overridden with buildArg pythonVersion. Module to start the application can be defined using buildArg startupModuleName
    
    owner:
      group:    # <-- your AD Group here
    notify:
      slack:
        channelName:    # <-- your team slack channel here
    profiles:
      - python-web
      - default-lab  #deploys to our default lab cluster
    
    build:
      docker:
        app:
          buildArgs:
            skipCodeCoverage: true
            sonarOpts: "-Dsonar.projectVersion=&#123;&#123; $.kitt.build.version &#125;&#125;
                      -Dsonar.projectKey=python-app-demo"
            
    deploy:
      releaseType:
        deployTimeout: 300  #app should deploy & boot up within 5 mins. increase as needed.
      helm:
        values:
          #values for min/max be adjusted as needed
          min:
            cpu: 100m
            memory: 256Mi
          max:
            cpu: 400m
            memory: 1024Mi
          livenessProbe:
            wait: 120   #your app should be booted & ready within 2 mins
          readinessProbe:
            wait: 120
    Other
    Don't see your desired platform? Contact us and let us know!
    
    All of the above platforms are WCNP managed, and utilize a CI approach we call kitt-native. This is not however intended to meet all platform needs for the enterprise.
    
    Alternatively, you can also provide your own custom dockerfile and let KITT build your image for you. While this means more up-front work by your team to develop and test the Dockerfile, it is recommended for purpose-built, highly-customized images. For more information on differing CI approaches, check out our CI Guide.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/5a71c3661e89ee54f8cabcd50faa5937c8b33f8175872ecce7acc51894cc3009": """
    KITT Native CI
    KITT-Native is our recommended CI approach for WCNP. Please check out the CI Guide to understand how this CI approach fits in context with other KITT-provided CI approaches.
    
    Overview
    Reasons to use this approach
    Drawbacks
    How-To
    KITT Pipeline
    Examples
    Looper Considerations
    Overview
    KITT Native CI offers the most built-in benefits within the KITT ecosystem. Native integration with Looper and Concord means users do not have to manage additional metadata or perform extra set up beyond the general KITT prerequisites, and the added kitt.yml file to the repo. KITT Native offers features including:
    
    Seamless git event integration means every commit to your repo automatically initiates a new build.
    Optional branch builds and deploys to temporary namespaces.
    Platform-appropriate, scalable Looper projects created and managaged automatically on strati-owned CI servers.
    An auto-incrementing release semver and tag created for any main and/or "release" branch.
    Use of strati-managed KITT profiles means a platform-appropriate container is built with no Dockerfile and minimal additional set up.
    Automatic image tagging and upload to Artifactory with successful builds.
    Future updates to the OS or container runtime dependencies are automatically sourced with each new build.
    Seamless integration with your KITT-enabled deployment pipeline.
    Reasons to use this approach
    You prefer to not deal directly with docker container builds.
    Your team may not have the bandwidth or skill set to stay on top of ongoing OS- or container-layer patches and updates.
    You are able to leverage common or open-source containers.
    Your team does not require a highly customized CI process.
    You have a greenfield application that can be designed as cloud- and container-native from the start.
    Potential Drawbacks
    If you have an existing, highly customized CI flow, you may find replacing it with KITT-Native difficult.
    How-To
    Determine the appropriate WCNP-supported profile that meets your platform needs.
    Add kitt.yml to your repo including a reference to the above profile.
    Wait for KITT to build and deploy your app. Correct any errors as notified in slack.
    For a detailed walkthrough of all changes you can make, check out the KITT Native runbook.
    
    KITT Pipeline
    The below diagram illustrates the end to end KITT Native pipeline.
    
    
    Examples
    We maintain and test KITT Native example repos for many major platforms.
    
    Java with Springboot
    Java with Tomcat
    Golang
    NodeJs
    Ruby + Nginx
    ASP.net core
    Python
    Looper Considerations
    With this approach, KITT automatically creates and configures a Looper job specific to your type of application.
    
    The job will be created in a folder with a name matching your GitHub organization, and a job name matching your repository name. Git commits on your repo are then fired to Concord, in turn triggering the appropriate Looper job.
    
    The folder created in Looper for your org is restricted and should only be used by KITT. Any job that is added to the org folder in Looper may be deleted at any time without warning by a KITT process. It is highly encouraged that teams create a separate folder for jobs unrelated to KITT.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/a1f076b19969a6615feb379153f78a979f7b380144a5699973efb3770cb8fbba": """
    KITT Continuous Integration Guide
     Are you ready to get started building and deploying your app with KITT?
    Make sure you are familiar with the prerequisites for your app before diving in further.
    
    Overview of CI Approaches
    Branching Practices
    KITT GitHub Badges
    Next Steps
    
    Overview of CI Approaches
    Enabling frictionless CICD with KITT is our mission. At the same time, we acknowledge there isn't always a "one-size-fits-all" process. Hence, we offer some distinct approaches that enable teams at various points in their CICD journey to get going more easily with KITT. The folowing table offers a feature comparison of each of these approaches.
    
    Approach	Faster onboarding	CI-best-practices built-in	automated releases, versioning	managed looper build	managed OS, app layers	custom image builds	custom CI
    KITT Native							
    KITT + Custom Dockerfile							
    BYOC	?	?	?				
     Our recommendation: start with KITT-Native if possible, and introduce the complexity of other approaches only as necessary.
    
    Be sure to follow the links above for the approach name for guidance and usage information on each.
    
    
    Branching Practices
    If you are opting to use BYOC, then these branching features will not apply.
    
    Any non-BYOC CI approach with KITT enables many helpful features to assist your team in making the development process as efficient as possible, including:
    
    Trunk-based development support
    Automated test container builds and execution
    Automated feature branch delpoyments
    For more information, Check out our detailed branching practices guide!
    
    
    KITT Github Badges
    KITT offers a GitHub badge service, based on shields.io content, which is similar to the Looper Build Status Badge. Combining a badge with the pipeline concord link offers your contributors a quick glance at pipeline health, and a straightforward means to navigate to the repo's KITT pipeline to see more details.
    
    To add a KITT badge to your repo, add the following snippet to your repo's root README.md file, ensuring that you replace the MYORG and MYREPO placeholders with your relevant git repo coordinates:
    
    [![KITT badge](https://kitt-badges.k8s.walmart.com/kittbadge?org=MYORG&repo=MYREPO)](https://concord.prod.walmart.com/#/org/strati/project/pipeline/process?meta.repoMetadata=MYORG%2FMYREPO&limit=50)
    or
    
    <a alt="KITT pipeline status" href="https://concord.prod.walmart.com/#/org/strati/project/pipeline/process?meta.repoMetadata=MYORG%2FMYREPO&limit=50">![KITT badge](https://kitt-badges.k8s.walmart.com/kittbadge?org=MYORG&repo=MYREPO)</a>
    The badge will show a status of unknown until at least one execution happens.
    
    
    Thereafter, a failing badge is displayed if the ratio of failures to successes over the pipeline's recent execution history exceeds 50%.
    
    
    If the failure ratio is between 50% and 15%, an unstable badge is shown.
    
    
    A healthy badge is shown for failure rates below 15%.
    
    
    KITT reports metrics during every pipeline execution. Keep your pipeline in good health for a green badge!
    
    Using Different Badge Error Thresholds
    
    The badge service endpoint has optional query parameters to adjust the thresholds used to evaluate the badge appearance:
    
    healthyRate: percentage of failures below which the badge should show as healthy. Default is 15%.
    unstableRate: percentage of failures below which the badge should show as unstable. Default is 50%.
    For an example badge URL that adjusts the thresholds:
    
    <a alt="KITT pipeline status" href="https://concord.prod.walmart.com/#/org/strati/project/pipeline/process?meta.repoMetadata=MYORG%2FMYREPO&limit=50">![KITT badge](https://kitt-badges.k8s.walmart.com/kittbadge?org=MYORG&repo=MYREPO&healthyRate=10&unstableRate=40)</a>
    With this example, a healthy badge is shown if failure rates are below 10%. If rates are below 40%, an unstable badge is shown. Otherwise, a failing badge is displayed.
    
    Note: Any rate higher than the unstableRate is, by definition, in an error state. Defaults are used for any rates not otherwise specified. If provided rates are not valid float formats, they are silently ignored.
    
    
    Next Steps: Deployment
    Once you have KITT CI going for your application, the next step is deployment.
    
    All KITT example projects automatically include the necessary configuration for deploying to our WCNP dev environment.
    For more information, you can consult the deployment guide.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/4d7d50fd9f63316045d667a3efae171ebb87f1d849fc10d9b3671e8d42ba0416": """
     Be sure you check out the CI Guide to understand how this fits into the overall KITT CI picture.

    Overview
    Any KITT-enabled CI process, such as KITT-native or KITT-with-custom-Dockerfile offer a number of CI features that are helpful during feature development as follows:
    
    Builds triggered on every commit
    Commit-sha-based versions uploaded to artifact repository(Artifactory/Proximity)
    Branch-based temporary namespaces allocated for deployment
    Github status updates posted back to the branch / PR
    These features exist to make the cycles between commits as efficient as possible. Proper consideration for source management practices is key to this efficiency.
    
    If you opt to use BYOC for your CI flow, then these branching features will not apply.**
    
    Trunk-Based Development
    Walmart recommends, and KITT supports, a trunk-based development SCM approach.
    
    What exactly is trunk-based-development (TBD)?
    
    A source-control branching model, where developers collaborate on code in a single branch called 'trunk', resist any pressure to create other long-lived development branches by employing documented techniques. They therefore avoid merge hell, do not break the build, and live happily ever after.
    
    ~ https://trunkbaseddevelopment.com/#one-line-summary
    
    This model is supported by default with KITT, as any stage has a default flow of release. This means, any commit to a release branch triggers a new build, and it is automatically deployed to the given stage.
    
    Although release is the default flow used for a stage, for clarity the following kitt yaml snippet shows how this would look in a simple two-stage setup:
    
     stages:
      - name: dev
        target:
          cluster_id: ["scus-lab-a1"]
        flows: [release]
    
      - name: prod
        target:
          cluster_id: ["some-prod-cluster"]
        flows: [release]
    What if my team does not follow TBD practices?
    
    Teams not yet following TBD may find adjusting to it a bit difficult at first.
    While techniques, such as branch by abstraction and feature flags can help, we recommend engaging with our DevOps Dojo Team for assistance in this vitally important journey!
    
    Nonetheless, if your team adheres to specific development processes, such as extensive use of forks, you may want to explore using BYOC for those portions of your development workflow, and allow KITT to manage when changes are merged to main. This approach allows for portions of highly customized CI flows, while still utilizing KITT where the development flows are more common.
    
    
    Feature Branches
    KITT also supports short-lived branches with the generic branch name in the flows element for any stage. When using this, KITT will:
    
    Trigger your pipeline on every commit to any non-release branch.
    Create and upload a temporary, sha-based container image during the build.
    Deploy your app to a temporary namespace on every stage having a branch flow.
    Push Github status updates back to your repo / branch for major pipeline steps.
    Automatically purge the temp namespace after a fixed / unused time period.
    Given a default flow of release, the following kitt yaml snippet shows the use of a dev stage to deploy both branches, and main (or trunk). And if dev deploys are successful, deployment then occurs for main releases to the subsequent prod stage.
    
    stages:
      - name: dev
        target:
          cluster_id: ["scus-lab-a1"]
        flows: [release,branch]
      - name: prod
        target:
          cluster_id: ["some-prod-cluster"]
        flows: [release]
    Multiple development / commit cycles can be done on a given branch, and a PR created against the branch. Once ready, the PR should be merged to main, based on the git statuses KITT provides against the PR. While multiple PRs might be opened on a branch, we recommend creating new branches. This keeps the scope of PRs and their respective branches small and contained.
    
    
    Using Temporary Namespaces with Branches
    Temporary namespaces allow for automated and manual tests to occur on different branches within the same repository. When using KITT CI, any non-release-ref commit is always deployed to a temporary namespace. By default, this happens for any non-main commit, unless otherwise specified.
    
    The names allocated for temp namespaces are stable-hashed names based on the repo, branch name, and PR number. This convention avoids name collisions across different repos, branches, and even PRs on the same branch. The naming strategy also ensures that, as work is iterated upon within the same branch, every commit redeploys the application back to the same temp namespace name. Once a PR is opened on a branch, by default the temp namespace name will hash differently to prevent validated merges from colliding with any branch-only deployments.
    
    Temporary namespaces are allocated a configurable percentage of the amount cpu/memory resources that the corresponding base namespaces has allocated. For more information on this please see here.
    
    It should be noted that temp namespaces do not participate in global routing rules configurations. However, applications deployed to temp namespaces may still be accessed externally through the cluster-specific default routes for any WCNP application. These endpoints are always printed in pipeline logs after a successful deployment. An example of this route for an app foo targeting namespace bar deployed, using a branch commit to the dev cluster might look like this:
    
    http://foo.bar-n1228001008.scus-lab-a1.cluster.k8s.us.walmart.net/hello
    
    Also note that KITT skips ownership validation and allows non-owners to contribute to temp namespaces. The owner.group value in kitt.yml is required for temp namespace flows only if the corresponding base namespace does not exist.
    
    As the name implies, these namespaces are meant to live only for a very short time, measured in hours or days. Once their fixed TTLs have expired, the namespace and all contained applications are automatically purged by WCNP. Moreover, similar to other non-prod namespaces, any redeployment to the same temp namespace resets the TTL.
    
    Temporary Namespaces are not supported in PCI environments. Make sure your pci stages are configured to only do release deployments, by adjusting your setup.releaseRefs and stage.refs or stage.flows
    
    
    Working with PRs
    KITT stages may also be triggered in response to pull request opened, synchronize, and reopened events.
    This is useful in cases where you want to trigger special stage deployments for PR events.
    
    The recommended way to trigger PR events is with a stage flows element. Stages using the flow named pr will:
    
    Trigger on PR opened, synchronize, and reopened events against the configured release refs (default of main).
    Deploy to temp namespaces.
    Optionally allow for associated PRs to be auto-merged and closed using tasks.
    Following is a simple kitt.yml snippet using stage-flows, auto-merging the PR upon successful deployment:
    
    deploy:
      stages:
      - name: dev
        flows: [pr, release]
        postDeploy:
        - task:
            name: mergePr
      - name: prod
        flows: [release]
    This simple setup enables the following series of actions:
    
    Any PR opened against main executes a PR-based build, including a validated merge from the parent branch during the build.
    Successful PR builds are deployed to dev.
    Successful deploys to dev auto-merge the PR.
    The PR merge auto-triggers a new dev deployment with the new release.
    Successful dev releases from main automatically deploy to production.
    KITT PR flows target specific github PR events, namely PR opened, synchronize, and PR reopened. For KITT these are onPROpen, onPRSync, and onPRReopen events respectively. In particular, if care is not taken, the onPRSyc event can lead to seemingly "duplicate" events when used in conjunction with branch flows. More specifically, commits against the branch for which the PR is attached may potentially fire the following two events:
    
    ONE onPush event for the the branch commit
    ONE onPRSync event for the PR synchronize event on the same commit
    Special consideration should be made when you are opting for both PR flows and branch flows, as this may result in duplicate (or worse, conflicting) deployments to the same namespaces.
    
    More about stage flows, and stage refs in general, can be seen in the yaml reference.
    
    
    PR Builds
    As mentioned above, when configured with the PR flow, KITT initiates a Looper build for every major PR action:
    
    When a PR is opened or reopened
    When a commit occurs on a branch with an open PR
    Unlike branch-based builds, PR builds execute with a locally merged copy of the code from the parent branch. This default behavior ensures that PR builds and testing occurs on a copy of the code that is likely to be used once the PR is merged to the parent branch. This also means PR builds will fail if conflicts are present on the branch. If merge conflicts are reported in the PR build, they should be resolved in the branch.
    
    If this auto-merge behavior is not desired, it can be disabled with the following feature flag:
    
    setup:
      featureFlagMap:
        skipPRMergeFromParent: true
    
    PR Analysis and Decoration
    For Sonar enabled profiles, KITT natively supports PR analysis and Decoration. Kitt creates a sonar report for every PR that has been opened in the Project's Sonar Dashboard. Kitt also publishes the PR-check with Sonar static code analysis and users will have to update the repo settings in case they need to make the check mandatory. For more information, go to Insights on PR-decoration.
    
    More information on the Sonarqube integration and PR analysis and decoration, can be found here.
    
    Automated Testing
    Combining either branch or main commit triggers, alongside test containers and deploy hooks, makes for a more robust pipeline that validates all source code modifications, and lending confidence, stability, and expedience for all application releases.
    
    Building a test container
    
    A great technique for automated pipeline testing is to build a test container. Such a container is typically a collection of tools and scripts that might invoke the app's service endpoints and check responses for validity. The container itself should output logs to the console, and abort with a non-zero exit code in case of test failure.
    
    Since KITT supports building multiple containers, building a test container can easily be done by specifying the path and name of the dockerfile relative to the repo's root directory. In the following example, the test dockerfile is located in a /tests subdirectory:
    
    build:
      docker:
        tests:
          dockerFile: Dockerfile
          contextDir: ./tests/
    If the above is part of a repo named my-app, then this results in a new container being built and pushed to the artifact respository(Artifactory/Proximity) with the name my-app-tests, having a release version matching the current app release version.
    
    Once the container is built, hooks can be leveraged to execute the tests after deployment occurs, like so:
    
    deploy:
      postDeploy:
        - job:   #example in-repo-compiled, cluster-level test execution hook
            action: create
            name: "{{$.kitt.build.artifact}}-tests"
            timeoutSeconds: 120  #timeout should be ample for the test container to come up & execute
            pollPeriodSeconds: 10
            fetchJobLogsAfterPolling: true
            namespace: "{{$.kitt.deploy.namespace}}"
            namePrefix: "{{$.kitt.build.artifact}}"
            image: "{{$.kitt.build.docker.tests.image}}:{{$.kitt.build.version}}"
            env:
              # optional, but you can provide env vars here
    This results in the test container execution occurring post-deploy on every stage, with the container's logs being pulled after execution. If the test container fails, the pipeline will automatically abort.
    
    Why should I use temp namespaces / kubernetes-cluster deployments for automated testing?
    
    Sometimes teams question use of an actual kubernetes deployment for automated pipeline testing, versus some kind of embedded deployment container, or other "local" hosting option. Leveraging an actual cluster deployment for test suite execution is preferable for a few key reasons:
    
    Apps often rely on many k8s cluster components / features, such as ingress, servicemesh, and networking setup, which can be difficult to set up on unmanaged or local setups.
    Local / embedded tooling, for example, minikube, can be resource-intensive.
    Local-only setups do not ensure tests are always executed for all code changes.
    You may certainly pursue local setups as desired, keeping in mind the above inherent limitations with them. As such, local setups might be viewed rather as complementary to cluster-hosted, automated setups.
    
    Can these test containers replace my unit tests?
    
    Integration test containers ought to be viewed more as complementary to unit tests, rather than as a replacement.
    
    Unit tests are normally higher in number, such as hundreds or thousands of tests, and very fast to execute (just a few seconds) relative to integration style tests. Unit tests are also often integrated directly into most IDEs to make the feedback loops much faster and more informative.
    
    Since integration test containers run alongside the deployed application, they must be built, published, and deployed. These are steps which could take several minutes. These tests also tend to focus on different aspects of the application, such as:
    
    Did the application start up successfully?
    Is the application properly configured?
    Are key service endpoints responding with expected response codes?
    Are the external-facing routes working?
    
    Release Versioning
    KITT utilizes github releases to track and manage the release version numbers for your application. Release versions follow the semver standards for numbering.
    
    When a repo is first set up with KITT, if there is no current release with a valid semver, a new release is created with a version of 0.0.1. Afterwards, any release always auto-increments the patch number of the latest github release, creating a new latest release with this new semver.
    
    Note that KITT never increments semver numbers other than patch. It is left up to users to manage major and minor revisions. As such, if you want to start at a specific semver, or increment major or minor revisions of the current release revision, you can do this by issuing a new github release with the desired semver.
    
    In this case, use the following steps:
    
    Navigate to your github repo main page.
    Click on the 'releases' tab. Example link: https://gecgithub01.walmart.com/myorg/myrepo/releases
    Click Draft a new release button at the top-right of the page. You need proper repo permissions to perform this action.
    Set both the Tag version and the Release title to the desired semver, for example, 1.0.0. You can optionally add a release description, no special format is required for this field.
    Click the Publish Release button at the bottom. Ensure This is a pre-release remains unchecked!
    In the 'releases' tab, your new release is labeled as 'Latest release'. If you notice your new release is NOT marked as 'Latest', then it may be that some older releases are made on top of newer commits. In this case you must push a new commit on the branch you're targeting for the latest release, and then either update the release or create a new one.
    From this point forward, KITT should increment on top of this release revision.
    Please avoid creating any other CI processes that also modify github releases on a KITT-CI-enabled repo. Conflicts commonly occur with KITT when other CI processes create non-semver release numbers. These conflicts often result in aborted KITT pipelines and require manual intervention to fix the release numbering.
    
    
    Non-Release Versioning
    
    KITT will also create temporary version numbers for non-release versions. These all follow the convention 0.0.1-<commitSha><pr-suffix>, where:
    
    0.0.1 remains a fixed semver, so any uploaded images follow the semver standard.
    <commitSha> is the first 9 characters of the commit SHA of the current branch commit.
    <pr-suffix> is suffix of .<pr-number> is added when a PR build occurs.
    For example, a commit sha of 9c2c2ba536d2409f90056d146fa5455f89aba87a, and for a branch-based trigger, KITT will generate a non-release version of:
    
    0.0.1-9c2c2ba53
    Moreover, if a PR having a PR number of 234 was opened on the same commit sha of 9c2c2ba536d2409f90056d146fa5455f89aba87a, KITT would generate a non-release version of:
    
    0.0.1-9c2c2ba53.234
    With this opinionated version approach, platform-specific version schemes, such as maven snapshot releases based on pom release versions, will not be followed. While this keeps KITT relatively platform-agnostic, it also means if you have need of platform-specific release mechanisms or versioning, you may instead want to consider using a BYOC approach.
    
    
    Non-Main Releases
    We recommend using trunk-based development, issuing all releases from main. However, it is occasionally necessary to issue releases from long-lived, non-main branches. KITT supports this with some additional configuration.
    
    For example, for a repo having a long-lived branch called "blue-version", the following configuration would cut actual release numbers from both main and the 'blue-version' branch:
    
    setup:
      releaseRefs: ["blue-version","main"]
    Image Versioning
    KITT-native builds will automatically push image tags of latest as well as the current release version to the repository.
    
      Referencing latest, or other static image tags, is considered an anti-pattern, and strongly discouraged for use in production.
    
    Moreover, during deployment, the specific release tag is transformed into an image digest reference. Image digest references ensure that a stable and consistent image reference is used across all current and future running pods for a given release.
    
    For example, given an org foo, application name bar, and version 1.0.0, the following images and tags would be pushed during a build:
    
    docker.prod.walmart.com/foo/bar:latest
    docker.prod.walmart.com/foo/bar:1.0.0
    For any subsequent cluster deployments, the release tag 1.0.0 would get resolved to the corresponding image digest sha: docker.prod.walmart.com/foo/bar:1.0.0@sha256:74c5b113171ce2c142d60ee2932183fbb5c4703162ecd609a401f81df48d1a31.
    
      Automatic image digest references only apply with KITT-managed charts (webapp-basic, cronjob, etc). If you are using BYOHC and building your own chart, you would need to add appropriate logic within your chart templates to use image digest references.
    
    Suppressing Image Digests With Deployments
    While using mutable image tags is discouraged, there are some cases in non-production environments where it may be desired so as to avoid unnecessary redeployments for frequently-changing, non-critical components.
    
    You can instruct KITT to suppress image digest references on deployments by providing one or more java regular expressions in your kitt.yml as follows:
    
    build:
      attributes:
        mutableImageExprs: [".*\\:latest",".*\\:some_other_fixed_tag"]
    The above configuration ensures any image reference with latest or some_other_fixed_tag would use a non-digest-based image reference at deploy-time.
    
    Controlling CI Triggers
    KITT provides a few optons which help control default CI trigger behavior.
    
    Synchronizing Stage Branch Refs
    When a commit occurs on a repo, the default behavior of KITT is generally to execute the binary build, even if there may potentially be no matching deploy stage on which to deploy the built image. This may not always be desirable in cases where a smaller subset of branches are used to actually deploy and test, such as branches existing for a time prior to a PR being created for them.
    
    If you feel an excessive number of builds are occurring, and your deploy configuration lends itself to eliminating some of these builds, you may enable the feature flag buildWhenStageRefMatches as follows:
    
    setup:
      featureFlagMap:
        buildWhenStageRefMatches: true
    With this flag enabled, upon a commit, KITT will immediately examine the current deploy stage configuration, and if no stage would match with the triggered commit, the pipeline promptly (and silently) exits.
    
    
    Skipping CI Using Commit Comments
    You may bypass KITT pipeline triggers for any given commit or PR creation by simply adding the tag [skip-ci] or [skip ci] anywhere in the commit comments or in the PR title. KITT CI triggers will not fire for any commits or PRs with these strings. As such, you will not observe any concord process execution for these commits in your concord history. Note that, when tagging commits, only those tagged will be skipped.
    
    Some git command examples:
    
    # KITT will NOT execute CI for any of these commits
    git commit -m '[skip-ci]' && git push
    #or
    git commit -m 'I want to [skip ci]' && git push
    #or
    git commit -m '[skip-ci] for this commit' && git push
    #or, create a PR with [skip-ci] or [skip ci] in the title in a similar fashion
    This skip feature only applies when KITT pipelines are "natively" triggered from commits. It does not apply for BYOC invocations of KITT from your own looper or concord processes. Pipelines will always be fired in those cases.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/4154f67ec95b15518e5becbb349f8e32358f22224e21cf6696a2b08dd62b917a": """
    Developing with Docker
    Docker is the used container technology at Walmart. Understanding Docker is, therefore an, important aspect of application development.

    Note: You are not required to construct an application docker image from scratch if you simply need a common platform image. KITT provides many of these common images and corresponding build and runtime configurations. Consult the CI Guide for more information.
    
    Concepts
    Installation
    Registry Usage
    Container Authoring
    Best Practices
    Resources
    Concepts
    Usage of Docker requires an understanding of cloud computing concepts, characteristics, and principles, as presented in our Cloud Computing and Cloud Native Fundamentals training class.
    
    This class also provides a high-level understanding of containers. For usage of Docker in your development efforts, you need to know about aspects such as:
    
    containers
    images
    host and container separation
    volumes
    Docker file
    registries
    To learn more see available resources .
    
    Installation
    Docker installation on your workstation or a virtual machine requires administrator/root-level access. Ensure you have this appropriate access and then install Docker.
    
    Installation using Docker Desktop (aka Docker for Mac or Docker for Windows) is preferred since it also includes Kubernetes-related tools you may find useful for local development. Generally, any Docker Community Edition/Docker CE is sufficient.
    
    We recommend usage of the latest stable version Docker CE or, at a minimum, version 17.03.
    
    Confirm your version with:
    
    $ docker --version
    Docker version 17.12.1-ce, build 7390fc6
    or docker version for more details.
    
    Registry Usage
    Docker containers are distributed as binary images by the use of Docker registries. At Walmart, we run our own Docker registries for internal images and provide access to external registries with our repository manager Artifactory.
    
    For more details, go to our specific Docker registry documentation.
    
    Container Authoring
    To create a Docker container that contains an application and configuration for your development efforts, you need to define the configuration with a Dockerfile. Then publish the binaries to the registry on Artifactory with a Looper job.
    
    A file named Dockerfile is required and contains all details.
    
    First, you must define the parent container you are building on top of with the FROM statement. This can be simply an operating system, or a much more complex container.
    
    FROM <registry>/<org-name>/<img-name>:<tag-name>
    The registry needs to be internally available. For example, to use openjdk:8-jre-alpine in your container, add the following to your Dockerfile:
    
    FROM hub.docker.prod.walmart.com/library/openjdk:8-jre-alpine
    This is enough information to build a container, though there is much more that you can add to your Dockerfile to further customize the container:
    
    docker build -t hello-container .
    Following is a more complete, yet simple example:
    
    FROM hub.docker.prod.walmart.com/library/openjdk:8-jre-alpine
    LABEL maintainer=“Test.User@walmartlabs.com”
    CMD mkdir -p /opt/app
    COPY target/*.war /opt/app/example.war
    EXPOSE 8080
    ENTRYPOINT ["java" , "-jar", "/opt/app/example.war"] 
    The above example creates a container with an executable Java web archive application, which is started automatically and exposed on port 8080.
    
    The container can be started with:
    
    docker run -p 127.0.0.1:8080:8080 hello-container
    An important best practice is to add a .dockerignore file to control what files are used in the container build context.
    
    Ideally, you ignore all files and only explicitly add exceptions for files that are actually needed:
    
    **
    !Dockerfile
    !/target/*.war
    Numerous example projects are available, the following are used in the WCNP training classes:
    
    hello-container
    hello-container-alpine
    hello-container-centos
    hello-container-ubuntu
    Best Practices
    This section is relevant to you if you bring your own chart and need to ensure that your container is following security best practices, as implemented with Pod Security Policies.
    
    Linux Distribution
    We recommend that you use a new or latest stable version of your desired Linux distribution, including any available security updates to packages applied.
    
    In addition, a smaller footprint from using a minimal OS distribution, such as Alpine is preferred. If possible, you can even opt to use no distribution in the container, relying solely on the host kernel, by using FROM scratch.
    
    Usage of larger distributions such as Ubuntu or CentOS is discouraged. When necessary, use smaller versions where available and ensure you optimize the installed packages.
    
    Installed Packages
    To avoid unnecessary security issues, it is recommended to install the minimum required packages and applications to run your application.
    
    For example, do not have curl, wget or many other applications installed on your container, if they are not needed by your application at runtime.
    
    User Account
    The trusted system administration best practice to never run your service/daemon using the root account applies to containers as well.
    
    Beyond the container itself, by default, the root user in a container is the same root (uid 0) as on the host machine. If an exploit manages to break out of an application running as root in a container, it may be able to gain access to the host with the same root user.
    
    To use a different user to run your application, first create that user according to the Linux distribution used in your container. After the creation, you can use the USER command to switch to the new user. Any command after the switch runs with the new user.
    
    The following examples all create a user and group with the name app and the ID 10000. They also set an invalid login shell and specify the home directory of the user.
    
    Create the user and group with a higher ID on Alpine:
    
    RUN addgroup -S -g 10000 app \
        && adduser -S -D -u 10000 -s /sbin/nologin -h /opt/app/ -G app app
    Create the user and group with a higher ID on Ubuntu:
    
    RUN adduser --system --uid 10000 --group --shell /sbin/nologin --home /opt/app/ app
    Create the user and group with a higher ID on CentOS:
    
    RUN groupadd -r app -g 10000 \
      && useradd -u 10000 -r -g app -m -d /opt/app -s /sbin/nologin app
    Once the user is created, you have to ensure you switch to using it before starting your application with, for example, ENTRYPOINT. It is required to use the UID and not the username for PSP to pick up the used UID correctly:
    
    USER 10000
    It is recommended to use a user ID and a group ID greater than 1000 as any values less than that are reserved for system utilities and daemons depending on the OS distribution.
    
    The other option is to use a securityContext stanza in the containers section of the pod and/or deployment. The securityContext in the Docker file has precedence over the values defined in the Docker image.
    
    You can validate if your container runs with the root ID or not with the id.
    
    Locally you can do this with docker run:
    
    $ docker run ubuntu id
    uid=10000(app) gid=10000(app) groups=10000(app)
    Or if the container is already running locally with docker exec:
    
    $ docker exec 66c61d8253cb id
    uid=10000(app) gid=10000(app) groups=10000(app)
    Similar exec command execution is possible with kubectl. If the pod is in a crash loop, you can see why it failed by running the following command:
    
    kubectl describe <your-pod> -n <your-namespace>
    Check the KITT/webapp-basic chart deployment file as an example to make your own chart PSP friendly.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/03c054ac6c5c6953f42c12c3e1de249fc999c63e8aa40f4cbcd94b75812b0f2b": """
    Artifactory Integration

    Artifactory Overview
    Artifactory is a third-party repository manager solution from Jfrog, Inc. Some of the benefits migrating to Artifactory include comprehensive Scalability, optimized Multi-region and Multi-cloud capabilities, unlimited storage growth, full polyglot support and resilient disaster recovery features. Phase I rollout would include support for Docker and Maven available to all teams within Global Tech Platform(GTP) organization. More information on the Artifactory can found on the product page.
    
    Architecture
    Artifactory Architecture
    
    Within each Azure development region, Artifactory repositories are federated within CI and CD clusters, providing a full active/active deployment. On the WCNP, two types of pipelines are supported.
    
    KITT Native
    Kitt Native + Custom Build Dockerfile
    Docker Artifacts
    Kitt supports publishing Docker artifacts to Artifactory for further usage. Kitt supports both Kitt Native and Bring Your Container flows.
    
    Kitt Native Flows
    Using Artifactory with KITT Native flow is simple and involves adding a feature flag useArtifactory in the Kitt.yml
    
    setup:
      featureFlagMap:
        useArtifactory: true
    Once a new deployment is triggered, Kitt internally sets the right image registry url in the Kitt model and Looper credentials based on the useArtifactory value. This ensures that proper repository urls are generated and on a successful build, pushes all built docker images to the Artifactory. Kitt also ensures during deployment, right urls are referenced in k8s manifests based on the flag. The image repository used in the build can be verified in the DockerImageStep of Looper logs as shown below.
    
    Artifactory logs
    
    KITT also supports Artifactory integration with OnlyDeploy flows and Kitt base profiles can be used to change the value of the flag if required.
    
    
    {
      "arguments": {
        "onlyDeployOrg": "strati",
        "onlyDeployRepo": "wcnp-example-simple-byoc",
        "onlyDeploySHA": "6c02ccc68025c2aee6f930e722573912bb6a487f",
        "onlyDeployBranch": "master",
        "onlyDeployVersion": "1.0.0-SNAPSHOT",
        "stageRefs": ["dev"],
        "baseProfile": {
          "setup": {
            "featureFlagMap": {
              "useArtifactory": true
            }
          }
        }
      }
    }
    Kitt Native + Custom Dockerfile
    Incase of custom Dockerfiles, useArtifactory flag can be added to Kitt.yml and update any explicit Docker registry references in the file. More details regarding this can be found in the Artifactory Docker blog here.
    
    Kitt dynamically determines the artifact repository url based on the above flag and sets the right repository url and credentials required by the Looper job to publish the image. A dedicated folder needs to be created in the Artifactory for each Git org and a suffix(-docker) is added to the folder name. Kitt uses Artifactory's CI url for publishing the images which are then automatically federated to CD instances as of Phase I. Reposolns team is working on a user enabled promotion process for future releases. In case of deployment flow, Kitt uses CI clusters for non release flows and CD cluster for release flows.
    
    Git org level migration
    The above examples describe self onboarding process to Artifactory on individual repos. KITT also supports automated onboarding of entire Git orgs to Artifactory once approved by the RepoSolns team. As of phase I, we are restricting this feature only to Kitt-Native flows in any given Git orgs approved by Reposolns team.
    
    To enable this feature, Kitt uses custom profiles to internally update the useArtifactory flag if the deployment request is from the approved list of Git orgs to set the right artifact repository url for the flow. Any particular repo can always override the value of the flag by updating it in the Kitt.yml files. To enable this feature on a Git org, please contact Reposolns team
    
    Image validation
    Kitt does image validation for every deployment unless disabled to make sure the image exists in either Proximity or Artifactory based on the same feature flag before proceeding with deployment. Kitt retries for three times before failing the pipeline if the image is not found in the repository. A sample error message to Slack when image cannot be found will be:
    
    Specified docker image docker.ci.artifacts.prod.walmart.com/artifactory/samplegitorg-docker/sampleapp:0.0.552 not found.
    
    More information on onboarding to Artifactory can be found here
    
    #help_artifactory Slack channel has been created to help with self onboarding process.
    
    Helm Artifacts
    Kitt also supports publishing Helm charts to Artifactory under the folder <org>-helm.
    
    Kitt native flows
    There will be no changes required from user point of view. As kitt-native profiles use webapp-basic helm chart internally, we have already migrated webapp-basic chart to artifactory and all the applications are currently using artifactory to retrieve their helm chart.
    
    Bring your own custom helm charts(BYOHC)
    To use artifactory for your helm charts, you will have to add an additional feature flag useArtifactoryForHelm in the Kitt.yml
    
    setup:
      featureFlagMap:
        useArtifactoryForHelm: true
    Please note that your folder structure or chart name will remain same as before. Once a new deployment is started, the charts are published to Artifactory. It can be confirmed by checking looper logs for Publish step as shown below
    
    BYOHC Artifactory logs
    
    You can verify while deploying the application to make sure helm repo add step would use artifactory url.
    
    BYOHC Concord Artifactory logs
    
    More information on WCNP's BYOHC can be found here.
    
    BYOHC + Custom Looper file
    To use artifactory for your helm charts, you will have to add an additional feature flag useArtifactoryForHelm in the Kitt.yml
    
    setup:
      featureFlagMap:
        useArtifactoryForHelm: true
    Update your global environment updates to .looper.yml as shown below
    
    envs:
      global:
        variables:
          ALLOW_ARTIFACTORY: true
    When trying to push to artifactory, use the below curl instead of that of proximity, curl --verbose --fail -H "Authorization:Bearer ${reposolnsPassword}" -T ./${CHART_NAME}-${VERSION}.tgz ${CHART_REGISTRY}/${CHART_NAME}/${VERSION}/${CHART_NAME}-${VERSION}.tgz CHART_REGISTRY will now point to pipelineCfg.build.helm.chart.helmRegistry
    
    Please refer to Looper Artifactory documentation for more information.
    
    Helm-build-only
    For the applications where separate repos are used to publish and consume the custom Helm charts, correct HelmRegistry path should be added in the kitt.yml of the client repo to be able to access the helm chart.
    
    Sample profile in the publishing repo
    
    profiles:
      - helm-build-only
    Sample helm registry in the client repo's kitt.yml
    
    deploy:
       helm:
          helmRegistry: https://helm.ci.artifacts.prod.walmart.com/artifactory/<publishing-org>-helm
          chartUrl: wmt/<chart-name>
          chartVersion: 0.0.XX
    MultiApp build and deploy
    MultiApp repos usually require image folder path hardcoded in their kitt.yml to publish and retrieve the right image for their individual apps. With the move to Artifactory, the git org part of the folder path in the image field needs to be updated with -docker suffix to point to the right folder under Artifactory.
    
    helm:
     values:
       container:
         image: devtools-docker/wcnp-example-java/automaton-k8s-flow-extractor     
         repository: docker.artifacts.walmart.com
    This is true in case of all hardcoded image paths in the kitt.yml. More information can be found in the blog published here.
    
    Foundational Artifacts
    A foundational artifact is the one which is developed at Walmart and used by other Walmart applications or services. This could be a reusable Java library, Docker image layer, npm package, etc. To help the teams that maintain and version these foundational artifacts for their users, WCNP allows a backup image to be published to Proximity along with Artifactory. Featureflag proximityBackupEnabled can be used in conjunction with useArtifactory flag to push the foundational artifacts to both Artifactory and Proximity at the same time. This feature will be available until the Proximity continues to be supported at Walmart GT. This flag can be used as follows
    
    setup:
      featureFlagMap:
        useArtifactory: true
        proximityBackupEnabled: true
    Please note that the flag proximityBackupEnabled would only work in conjunction with useArtifactory. To achieve this task, WCNP would add additional tags in the Docker push step to publish the images to both Proximity and Artifactory
    
    Artifactory Proximity Backup
    
    Future updates
    Some future plans and updates on the WCNP Artifactory integration include
    
    As of June 2022, we are automatically federating the artifacts from CI to CD clusters and in future would be using Promotion process to federate the artifacts to CI.
    We are working on a new feature flag to allow foundational artifacts to be published to both Proximity and Artifactory for the time being to maintain same versions across the repositories.
    We are also exploring a new gating mechanism to enforce Artifactory usage on all the repos.
    Artifactory project outside the context of WCNP supports manual onboarding to the repository and more information can be found on the Artifactory documentation.
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/4eeab80c1c58bc2e0db2f886eab0fb8e5ea5244280cdc669600087a160622f69": """
    Multi Module Microservices With KITT
    This page defines the approach to use KITT with two different styles of maven microservice repos. The page focuses on the steps needed to use maven to build individual modules or microservices in the repo. For a more general overview, go to microservices with kitt:

    Repo with multiple independent microservices
    Multi Module Reactor Build microservices
    Repo with multiple independent microservices
    In this repository structure, you have multiple microservices in a single repo. Each microservice has its own pom file and builds and deploys independently. This is the repo we use as a proof of concept. It has two services service1 and service2. Both service1 and service2 have their own pom file, but there is no pom file in the root of the repo.
    
    Onboarding steps
    The guide uses our sample repo as a proof of concept multi-module microservices repo.
    
    Specify the path to individual microservice kitt files in the services section.
    
     services:
       - path: service1/kitt.yml
       - path: service2/kitt.yml
    In the child kitt for each service, set build.buildType to maven-multimodule.
    
     build:
       buildType: maven-multimodule
    Add the modulePath docker build argument modulePath which points to the directory where the pom file for the service is located.
    
    build:
     buildType: maven-multimodule
     docker:
       app:
         buildArgs:
           modulePath: service1
    Add the mvnGoals build attribute. This contains the mvn goal you want to run. For services, teams generally set this to clean install and for libraries clean deploy.
    
    build:
      attributes:
        mvnGoals: clean install
      buildType: maven-multimodule
      docker:
        app:
          buildArgs:
            modulePath: service1
    This is an optional step if you're publishing a library and not a microservice. To just publish a library to Artifactory, skip the docker build for your library. The skipDocker build attribute allows you to skip the docker image step in looper.
    
    build:   
      buildType: maven-multimodule
      attributes:
        mvnGoals: clean install
        skipDocker: true
      docker:
        app:
          buildArgs:
            modulePath: service1
    Multi-module reactor build microservices
    In this repository structure, each microservice is a submodule that depends on other modules in the repo, and it is built using reactor. This is the repo we will use as a proof of concept. It specifies two modules in the root pom file, api and web. The web module depends on api.
    
    Onboarding steps
    Specify the path to individual microservice KITT files in the services section.
    
    services:
      - path: api/kitt.yml
      - path: web/kitt.yml
    In the child kitt for each service, set build.buildType to maven-multimodule.
    
     build:
       buildType: maven-multimodule
    Add the modulePath docker build argument modulePath that points to the directory where the pom file for the service is located.
    
    build:
     buildType: maven-multimodule
     docker:
       app:
         buildArgs:
           modulePath: web
    Add the mvnGoals build attribute that contains the MVN goal that you want to run. For services, teams generally set this to clean install and for libraries clean deploy.
    
    build:
      attributes:
        mvnGoals: clean install
      buildType: maven-multimodule
      docker:
        app:
          buildArgs:
            modulePath: web
    Since the web module depends on the api module, specify the reactor to auto make dependent modules. You can pass any extra flags that reactor needs in the build attribute moduleCommand
    
    build:
      attributes:
        moduleCommand: "-pl {{ $.kitt.build.docker.app.buildArgs.modulePath }} -am"
        mvnGoals: clean install
      buildType: maven-multimodule
      docker:
        app:
          buildArgs:
            modulePath: web
    KITT runs mvn versions:set before it runs the maven goals to set the right version for the build. You may have a requirement to run this command on the pom file in the repo root to reflect the correct version in all modules. To do this, you can use a build attribute moduleVersionCommand
    
    build:
      attributes:
        moduleCommand: "-pl {{ $.kitt.build.docker.app.buildArgs.modulePath }} -am"
        mvnGoals: clean install
        moduleVersionCommand: "-f ."
      artifact: web
      buildType: maven-multimodule
      docker:
        app:
          buildArgs:
            modulePath: web
    """
}
