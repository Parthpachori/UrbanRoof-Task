import json
import os

def summarize_extracted_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"Summary for {data['filename']}:")
    print(f"Total Pages: {len(data['pages'])}")
    
    all_text = ""
    for page in data['pages']:
        all_text += f"\n--- Page {page['page_number']} ---\n"
        all_text += page['text']
        print(f"Page {page['page_number']}: {len(page['text'])} chars, {len(page['images'])} images")
    
    return all_text

if __name__ == "__main__":
    extracted_dir = r"d:\UrbanRoof\data\extracted"
    
    sample_text = summarize_extracted_data(os.path.join(extracted_dir, "Sample Report.json"))
    thermal_text = summarize_extracted_data(os.path.join(extracted_dir, "Thermal Images.json"))
    main_ddr_text = summarize_extracted_data(os.path.join(extracted_dir, "Main DDR.json"))
    
    # Save text summaries for LLM review
    with open(os.path.join(extracted_dir, "sample_report_text.txt"), "w", encoding="utf-8") as f:
        f.write(sample_text)
    with open(os.path.join(extracted_dir, "thermal_report_text.txt"), "w", encoding="utf-8") as f:
        f.write(thermal_text)
    with open(os.path.join(extracted_dir, "main_ddr_text.txt"), "w", encoding="utf-8") as f:
        f.write(main_ddr_text)
