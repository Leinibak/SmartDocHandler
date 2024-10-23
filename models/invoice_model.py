from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class InvoicePattern(Base):
    __tablename__ = 'invoice_patterns'

    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    doc_type = Column(String, nullable=False)
    region = Column(String, nullable=False)
    field_name = Column(String, nullable=False)
    pattern = Column(Text, nullable=False)

# Database connection setup
engine = create_engine('sqlite:///patterns.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def insert_pattern(company_name, doc_type, region, field_name, pattern):
    new_pattern = InvoicePattern(
        company_name=company_name,
        doc_type=doc_type,
        region=region,
        field_name=field_name,
        pattern=pattern
    )
    session.add(new_pattern)
    session.commit()

def get_patterns(company_name, doc_type, region):
    patterns = session.query(InvoicePattern).filter_by(
        company_name=company_name,
        doc_type=doc_type,
        region=region
    ).all()
    return {pattern.field_name: pattern.pattern for pattern in patterns}

 