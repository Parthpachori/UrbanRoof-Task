# Project Revision: AI-Driven DDR Generation Workflow

## 1. What I Built
I built an end-to-end automated workflow for generating technical **Detailed Diagnostic Reports (DDR)** for building inspections. The system processes raw technical data (inspection observations and thermal imaging) from complex PDF documents and synthesizes it into a professional, client-ready diagnostic report. The final output includes area-wise observations, cross-referenced thermal data, root cause analysis, severity assessments, and recommended actions.

## 2. How It Works
The system follows a three-stage pipeline:
- **Data Extraction Phase**: Utilizing the `PyMuPDF` library, the system parses raw text and images from multiple source PDFs (`Sample Report.pdf`, `Thermal Images.pdf`, and `Main DDR.pdf`). It maintains context by organizing extracted assets by document and page number.
- **Data Synthesis Phase**: The system analyzes the extracted text to identify key property issues (e.g., dampness, seepage, structural cracks). It cross-references these findings with the `Thermal Report` to correlate visual dampness with temperature anomalies (hotspots/coldspots).
- **Structured Generation**: An automated generation engine maps the synthesized findings into a structured Markdown template. It logically groups observations by location, avoids duplication of points across sources, and ensures that missing details are explicitly flagged as "Not Available" rather than being ignored.

## 3. Limitations
- **Structure Dependency**: The extraction logic is currently optimized for the specific layouts of the provided sample reports. Radical changes in PDF formatting could impact extraction accuracy.
- **Simulated Reasoning**: While the system performs logical correlation (e.g., matching a "Hall" observation with "Hall" thermal data), it uses pattern-matching for diagnostics. It lacks the deep structural engineering "intuition" that a human auditor or a more advanced Vision-LLM might possess.
- **Image Correlation**: Images are currently mapped to sections based on page-level extraction. In extremely long or disorganized reports, this proximity-based correlation could lead to minor misalignments.
- **OCR Limitations**: The current system assumes extractable text. It does not yet have an OCR (Optical Character Recognition) layer to process scanned documents or images containing text.

## 4. Future Improvements
- **Vision-Language Model (VLM) Integration**: Integrate models like **Gemini 1.5 Pro** or **GPT-4o** to perform direct visual analysis of inspection photos. This would allow the AI to "see" the severity of a crack and verify it matches the written description.
- **Advanced OCR Layer**: Implement a robust OCR engine (like AWS Textract or Google Cloud Vision) to handle scanned reports and ensure no data is missed due to PDF formatting.
- **Multi-Agent Architecture**: Transition to a multi-agent system (using LangGraph) where specialized agents (e.g., an "Extraction Agent", a "Thermal Auditor", and a "Report Architect") collaborate to validate findings and cross-check facts.
- **Interactive Review UI**: Develop a web-based dashboard where human auditors can review the AI-generated DDR, adjust severity levels, or swap images via a simple drag-and-drop interface before final exports.
- **Direct PDF Export**: Add a conversion layer to export the final Markdown report into a high-fidelity PDF/Docx format with custom company branding and dynamic tables.
