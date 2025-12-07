import firebase_admin
from firebase_admin import credentials, firestore
from langchain_core.documents import Document
from typing import List, Optional

class FirestoreInterviewLoader:
    """
    Loads interview questions and details from Firestore.
    """
    def __init__(self, service_account_path: str, collection_name: str):
        self.service_account_path = service_account_path
        self.collection_name = collection_name
        self._initialize_app()
    
    def _initialize_app(self):
        try:
            # Check if app is already initialized
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(self.service_account_path)
            firebase_admin.initialize_app(cred)
            
    def load(self) -> List[Document]:
        print(f"Connecting to Firestore collection: {self.collection_name}")
        db = firestore.client()
        collection_ref = db.collection(self.collection_name)
        docs_stream = collection_ref.stream()
        
        documents = []
        for doc in docs_stream:
            data = doc.to_dict()
            
            # Extract fields based on provided schema
            role = data.get('role', 'Unknown Role')
            level = data.get('level', 'Unknown Level')
            techstack = ", ".join(data.get('techstack', []))
            questions = data.get('questions', [])
            
            # Format questions list
            questions_text = ""
            for i, q in enumerate(questions):
                questions_text += f"{i+1}. {q}\n"
            
            # Construct meaningful content for the LLM
            content = f"""
INTERVIEW DATA
Role: {role}
Level: {level}
Tech Stack: {techstack}

QUESTIONS:
{questions_text}
            """.strip()
            
            # Metadata for filtering
            metadata = {
                'source': 'firestore',
                'collection': self.collection_name,
                'doc_id': doc.id,
                'userId': data.get('userId'),
                'finalized': data.get('finalized', False),
                'type': data.get('type', 'unknown'),
                'createdAt': data.get('createdAt')
            }
            
            documents.append(Document(page_content=content, metadata=metadata))
            
        print(f"Successfully loaded {len(documents)} documents from Firestore.")
        return documents
