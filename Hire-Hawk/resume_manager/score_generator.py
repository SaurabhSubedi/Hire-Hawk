import PyPDF2
from self_cosine_sim import my_cosine_similarity

a = PyPDF2.PdfReader("E:\CV\Saurabh Resume(data analysis).pdf")
total_pages = len(a.pages)
resume_text = ""
for page_num in range(total_pages):
    page = a.pages[page_num]
    text = page.extract_text()
    resume_text += text

job_descritpion = ''' Bachelor’s/Master’s degree in Engineering, Computer Science (or equivalent experience)
At least 3+ years of relevant experience as a data analyst
Demonstrable experience working with Power BI 
Extensive knowledge and experience with SQL, Python, MS Excel, and MS PowerPoint
Data Management related certification is desirable
Nice to have Agile certification such as Scrum Master or Product Owner
Comprehensive understanding of Finance concepts and the broker industry is desirable
Prior experience taking ownership and driving workshops to elicit requirements
Strong action-oriented and proactive tendencies 
Foundational knowledge of data management topics
Some expertise in developing and implementing cross-border/global requirements and procedures
Excellent data quality and metadata management skills
Fluent in conversational and written English communication '''

result = my_cosine_similarity(resume_text,job_descritpion)
print(result)



