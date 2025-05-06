# Write the CV content to a Markdown file in order to import it into My Notion.

cv_content = """
# 📄 Dinh Nguyen
*Computer Applications Student | Website Content Assistant | Admin & Support Specialist*
📍 Hämeenlinna, Finland | 📧 dinh23000@student.hamk.fi | 🔗 [LinkedIn] | 💻 [GitHub]

---

## 🎯 Career Objective
Motivated and detail-oriented **Computer Applications (BIT)** student at HAMK, seeking an **internship or entry-level opportunity** in **website content updates and digital maintenance**. Combining strong customer service and admin experience with CMS tools and analytics knowledge, I aim to contribute effectively while advancing my skills in the IT industry.

---

## 🛠️ Key Skills
- Content Management Systems (CMS)
- Website Updates & Maintenance
- HTML/CSS Fundamentals
- Image & Video Editing: Photoshop, Filmora
- Microsoft Office Suite: Excel, Word, PowerPoint
- Customer Support Tools: Salesforce, Slack, VoIP
- Team Collaboration & Training Support
- Documentation & Scheduling

---

## 🎓 Education

**HAMK University of Applied Sciences – Finland**
*BA in Computer Applications (BIT), 2023 – 2026*

**HCMC University of Foreign Languages – IT, Vietnam**  
*BA in English – Business Administration, 2003 – 2007*

---

## 📜 Certifications & Achievements

- **Google Analytics – Skillshop**
   ▫ Get Started Using Google Analytics
   ▫ Manage GA4 Data and Read Reports

- **Scrum Fundamentals Test – Score: 86.7%**
   ▫ Verified by Scrum Institute

- **3rd Place – Dilli Project**
   ▫ Contributor for "Road to Vostok" game development assets

- **HackTheBox Academy**
   ▫ Self-learning in web security, account active

---

## 💼 Professional Experience

### **Admin Assistant**  
**Thanh Truc Shipping Petrol & Oil Co., Ltd.** | *Oct 2022 – Present*  
- Coordinate schedules, emails, and task priorities for director  
- Prepare reports, documents, and manage both digital and physical records  
- Assist in internal meetings and administrative task streamlining  
*→ Relevant to document workflows and structured content updates*

---

### **Customer Support Executive – Traveloka Project**  
**Transcosmos Vietnam** | *Mar 2022 – Sep 2022*  
- Supported customers through chat/email for hotel booking issues  
- Troubleshooted issues based on standard operating procedures  
- Tools used: Salesforce, VoIP, Slack  

---

### **Senior Reservations Agent**  
**InterContinental Phu Quoc Resort (IHG)** | *Apr 2018 – May 2021*  
- Managed multi-channel booking and special guest requests  
- Assisted training refreshers and team quality observations  
- Tools: Opera PMS, IHG Concerto, Outlook  

---

### **Account Executive – Web Services**  
**SGP Vietnam** | *Oct 2011 – Sep 2017*  
- Managed web content projects for SMEs  
- Collaborated via CMS and freelance platforms (Fiverr)  
- Tools: CMS, Photoshop, GoAnimate, Filmora  

---

### **Sales Admin**  
**Tan Long Phat Exim Co., Ltd.** | *Apr 2008 – Sep 2011*  
- Supported technical sales operations and client communications  
- Created reports, planned team activities  

---

## 🌐 Languages  
- Vietnamese – Native  
- English – Intermediate (Written & Business Communication)

---

## 🤝 Volunteering  

- **Green Summer Campaign – 2005**  
   ▫ Promoted public health & education in rural Vietnam  

- **HUFLIT Volunteer Community (HVC)** | *2005–2007*  

---

## 🔗 Tech & Tools  
CMS | HTML | Photoshop | Filmora | Google Analytics GA4  
Salesforce | Slack | VoIP | Outlook | Excel | Notion  
"""

# Save to markdown file
markdown_path = "/mnt/data/DinhNguyen_CV_Notion.md"
with open(markdown_path, "w", encoding="utf-8") as f:
    f.write(cv_content)

markdown_path
