# a script to create a new lesson notebook, populate header, etc.
import json
import os
from nbformat import v4

# Read the syllabus.json file
with open('resources/syllabus.json', 'r') as f:
    syllabus = json.load(f)

# Extract course info
course_info = syllabus['course_info']

# Loop through lessons
for lesson in syllabus['lessons']:
    week_number = lesson['week_number']
    
    # Create directory if it doesn't exist
    dir_path = f'lessons/Wk{week_number}'
    os.makedirs(dir_path, exist_ok=True)
    
    # Check for existing files and avoid overwriting
    file_index = 1
    file_name = f'L{week_number}{lesson["lesson_number"]:01d}.ipynb'
    while os.path.exists(os.path.join(dir_path, file_name)):
        file_name = f'L{week_number}{lesson["lesson_number"]:01d}_{file_index}.ipynb'
        file_index += 1

    # Generate Markdown text for the header
    header_md = """\
#### {} - {} - {}
## Week {}-{}: {}  
### Objectives
""".format(course_info['course_name'], course_info['instructor'], course_info['quarter'], week_number, lesson['lesson_number'], lesson['lesson_name'])

    header_md += "".join([f"{i+1}. *{obj}*\n" for i, obj in enumerate(lesson['objectives'])])

    header_md += """
### Key Concepts
- **"""

    header_md += "".join([f"{concept}**\n- **" for concept in lesson['key_concepts']])[:-4]

    header_md += """
### Key Equations
"""

    header_md += "".join([f"{eq}\n" for eq in lesson['key_equations']])

    # Create a new Jupyter Notebook with the header
    notebook = v4.new_notebook()
    notebook.cells.append(v4.new_markdown_cell(header_md.strip()))
    
    # Save the notebook
    with open(os.path.join(dir_path, file_name), 'w') as f:
        f.write(v4.writes(notebook))

print("Lesson notebooks generated successfully!")
