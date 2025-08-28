from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# File path for polished version
file_path_visual = "David-Ashby_Security-Automation_Resume_Visual.pdf"

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="HeaderVisual", fontSize=14, leading=16, alignment=1, textColor=colors.HexColor("#1a1a1a"), spaceAfter=8))
styles.add(ParagraphStyle(name="SubHeaderVisual", fontSize=10, leading=12, alignment=1, textColor=colors.HexColor("#444444"), spaceAfter=12))
styles.add(ParagraphStyle(name="SectionHeaderVisual", fontSize=11, leading=13, spaceAfter=6, spaceBefore=10, textColor=colors.HexColor("#003366"), underlineWidth=0.5, underlineOffset=-2))
styles.add(ParagraphStyle(name="BodyVisual", fontSize=9.5, leading=12, textColor=colors.HexColor("#222222")))
styles.add(ParagraphStyle(name="BulletVisual", fontSize=9.5, leading=12, leftIndent=14, bulletIndent=6, textColor=colors.HexColor("#222222")))

doc = SimpleDocTemplate(file_path_visual, pagesize=letter,
                        rightMargin=40, leftMargin=40,
                        topMargin=28, bottomMargin=28)

story = []

# Header with name
story.append(Paragraph("David Ashby", styles["HeaderVisual"]))
story.append(Paragraph("Security Automation | Red Team Engineering", styles["SubHeaderVisual"]))
contact_info = "Helena, MT | 801-857-9474 | da@vidashby.com<br/>GitHub: github.com/Cfomodz | LinkedIn: linkedin.com/in/david-ashby | Skool: skool.com/@david-ashby-7018"
story.append(Paragraph(contact_info, styles["BodyVisual"]))
story.append(Spacer(1, 5))

# Professional Summary
summary = """Security automation engineer focused on enabling red team workflows through reliable web automation, AI-assisted code analysis, and secure pipeline design. Reduced issue backlogs by ~50% with automated triage, built reusable auth and session-handling patterns used across contributors, and hardened sandboxed evaluation environments. Proficient with Python, Playwright/Selenium, Burp Suite, OWASP ZAP, Kali, Wireshark, GitHub Actions, and Docker."""
story.append(Paragraph("Professional Summary", styles["SectionHeaderVisual"]))
story.append(Paragraph(summary, styles["BodyVisual"]))

# Security Highlights
highlights = [
    "Analyzed AI-generated code to surface vulnerabilities and regulatory risks; hardened pipelines for integrity and repeatability (METR).",
    "Cut GitHub backlog ~50% with automation; designed reusable auth/session patterns; manage a 20k+ OSS community (Browser Use).",
    "Built high-scale personalized outreach systems with deliverability, compliance, and security safeguards (Hughes Real Estate Group)."
]
story.append(Paragraph("Security Highlights", styles["SectionHeaderVisual"]))
for h in highlights:
    story.append(Paragraph("• " + h, styles["BulletVisual"]))

# Experience
experience = [
    ("n8n — AI Automation Workflow Creator | Mar 2025–Present", [
        "Built automations saving 10k+ manual hours.",
        "Teach 250+ students via Automation Lab.",
        "Featured #1 on n8n Creators page (n8n.io/creators).",
        "Maintain free OSS workflows: github.com/Cfomodz/community-use."
    ]),
    ("Browser Use (OSS) — Web Automation Engineer & Maintainer | Feb 2025–Present", [
        "Cut GitHub backlog ~50% with automated triage, CI checks, and contributor playbooks.",
        "Designed reusable web automation patterns (auth, pagination, human-in-the-loop).",
        "Manage 20k+ developer Discord: link.browser-use.com/discord.",
        "Core repo: github.com/browser-use/browser-use."
    ]),
    ("Open Source Development — Developer | Apr 2024–Aug 2025", [
        "Chrome WebSocket proxy for controlled browser/OBS integrations.",
        "Object-scanning frontend for structured capture/pipeline ingestion.",
        "Brokerage library for Charles Schwab API with dry-run and safety checks."
    ]),
    ("METR (Model Evaluation & Threat Research) — AI Differential Programmer | Dec 2024–Jan 2025", [
        "Analyzed AI-authored code for vulnerabilities; mapped findings to regulatory risks.",
        "Hardened pipelines (sandboxing, dependency pinning, integrity checks)."
    ]),
    ("Hughes Real Estate Group — Software Developer | Mar 2023–Apr 2024", [
        "Built SMS outreach system sending hundreds of thousands of personalized listings with deliverability, opt-out, and security safeguards.",
        "Automated internal workflows; maintained backend services."
    ]),
    ("Hughes Real Estate Group — IT Support Specialist | Jan 2021–Mar 2023", [
        "Resolved technical issues; maintained Linux servers; generated actionable reports."
    ]),
]

story.append(Paragraph("Experience", styles["SectionHeaderVisual"]))
for role, bullets in experience:
    story.append(Paragraph(f"<b>{role}</b>", styles["BodyVisual"]))
    for b in bullets:
        story.append(Paragraph("• " + b, styles["BulletVisual"]))

# Skills
skills = """<b>Security:</b> Burp Suite, OWASP ZAP, Kali, Wireshark, John the Ripper, Maltego<br/>
<b>Programming:</b> Python, Java, PHP, SQL, HTML/CSS, JavaScript<br/>
<b>Automation/Agents:</b> n8n, Browser Use, Playwright, Selenium<br/>
<b>DevOps/SDLC:</b> Git, GitHub, GitHub Actions, Docker, static/dynamic analysis<br/>
<b>Platforms:</b> Linux"""
story.append(Paragraph("Skills", styles["SectionHeaderVisual"]))
story.append(Paragraph(skills, styles["BodyVisual"]))

# Certifications & Education
certs = """CompTIA Security+, 2024<br/>
TestOut PC Pro, 2020"""
edu = """Certificate in Computer Programming, BYU-Idaho, 2020"""

story.append(Paragraph("Certifications", styles["SectionHeaderVisual"]))
story.append(Paragraph(certs, styles["BodyVisual"]))
story.append(Paragraph("Education", styles["SectionHeaderVisual"]))
story.append(Paragraph(edu, styles["BodyVisual"]))

doc.build(story)

