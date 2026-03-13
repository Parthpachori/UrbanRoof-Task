import fitz  # PyMuPDF
import os
import json
import io
from PIL import Image

def extract_pdf_data(pdf_path, output_dir, image_dir):
    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    extracted_data = {
        "filename": base_name,
        "pages": []
    }
    
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for page_index in range(len(doc)):
        page = doc[page_index]
        text = page.get_text()
        
        page_info = {
            "page_number": page_index + 1,
            "text": text,
            "images": []
        }
        
        # Extract images from page
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            image_filename = f"{base_name}_p{page_index+1}_img{img_index+1}.{image_ext}"
            image_path = os.path.join(image_dir, image_filename)
            
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            
            page_info["images"].append({
                "filename": image_filename,
                "path": os.path.abspath(image_path)
            })
            
        extracted_data["pages"].append(page_info)
    
    output_json = os.path.join(output_dir, f"{base_name}.json")
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4)
    
    print(f"Extracted data for {base_name} saved to {output_json}")
    return extracted_data

if __name__ == "__main__":
    raw_dir = r"d:\UrbanRoof\data\raw"
    extracted_dir = r"d:\UrbanRoof\data\extracted"
    
    pdfs = ["Sample Report.pdf", "Thermal Images.pdf", "Main DDR.pdf"]
    
    for pdf in pdfs:
        path = os.path.join(raw_dir, pdf)
        if os.path.exists(path):
            extract_pdf_data(path, extracted_dir, os.path.join(extracted_dir, "images"))
        else:
            print(f"File not found: {path}")
