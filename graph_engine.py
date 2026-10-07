import sys
from typing import Dict, TypedDict, Literal, Optional  # Added Optional here!
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from schema import RiskEntity
from database import save_risk_to_database


# 1. Define our Shared Graph Memory State
class PipelineState(TypedDict):
    raw_text: str
    extracted_data: Optional[RiskEntity]
    error_message: Optional[str]
    iterations: int

# 2. Initialize our Local Core Reasoning Layer
llm = ChatOllama(model="llama3.1", temperature=0.0)
structured_extractor = llm.with_structured_output(RiskEntity)

# Node 1: The Extraction Process Engine
def extraction_node(state: PipelineState) -> Dict:
    print("\n[Node 1] 🧠 Running Semantic Extraction Engine...")
    current_iterations = state.get("iterations", 0) + 1
    
    prompt = state["raw_text"]
    # If a previous run failed validation, inject the error as a correction context
    if state.get("error_message"):
        prompt += f"\n\nCRITICAL FIX REQUIRED FROM PREVIOUS ATTEMPT:\n{state['error_message']}\nRe-parse carefully."
        
    try:
        report = structured_extractor.invoke(prompt)
        return {"extracted_data": report, "error_message": None, "iterations": current_iterations}
    except Exception as e:
        return {"error_message": str(e), "iterations": current_iterations}

# Node 2: The Hallucination & Data Integrity Guard
def audit_node(state: PipelineState) -> Dict:
    print("[Node 2] 🔍 Running Data Integrity Audit...")
    report = state["extracted_data"]
    
    # Validation Rule: Verification firms require precise citation strings
    if not report.source_citations or len(report.source_citations) == 0:
        return {"error_message": "Validation Failed: 'source_citations' cannot be empty. Extracted data must be grounded in text."}
        
    # Validation Rule: Prevent arbitrary out-of-bounds score slips
    if report.severity_score < 1 or report.severity_score > 10:
        return {"error_message": "Validation Failed: 'severity_score' falls outside strict 1-10 taxonomic bounds."}
        
    print("✅ Audit Node Verification Passed.")
    return {"error_message": None}

# Node 3: The Human-in-the-Loop Approval Gate
def human_gate_node(state: PipelineState) -> Dict:
    report = state["extracted_data"]
    print(f"\n🚨 [CRITICAL ALERT] High-Risk Severity Flag Detected: {report.severity_score}/10")
    print(f"Target Entity: {report.entity_name}")
    print(f"Verdict Summary: {report.verdict_summary}")
    print("-" * 60)
    
    # Interactive CLI checkpoint mimicking a background screener's verification interface
    user_input = input("REVIEWER INTERVENTION REQUIRED. Approve record entry? (yes/no): ").strip().lower()
    
    if user_input != "yes":
        print("❌ Entry rejected by Compliance Analyst. Terminating pipeline.")
        sys.exit("\nPipeline execution halted by human supervisor.")
        
    print("🔓 Reviewer cleared entry. Synchronizing with state machine...")
    return {}

# Node 4: The Final Persistent Memory Database Writer
def commit_node(state: PipelineState) -> Dict:
    print("[Node 4] 💾 Saving audited record to permanent storage layers...")
    report = state["extracted_data"]
    save_risk_to_database(
        entity_name=report.entity_name,
        risk_category=report.risk_category,
        severity=report.severity_score,
        summary=report.verdict_summary
    )
    return {}

# Conditional Router Logic
def compliance_router(state: PipelineState) -> Literal["extraction", "human_gate", "commit", "__end__"]:
    # Loop Guard: Prevent runaway infinite billing or system context bloat
    if state.get("iterations", 0) > 3:
        print("🛑 Max correction loop threshold breached. Halting pipeline.")
        return END
        
    if state.get("error_message"):
        print(f"⚠️ Routing back to Extraction Node. Loop Context: {state['error_message']}")
        return "extraction"
        
    # Check severity parameters for human-in-the-loop triggers
    if state["extracted_data"].severity_score >= 8:
        return "human_gate"
        
    return "commit"

# 3. Assemble and Compile our Finite State Machine Framework
workflow = StateGraph(PipelineState)

# Define Positions
workflow.add_node("extraction", extraction_node)
workflow.add_node("audit", audit_node)
workflow.add_node("human_gate", human_gate_node)
workflow.add_node("commit", commit_node)

# Set Pipeline Entrypoint
workflow.set_entry_point("extraction")

# Construct Interconnected Architecture Layout
workflow.add_edge("extraction", "audit")

# Attach Routing Logic to the Audit and Human Gate Terminals
workflow.add_conditional_edges("audit", compliance_router)
workflow.add_edge("human_gate", "commit")
workflow.add_edge("commit", END)

# Compile Graph Instance
compliance_pipeline = workflow.compile()
