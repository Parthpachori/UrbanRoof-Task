# UrbanRoof - AI DDR Generation Workflow

This project is an AI-driven workflow that converts technical site inspection reports and thermal imaging data into a client-ready **Detailed Diagnostic Report (DDR)**.

## Project Structure
- `data/raw/`: Contains the input PDF documents.
- `data/extracted/`: Contains extracted text (JSON) and images correlated to specific pages.
- `scripts/`: Python scripts for data extraction and report generation.
  - `extract_pdf.py`: Uses PyMuPDF to parse data from PDFs.
  - `generate_ddr.py`: Synthesizes data and generates the final report.
- `output/`: The final generated DDR reports in Markdown format.

## Key Features
- **Automated Data Extraction**: Extracts structured data and images from complex technical PDFs.
- **Thermal Correlation**: Maps thermal readings (hotspots/coldspots) to visual observations.
- **Logical Synthesis**: Differentiates between internal (plumbing) and external (structural) issues.
- **Severity Assessment**: Evaluates the urgency of repairs based on findings.

## How to Run
1. Install dependencies:
   ```bash
   pip install pymupdf
   ```
2. Run extraction:
   ```bash
   python scripts/extract_pdf.py
   ```
3. Generate report:
   ```bash
   python scripts/generate_ddr.py
   ```
