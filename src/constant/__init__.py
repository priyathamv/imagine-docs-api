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
OPENAI_API_KEY = 'AZURE_OPENAI_API_KEY'
OPENAI_LOCATION = 'AZURE_OPENAI_LOCATION'
OPENAI_ENDPOINT = 'AZURE_OPENAI_ENDPOINT'
OPENAI_DEPLOYMENT_NAME = 'AZURE_OPENAI_DEPLOYMENT_NAME'
OPENAI_MODEL = 'OPENAI_MODEL'
OPENAI_API_VERSION = 'OPENAI_API_VERSION'

# Exception messages
RESOURCE_NOT_FOUND = 'Resource not found'
INVALID_REQUEST = 'Invalid request'
INTERNAL_SERVER_ERROR = 'Internal Server Error'

LINK_TO_CONTENT_DICT = {
    "https://dx.walmart.com/documents/product/DX.io/How-to-Contribute-to-DX-io-izdpqsncp9": """"
    The Global Tech Platform associates are the primary contributors for DX.io, but we welcome contributions from all Walmart organizations as well. Here are ways you can contribute to DX.io:
    1) Create new blogs in DX.io
    Blogs are a great way to share technological insights, case studies, updates about products, or provide general announcements. DX.io provides a simple blog text editor to create new blogs and have them published in
    [DX.io Blogs.](https://dx.walmart.com/blogs)
    Get started and
    [create a new blog](https://dx.walmart.com/blogs/blogpost) now.
    2) Add Documentation in DX.io
    Documentation in DX.io is created using our internal Content Management Solution,
    [HelpDocs](https://etools.helpdocs.io/app/content). The articles must be created in the “DX” folder in their respective sections (e.g. Products, Guides, Services, etc.).
    Get Started with this guide:
    [Add Documentation in DX.io using HelpDocs](/documents/article/1dn24txszm)
    3) Add New Products in the DX.io Catalog
    Products shown in our
    [DX.io Product Catalog](https://dx.walmart.com/products) are created and managed centrally through a UI-based form.
    If you'd like to add a new product, or modify an existing product, please request access by following the
    [Request Access to Add Product to DX.io Catalog](/documents/article/xoebs1sz0v) guide.
    4) Integrate Product into DX Console
    If you have an existing tool or looking to build a new one, you can easily integrate using our DX Console SDK. The DX Console SDK offers UI Templates, API toolkits, and everything you need to bootstrap and launch.
    Learn more about our
    [Product Development Process](/documents/article/nezmomilov) to get started.
    5) Add a Starter Kit
    A starter kit is a compiled set of code that help teams get started with a project and deploy code faster. If you've build an application and would like to share a template for others in Walmart to use,
    [Starter Kit Contributor](https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/overview) gives you the ability to easily create and publish one into Starter Kit Explorer. View our [Quick Start Guide](https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/857385746) to get started.
    Comments(0)
    - VSType your comment here0/0
    """,
    "https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/overview": """
    Starter Kit Contributor Overview
    Was this helpful?
    Helpful
    Not Helpful
    The Starter Kit Contributor product supports creation and administration of templates and blueprints used to bootstrap developers. Contributors can push updates to their starter kit and view adoption analytics so they can work with their users and continue to enhance their starter kit. If you would like to see the starter kits that are available for use, please use the following link: https://dx.walmart.com/documents/confluenceArticle/925748668
    Was this helpful?
    Helpful
    Not Helpful
    Comments(0)
    - VSType your comment here0/0
    """,
    "https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/overview": """
    Comments(21)
    - VSType your comment here0/0
    - KDKapil DevOctober 28th 2022, 1:46 AM
    We made some changes yesterday in Prod CCM for some CRQ. We tried to add the flags on the base config file but, had errors while saving on root config. So, we added the new flag to prod config and also on WALMART-US-B2C config files. When the migration happens, will it override the values from base to these prod and WALMART-US-B2C config files ? please let us knowCommentLikeShare
    - WJWilliam JuroffOctober 3rd 2022, 9:12 PM
    Baskar Vangili - link is point to #wcnp_slack not #wcnpCommentLikeShare
    - WJWilliam JuroffSeptember 30th 2022, 11:11 PMCommentLikeShare
    - RBRaja BanerjeeAugust 10th 2022, 9:19 PM
    Hello all - please use the support links (slack, JIRA ticket, stack overflow) to ask questions. Thank you. Ticket:
    [https://jira.walmart.com/servicedesk/customer/portal/162/group/7720](https://jira.walmart.com/servicedesk/customer/portal/162/group/7720); Slack: [https://walmart.slack.com/app_redirect?channel=wcnp](https://walmart.slack.com/app_redirect?channel=wcnp); Stack Overflow: [https://stackoverflow.dx.walmart.com/](https://stackoverflow.dx.walmart.com/)CommentLikeShare
    - SSSeyoung SongAugust 8th 2022, 3:55 AM
    Please add source code link in the main body.Comment1Share
    - BTBhupendrasinh ThakreJuly 26th 2022, 9:28 PM
    The training link for US associate is giving error.
    This course is currently unavailable to studentsComment4Share
    - SISuresh IthaJuly 20th 2022, 12:57 AM
    The Training link above one is does not redirecting me to the install kubectl.html page and same as for install Sledge for training. Pls help to download this softwares to proceed further.Comment1Share
    - NANicholas AntzoulisJuly 12th 2022, 8:13 PM
    The Training link above does not navigate to training. It takes you to a "WCNP Overview" page with a single link back to this page.Comment3Share
    - RBRaja BanerjeeJuly 11th 2022, 9:14 PM
    Hello all - please use the support links (slack, JIRA ticket, stack overflow) to ask questions. Thank you. Ticket:
    [https://jira.walmart.com/servicedesk/customer/portal/162/group/7720](https://jira.walmart.com/servicedesk/customer/portal/162/group/7720); Slack: [https://walmart.slack.com/app_redirect?channel=wcnp](https://walmart.slack.com/app_redirect?channel=wcnp); Stack Overflow: [https://stackoverflow.dx.walmart.com/](https://stackoverflow.dx.walmart.com/)CommentLikeShare
    - MGMichael GaryJuly 8th 2022, 12:18 AM
    Hey, I was trying to access the intro to wcnp training video and it doesn't look like it exists anymore. Is that already inactive or is there a new link? It says it was posted late 2021CommentLikeShare
    - FVFelipe Villalobos (Chile) VendorJuly 6th 2022, 6:01 PM
    Hi, how can i find get access for splunk, where must to go?CommentLikeShare
    - NYNikhil YathindraJuly 1st 2022, 12:50 AM
    Is there a link on how to install kubectl?CommentLikeShare
    - RJRicardo JimenezJune 10th 2022, 10:25 AM(edited)
    Where is the documentation for fields in kitt file? example: refs, refEventFilters. etc.Comment1Share
    - NCNavya ChettireddyJune 9th 2022, 10:52 PM(edited)
    How can we create/request for windows servers in WCNP for our new project ? (its a pre-requisite). Could someone please help with the correct team who can help on this?CommentLikeShare
    - MBManali BordiaJune 8th 2022, 4:02 PMOlder links to a page lands us to this main page now and then we have to check in the complete document. Can't search also.CommentLikeShare
    - RJRicardo JimenezJune 2nd 2022, 9:31 AMIt is hard to find the full kitt structure documentationComment12Share
    - BSBert SandersMay 31st 2022, 7:46 PMWhy can't I search the docs like I could the old ones? That makes this very hard to use.Comment15Share
    - KDKrushna Chandra DashMay 26th 2022, 4:54 PM"All WCNP HIPAA clusters are configured to forward platform audit and application logs to the HIPAA-compliant Splunk cluster."However can you please confirm whether the audit log further gets forwarded to Google Chronicle as per HIPAA requirements? This confirmation is necessary to get our SSP approved by the SOC team Also, can you please confirm whether the WCNP platform is HIPAA compliant or not? If it is can you please provide the evidence that the platform audit log is sent to Google Chronicle thanksCommentLikeShare
    - PGPriyanka Gangula - VendorMay 26th 2022, 9:15 AMWhere can I find link to get access for splunk?CommentLikeShare
    - AVAdrian ValenciaMay 14th 2022, 12:33 AMwhere can i find how to install sledge? thanksComment4Share
    - ASAjitsen SurendranMay 6th 2022, 2:35 PMWhere can I get the kitt.yml documentation ?Comment6Share
    """,
    "https://dx.walmart.com/documents/product/DX.io/overview": """
    DX.io Overview
    Was this helpful?
    Helpful
    Not Helpful
    DX.io is a one stop-shop for all the developers, with a mission to connect the developers to the tools and resources needed to accelerate, optimize, and ship quality code. Discover and learn about the different products, best practices, and code templates to build and deploy code faster.
    Was this helpful?
    Helpful
    Not Helpful
    Comments(0)
    - VSType your comment here0/0
    """,
    "https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/857385746": """
    New starter kit development
    For an in depth walkthrough please refer to
    [https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/857394906](https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/857394906).
    Step One
    Go to
    [https://console.dx.walmart.com/code/starterkits](https://console.dx.walmart.com/code/starterkits)
    Click create starter kit
    Fill in required fields
    Use tags to improve searchability
    Select all features that will be present in the starter kit
    Using this will spin up template git repo that contains the required fields (mentioned below).
    Step Two
    Read the readme file, download Docker containers to develop and test locally.
    Step Three
    Add new code to template with cookiecutter tokens/etc.
    Cookiecutter transforms the template blueprint into an actual software/component that can be built further. Modify the variables defined in the cookiecutter.json file in the repo that was created from step one.
    To get more information regarding cookiecutter, please reference their documentation. A few articles that should get you started can be found in the links below.
    Additional resources
    [https://cookiecutter.readthedocs.io/en/1.7.2/](https://cookiecutter.readthedocs.io/en/1.7.2/) [https://cookiecutter.readthedocs.io/en/1.7.2/usage.html](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)
    Step Four
    Create the landing page for your users learn more about your starter kit.
    Before deploying to production, you will need to create an informational page that will be your users' first impression of your starter kit. You should fill out the needed content in each section. An example can be found in the link below.
    Step Five
    When you are ready to deploy your template and / or test your starter kit you will need to commit updates to your main branch. This will pull all the enhancements you have made into the version available on DX.
    Step Six
    Enable your starter kit and select the version you want to make available to your users.
    Comments(0)
    - VSType your comment here0/0
    """
}
