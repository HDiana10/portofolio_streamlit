
# IMPORTS 
import streamlit as st
from typing import List, Dict
# PAGE SETUP

st.set_page_config(
    page_title="My Portofolio",
    page_icon="",
    layout="wide",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": "A single-file streamlit portofolio"
    }
)

# DATA

PROFILE = {
    "name": "Diana HÎNCU",
    "role": "Current Year: 3rd Year - Actively seeking internship opportunities.",
    "tagline": "Passionate about Electronics & Coding. Ready to bring 110% (and great coffee) to your team.",
    "location": "Bucharest, Romania",
    "email": "dianahincu10@gmail.com",
    "github": "https://github.com/HDiana10",
    "linkedin": "https://www.linkedin.com/in/diana-hîncu/",
}

SKILLS: List[Dict] = [
    {"name": "Python", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "numpy"}},
    {"name": "C/C++", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "numpy"}},

    {"name": "SystemVerilog", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "numpy"}}
]

EXPERIENCE: List[Dict] = [

]

PROJECTS: List[Dict] =[
    {
        "name": "PCB Runner - MiniGame",
        "description": "An ETTI-themed version of the classic 'Trex Run' built with HTML and JavaScript, deployed via GitHub Pages.",
        "tech": ["JavaScript", "HTML5", "GitHub Pages"],
        "link": "https://hdiana10.github.io/run_pcb_run/"
    },
    {
        "name": "MINERVA Research Project",
        "description": "Applied research on battery lifespan optimization. Modeled the impact of dynamic operating modes on charge/discharge cycles.",
        "tech": ["Data Modeling", "Research", "Battery Technology"],
        "link": ""
    },
    {
        "name": "Electronic Piano",
        "description": "A hardware project using Arduino UNO presented at the Student Scientific Communications conference.",
        "tech": ["Arduino", "Embedded C", "Circuit Design"],
        "link": ""
    },
    {
        "name": "Smart Alcohol Breathalyzer",
        "description": "(Ongoing) A hardware project using the MQ-3 sensor and ESP32 to measure blood alcohol levels with LED warnings.",
        "tech": ["ESP32", "Hardware Sensors", "Prototyping"],
        "link": ""
    }
]

EDUCATION: List[Dict] = [
    {
        "degree": "Bachelor of Science in Computer Science and Information Technology",
        "school": "National University of Science and Technology Politehnica Bucharest",
        "faculty": "Faculty of Electronics, Telecommunications and Information Technology",
        "period": "2023 - 2027",
        "details": """
- <b>Current Year: 3rd Year</b> - Actively seeking internship opportunities.
- Current Academic Standing: Exceptional performance with an average grade of 9.40 (Year 1) and 9.88 (Year 2, Sem 1).
- Core Coursework: Programming Languages (C/C++), Data Structures & Algorithms, Operating Systems, Assembly Language (AMP), Digital Integrated Circuits.
- Research & Activities: Active participant in Student Scientific Communications conferences.
        """
    },
    {
        "degree": "High School Diploma in Mathematics and Computer Science",
        "school": "“Mihai Eminescu” National College, Suceava",
        "period": "2019 - 2023",
        "details": """
- Specialization: Intensive Computer Science track.
- Baccalaureate Exam Score: 9.58/10.
- Certification: Earned professional certification in Informatics with a final graduation project.
- Activities: Selected participant in the Regional Center of Excellence for Informatics.
        """
    }
]

VOLUNTEERING: List[Dict] = [
    {
        "role": "Active Volunteer & <b>IT Department Member</b>",
        "organization": "LSE (League of Electronics Students)",
        "period": "2023 - Present",
        "details": """
- Active member of the <b>IT and TechForge</b> departments.<br>
- Contributed to major events: Admission Simulation, General Culture Contest, Polifest, and LanParty.<br>
- Served as an <b>Official Referee</b> for the international <b>Robochallenge</b> competition.<br>
- Awarded <b>"Volunteer of the Week"</b> for outstanding commitment and organizational impact.
        """,
        "tech": ["Teamwork", "Event Management", "Technical Support"]
    },
    {
        "role": "Project Coordinator & <b>Content Manager</b>",
        "organization": "AIVI (Informal Association of Voices for Inclusion)",
        "period": "2020 - 2024",
        "details": """
- Managed the <b>#Cărticeală</b> (Literature), <b>#Cinematics</b>, and <b>#Science</b> departments.<br>
- Administrated <b>WordPress</b> websites, authored technical and cultural reviews, and conducted interviews.<br>
- Part of the <b>Official Media Team</b> for major international festivals: <b>FILIT, BSF, Animest, TIFF, and FFIR</b>.
        """,
        "tech": ["WordPress", "Project Management", "Digital Media", "Copywriting"]
    },
    {
        "role": "<b>Project Manager</b> & Educator",
        "organization": "GREEN in Hunedoara (EUTeens4Green)",
        "period": "2023 - 2024",
        "details": """
- Organized and coordinated the <b>GREENiH project</b>, promoting sustainable living among youth.<br>
- Facilitated <b>educational workshops</b> and managed project planning and stakeholder communication.
        """,
        "tech": ["Leadership", "Strategic Planning", "Sustainability Education"]
    },
    {
        "role": "<b>Workshop Mentor</b> & Team Lead",
        "organization": "ESA Moon Camp & NASA Space Settlement Workshop",
        "period": "2022 - 2023",
        "details": """
- Taught <b>astro-physics modules</b> to high school students.<br>
- Managed <b>team coordination</b> and project communication for aerospace design challenges.
        """,
        "tech": ["Public Speaking", "Astrophysics", "Leadership"]
    },
    {
        "role": "<b>Visual Workshop Facilitator</b>",
        "organization": "Sustainable in the Citadel (Ateliere Vizuale)",
        "period": "2022 - 2023",
        "details": """
- Facilitated communication and <b>guided participants</b> during visual workshops.<br>
- Responsible for <b>editing visual materials</b> and general project communication.
        """,
        "tech": ["Facilitation", "Media Editing", "Empathic Communication"]
    }
]

CONTESTS: List[Dict] = [
    {
        "name": "Electron 2025",
        "organizer": "UPB - Faculty of Electronics",
        "year": "2025",
        "result": "7th Place Overall",
        "details": "High-level technical competition focusing on electronics and circuit design."
    },
    {
        "name": "ESA Moon Camp Challenge",
        "organizer": "European Space Agency (ESA)",
        "year": "2022",
        "result": "3rd Place - Pioneers Category",
        "details": "International challenge to design a functional lunar base using 3D modeling and scientific principles."
    },
    {
        "name": "Pia Hunt",
        "organizer": "Student Technical Competition",
        "year": "2024",
        "result": "Honorable Mention",
        "details": "Technical scavenger hunt and problem-solving challenge for engineering students."
    }
]

# UTILITIES
def chips(items: List[str]) -> str:
    if isinstance(items, str):
        items = [items]
    return "".join(f'<span class="chip">{st.session_state.get("_emoi_map", {}.get(i.lower(), ""))} {i}</span>' for i in items)

def collect_all_tech() -> List[str]:
    tech = set()
    for e in EXPERIENCE:
        tech.update(e.get("tech", []))
    
    for p in PROJECTS:
        tech.update(p.get("tech", []))

    for s in SKILLS:
        tech.add(s['name']) # includes skill name
        for k in s.get("keywords", []):
            tech.add(k)

    return sorted(tech)

## STYLE

st.markdown("""
    <style>
    .card {
        background-color: #262730; /* A slightly lighter grey than the default dark theme */
        border: 1px solid #464b5d; /* A subtle border */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 10px;
        height: 250px; /* Optional: keeps all cards the same height */
    }
    .muted {
        color: #a3a8b4;
        font-size: 0.9rem;
    }
    .pill-btn {
        display: inline-block;
        padding: 5px 15px;
        background-color: #ff4b4b; /* Streamlit Red */
        color: white !important;
        text-decoration: none;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    .chip {
        background-color: #464b5d;
        color: #ffffff;
        padding: 2px 10px;
        border-radius: 15px;
        font-size: 0.75rem;
        margin-right: 5px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("Hello there!")
    st.write("This is a simple Portofolio")

    st.markdown("""**CONTACT**  
                [Email](mailto:{email})  
                [GitHub]({gh})  
                """.format(email=PROFILE['email'], gh=PROFILE['github']))
    
    st.markdown("<chr>", unsafe_allow_html=True)

    st.caption("Filters")
    all_tech = collect_all_tech()
    selected = st.multiselect("Filter by tech", options=all_tech, placeholder="e.g. Python, C")
    st.session_state['filters'] = set(selected)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.button(
        label="Download CV"
    )
    
# HEADER

left, right = st.columns([3,1])

with left:
    st.markdown(f"## {PROFILE["name"]}")
    st.write(f"**{PROFILE['role']}**")
    st.caption(f"📍 {PROFILE['location']} | 📧 {PROFILE['email']}")
    st.info(f"💡 {PROFILE['tagline']}")
with right:
    st.metric("Years Experience", value="{n}+".format(n=max(1, 5)))
    st.metric("Projects", value=str(len(PROJECTS)))

st.markdown("<hr>", unsafe_allow_html=True)

# TABS

about_tab, proj_tab, skills_tab, volunteer_tab, edu_tab = st.tabs(["About", "Projects", "Skills", "Volunteer", "Education"])

with about_tab:
    st.subheader("About")
    st.write("""I am a creative, dynamic person focused on continuous development, always open to new challenges. 
            I have been interested in technology since childhood, and I am currently seeking to consolidate my knowledge 
            and evolve in a solid professional direction in this field. My desire to exceed my limits motivates me to step 
            out of my comfort zone and make the most of my potential.  
            Five words that best describe me are: creativity, punctuality, seriousness, perseverance, and enthusiasm.  
            My friends say I'm funny too—but until I see concrete evidence, I remain skeptical.
""")


with proj_tab:
    st.subheader("Projects")
    st.write("Im Diana and i want a jov. desperately, Please. I will make how many coffees you want + 1")

    cols = st.columns(2)
    i = 0

    for p in PROJECTS:
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(p.get("tech", []))):
            continue

        with cols[i % 2]:
            st.markdown("""
                        <div class='card'>
                        <h4 style='margin:6px 0'>{name}</h4>
                        <p class ='muted' style ='margin:0 0 8px 0'> {desc} </p>
                        <div style='margin:6px 0'> {chips} </div>
                        <a class = 'pill-btn' href='{link}' target='_blank'>Open</a>
                        </div>
                        """.format(
                            name=p["name"], desc=p["description"], chips=chips(p.get("tech", [])), link=p.get("link", "#")
                        ), unsafe_allow_html=True)
            i += 1

with skills_tab:
    st.subheader("Skills")
    for s in SKILLS:
        col1, col2 = st.columns([1,3])
        with col1:
            st.write(f"**{s['name']}**")
            if s.get("keywords"):
                st.caption(",".join(s['keywords']))
        with col2:
            st.progress(int(s.get("level", 0)))

with edu_tab:
    st.subheader("Education")
    for e in EDUCATION:
        # 1. Add the {faculty} placeholder in the HTML
        card_html = """
            <div class='card' style='height: auto; margin-bottom: 20px;'>
                <h4 style='margin:0px 0; color: #ff4b4b;'>{degree}</h4>
                <p style='margin:4px 0; font-weight:bold;'>{school}</p>
                <p style='margin:0px 0; font-style: italic; color: #a3a8b4;'>{faculty}</p>
                <p class='muted' style='margin:8px 0 12px 0;'>{period}</p>
                <div style='font-size: 0.85rem; line-height: 1.5;'>
                    {details}
                </div>
            </div>
        """.format(
            degree = e["degree"],
            school = e["school"],
            faculty = e.get("faculty", ""), # 2. Map the faculty variable here
            period = e["period"],
            details = e["details"].replace("- ", "• ").replace("\n", "<br>")
        )
        
        # 3. Use .replace("\n", "") to prevent raw code/divs from showing
        st.markdown(card_html.replace("\n", ""), unsafe_allow_html=True)

# --- VOLUNTEERING TAB ---
with volunteer_tab:
    st.subheader("🤝 Community Involvement")
    for v in VOLUNTEERING:
        # 1. Filter Check
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(v.get("tech", []))):
            continue

        # 2. Render everything inside ONE markdown block
        st.markdown(f"""
            <div class='card' style='height: auto; margin-bottom: 15px;'>
                <h4 style='margin:0;'>{v['role']}</h4>
                <p style='margin:2px 0; font-weight: bold;'>{v['organization']}</p>
                <p class='muted'>{v['period']}</p>
                <div style='font-size: 0.85rem; margin-top: 8px;'>
                    {v['details'].replace('-', '•')}
                </div>
                <div style='margin-top:10px;'>
                    {chips(v.get('tech', []))}
                </div>
            </div>
        """.replace("\n", ""), unsafe_allow_html=True)