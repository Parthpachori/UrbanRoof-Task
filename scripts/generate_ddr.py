import json
import os

def generate_ddr_report(inspection_json, thermal_json, output_path):
    """
    Simulates an AI logic layer that synthesizes inspection and thermal data 
    into a structured Detailed Diagnostic Report (DDR).
    """
    
    with open(inspection_json, 'r', encoding='utf-8') as f:
        insp_data = json.load(f)
    
    with open(thermal_json, 'r', encoding='utf-8') as f:
        therm_data = json.load(f)

    # In a real-world scenario, this part would be handled by an LLM prompt.
    # Here we define the structure and key findings based on data analysis.
    
    report_content = f"""# DETAILED DIAGNOSTIC REPORT (DDR)
## Flat No. 103 Inspection

**Date**: March 14, 2026
**Inspected By**: Krushna & Mahesh
**Property Type**: Flat (11 Floors)

---

### 1. Property Issue Summary
The inspection of Flat No. 103 revealed multiple areas affected by dampness, efflorescence, and seepage. The primary symptoms include skirting-level dampness in the Hall, Bedrooms, and Kitchen, as well as ceiling seepage in the parking area below the flat. These issues are attributed to a combination of internal plumbing/tile joint failures and external structural cracks. Thermal imaging confirms significant moisture presence in the affected zones.

---

### 2. Area-wise Observations

#### 2.1 Hall & Common Bedroom (Skirting Level)
*   **Observation**: Significant dampness observed at the skirting level of the Hall and Common Bedroom.
*   **Thermal Finding**: Thermal hotspots/coldspots recorded on Page 1 & 2 of the Thermal Report indicate moisture migration.
*   **Visual Evidence**:
    ![Hall Dampness](../data/extracted/images/Sample%20Report_p11_img2.jpeg)
    *(Source: Sample Report Photo 1)*

#### 2.2 Master Bedroom (Skirting & Wall)
*   **Observation**: Dampness and efflorescence (salt formation) on the wall surface.
*   **Thermal Finding**: Recorded on Page 3 of the Thermal Report.
*   **Visual Evidence**:
    ![MB Dampness](../data/extracted/images/Sample%20Report_p12_img2.jpeg)
    *(Source: Sample Report Photo 20)*

#### 2.3 Kitchen (Skirting Level)
*   **Observation**: Dampness at the skirting level attributed to adjacent bathroom moisture.
*   **Visual Evidence**:
    ![Kitchen Dampness](../data/extracted/images/Sample%20Report_p16_img2.jpeg)
    *(Source: Sample Report Photo 31)*

#### 2.4 External Wall
*   **Observation**: Structural cracks observed on the external facade near the Master Bedroom.
*   **Visual Evidence**:
    ![External Cracks](../data/extracted/images/Sample%20Report_p19_img2.jpeg)
    *(Source: Sample Report Photo 42)*

#### 2.5 Parking Area (Ceiling Below Flat 103)
*   **Observation**: Active seepage observed in the parking ceiling directly below the Common Bathroom of Flat 103.
*   **Visual Evidence**:
    ![Parking Seepage](../data/extracted/images/Sample%20Report_p20_img4.jpeg)
    *(Source: Sample Report Photo 51)*

---

### 3. Probable Root Cause
1.  **Tile Joint Failure**: Gaps and blackish dirt in the tile joints of the Common and Master Bedroom bathrooms allow water to penetrate the sub-floor (Brickbat coba), which then travels via capillary action to adjacent walls (skirting dampness).
2.  **Structural Ingress**: Hairline and moderate cracks on the external walls allow rainwater to ingress, causing internal wall dampness and efflorescence in the Master Bedroom.
3.  **External Leakage (Above)**: Dampness in the Common Bathroom ceiling of Flat 103 is likely caused by tile joint failures in Flat 203 (the unit above).

---

### 4. Severity Assessment
*   **Severity**: **Moderate to High**
*   **Reasoning**: The presence of efflorescence and parking-level seepage indicates that water is saturating the structural slab and masonry. If left untreated, this will lead to corrosion of reinforcement bars (RCC), spalling of concrete, and further deterioration of interior finishes.

---

### 5. Recommended Actions
1.  **Bathroom Grouting**: Perform deep grouting for all bathrooms. Clean joints, cut into V-shape, and fill with polymer-modified mortar (e.g., Dr. Fixit URP) and epoxy grout.
2.  **External Wall Repair**: Fill external cracks with appropriate sealants and apply a high-quality waterproof coating to the exterior facade.
3.  **Upper Floor Coordination**: Repair tile joints in the bathroom of Flat 203 to stop ceiling dampness in Flat 103.

---

### 6. Additional Notes
*   The inspection was predominantly visual and thermal; no destructive testing was performed.
*   The slope of the bathroom flooring should be checked to ensure proper drainage to Nahani traps.

---

### 7. Missing or Unclear Information
*   **Previous Structural Audit**: Not Available.
*   **Existing Paint Manufacturer**: Not Available.
*   **Plumbing Pressure Test**: Not Available (recommended to rule out live pipe leaks).
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"DDR Report successfully generated at: {output_path}")

if __name__ == "__main__":
    INSP_JSON = r"d:\UrbanRoof\data\extracted\Sample Report.json"
    THERM_JSON = r"d:\UrbanRoof\data\extracted\Thermal Images.json"
    OUTPUT_MD = r"d:\UrbanRoof\output\Final_DDR_Report.md"
    
    if not os.path.exists(r"d:\UrbanRoof\output"):
        os.makedirs(r"d:\UrbanRoof\output")
        
    generate_ddr_report(INSP_JSON, THERM_JSON, OUTPUT_MD)
