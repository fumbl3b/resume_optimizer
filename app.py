import os
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key="KEY GOES HERE")
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_relevant_keywords(job_description, model="gpt-4o"):
    """
    Extracts relevant keywords, skills, and qualifications from the job description.
    """
    prompt = (
        "You are a professional career advisor. Extract the most important keywords, technical skills, "
        "and qualifications from the following job description. "
        "Return the results as a comma-separated list.\n\n"
        f"Job Description:\n{job_description}\n\n"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def suggest_resume_improvements(resume_text, job_description, model="gpt-4o"):
    """
    Suggest improvements to the resume based on the job description.
    """
    prompt = (
        "You are a professional resume writer. You have been given a resume (in LaTeX) and a job description. "
        "Analyze the resume and identify how it can be improved and tailored to better match the job description. "
        "Do not rewrite the entire resume here, just list suggestions. "
        "Focus on skills, keywords, relevant experience, and how to emphasize the candidate's fit.\n\n"
        f"Job Description:\n{job_description}\n\n"
        f"Resume:\n{resume_text}\n\n"
        "List out suggestions in bullet points."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def generate_optimized_resume(resume_text, suggestions, model="gpt-4o"):
    """
    Take the original resume (LaTeX formatted) and the suggestions, and create a revised version
    that incorporates the suggested improvements.
    """
    prompt = (
        "You are a professional resume writer skilled in LaTeX formatting. "
        "You have a LaTeX-formatted resume and a set of improvement suggestions. "
        "Incorporate these suggestions into the resume while maintaining the LaTeX formatting and structure. "
        "Do not remove the original formatting commands, only update text where it makes sense. "
        "Make sure to incorporate relevant keywords, highlight experiences and skills that match the job description.\n\n"
        f"Suggestions:\n{suggestions}\n\n"
        f"Original Resume:\n{resume_text}\n\n"
        "Return the full updated resume in LaTeX."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    # Example usage:
    resume_text = r"""\documentclass[letterpaper,11pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[pdftex]{hyperref}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.375in}
\addtolength{\evensidemargin}{-0.375in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Custom commands
\newcommand{\resumeItem}[2]{
  \item\small{
    \textbf{#1}{: #2 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-1pt}\item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-5pt}
}

\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}

\renewcommand{\labelitemii}{$\circ$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%%%%%%  CV STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

%----------HEADING-----------------
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
  % \textbf{\href{http://www.linkedin.com/in/harry-winkler}{\Large Harry Winkler}} & Email : \href{mailto:harry@fumblebee.site}{harry@fumblebee.site}\\
  % \href{http://www.linkedin.com/in/harry-winkler}{linkedin.com/in/harry-winkler} & Mobile : +1-484-620-6919 \\
  \textbf{{\Large Harry Winkler}} & Email : {harry@fumblebee.site}\\
  {linkedin.com/in/harry-winkler} & Mobile : +1-484-620-6919 \\
\end{tabular*}

\section{Summary}
    {Proficient Software Engineer versed in designing, developing, and maintaining both mobile and web applications. Extensive experience deploying and maintaining cloud services. Skilled in Java, Kotlin, Javascript ES6, Typescript and Python. Experience with Test-Driven-Development, ADA Accessible UI implementation, continuous integration tools, and agile software development methodologies.  Excels in collaborative environments and has a strong understanding of the software development lifecycle and modern architecture patterns.}

\section{Skills}
    \resumeItemListStart
        \resumeItem{Programming Languages}{Kotlin, Java, XML, Javascript (ES6), TypeScript, Python, HTML5, CSS, Bash, C\#, Swift}
        \resumeItem{Frameworks}{Android SDK, .NET Core, React, Angular, Node, Vue.js, jQuery, Next, Tailwind, Express, Django}
        \resumeItem{Database/Cloud}{Oracle, PostgreSQL, SQLite, MongoDB, GraphQL, Redis, AWS, Kubernetes, Heroku, Vercel, Docker}
        \resumeItem{APIs and Libraries}{RESTful APIs, Picasso, Glide, Dagger2, Hilt, RxJava, Lodash, Kafka, Hibernate}
        \resumeItem{Project Tools}{Git, Github, Teams, Bitbucket, SonarQube, Crashlytics, JIRA, Trello, Slack, Confluence, InVision, Figma, Jenkins, Postman}
        \resumeItem{IDE}{Android Studio, Intellij IDEA, Eclipse, VS Code, vim}
    \resumeItemListEnd

%-----------EXPERIENCE-----------------
\section{Experience}
  \resumeSubHeadingListStart
  % add a SOAP API and Kafka section
    \resumeSubheading
      {JP Morgan Chase \& Co}{Wilmington, DE}
      {Software Engineer II Reference Data}{Aug 2023 - June 2024}
      \resumeItemListStart
        \item{Worked closely with a small team maintaining 20 internal services for managing easy-to-define, instantiate, and consume group data structures used downstream for processing purposes.}
        \item{Maintained and enhanced existing legacy Java applications ensuring robust performance, load balancing, and testing against security and vulnerability}
        \item{Developed and implemented new features in Spring Boot and React, adding new functionality and a complete user experience overhaul.}
        \item{Conducted comprehensive unit and integration testing, both automated and manual to ensure software reliability.}
        \item{Actively participated in Scrum ceremonies, contributing to sprint planning, retrospectives, and daily stand-ups, enhancing team agility and project transparency.}
        \item{Collaborated closely with business stakeholders across all 3 LOBs to align application development with requirements and timelines.}
        \item{Optimized product quality through comprehensive code reviews, pair programming, and refactoring resulting in increased efficiency and optimized compute costs.}
        \item{Managed CI pipelines, ensuring remote testing, code quality, manual testing documentation, and coverage rules enforced before deployment}
      \resumeItemListEnd

    \resumeSubheading
      {Wells Fargo}{San Francisco, CA / Remote}
      {Android Developer}{Dec 2021 - Jul 2023}
      \resumeItemListStart
        \item{Contributed to the full redevelopment of the Android application, adapting all features from Java/WebView to full native Kotlin functionality.}
        \item{Monitored performance and crash information for a live application with 10M+ downloads.}
        \item{Interfaced with device contacts and Zelle API to populate users with 'ready to transfer' feature.}
        \item{Used deep linking to implement the Guided Account Set-Up feature, navigating users directly to the many portions of the application.}
        \item{Collaborated closely with design and business to launch the new LifeSync financial planning tool, providing users with a dashboard and live investment data.}
      \resumeItemListEnd

    \resumeSubheading
        {Rave Business Systems} {Philadelphia, PA}
        {Android Developer} {Aug 2021 - Dec 2021}
        \resumeItemListStart
            \item{Developed Android Applications using Kotlin, Java and React Native}
            \item{Implemented Jetpack architecture components including Compose, ViewModel, LiveData, DataStore, RoomDB, Navigation Component, and others.}
        \resumeItemListEnd

    \resumeSubheading
        {Pathrise} {New York, NY / Remote}
        {Software Engineer} {May 2021 - Aug 2021}
        \resumeItemListStart
            \item{Engineered and deployed scalable full-stack web applications using React, Node.js, and MongoDB, focusing on optimizing user interfaces and backend services for performance and efficiency.}
            \item{Collaborated with cross-functional teams to define project scopes and requirements, translating business and user needs into technical specifications and user stories.}
            \item{Performed debugging and maintenance for existing applications, implementing fixes and enhancements to improve overall system reliability and user satisfaction.}
            \item{Contributed to the development and documentation for RESTful API services, enhancing communication between frontend and backend components.}
        \resumeItemListEnd

    \resumeSubheading
    {La Colombe Coffee Roasters}{Philadelphia, PA/Chicago, IL}
    {Data Developer, Quality Assurance, Production}{2014 - 2019}
    \resumeItemListStart
        \item{Designed and implemented a comprehensive data management system to enhance coffee quality control across 30+ locations, integrating data from various sources to monitor quality metrics effectively.}
        \item{Developed and managed automated data pipelines that streamlined the collection, storage, and processing of large datasets related to coffee quality and sales, significantly reducing manual data handling and potential for errors.}
        \item{Created dynamic, user-friendly dashboards that provided real-time insights into coffee quality and sales trends, enabling data-driven decision-making and improved operational efficiency across the company.}
        \item{Led cross-functional teams to ensure the seamless integration of the data management system with existing IT infrastructure, facilitating smooth workflow and data accessibility for all stakeholders.}
        \item{Conducted rigorous testing and validation of the data systems and dashboards to ensure high reliability, accuracy, and user satisfaction.}
        \item{Designed and produced training materials and conducted workshops to empower staff at all levels with the tools and knowledge to leverage data insights effectively in their roles.}
        \item{Managed the satellite Chicago Roasting operation, overseeing weekly production and distribution processes to maintain consistent coffee quality and supply chain efficiency.}
        \item{Coordinated closely with the director of coffee to ensure alignment on roasting profiles and quality standards, optimizing production strategies to meet market demands.}
        \item{Evaluated and recommended new equipment acquisitions, working with the cafe operations team to integrate technology solutions that enhanced product quality and operational effectiveness.}
    \resumeItemListEnd
\resumeSubHeadingListEnd

%-----------EDUCATION-----------------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubItem{Temple University}
      {Computer Science} {Present}
    \resumeSubItem{Thinkful}
        {Full Stack Software Engineering Certificate} {Sept 2020 - Jan 2021}
    \resumeSubItem{Washington University in St. Louis}
      {Art History} {2009 - 2010}
    \resumeSubItem {Lower Merion High School}
        {2009}
  \resumeSubHeadingListEnd
  
%-------------------------------------------
\end{document}"""

    job_description = """
   LinkedIn is the worlds largest professional network, built to create economic opportunity for every member of the global workforce. Our products help people make powerful connections, discover exciting opportunities, build necessary skills, and gain valuable insights every day. We're also committed to providing transformational opportunities for our own employees by investing in their growth. We aspire to create a culture that's built on trust, care, inclusion, and fun – where everyone can succeed.

Join us to transform the way the world works.

At LinkedIn, we trust each other to do our best work where it works best for us and our teams. This role offers a hybrid work option, meaning you can both work from home and commute to a LinkedIn office, depending on what's best for you and when it is important for your team to be together.

Responsibilities:
· You will design and execute user-facing features for the native LinkedIn app on Android devices by leveraging mobile operating system frameworks for multi-threading, persisting data, and managing user experience and graphics across multiple screen sizes.
· You will use the latest cutting edge technologies and libraries suggested by Google for building responsive native apps for Android.
· You will build scalable native mobile apps using LinkedIns internal libraries.
· You will make architectural trade-offs applying synchronous and asynchronous design patterns, write code, and deliver with speediness and quality.
· You will produce high-quality software that is unit tested, code reviewed and checked in regularly for continuous integration.
· You will provide technical leadership, driving and performing best engineering practices to initiate, plan, and execute large-scale, cross-functional, and company-wise critical programs.
· You will identify, leverage, and successfully evangelize opportunities to improve engineering productivity.

Basic Qualifications:
• BA/BS in Computer Science or related technical field or equivalent practical experience.
• 1+ years of industry experience
• Programming experience in languages such as Java, C/C++, Python, JavaScript, Kotlin, etc.

Preferred Qualifications:
• 2+ years of relevant work experience.
• MS or PhD in Computer Science or related technical discipline.
· Foundation in computer science with a strong understanding of data structures, object-oriented programming, and algorithms.
· Knowledge of common mobile application design patterns (MVC, MVVM, MVP, etc.)
· Familiarity with API design and client/server communication principles.
· Understanding of best practices for multithreading and performance optimizations.
· Knowledge of Android debugging tools including profiling app performance.
· Experience writing automated tests for Android apps.
· Programming experience in Kotlin.

Suggested Skills:
· Java
· Kotlin 
· Mobile Development 

You will Benefit from our Culture:
We strongly believe in the well-being of our employees and their families. That is why we offer generous health and wellness programs and time away for employees of all levels.

LinkedIn is committed to fair and equitable compensation practices. The pay range for this role is $99,000 - $163,000. Actual compensation packages are based on a wide array of factors unique to each candidate, including but not limited to skill set, years & depth of experience, certifications and specific office location. This may differ in other locations due to cost of labor considerations.

The total compensation package for this position may also include annual performance bonus, stock, benefits and/or other applicable incentive compensation plans. For additional information, visit: https://careers.linkedin.com/benefits.
    """

    # Extract keywords
    keywords = extract_relevant_keywords(job_description)
    print("Keywords & Skills Extracted:")
    print(keywords)

    # Get suggestions for improvements
    suggestions = suggest_resume_improvements(resume_text, job_description)
    print("\nSuggestions for Improvement:")
    print(suggestions)

    # Generate optimized resume
    optimized_resume = generate_optimized_resume(resume_text, suggestions)
    print("\nOptimized Resume:")
    print(optimized_resume)