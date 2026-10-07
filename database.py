import chromadb

# 1. Initialize a persistent local ChromaDB client
# This automatically creates a physical folder on your disk to save data permanently.
chroma_client = chromadb.PersistentClient(path="./compliance_vector_db")

# 2. Create or fetch our dedicated collection (similar to an SQL table)
collection = chroma_client.get_or_create_collection(name="risk_records")

def save_risk_to_database(entity_name: str, risk_category: str, severity: int, summary: str):
    """
    Transforms structured extraction data into a semantic document vector 
    and inserts it directly into the local ChromaDB collection.
    """
    print(f"\n📦 Saving record for '{entity_name}' into ChromaDB...")
    
    # We construct a rich text profile so the database can index the data semantically
    semantic_document = f"Entity: {entity_name}. Risk Category: {risk_category}. Severity: {severity}/10. Summary: {summary}"
    
    # Generate a safe, sanitized primary key ID
    unique_id = entity_name.lower().replace(" ", "_")
    
    # Safely insert or update the record inside our collection
    collection.upsert(
        documents=[semantic_document],
        metadatas=[{
            "entity_name": entity_name,
            "risk_category": risk_category,
            "severity_score": severity
        }],
        ids=[unique_id]
    )
    print("✅ Record securely synchronized with local vector repository!")

def search_risk_records(query_text: str):
    """
    Performs a semantic query across internal vector records to find risks.
    """
    print(f"\n🔍 Querying database for: '{query_text}'...")
    
    results = collection.query(
        query_texts=[query_text],
        n_results=1  # Pull the single closest matching record
    )
    return results
