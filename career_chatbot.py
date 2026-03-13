import streamlit as st
import time
import random
from datetime import datetime

# ─────────────────────────────────────────────
#  RULE-BASED ENGINE
# ─────────────────────────────────────────────

CAREER_RULES = {
    # Greetings
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "start", "begin"],
        "responses": [
            "Hello! 👋 Welcome to CareerCompass. I'm here to help you navigate your career journey. What would you like to explore today?",
            "Hi there! 👋 Great to have you here. I can help with career advice, resume tips, interview prep, and much more. What's on your mind?"
        ]
    },

    # Career Exploration
    "career_exploration": {
        "patterns": ["career", "what career", "career path", "choose career", "which career", "career options", "career change", "switch career", "new career", "different career"],
        "responses": [
            """**Exploring Career Paths** 🗺️

Great question! Choosing the right career involves understanding yourself and the market. Here's a framework:

**Step 1 — Self Assessment**
- 🎯 Identify your **strengths** and natural talents
- 💡 Discover your **interests** and passions
- 📊 Evaluate your **values** (work-life balance, impact, income)

**Step 2 — Market Research**
- 📈 Explore high-growth industries (tech, healthcare, renewable energy)
- 🔍 Research job roles within those industries
- 💼 Look at salary ranges and advancement opportunities

**Step 3 — Skill Gap Analysis**
- Compare your current skills to job requirements
- Identify certifications or degrees needed

Would you like advice on a **specific field**, or help with **self-assessment**?"""
        ]
    },

    # Technology / IT Careers
    "tech_career": {
        "patterns": ["software", "developer", "coding", "programming", "it career", "tech career", "computer science", "data science", "machine learning", "ai career", "web development", "cybersecurity", "cloud computing"],
        "responses": [
            """**Technology Career Roadmap** 💻

Tech is one of the fastest-growing and highest-paying sectors. Here are top paths:

| Role | Avg Salary | Demand |
|------|-----------|--------|
| Software Engineer | $110K–$180K | 🔥 Very High |
| Data Scientist | $100K–$160K | 🔥 Very High |
| Cybersecurity Analyst | $90K–$140K | 🔥 Critical |
| Cloud Architect | $130K–$200K | ⚡ High |
| ML Engineer | $120K–$190K | ⚡ High |

**Top Skills to Learn:**
- Python, JavaScript, or Java
- Cloud platforms (AWS, Azure, GCP)
- Version control (Git)
- System design & architecture

**Recommended Learning Path:**
1. Pick a language (Python is beginner-friendly)
2. Build 3–5 portfolio projects
3. Contribute to open source
4. Earn a relevant certification

Need guidance on a **specific tech role**?"""
        ]
    },

    # Business / Management
    "business_career": {
        "patterns": ["business", "management", "mba", "marketing", "finance", "consulting", "entrepreneur", "startup", "hr", "human resources", "operations"],
        "responses": [
            """**Business & Management Careers** 📊

Business careers offer incredible diversity and leadership opportunities:

**High-Impact Roles:**
- 📈 **Management Consulting** — Problem-solving for organizations ($80K–$200K+)
- 💰 **Investment Banking / Finance** — Capital markets & M&A ($100K–$300K+)
- 🎯 **Product Management** — Bridge between tech and business ($110K–$175K)
- 📢 **Digital Marketing** — Growing demand, creative + analytical ($60K–$130K)
- 🧠 **Strategy & Operations** — Driving company growth ($90K–$160K)

**Key Credentials:**
- MBA from a target school (for consulting/finance)
- CFA for investment/finance roles
- PMP for project management
- Google/Meta certifications for marketing

**Pro Tips:**
✅ Build a professional network on LinkedIn
✅ Seek internships early — they lead to full-time offers
✅ Develop both analytical AND communication skills

Want advice on breaking into a **specific business field**?"""
        ]
    },

    # Healthcare Careers
    "healthcare_career": {
        "patterns": ["doctor", "medicine", "nursing", "healthcare", "medical", "pharmacy", "dentist", "therapist", "psychologist", "public health"],
        "responses": [
            """**Healthcare Career Paths** 🏥

Healthcare is one of the most stable and rewarding sectors:

**Clinical Roles:**
- 👨‍⚕️ **Physician** — MD/DO required (8–12 years training, $200K–$400K+)
- 🩺 **Nurse Practitioner** — MSN required ($100K–$140K, growing fast)
- 💊 **Pharmacist** — PharmD required ($120K–$145K)
- 🦷 **Dentist** — DDS/DMD required ($150K–$220K)

**Non-Clinical Roles (High Growth):**
- 📊 **Healthcare Data Analyst** — Intersection of tech + healthcare
- 🏗️ **Health IT / Informatics** — Digital transformation of healthcare
- 📋 **Healthcare Administrator** — MBA in Healthcare preferred
- 🧬 **Medical Research / Biotech** — PhD or MS required

**Important Considerations:**
⏰ Most clinical roles require significant education investment
💡 Non-clinical roles offer shorter paths to entry
📈 Telehealth and health tech are booming sectors

Shall I dive deeper into any specific healthcare area?"""
        ]
    },

    # Resume Tips
    "resume": {
        "patterns": ["resume", "cv", "curriculum vitae", "cover letter", "portfolio", "application"],
        "responses": [
            """**Resume Building Guide** 📄

A strong resume is your first impression. Here's how to make it exceptional:

**Essential Sections:**
1. **Header** — Name, phone, email, LinkedIn, portfolio URL
2. **Professional Summary** — 2–3 punchy lines about your value
3. **Work Experience** — Most critical section
4. **Education** — Degrees, certifications, relevant courses
5. **Skills** — Technical + soft skills

**The STAR-CAR Method for Experience Bullets:**
> Used **Action Verb** + **What you did** + **Measurable Result**

❌ "Responsible for managing social media"
✅ "Grew Instagram following by **340%** in 6 months, driving $45K in revenue"

**ATS Optimization Tips:**
- Mirror keywords from the job description
- Use standard section headers (not creative names)
- Save as PDF unless told otherwise
- Keep to 1 page (2 pages for 10+ years experience)

**Common Mistakes to Avoid:**
🚫 Generic objective statements
🚫 Spelling/grammar errors
🚫 Listing duties instead of achievements
🚫 Including personal info (photo, age, marital status)

Would you like tips on a **specific resume section**?"""
        ]
    },

    # Interview Prep
    "interview": {
        "patterns": ["interview", "job interview", "interview tips", "interview questions", "prepare interview", "behavioral", "technical interview"],
        "responses": [
            """**Interview Preparation Masterclass** 🎤

Interviews are skills you can learn and improve. Here's a complete framework:

**Before the Interview:**
- 🔍 Research the company deeply (mission, values, recent news)
- 📝 Prepare 5–7 STAR stories (Situation, Task, Action, Result)
- ❓ Prepare 3–5 thoughtful questions to ask
- 👔 Dress one level above the company culture

**Common Question Types & How to Answer:**

**Tell me about yourself:**
> [Current role] + [Key achievement] + [Why this opportunity excites you]

**Behavioral Questions (STAR Method):**
> "Tell me about a time you led a difficult project..."
> S: Set the scene → T: Your task → A: Actions you took → R: Measurable result

**Salary Questions:**
> Research market rates first. State a range, not a single number.
> "Based on my research and experience, I'm targeting $X–$Y"

**During the Interview:**
✅ Listen actively, pause before answering
✅ Ask clarifying questions
✅ Show enthusiasm genuinely

**After the Interview:**
📧 Send a thank-you email within 24 hours

Want me to walk through **common interview questions** for a specific role?"""
        ]
    },

    # Salary / Negotiation
    "salary": {
        "patterns": ["salary", "pay", "compensation", "negotiate", "negotiation", "raise", "promotion", "offer", "money"],
        "responses": [
            """**Salary Negotiation Strategy** 💰

Negotiating your salary is one of the highest-ROI skills you can develop:

**Research Phase:**
- Use **Glassdoor**, **Levels.fyi** (tech), **LinkedIn Salary**, **PayScale**
- Know the range for your role, level, and location
- Factor in total compensation: base + bonus + equity + benefits

**The Golden Rules:**
1. **Never give the first number** — Let them anchor first
2. **Always negotiate** — 85% of employers expect it
3. **Negotiate the whole package** — PTO, remote work, sign-on bonus
4. **Get it in writing** before resigning from current role

**Scripts That Work:**

When asked "What are your salary expectations?":
> *"I'd love to understand the full scope of the role first. What is the budgeted range for this position?"*

When you receive an offer:
> *"Thank you — I'm very excited about this opportunity. Based on my research and experience, I was expecting something closer to $X. Is there flexibility there?"*

**Negotiation Leverage:**
- Competing offers (best leverage)
- Specialized skills in demand
- Strong track record with metrics

**Average Salary Increase from Negotiating:** 10–20% 📈

Want a negotiation script for a **specific situation**?"""
        ]
    },

    # Skills Development
    "skills": {
        "patterns": ["skill", "learn", "course", "certification", "upskill", "training", "education", "degree", "bootcamp", "study"],
        "responses": [
            """**Skills Development Roadmap** 🎓

The most future-proof professionals are lifelong learners. Here's how to develop strategically:

**High-Value Skills in 2025:**

*Technical:*
- 🤖 AI/ML & Prompt Engineering
- ☁️ Cloud Computing (AWS/Azure/GCP)
- 📊 Data Analysis (Python, SQL, Tableau)
- 🔒 Cybersecurity

*Soft Skills (Often Underdeveloped):*
- 💬 Executive Communication
- 🧠 Critical Thinking & Problem Solving
- 🤝 Cross-functional Collaboration
- 📋 Project Management

**Best Learning Platforms:**
| Platform | Best For | Cost |
|----------|----------|------|
| Coursera | University courses | Free audit / $50/mo |
| LinkedIn Learning | Professional skills | $40/mo |
| Udemy | Practical tech skills | $10–$15/course |
| Pluralsight | IT & dev skills | $45/mo |
| YouTube | Getting started | Free |

**Learning Strategy:**
1. Learn one skill deeply before spreading thin
2. Apply it in a project immediately
3. Teach it to solidify understanding
4. Add it to your portfolio with proof

What **specific skill** are you looking to develop?"""
        ]
    },

    # Networking
    "networking": {
        "patterns": ["network", "networking", "linkedin", "connect", "mentor", "mentorship", "relationship", "contact", "referral"],
        "responses": [
            """**Professional Networking Guide** 🤝

85% of jobs are filled through networking. Here's how to do it authentically:

**LinkedIn Optimization:**
- 🖼️ Professional headshot (increases views by 14x)
- 📝 Compelling headline (not just job title)
- 📖 Story-driven About section
- ✅ Get skills endorsed and give recommendations

**How to Reach Out Without Being Awkward:**

**Cold message template:**
> *"Hi [Name], I came across your work at [Company] and found your post on [Topic] really insightful. I'm exploring a career in [Field] and would love to hear about your experience — would you be open to a 20-minute virtual coffee chat?"*

**Networking Events:**
- Industry conferences & meetups
- Alumni networks (very powerful!)
- Slack communities & Discord servers
- Professional associations

**Nurturing Relationships:**
- Comment thoughtfully on their posts
- Share articles they'd find useful
- Congratulate on promotions/milestones
- Follow up periodically — not just when you need something

**The Give-First Mindset:**
> Always ask "How can I add value to this person?" before asking for anything.

Want tips on networking for a **specific industry**?"""
        ]
    },

    # Work-Life Balance
    "wellbeing": {
        "patterns": ["stress", "burnout", "work life balance", "overwhelmed", "mental health", "tired", "exhausted", "toxic", "workplace culture", "happiness", "motivation"],
        "responses": [
            """**Career Wellbeing & Burnout Prevention** 🌿

A sustainable career is a long-term marathon, not a sprint. Your wellbeing matters.

**Signs of Burnout:**
- 😔 Chronic exhaustion even after rest
- 😤 Increasing cynicism about your work
- 📉 Reduced performance and concentration
- 🚫 Dreading going to work regularly

**Immediate Recovery Strategies:**
1. **Set boundaries** — Define "off hours" and protect them
2. **Talk to your manager** — Be honest about workload
3. **Take your PTO** — Fully disconnect during vacation
4. **Seek support** — EAP (Employee Assistance Programs) are free and confidential

**Long-Term Prevention:**
- 🎯 Align daily work with your core values
- 🏃 Regular exercise (proven stress reducer)
- 📵 Digital detox boundaries (no emails after 7pm)
- 🧘 Mindfulness or journaling practice

**When to Consider a Change:**
If you've addressed the root causes and still feel unfulfilled, it may be time to explore:
- A role change within the same company
- A new company with better culture
- A different industry altogether

You're not alone in feeling this way — it's one of the most common career challenges. What's weighing on you most right now?"""
        ]
    },

    # Entrepreneurship
    "entrepreneurship": {
        "patterns": ["entrepreneur", "startup", "business idea", "own business", "freelance", "self employed", "side hustle", "founder", "venture"],
        "responses": [
            """**Entrepreneurship & Startup Guide** 🚀

Building something of your own is both thrilling and challenging. Here's a realistic roadmap:

**Validating Your Idea (Before Quitting Your Job):**
1. **Problem-first thinking** — What painful problem are you solving?
2. **Talk to 20 potential customers** before writing a line of code
3. **Build an MVP** — Minimum viable product in 2–4 weeks
4. **Pre-sell** — Get someone to pay before you build the full thing

**Business Models to Consider:**
- 💡 SaaS (Software as a Service) — Recurring revenue
- 🛒 E-commerce — Products, dropshipping
- 📚 Info products — Courses, ebooks, coaching
- 🔧 Freelancing/Consulting — Services based on expertise
- 📱 Mobile apps — B2C or B2B

**Funding Options:**
| Stage | Option | Typical Amount |
|-------|--------|---------------|
| Idea | Bootstrapping | $0–$10K |
| Early | Friends & Family | $10K–$100K |
| Traction | Angel Investors | $100K–$1M |
| Growth | Series A VC | $1M–$10M+ |

**Top Resources:**
- 📖 "The Lean Startup" by Eric Ries
- 🎙️ How I Built This (podcast)
- 🌐 Y Combinator Startup School (free)
- 💬 r/entrepreneur community

What stage are you at with your business idea?"""
        ]
    },

    # Help menu
    "help": {
        "patterns": ["help", "what can you do", "options", "topics", "menu", "guide", "capabilities"],
        "responses": [
            """**CareerCompass Menu** 🧭

Here's everything I can help you with:

| Topic | Ask me about... |
|-------|----------------|
| 🗺️ Career Exploration | "How do I choose a career?" |
| 💻 Tech Careers | "How do I become a software engineer?" |
| 📊 Business Careers | "Tell me about consulting careers" |
| 🏥 Healthcare | "What are my options in healthcare?" |
| 📄 Resume | "How do I write a strong resume?" |
| 🎤 Interviews | "How do I prepare for interviews?" |
| 💰 Salary | "How do I negotiate my salary?" |
| 🎓 Skills | "What skills should I learn?" |
| 🤝 Networking | "How do I network effectively?" |
| 🌿 Wellbeing | "How do I avoid burnout?" |
| 🚀 Entrepreneurship | "How do I start a business?" |

Just type your question naturally — I'll find the best guidance for you!"""
        ]
    },

    # Goodbye
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "thanks", "thank you", "exit", "quit", "done"],
        "responses": [
            "Thank you for using CareerCompass! 🌟 Best of luck on your career journey. Remember — every expert was once a beginner. Keep going!",
            "Goodbye! 👋 It was great chatting with you. Feel free to return anytime you need career guidance. You've got this! 🚀"
        ]
    }
}

def get_response(user_input: str) -> str:
    """Rule-based response engine."""
    user_lower = user_input.lower().strip()

    # Score each rule category
    best_match = None
    best_score = 0

    for category, data in CAREER_RULES.items():
        score = sum(1 for pattern in data["patterns"] if pattern in user_lower)
        if score > best_score:
            best_score = score
            best_match = category

    if best_match and best_score > 0:
        return random.choice(CAREER_RULES[best_match]["responses"])

    # Fallback
    return """I appreciate your question! 🤔 I'm best equipped to help with:

- 🗺️ **Career exploration & planning**
- 💻 **Tech, business, or healthcare career paths**
- 📄 **Resume & cover letter writing**
- 🎤 **Interview preparation**
- 💰 **Salary negotiation**
- 🎓 **Skills development & learning**
- 🤝 **Professional networking**
- 🚀 **Entrepreneurship & freelancing**

Try asking something like *"How do I get into data science?"* or type **help** to see all topics!"""


# ─────────────────────────────────────────────
#  STREAMLIT UI
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="CareerCompass — AI Career Guide",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root variables ── */
:root {
    --bg-primary: #0D1117;
    --bg-secondary: #161B22;
    --bg-card: #1C2333;
    --bg-input: #21262D;
    --accent-gold: #C9A84C;
    --accent-gold-light: #E8C96D;
    --accent-teal: #39D2C0;
    --text-primary: #E6EDF3;
    --text-secondary: #8B949E;
    --text-muted: #6E7681;
    --border: #30363D;
    --user-bubble: #1D3557;
    --bot-bubble: #1C2333;
    --radius: 16px;
    --shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* ── Global reset ── */
html, body, [data-testid="stApp"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg-secondary) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* ── Main content padding ── */
.main-content { padding: 0 2rem 2rem 2rem; }

/* ── Header ── */
.chat-header {
    background: linear-gradient(135deg, var(--bg-secondary) 0%, #1a2744 100%);
    border-bottom: 1px solid var(--border);
    padding: 1.5rem 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(12px);
}

.header-logo {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, var(--accent-gold), #a07d2e);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 4px 20px rgba(201,168,76,0.3);
}

.header-text h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: var(--accent-gold-light) !important;
    margin: 0 !important;
    line-height: 1 !important;
}

.header-text p {
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin: 2px 0 0 0;
}

.status-pill {
    margin-left: auto;
    background: rgba(57, 210, 192, 0.15);
    border: 1px solid rgba(57, 210, 192, 0.4);
    color: var(--accent-teal) !important;
    padding: 6px 14px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.status-dot {
    width: 7px;
    height: 7px;
    background: var(--accent-teal);
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

/* ── Chat area ── */
.chat-area {
    padding: 1.5rem 1rem;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    min-height: 60vh;
    max-height: 65vh;
    overflow-y: auto;
}

.chat-area::-webkit-scrollbar { width: 4px; }
.chat-area::-webkit-scrollbar-track { background: transparent; }
.chat-area::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

/* ── Message bubbles ── */
.msg-row {
    display: flex;
    gap: 12px;
    animation: fadeUp 0.3s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

.msg-row.user { flex-direction: row-reverse; }

.avatar {
    width: 38px;
    height: 38px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
    margin-top: 2px;
}

.avatar.bot {
    background: linear-gradient(135deg, var(--accent-gold), #8a5a10);
    box-shadow: 0 2px 12px rgba(201,168,76,0.3);
}

.avatar.user {
    background: linear-gradient(135deg, #1D4ED8, #1e3a8a);
    box-shadow: 0 2px 12px rgba(29,78,216,0.3);
}

.bubble {
    max-width: 72%;
    padding: 14px 18px;
    border-radius: var(--radius);
    font-size: 0.9rem;
    line-height: 1.7;
}

.bubble.bot {
    background: var(--bot-bubble);
    border: 1px solid var(--border);
    border-top-left-radius: 4px;
    color: var(--text-primary);
}

.bubble.user {
    background: var(--user-bubble);
    border: 1px solid #2d4a7a;
    border-top-right-radius: 4px;
    color: var(--text-primary);
}

/* Tables inside bubbles */
.bubble table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.8rem 0;
    font-size: 0.85rem;
}
.bubble th {
    background: rgba(201,168,76,0.15);
    color: var(--accent-gold-light) !important;
    padding: 8px 12px;
    text-align: left;
    border: 1px solid rgba(201,168,76,0.2);
}
.bubble td {
    padding: 8px 12px;
    border: 1px solid var(--border);
    color: var(--text-primary);
}
.bubble tr:nth-child(even) td { background: rgba(255,255,255,0.03); }

/* Headings inside bubbles */
.bubble strong { color: var(--accent-gold-light); }

/* ── Timestamp ── */
.msg-meta {
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-top: 4px;
    padding: 0 4px;
}
.msg-row.user .msg-meta { text-align: right; }

/* ── Input area ── */
.input-area {
    background: var(--bg-secondary);
    border-top: 1px solid var(--border);
    padding: 1.2rem 1.5rem;
    position: sticky;
    bottom: 0;
}

/* Streamlit input override */
[data-testid="stTextInput"] input {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 14px 16px !important;
    transition: border-color 0.2s ease !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--accent-gold) !important;
    box-shadow: 0 0 0 3px rgba(201,168,76,0.15) !important;
    outline: none !important;
}
[data-testid="stTextInput"] input::placeholder { color: var(--text-muted) !important; }

/* Streamlit buttons override */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, var(--accent-gold), #a07d2e) !important;
    color: #0D1117 !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.2s ease !important;
}
[data-testid="stButton"] button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(201,168,76,0.4) !important;
}

/* ── Sidebar cards ── */
.sidebar-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    margin-bottom: 1rem;
}
.sidebar-card h4 {
    font-family: 'Playfair Display', serif;
    color: var(--accent-gold-light);
    font-size: 0.95rem;
    margin: 0 0 0.7rem 0;
}
.sidebar-card p, .sidebar-card li {
    color: var(--text-secondary);
    font-size: 0.8rem;
    line-height: 1.6;
}
.topic-chip {
    display: inline-block;
    background: rgba(201,168,76,0.12);
    border: 1px solid rgba(201,168,76,0.25);
    color: var(--accent-gold-light);
    padding: 4px 10px;
    border-radius: 50px;
    font-size: 0.75rem;
    margin: 3px 2px;
    cursor: pointer;
    transition: background 0.2s;
}

/* ── Welcome banner ── */
.welcome-banner {
    background: linear-gradient(135deg, #1a2744 0%, #1C2333 100%);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 18px;
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}
.welcome-banner h2 {
    font-family: 'Playfair Display', serif;
    color: var(--accent-gold-light);
    font-size: 1.6rem;
    margin-bottom: 0.5rem;
}
.welcome-banner p { color: var(--text-secondary); font-size: 0.9rem; }

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* Markdown tables in Streamlit */
[data-testid="stMarkdown"] table {
    width: 100%;
    border-collapse: collapse;
}
[data-testid="stMarkdown"] th {
    background: rgba(201,168,76,0.15);
    color: var(--accent-gold-light);
    padding: 8px 12px;
    border: 1px solid rgba(201,168,76,0.2);
}
[data-testid="stMarkdown"] td {
    padding: 8px 12px;
    border: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": """**Welcome to CareerCompass!** 🧭

I'm your professional career guidance assistant. I'm here to help you navigate every stage of your career journey.

Here's what I can help you with:
- 🗺️ Explore career paths and industries
- 📄 Craft a winning resume & cover letter
- 🎤 Ace your interviews
- 💰 Negotiate your salary
- 🎓 Develop in-demand skills
- 🤝 Build your professional network
- 🚀 Launch your entrepreneurial journey

**Try asking:**
> *"How do I get into data science?"*
> *"Give me resume tips"*
> *"How do I negotiate a higher salary?"*

Or type **help** to see all topics. Let's build your career! 💼""",
        "time": datetime.now().strftime("%I:%M %p")
    })

# ── Header ────────────────────────────────
st.markdown("""
<div class="chat-header">
    <div class="header-logo">🧭</div>
    <div class="header-text">
        <h1>CareerCompass</h1>
        <p>Professional Career Guidance Assistant</p>
    </div>
    <div class="status-pill">
        <div class="status-dot"></div> Online
    </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1.5rem 0.5rem 0.5rem 0.5rem;">
        <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #C9A84C; margin-bottom: 0.25rem;">
            🧭 CareerCompass
        </div>
        <div style="color: #6E7681; font-size: 0.75rem; margin-bottom: 1.5rem;">
            Your AI-Powered Career Guide
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <h4>📚 Quick Topics</h4>
        <div>
            <span class="topic-chip">Career Change</span>
            <span class="topic-chip">Tech Careers</span>
            <span class="topic-chip">Resume Tips</span>
            <span class="topic-chip">Interview Prep</span>
            <span class="topic-chip">Salary Tips</span>
            <span class="topic-chip">Networking</span>
            <span class="topic-chip">MBA</span>
            <span class="topic-chip">Freelancing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <h4>💡 Suggested Questions</h4>
        <ul style="padding-left: 1rem; margin: 0;">
            <li>How do I switch to tech?</li>
            <li>What makes a strong resume?</li>
            <li>How do I handle salary negotiation?</li>
            <li>What skills are in demand in 2025?</li>
            <li>How do I start a startup?</li>
            <li>Tips to avoid burnout?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <h4>📊 Session Stats</h4>
    """, unsafe_allow_html=True)

    msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    st.markdown(f"""
        <p>💬 Messages sent: <strong style="color:#C9A84C">{msg_count}</strong></p>
        <p>🤖 Topics covered: <strong style="color:#39D2C0">{min(msg_count, 11)}</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Conversation cleared! 🌟 How can I help you today? Type **help** to see all topics.",
            "time": datetime.now().strftime("%I:%M %p")
        })
        st.rerun()

    st.markdown("""
    <div style="margin-top: 2rem; padding: 0 0.5rem; color: #6E7681; font-size: 0.7rem; text-align: center; line-height: 1.6;">
        CareerCompass v1.0<br>
        Rule-Based Career Intelligence<br>
        <span style="color: #C9A84C;">Built with Python & Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

# ── Chat Display ──────────────────────────
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            with st.chat_message("assistant", avatar="🧭"):
                st.markdown(msg["content"])
                st.caption(f"🕐 {msg.get('time', '')}")
        else:
            with st.chat_message("user", avatar="👤"):
                st.markdown(msg["content"])
                st.caption(f"🕐 {msg.get('time', '')}")

# ── Input Area ────────────────────────────
st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

if prompt := st.chat_input("Ask me about careers, resumes, interviews, salary..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "time": datetime.now().strftime("%I:%M %p")
    })

    # Get response
    response = get_response(prompt)

    # Simulate typing delay for realism
    time.sleep(0.4)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": datetime.now().strftime("%I:%M %p")
    })

    st.rerun()
