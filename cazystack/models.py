from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Association table model


# Association table model


# Class model to the X data table
class Cz_Overview(Base):
    __tablename__ = "cz_overview"

    gene_id = Column(String, primary_key=True)
    ec_num = Column(String)
    hmmer = Column(String)
    dbcan_sub = Column(String)
    diamond = Column(String)
    num_of_tools = Column(Integer)


class Cz_Gff(Base):
    __tablename__ = "cz_gff"

    seqid = Column(String)
    source = Column(String)
    type_ = Column(String)
    start = Column(Integer)
    end = Column(Integer)
    score = Column(Integer)
    strand = Column(String)
    phase = Column(Integer)
    attributes = Column(String)


class Cz_CgcStandard(Base):
    __tablename__ = "cgc_standard"

    cgc_num = Column(String)
    gene_type = Column(String)
    contig_id = Column(String)
    protein_id = Column(String)
    gene_start = Column(Integer)
    gene_stop = Column(Integer)
    direction = Column(String)
    protein_family = Column(String)
