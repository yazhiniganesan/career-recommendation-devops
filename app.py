import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret")

# ===================== Auth (hard-coded) =====================
def check_user(username, password):
    VALID_USERS = {
        "admin": "admin123",
        "user": "user123"
    }
    return VALID_USERS.get(username) == password

# ===================== Helper functions =====================
def roadmap_for_role(role):
    roadmaps = {
        "Software Engineer": """
        <div style="font-size: 1.1rem; line-height: 1.8;">
            <h3 style="color: #667eea; margin: 24px 0 16px 0;">📍 Phase 1: Fundamentals (2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Programming:</strong> Python/JavaScript basics, variables, loops, functions</li>
                <li><strong>CS Fundamentals:</strong> OOP, Data Structures (arrays, linked lists), Algorithms</li>
                <li><strong>Databases:</strong> SQL basics (SELECT, INSERT, JOIN)</li>
                <li><strong>Tools:</strong> Git, VS Code, terminal commands</li>
            </ul>
            
            <h3 style="color: #667eea; margin: 24px 0 16px 0;">📍 Phase 2: Core Development (3 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Frontend:</strong> HTML/CSS, JavaScript ES6, React/Vue basics</li>
                <li><strong>Backend:</strong> Node.js/Express or Python/Flask, REST APIs</li>
                <li><strong>Database:</strong> MongoDB/PostgreSQL basics</li>
                <li><strong>Projects:</strong> Todo app, Blog API, E-commerce frontend</li>
            </ul>
            
            <h3 style="color: #667eea; margin: 24px 0 16px 0;">📍 Phase 3: Advanced (2-3 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>System Design:</strong> Scalability, caching, load balancing</li>
                <li><strong>DevOps:</strong> Docker, CI/CD, AWS basics</li>
                <li><strong>Advanced:</strong> Microservices, GraphQL, Testing</li>
                <li><strong>Portfolio:</strong> 3-5 full-stack projects</li>
            </ul>
            
            <h3 style="color: #10b981; margin: 32px 0 16px 0;">🎯 Interview Prep</h3>
            <ul>
                <li>LeetCode 200+ problems (Easy/Medium)</li>
                <li>System design interviews</li>
                <li>Mock technical interviews</li>
            </ul>
        </div>
        """,
        "UI/UX Designer": """
        <div style="font-size: 1.1rem; line-height: 1.8;">
            <h3 style="color: #f59e0b; margin: 24px 0 16px 0;">🎨 Phase 1: Design Foundations (1-2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Principles:</strong> Color theory, typography, layout, hierarchy</li>
                <li><strong>User Research:</strong> Personas, user journeys, interviews</li>
                <li><strong>Wireframing:</strong> Low-fidelity sketches, information architecture</li>
            </ul>
            
            <h3 style="color: #f59e0b; margin: 24px 0 16px 0;">🎨 Phase 2: Tools & Prototyping (2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Figma:</strong> Interface design, components, variants</li>
                <li><strong>Prototyping:</strong> Click-through prototypes, micro-interactions</li>
                <li><strong>Responsive:</strong> Mobile-first design, breakpoints</li>
            </ul>
            
            <h3 style="color: #f59e0b; margin: 24px 0 16px 0;">🎨 Phase 3: Advanced Skills (2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Design Systems:</strong> Tokens, components, documentation</li>
                <li><strong>Accessibility:</strong> WCAG guidelines, screen readers</li>
                <li><strong>Motion:</strong> Animation principles, After Effects basics</li>
            </ul>
            
            <h3 style="color: #10b981; margin: 32px 0 16px 0;">🎯 Portfolio</h3>
            <ul>
                <li>3 case studies (problem → research → design → results)</li>
                <li>Figma community profile</li>
                <li>Dribbble/Behance presence</li>
            </ul>
        </div>
        """,
        "Data Analyst": """
        <div style="font-size: 1.1rem; line-height: 1.8;">
            <h3 style="color: #3b82f6; margin: 24px 0 16px 0;">📊 Phase 1: Data Foundations (1 month)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Excel:</strong> Pivot tables, VLOOKUP, charts, data cleaning</li>
                <li><strong>SQL:</strong> SELECT, GROUP BY, JOINs, subqueries</li>
                <li><strong>Statistics:</strong> Mean, median, distributions, hypothesis testing</li>
            </ul>
            
            <h3 style="color: #3b82f6; margin: 24px 0 16px 0;">📊 Phase 2: Analysis Tools (2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Python:</strong> Pandas, NumPy, Matplotlib, Seaborn</li>
                <li><strong>Tableau/PowerBI:</strong> Dashboards, storytelling</li>
                <li><strong>Projects:</strong> Sales analysis, customer segmentation</li>
            </ul>
            
            <h3 style="color: #3b82f6; margin: 24px 0 16px 0;">📊 Phase 3: Advanced (1-2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Advanced SQL:</strong> Window functions, CTEs, optimization</li>
                <li><strong>Big Data:</strong> Google BigQuery basics</li>
                <li><strong>ML Basics:</strong> Linear regression, clustering</li>
            </ul>
        </div>
        """,
        "Digital Marketer": """
        <div style="font-size: 1.1rem; line-height: 1.8;">
            <h3 style="color: #ef4444; margin: 24px 0 16px 0;">🚀 Phase 1: Digital Foundations (1 month)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>SEO:</strong> Keywords, on-page, technical SEO</li>
                <li><strong>Content:</strong> Blogging, copywriting basics</li>
                <li><strong>Analytics:</strong> Google Analytics setup, tracking</li>
            </ul>
            
            <h3 style="color: #ef4444; margin: 24px 0 16px 0;">🚀 Phase 2: Paid & Social (2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Google Ads:</strong> Search campaigns, conversion tracking</li>
                <li><strong>Social Media:</strong> Instagram, LinkedIn, content calendars</li>
                <li><strong>Email:</strong> Mailchimp, automation flows</li>
            </ul>
            
            <h3 style="color: #ef4444; margin: 24px 0 16px 0;">🚀 Phase 3: Strategy (1-2 months)</h3>
            <ul style="margin-bottom: 20px;">
                <li><strong>Strategy:</strong> Campaign planning, A/B testing</li>
                <li><strong>Tools:</strong> SEMrush, Ahrefs, Hotjar</li>
                <li><strong>Portfolio:</strong> 3 complete campaigns</li>
            </ul>
        </div>
        """
    }
    return roadmaps.get(role, "Roadmap coming soon")

def estimate_for_role(role):
    lookup = {
        "Software Engineer": "4-6 months",
        "UI/UX Designer": "3-5 months",
        "Data Analyst": "3-4 months",
        "Digital Marketer": "2-4 months"
    }
    return lookup.get(role, "Varies")

def videos_for_role(role):
    if role == "Software Engineer":
        return [
            # Existing
            {"title": "Full Course Web Development [HTML, CSS, JS, React, Node]", "url": "https://www.youtube.com/watch?v=ZxKM3DCV2kE"},
            {"title": "Python for Beginners", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
            {"title": "Git & GitHub Crash Course", "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},

            # English
            {"title": "DSA Full Course", "url": "https://www.youtube.com/watch?v=8hly31xKli0"},
            {"title": "React JS Full Course", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8"},
            {"title": "Node.js Crash Course", "url": "https://www.youtube.com/watch?v=fBNz5xF-Kx4"},
            {"title": "Java Programming for Beginners", "url": "https://www.youtube.com/watch?v=eIrMbAQSU34"},
            {"title": "System Design Basics", "url": "https://www.youtube.com/watch?v=MbjObHmDbZo"},
            
            # Tamil
            {"title": "Python Tutorial in Tamil", "url": "https://www.youtube.com/watch?v=YfO28Ihehbk"},
            {"title": "Web Development in Tamil", "url": "https://www.youtube.com/watch?v=HGSR3FDVkkQ"},
            {"title": "Git & GitHub in Tamil", "url": "https://www.youtube.com/watch?v=SWYqp7iY_Tc"},
            {"title": "Java Full Course in Tamil", "url": "https://www.youtube.com/watch?v=grEKMHGYyns"},
            {"title": "DSA in Tamil", "url": "https://www.youtube.com/watch?v=4VY5U4R4b0E"},
        ]

    elif role == "UI/UX Designer":
        return [
            # Existing
            {"title": "Figma UI Design Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8"},
            {"title": "UI/UX Design for Beginners", "url": "https://www.youtube.com/watch?v=c9Wg6Cb_YlU"},

            # English
            {"title": "UI Design Principles", "url": "https://www.youtube.com/watch?v=_Hp_dI0DzY4"},
            {"title": "UX Research Basics", "url": "https://www.youtube.com/watch?v=Ovj4hFxko7c"},
            {"title": "Adobe XD Tutorial", "url": "https://www.youtube.com/watch?v=68w2VwalD5w"},
            {"title": "Wireframing & Prototyping", "url": "https://www.youtube.com/watch?v=qpH7-KFWZRI"},
            {"title": "Design Thinking", "url": "https://www.youtube.com/watch?v=_r0VX-aU_T8"},

            # Tamil
            {"title": "UI/UX Design in Tamil", "url": "https://www.youtube.com/watch?v=6xjJ2s2FdK0"},
            {"title": "Figma Tutorial in Tamil", "url": "https://www.youtube.com/watch?v=R1x3_7GZ6Q4"},
            {"title": "Graphic Design Basics in Tamil", "url": "https://www.youtube.com/watch?v=J3uQ9Pp5P6s"},
            {"title": "Color Theory in Tamil", "url": "https://www.youtube.com/watch?v=8z2F5s6w7tQ"},
            {"title": "UX Case Study in Tamil", "url": "https://www.youtube.com/watch?v=7N9QK2XqF9Y"},
        ]

    elif role == "Data Analyst":
        return [
            # Existing
            {"title": "Excel for Data Analysis", "url": "https://www.youtube.com/watch?v=opF1ZbRBoCk"},
            {"title": "SQL Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},

            # English
            {"title": "Python for Data Analysis", "url": "https://www.youtube.com/watch?v=LHBE6Q9XlzI"},
            {"title": "Power BI Full Course", "url": "https://www.youtube.com/watch?v=AGrl-H87pRU"},
            {"title": "Tableau Tutorial", "url": "https://www.youtube.com/watch?v=aHaOIvR00So"},
            {"title": "Statistics for Data Science", "url": "https://www.youtube.com/watch?v=xxpc-HPKN28"},
            {"title": "Data Cleaning in Python", "url": "https://www.youtube.com/watch?v=Zj4cT4F5v7E"},

            # Tamil
            {"title": "Data Analyst Roadmap in Tamil", "url": "https://www.youtube.com/watch?v=7V7Z0cYqZ4I"},
            {"title": "Excel in Tamil", "url": "https://www.youtube.com/watch?v=1y5N4Z2G9H0"},
            {"title": "SQL in Tamil", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
            {"title": "Power BI in Tamil", "url": "https://www.youtube.com/watch?v=YxRz4E8Pq0M"},
            {"title": "Python Pandas in Tamil", "url": "https://www.youtube.com/watch?v=5y6S8Z9pY8Q"},
        ]

    elif role == "Digital Marketer":
        return [
            # Existing
            {"title": "Digital Marketing Full Course", "url": "https://www.youtube.com/watch?v=nU-IIXBWlS4"},
            {"title": "Google Ads Tutorial", "url": "https://www.youtube.com/watch?v=Ni8_nK7Tj6g"},

            # English
            {"title": "SEO Full Course", "url": "https://www.youtube.com/watch?v=xsVTqzratPs"},
            {"title": "Content Marketing Strategy", "url": "https://www.youtube.com/watch?v=7aX0o5j7M_Y"},
            {"title": "Social Media Marketing", "url": "https://www.youtube.com/watch?v=F8vQ7hGv7cU"},
            {"title": "Email Marketing", "url": "https://www.youtube.com/watch?v=Y2yXqZqjD3I"},
            {"title": "Affiliate Marketing", "url": "https://www.youtube.com/watch?v=9p9vE6i3QpQ"},

            # Tamil
            {"title": "Digital Marketing in Tamil", "url": "https://www.youtube.com/watch?v=JXQ4QJ7w4Gg"},
            {"title": "SEO in Tamil", "url": "https://www.youtube.com/watch?v=Yw7Y5s6pQ0Y"},
            {"title": "YouTube Marketing in Tamil", "url": "https://www.youtube.com/watch?v=6n3fPZp5q8M"},
            {"title": "Instagram Marketing in Tamil", "url": "https://www.youtube.com/watch?v=3FZP9Y8vF9M"},
            {"title": "Freelancing Digital Marketing in Tamil", "url": "https://www.youtube.com/watch?v=4A1D0K5Y9XQ"},
        ]

    else:
        return []
    
def project_details(project_name):
    details = {
        "Todo List App": {
            "description": "A simple task management application to add, delete and update tasks.",
            "steps": [
                "Design UI layout",
                "Create backend using Flask",
                "Create database (SQLite)",
                "Add CRUD operations",
                "Connect frontend & backend",
                "Test the app",
                "Deploy"
            ],
            "github": "https://github.com/topics/todo-app"
        },

        "Student Management System": {
            "description": "Manage students, courses, attendance and marks.",
            "steps": [
                "Create database schema",
                "Design forms",
                "Implement CRUD operations",
                "Add authentication",
                "Create reports",
                "Test and deploy"
            ],
            "github": "https://github.com/topics/student-management-system"
        },

        # You can keep adding like this for all projects
    }

    return details.get(project_name, {
        "description": "Project details coming soon.",
        "steps": [],
        "github": "https://github.com"
    })



def projects_for_role(role):
    projects = {
        "Software Engineer": [
            "Student Management System",
            "Todo List App",
            "Weather App",
            "Expense Tracker",
            "Chat Application",
            "Blog Website",
            "E-commerce Website",
            "Quiz Application",
            "Password Manager",
            "Portfolio Website"
        ],

        "UI/UX Designer": [
            "Redesign College Website",
            "Food Delivery App UI",
            "Fitness App UI",
            "Travel App UI",
            "Music Player UI",
            "Banking App UI",
            "E-Learning App UI",
            "Shopping App UI",
            "Dashboard Design",
            "Landing Page Design"
        ],

        "Data Analyst": [
            "Sales Data Analysis",
            "Student Performance Dashboard",
            "COVID-19 Data Visualization",
            "E-commerce Customer Analysis",
            "Stock Market Analysis",
            "Weather Trend Analysis",
            "Employee Attrition Analysis",
            "Movie Rating Analysis",
            "Traffic Accident Analysis",
            "Social Media Analytics"
        ],

        "Digital Marketer": [
            "Instagram Marketing Campaign",
            "SEO Audit for Website",
            "Google Ads Campaign",
            "Email Marketing Funnel",
            "Content Marketing Plan",
            "YouTube Channel Promotion",
            "Affiliate Marketing Setup",
            "Brand Awareness Campaign",
            "Product Launch Strategy",
            "Website Conversion Optimization"
        ]
    }
    return projects.get(role, [])


def website_for_role(role):
    lookup = {
        "Software Engineer": {
            "website": "https://www.geeksforgeeks.org/software-engineering/software-development/",
            "punch_line": "Build the future with logic and code.",
            "points": [
                "Strong problem solving skills",
                "Master at least one programming language",
                "Understanding of Data Structures & Algorithms",
                "Knowledge of frontend and backend",
                "Database management skills",
                "Version control using Git & GitHub",
                "System design basics",
                "Debugging and testing",
                "Continuous learning mindset",
                "Team collaboration"
            ]
        },

        "UI/UX Designer": {
            "website": "https://www.interaction-design.org/courses",
            "punch_line": "Design that looks good and feels right.",
            "points": [
                "User-centered thinking",
                "Strong sense of design principles",
                "Color theory and typography",
                "Wireframing and prototyping",
                "Figma / Adobe XD skills",
                "Usability testing",
                "Problem-solving through design",
                "Consistency and simplicity",
                "Responsive design knowledge",
                "Portfolio with case studies"
            ]
        },

        "Data Analyst": {
            "website": "https://www.coursera.org/specializations/data-analytics",
            "punch_line": "Turn data into decisions.",
            "points": [
                "Strong Excel skills",
                "SQL for database querying",
                "Python for data analysis",
                "Data cleaning and preprocessing",
                "Data visualization skills",
                "Statistical thinking",
                "Business understanding",
                "Attention to detail",
                "Storytelling with data",
                "Dashboard creation"
            ]
        },

        "Digital Marketer": {
            "website": "https://www.hubspot.com/courses",
            "punch_line": "Reach the right people at the right time.",
            "points": [
                "SEO knowledge",
                "Social media marketing",
                "Content creation",
                "Google Ads & Meta Ads",
                "Email marketing",
                "Analytics and tracking",
                "Brand building",
                "Creative thinking",
                "Customer engagement strategies",
                "Campaign management"
            ]
        }
    }

    return lookup.get(role, {
        "website": "https://www.google.com",
        "punch_line": "Choose your path, build your future.",
        "points": []
    })


# ===================== Routes =====================
@app.route('/')
def home():
    logged_in = 'username' in session
    return render_template('home.html', logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.context_processor
def inject_logged_in():
    return dict(logged_in=('username' in session))

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if 'username' not in session:
        return redirect(url_for('login_view'))

    if request.method == 'POST':
        answers = [request.form.get(f'q{i}') for i in range(1, 11)]
        counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        for ans in answers:
            if ans in counts:
                counts[ans] += 1

        career_map = {
            'a': ("Software Engineer", "You enjoy logic, coding and technology innovation."),
            'b': ("UI/UX Designer", "You thrive in creative design and visual aesthetics."),
            'c': ("Data Analyst", "You love analysis and working with data."),
            'd': ("Digital Marketer", "You excel in content, marketing and communication.")
        }

        highest = max(counts, key=counts.get)
        recommended_role, description = career_map.get(highest, ("Unknown Role", ""))

        session['recommended_role'] = recommended_role
        session['description'] = description
        return redirect(url_for('result'))

    return render_template('questionnaire.html')

@app.route('/result')
def result():
    if 'username' not in session or 'recommended_role' not in session:
        return redirect(url_for('questionnaire'))
    return render_template(
        'result.html',
        recommended_role=session['recommended_role'],
        description=session['description']
    )

@app.route('/roadmap')
def roadmap():
    if 'username' not in session or 'recommended_role' not in session:
        return redirect(url_for('questionnaire'))
    role = session['recommended_role']
    return render_template(
        'roadmap.html',
        recommended_role=role,
        roadmap_description=roadmap_for_role(role)
    )

@app.route('/videos')
def videos():
    if 'username' not in session or 'recommended_role' not in session:
        return redirect(url_for('questionnaire'))
    role = session['recommended_role']
    return render_template(
        'videos.html',
        recommended_role=role,
        recommended_videos=videos_for_role(role)
    )

@app.route('/projects')
def projects():
    if 'username' not in session or 'recommended_role' not in session:
        return redirect(url_for('questionnaire'))
    role = session['recommended_role']
    return render_template(
        'projects.html',
        recommended_role=role,
        recommended_projects=projects_for_role(role)
    )

@app.route('/project/<project_name>')
def project_detail(project_name):
    if 'username' not in session:
        return redirect(url_for('login_view'))

    project = project_details(project_name)

    return render_template(
        'project_detail.html',
        project_name=project_name,
        description=project["description"],
        steps=project["steps"],
        github=project["github"]
    )

@app.route('/websites')
def websites():
    if 'username' not in session or 'recommended_role' not in session:
        return redirect(url_for('questionnaire'))

    role = session['recommended_role']
    data = website_for_role(role)   # get website data

    # Define carousel images for each role
    carousel_images_map = {
        "Software Engineer": [
            "/static/images/se5.jpg",
            "/static/images/se5.jpg",
            "/static/images/se5.jpg"
        ],
        "UI/UX Designer": [
            "/static/images/uiux1.jpg",
            "/static/images/uiux2.jpg",
            "/static/images/uiux3.jpg"
        ],
        "Data Analyst": [
            "/static/images/da1.jpg",
            "/static/images/da2.jpg",
            "/static/images/da3.jpg"
        ],
        "Digital Marketer": [
            "/static/images/dm1.jpg",
            "/static/images/dm2.jpg",
            "/static/images/dm3.jpg"
        ]
    }

    # Get the carousel images or fallback to empty list
    carousel_images = carousel_images_map.get(role, [])

    # Get role roadmap HTML for detailed content below carousel
    role_content = roadmap_for_role(role)

    return render_template(
        'websites.html',
        recommended_role=role,
        course_website=data["website"],   # URL for recommended website
        punch_line=data["punch_line"],
        points=data["points"],
        carousel_images=carousel_images,
        role_content=role_content
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
