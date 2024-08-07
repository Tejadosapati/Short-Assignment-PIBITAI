import json

def parse_resume(resume_text):
    resume_data = {
        "Name": "",
        "Contact Information": {
            "Email": "",
            "Phone": "",
            "Address": ""
        },
        "Education": "",
        "Experience": [],
        "Skills": [],
        "Projects": [],
        "Training Program": [],
        "Certificates": [],
        "Achievements": []
    }

    lines = resume_text.split('\n')

    # Extracting name and contact information
    resume_data["Name"] = lines[0].strip()
    for line in lines:
        if "Email:" in line:
            resume_data["Contact Information"]["Email"] = line.split("Email:")[1].strip()
        if "Mobile:" in line:
            resume_data["Contact Information"]["Phone"] = line.split("Mobile:")[1].strip()

    # Extracting skills
    skills_index = lines.index("SKILLS") + 1
    while skills_index < len(lines) and not lines[skills_index].startswith("PROJECTS"):
        resume_data["Skills"].append(lines[skills_index].strip())
        skills_index += 1

    # Extracting projects
    projects_index = lines.index("PROJECTS") + 1
    while projects_index < len(lines) and not lines[projects_index].startswith("TRAINING PROGRAM"):
        resume_data["Projects"].append(lines[projects_index].strip())
        projects_index += 1

    # Extracting training programs
    training_index = lines.index("TRAINING PROGRAM") + 1
    while training_index < len(lines) and not lines[training_index].startswith("CERTIFICATES"):
        resume_data["Training Program"].append(lines[training_index].strip())
        training_index += 1

    # Extracting certificates
    certificates_index = lines.index("CERTIFICATES") + 1
    while certificates_index < len(lines) and not lines[certificates_index].startswith("ACHIEVEMENTS"):
        resume_data["Certificates"].append(lines[certificates_index].strip())
        certificates_index += 1

    # Extracting achievements
    achievements_index = lines.index("ACHIEVEMENTS") + 1
    while achievements_index < len(lines) and not lines[achievements_index].startswith("EDUCATION"):
        resume_data["Achievements"].append(lines[achievements_index].strip())
        achievements_index += 1

    # Extracting education
    education_index = lines.index("EDUCATION") + 1
    while education_index < len(lines):
        resume_data["Education"] += lines[education_index].strip() + " "
        education_index += 1
    resume_data["Education"] = resume_data["Education"].strip()

    return json.dumps(resume_data, indent=4)

resume_text = """
Dosapati Teja
Linkedin: Dosapati-teja Email: tejadosapati012@gmail.com
Github: Tejadosapati Mobile: 7893678947

SKILLS
• Languages: C++, JavaScript, Java, Python
• Frameworks: HTML and CSS
• Tools/Platforms: MySQL, Excel, Tableau
• Soft Skills: Problem-Solving Skills, Team Player, Project Management, Adaptability

PROJECTS
• Netflix Dashboard – Data Visualization (Tableau) Apr’24
• Utilized the Netflix Titles dataset, which includes information on over 7,000 titles such as movies, TV shows, release year, genre, country, and cast.
• Developed charts to showcase the popularity of different genres and their evolution over time.
• Mapped content availability across different countries, revealing regions with the most diverse selections.
Tech: Tableau

• World Clock: Apr’23
• Designed and developed an interactive Java Swing application to display real-time time zones for various regions based on mouse hover events over a world map.
• Utilized java.time API to fetch and display current local time for specified global regions, enhancing application relevance for an international audience.
Tech: Java GUI

• RS Fitness Studio – Web Application Mar’22
• Developed a comprehensive and visually appealing fitness studio interface using HTML and CSS. The project aimed to provide an engaging user experience for visitors looking to learn more about the fitness studio's offerings, register for programs.
• Developed a welcoming homepage with a clear and attractive title, "RS FITNESS STUDIO," and a slogan, "Fitness Edge."
Tech: HTML, CSS

TRAINING PROGRAM
Summer Training – Programming Pathshala July ‘23
• Programming Pathshala
◦ About: Developed a text-based captcha using python programming. Imported necessary modules: random for generating random choices, and string for accessing uppercase letters and digits. Generated a random CAPTCHA string using random.choices(), combining uppercase letters and digits, and forming a string of length 6. Verified the user's input by comparing it with the generated CAPTCHA and provided feedback through a conditional statement, informing whether the verification succeeded or failed.
Tech stacks used: Python, Library - Tkinter

CERTIFICATES
• Python certification provided by Kaggle Oct’23
• Data Structures and Algorithms – by Udemy Sept’23

ACHIEVEMENTS
• Secured EXP 8711 in coding ninjas: Jan ‘24
Achieved 15+ Badges of Achiever and Specialist badges in DSA, Coding Ninjas
• Hackerrank Mar’24
Achieved 4-star proficiency rating in java hackerrank, showcasing strong skills in programming and problem solving.

EDUCATION
Lovely Professional University Jalandhar, India
• Bachelor of Technology - Computer Science and Engineering; CGPA: 7.96 Since Aug 2021
• Sri Gayatri Educational Institutes Vijayawada, Andhra Pradesh
Intermediate; Percentage: 94.1% 2019 - 2021

Ravindra Bharathi Public School Nuzvid , Andhra Pradesh
• Matriculation; Percentage: 95.5% 2018 - 2019
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
