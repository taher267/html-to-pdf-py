from flask import Flask
import asyncio
from pyppeteer import launch
from .html_content import content
app=Flask(__name__)
# ////////////////////////////////////////////

async def generate_pdf_from_html(html_content, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.setContent(html_content)
    
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    
    await browser.close()

# HTML content


# Run the function
asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(content(), 'from_html.pdf'))



# //////////////////////////////////////











@app.route("/")
def home():
    return "Bismillah"

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()