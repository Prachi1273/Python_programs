from graph_engine import compliance_pipeline

# Realistic high-risk media sample to test our complete pipeline logic
sample_adverse_media = """ 
PUNE TECH REPORT — Investigators uncovered an extensive accounting discrepancy 
inside Mumbai-based logistics giant 'Apex Shipping Corp' earlier this morning. 
An independent internal audit revealed that high-level executives systematically 
fabricated shipping invoices between 2024 and 2025, overstating overall revenue 
by roughly 42 Crore Rupees. The company's chief financial officer resigned immediately 
following the discovery, and legal compliance experts warn that international regulatory 
sanctions and massive financial fines are highly likely to follow within the upcoming weeks.
""" 

def start_enterprise_run():
    print("============= STARTING COMPLIANCE GRAPH PIPELINE =============")
    
    # Initialize initial state inputs
    initial_state = {
        "raw_text": sample_adverse_media,
        "extracted_data": None,
        "error_message": None,
        "iterations": 0
    }
    
    # Stream individual graph state transitions to console
    compliance_pipeline.invoke(initial_state)
    print("\n============= GRAPH EXECUTION COMPLETED SUCCESSFULLY =============")

if __name__ == "__main__":
    start_enterprise_run()
