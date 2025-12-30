
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
    {"name": "Python", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "Numpy"}},
    {"name": "C/C++", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "Numpy"}},

    {"name": "SystemVerilog", "level": 90, "keywords":{"ML", "Streamlit", "Pandas", "Numpy"}}
]

PROJECTS: List[Dict] = [
    {
        "name": "🔊 MP3 Player - Python",
        "description": "Desktop application for audio playback developed with <b>Python</b> and <b>Custom Tkinter</b>. Features <b>playlist management</b>, shuffle, and real-time audio control via <b>pygame.mixer</b>.",
        "tech": ["Python", "Pygame", "CustomTkinter", "UI/UX"],
        "link": "https://github.com/HDiana10/Proiect_MP3"
    },
    {
        "name": "🚦 FPGA Smart Traffic Light Controller",
        "description": "A complex <b>System Verilog</b> implementation of a traffic management system. It features <b>finite state machine (FSM)</b> logic to handle multiple intersections, pedestrian sensors, and emergency vehicle overrides.",
        "tech": ["System Verilog", "FPGA", "Digital Design", "Vivado",],
        "link": "https://github.com/HDiana10/FPGA-Smart-Traffic-Light-Controller"
    },
    {
        "name": "🛗 FPGA Elevator with Door Control",
        "description": "A <b>System Verilog</b> implementation of an elevator control system. It manages <b>state transitions</b> between floors, prioritized request handling, and safety-critical <b>door control logic</b> using a <b>Finite State Machine (FSM)</b>.",
        "tech": ["System Verilog", "FPGA", "Digital Design", "Control Systems", "Vivado"],
        "link": "https://github.com/HDiana10/FPGA-Elevator-with-Door-Control"
    },
    {
        "name": "🔢 4-bit ALU with 7-Segment Display",
        "description": "Designed and implemented a <b>4-bit Arithmetic Logic Unit (ALU)</b> in <b>System Verilog</b>. The project includes logic for arithmetic operations and a decoder to visualize results on a <b>7-segment display</b>.",
        "tech": ["System Verilog", "Digital Design", "Vivado"],
        "link": "https://github.com/HDiana10/ALU-4-bit-with-7-Segment-Display"
    },
    {
        "name": "🌐 Professional Digital Portfolio",
        "description": "A dynamic web application built to showcase my engineering journey. Developed using <b>Streamlit</b> and <b>Python</b>, featuring interactive project filtering, and automated content rendering.",
        "tech": ["Python", "Streamlit", "CSS", "Cloud Deployment"],
        "link": "https://github.com/HDiana10/portofolio_streamlit" # Or your specific repo link
    },
    {
        "name": "🕹️ PCB Runner - MiniGame",
        "description": "An ETTI-themed version of the classic 'Trex Run' built with <b>HTML</b> and <b>JavaScript</b>, deployed via <b>GitHub Pages</b>.",
        "tech": ["JavaScript", "HTML5", "GitHub Pages"],
        "link": "https://hdiana10.github.io/run_pcb_run/"
    },
    {
        "name": "🔋 MINERVA Research Project",
        "description": "Applied research on <b>battery lifespan optimization</b>. Modeled the impact of dynamic operating modes on charge/discharge cycles in <b>CCP</b> systems.",
        "tech": ["Data Modeling", "Research", "Battery Technology"],
        "link": ""
    },
    {
        "name": "🎹 Electronic Piano",
        "description": "A hardware project using <b>Arduino UNO</b> presented at the Student Scientific Communications conference. Built with custom <b>Embedded C</b> logic and analog circuit design.",
        "tech": ["Arduino", "Embedded C", "Circuit Design"],
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
        - Serve as a <b>Technical Assistant</b> within the IT department, providing <b>mentorship</b> and guidance for junior members on technical projects.<br>
        - Contributed to major events: Admission Simulation, General Culture Contest, Polifest, and LanParty.<br>
        - Served as an <b>Official Referee</b> for the international <b>Robochallenge</b> competition.<br>
        - Awarded <b>"Volunteer of the Week"</b> for outstanding commitment and organizational impact.
        """,
        "tech": ["Teamwork", "Time Management", "Technical Support"]
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
        "name": "🥇 Code Quest 2025 - Applied Electronics",
        "organizer": "SIE, CAMPUS",
        "result": "1st Place (Winners)",
        "details": "Engineered a hardware-level <b>Enigma Machine</b> using <b>SystemVerilog</b> within 12 hours. Implemented logic for <b>VGA display</b>, <b>PS/2 keyboard</b> input, and Enigma Machine encoding mechanism.",
        "tech": ["SystemVerilog", "Vivado", "VGA", "UART"]
    },
    {
        "name": "🏆 Electron 2025",
        "organizer": "UPB - Faculty of Electronics, Telecomunications, and Information Technology",
        "result": "7th Place Overall",
        "details": "A 24-hour <b>Capture The Flag (CTF)</b> competition. Solved complex tasks across <b>Electronics</b>, <b>Digital Design</b>, <b>PSpice circuit simulation</b>, Python, and signal processing (audio editing).",
        "tech": ["CTF", "Vivado", "PSpice", "Python", "Adacity"]
    },
    {
        "name": "🛰️ ESA Moon Camp Challenge",
        "organizer": "European Space Agency (ESA)",
        "result": "3rd Place - Pioneers",
        "details": "Designed a sustainable <b>lunar base</b> focusing on habitability and energy.",
        "tech": ["3D Modeling", "Aerospace Design"]
    },
    {
        "name": "🔍 Pia Hunt",
        "organizer": "Student Technical Competition",
        "result": "Honorable Mention",
        "details": "Logic and rapid problem-solving challenge.",
        "tech": ["Logic", "Teamwork"]
    }
]

SCHOOLS: List[Dict] = [
    {
        "name": "🤖 ETTI-AI Summer School",
        "organizer": "DCAE Department",
        "period": "September 2025",
        "details": "Basics of <b>ML/AI</b>: handled data (images, vectors, audio) using <b>Pandas/NumPy</b>. Developed mini-projects in Computer Vision, Speech to Text, Biomedical.",
        "tech": ["Python", "Machine Learning", "Embedded AI"]
    },
    {
        "name": "🔌 Infineon Digital Circuits Summer School",
        "organizer": "Infineon Technologies",
        "period": "7th - 25th July 2025",
        "details": "Professional workshop on <b>digital design flow</b>, hardware description, and <b>verification</b>.",
        "tech": ["Digital Design", "Verification", "System Verilog"]
    },
    {
        "name": "🛰️ ROSPIN-SAT-1 Summer School",
        "organizer": "ROSPIN",
        "period": "June - August 2025",
        "details": "Specialized training in <b>Satellite Data Processing</b> and telemetry handling.",
        "tech": ["Satellite Data", "Signal Processing"]
    },
    {
        "name": "🛡️ Security Summer School, Essentials",
        "organizer": "UPB",
        "period": "22nd June - 27th July 2025",
        "details": "Fundamental concepts of <b>Cybersecurity</b>, network security, and cryptography.",
        "tech": ["Cybersecurity", "Network Security", "Criptography"]
    },
    {
        "name": "EPiC Summer School",
        "organizer": "European Partnership",
        "period": "18th - 20th June 2025",
        "details": "International program on innovative campus technologies.",
        "tech": ["Innovation", "Collaboration"]
    }
]

SCHOOLS: List[Dict] = [
    {
        "name": "🤖 ETTI-AI Summer School",
        "organizer": "UPB - DCAE Department",
        "period": "September 2025",
        "details": "Intensive program on <b>ML/AI fundamentals</b>. Mastered <b>NumPy</b> and <b>Pandas</b> for data manipulation. Developed mini-projects in <b>Computer Vision</b>, Speech-to-Text, and <b>Embedded AI</b>.",
        "tech": ["Python", "Machine Learning", "Embedded AI"]
    },
    {
        "name": "🔌 Infineon Digital Circuits, Design & Verification",
        "organizer": "Infineon Technologies",
        "period": "July 2025",
        "details": "Professional-grade workshop on the <b>digital design flow</b>. Focused on hardware description, <b>verification methodologies</b>, and industry-standard circuit design.",
        "tech": ["Digital Design", "Verification", "VLSI"]
    },
    {
        "name": "🛡️ Security Summer School, Essentials",
        "organizer": "UPB / Cybersecurity Partners",
        "period": "June - July 2025",
        "details": "Deep dive into <b>Cybersecurity fundamentals</b>. Explored network security, cryptography basics, and hardware-level security vulnerabilities.",
        "tech": ["CTF", "Criptography", "Cybersecurity", "Network Security"]
    },
    {
        "name": "🚗 NXP - Eat, Sleep, Code, Repeat",
        "organizer": "NXP Semiconductors",
        "period": "Nov 2025 - Present",
        "details": "Long-term <b>Automotive Embedded Systems</b> program. Developing an integrated car simulation by programming distributed nodes for <b>braking, steering,comfort systems and more.</b>.",
        "tech": ["Embedded C", "Automotive", "Microcontrollers"]
    },
    {
        "name": "🛰️ ROSPIN-SAT-1 Summer School",
        "organizer": "ROSPIN",
        "period": "June - August 2025",
        "details": "Comprehensive school on <b>Satellite Data Processing</b>. Learned to handle telemetry and process complex data streams from space missions.",
        "tech": ["Satellite Data", "Signal Processing"]
    },
    {
        "name": "🇪🇺 EPiC Summer School",
        "organizer": "European Partnership for Innovative Campus",
        "period": "June 2025",
        "details": "International collaboration focused on innovative technologies and cross-disciplinary engineering solutions.",
        "tech": ["Innovation", "International Collaboration"]
    },
    # Keep your previous contests (Electron 2025, ESA, etc.) below...
]

# UTILITIES
def chips(items: List[str]) -> str:
    if isinstance(items, str):
        items = [items]
    return "".join(f'<span class="chip">{st.session_state.get("_emoi_map", {}.get(i.lower(), ""))} {i}</span>' for i in items)

def collect_all_tech() -> List[str]:
    tech = set()
    
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
# SIDEBAR
with st.sidebar:
    # 2. Name and Greeting
    st.title(f"Hi! I'm {PROFILE['name']}")
    st.write("Welcome to my digital portfolio!")

    st.markdown("---")
    
    # 3. Contact Info with Emojis & Links
    st.subheader("📬 Contact Info")
    
    # Email
    st.markdown(f"📧 **Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
    # LinkedIn
    st.markdown(f"🔗 **LinkedIn:** [View Profile]({PROFILE['linkedin']})")
    
    # GitHub
    st.markdown(f"💻 **GitHub:** [View Repos]({PROFILE['github']})")
    
    st.markdown("---")

    # 4. Filters (Keeping your existing logic)
    st.caption("🔍 Project Filters")
    all_tech = collect_all_tech()
    selected = st.multiselect("Filter by tech", options=all_tech, placeholder="e.g. SystemVerilog")
    st.session_state['filters'] = set(selected)

    st.markdown("---")
    
    # 5. Download Resume Button
    # For now, this is a placeholder. To make it work, you'd add: data=open("resume.pdf", "rb")
    st.download_button(
        label="📄 Download My CV",
        data="Your PDF data here",
        file_name="Diana_Hincu_CV.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
# HEADER

left, right = st.columns([1, 3])

with right:
    st.markdown(f"## {PROFILE["name"]}")
    st.write(f"**{PROFILE['role']}**")
    st.caption(f"📍 {PROFILE['location']} | 📧 {PROFILE['email']}")
    st.info(f"💡 {PROFILE['tagline']}")
with left:
    st.image("me.png", width=300, use_container_width=True) 

st.markdown("<hr>", unsafe_allow_html=True)

# TABS

about_tab,  edu_tab, proj_tab, contests_tab, volunteer_tab, skills_tab, = st.tabs(["About", "Education", "Projects", "Contests & SS", "Volunteer", "Skills"])

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
    st.write("Here are some of the projects I have done/ am working on.")

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

with contests_tab:
    # --- 1. CONTESTS SECTION ---
    st.subheader("🏆 Competitive Achievements")
    c_cols = st.columns(2)
    for idx, c in enumerate(CONTESTS):
        # Filter Logic
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(c.get("tech", []))):
            continue
            
        with c_cols[idx % 2]:
            st.markdown(f"""
                <div class='card' style='margin-bottom: 15px; height: auto;'>
                    <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
                        <h5 style='margin:0;'>{c['name']}</h5>
                        <span style='color: #ff4b4b; font-weight: bold; font-size: 0.8rem;'>{c.get('result', '')}</span>
                    </div>
                    <p class='muted' style='margin:4px 0; font-size: 0.8rem;'><i>{c['organizer']}</i></p>
                    <div style='font-size: 0.8rem; margin-top: 8px; line-height: 1.4;'>{c['details']}</div>
                    <div style='margin-top:10px;'>{chips(c.get('tech', []))}</div>
                </div>
            """.replace("\n", ""), unsafe_allow_html=True)

    st.write("---")

    # --- 2. SUMMER SCHOOLS SECTION ---
    st.subheader("☀️ Technical Summer Schools")
    s_cols = st.columns(2)
    for idx, s in enumerate(SCHOOLS):
        # Filter Logic
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(s.get("tech", []))):
            continue
            
        with s_cols[idx % 2]:
            st.markdown(f"""
                <div class='card' style='margin-bottom: 15px; height: auto;'>
                    <h5 style='margin:0;'>{s['name']}</h5>
                    <p style='margin:4px 0; font-size: 0.8rem; font-weight: bold; color: #ff4b4b;'>{s['organizer']}</p>
                    <p class='muted' style='font-size: 0.75rem; margin:0;'>📅 {s['period']}</p>
                    <div style='font-size: 0.8rem; margin-top: 8px; line-height: 1.4;'>{s['details']}</div>
                    <div style='margin-top:10px;'>{chips(s.get('tech', []))}</div>
                </div>
            """.replace("\n", ""), unsafe_allow_html=True)


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
        
with skills_tab:
    st.subheader("🛠️ Technical Proficiency")
    st.write("My technical stack is validated through high-pressure competitions (Code Quest 1st Place) and industry-led programs (NXP, Infineon).")

    # Create two columns for a clean split between Hardware and Software
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🔌 Hardware & Digital Design")
        st.write("- **HDLs:** SystemVerilog")
        st.write("- **Interface Design:** VGA Controller, UART/Serial, PS/2 Keyboard Protocols")
        st.write("- **EDA Tools:** Vivado (Synthesis & Implementation), PSpice, Orcad")
        st.write("- **Core Concepts:** Digital Integrated Circuits, Circuit Analysis, RTL Design")
        
    with col2:
        st.markdown("#### 💻 Software & AI")
        st.write("- **Programming:** Python, C/C++, JavaScript, Assembly (AMP)")
        st.write("- **AI/ML:** Computer Vision, NumPy, Pandas (Data maneuvering for Images/Audio)")
        st.write("- **Embedded Systems:** Automotive Node Programming (NXP), Microcontrollers (Arduino/ESP32)")
        st.write("- **Tools & DevOps:** Git, Streamlit, WordPress, Linux basics")

    st.markdown("---")
    
    # Professional & Soft Skills Section
    st.subheader("🌟 Professional & Leadership")
    
    # We use st.info and st.success to make these high-impact accomplishments stand out
    st.success("""
    **🏆 Project Execution & Leadership:** Proven ability to lead and execute complex technical projects under extreme time constraints, evidenced by a **1st Place win at Code Quest 2025**.
    """)
    
    st.info("""
    **🤝 Technical Mentorship:** Active mentor within the **LSE IT Department**, facilitating the onboarding of junior members and providing guidance on codebase structure and hardware prototyping.
    """)