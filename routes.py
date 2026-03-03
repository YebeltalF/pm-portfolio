from flask import Blueprint, render_template

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/')
def index():
    # Data abstracted from Yebeltal Fisseha's CV
    profile = {
        "name": "Yebeltal Fisseha",
        "role": "Senior Product Owner / Manager",
        "bio": "Proven leader with 4+ years of experience directing software teams to deliver high-impact products. Expert in translating complex business needs into functional systems.",
        "contact": {"phone": "+251 9 52 66 02 16", "email": "fissehayebeltal@gmail.com"},
        "links": {"github": "#", "linkedin": "#"}
    }

    experience = [
        {
            "company": "Mereb Technologies",
            "role": "Senior Software Project Manager",
            "period": "Jul 2025 - Present",
            "highlights": [
                "Managing Healthcare and Recruitment projects across two development teams.",
                "Leading AI capability integrations and executive stakeholder reporting.",
                "Coaching team members on Agile and Product thinking."
            ]
        },
        {
            "company": "Convex Technologies",
            "role": "Product Owner Manager (SaaS)",
            "period": "Dec 2024 - July 2025",
            "highlights": [
                "Scaled Africa's leading iGaming B2B2C platform for 30+ enterprise clients.",
                "Managed a platform engaging millions of users and generating hundreds of millions in revenue.",
                "Led a team of 25 software engineers through sprint execution."
            ]
        },
        {
            "company": "Quantum Technologies",
            "role": "Product Owner (Fintech)",
            "period": "Mar 2024 - Oct 2024",
            "highlights": [
                "Owned credit scoring and Loan Management products for 2 large local banks.",
                "Applied data models to improve credit decision-making processes.",
                "Managed international development teams."
            ]
        },
        {
            "company": "BeU Delivery",
            "role": "Product Owner (Food Delivery)",
            "period": "Oct 2021 - Oct 2023",
            "highlights": [
                "Owned investor-backed market-leading delivery product.",
                "Reduced time-to-market by implementing streamlined Agile processes.",
                "Conducted research and data analysis for competitive differentiation."
            ]
        }
    ]

    skills = ["Project Management", "Product Strategy", "Agile & Scrum", "System Design", "AI Utilization", "GTM Planning"]
    tools = ["JIRA", "Notion", "ClickUp", "Figma", "Postman", "LLMs"]

    return render_template('index.html', profile=profile, experience=experience, skills=skills, tools=tools)