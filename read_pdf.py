from langchain_core.tools import tool
import io
import PyPDF2
import requests

@tool
def read_pdf(url:str)->str:  
    """ Read and extract text from a PDF file given its URL.
    Args:
        url: The URL of the pdf file to read
        
    Returns:
    THe extracted text content from the pdf file.
    """

    try:
        #access pdf via url
        response=requests.get(url)
        #convert to bytes and read the pdf content
        pdf_file=io.BytesIO(response.content)

        pdf_reader=PyPDF2.PdfReader(pdf_file)
        num_pages=len(pdf_reader.pages)
        text=""
        for i,page in enumerate(pdf_reader.pages,1):
            print(f"Extracting text from page{i}/{num_pages}")
            text+=page.extract_text() +"\n"

        print(f"Extracted successfully {len(text)}characters of text  from the pdf ")
        return text.strip()
    except Exception as e:
        print(f"Error reading pdf:{str(e)}")
        raise ValueError(f"Failed to read pdf from url:{url}\nError:{str(e)}")
    
# url="https://arxiv.org/pdf/2306.14881.pdf"
# result=read_pdf.invoke(url)
# print(result)
