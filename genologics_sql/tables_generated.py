## This file was automatically generated from a clarityDB's schema for clarity v3.5
## It is not expeted to replace table.py but to serve as a usefull reference when a new table needs to be added

# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_DIM_PEPTIDE = Table(
    'DIM_PEPTIDE', metadata,
    Column('PEPTIDESEQUENCE', Text),
    Column('DETECTEDMODIFICATIONS', Text),
    Column('MODIFIEDSEQUENCE', Text)
)


t_DIM_PEPTIDE_QUANTITATION = Table(
    'DIM_PEPTIDE_QUANTITATION', metadata,
    Column('QUANTRESULTS', Text),
    Column('PEPTIDEHITID', BigInteger)
)


t_DIM_PEPTIDE_UDF = Table(
    'DIM_PEPTIDE_UDF', metadata,
    Column('PEPTIDEHITID', BigInteger),
    Column('NAME', Text),
    Column('VALUE', Text),
    Column('UDFVALUEID', Text)
)


t_DIM_PROTEIN = Table(
    'DIM_PROTEIN', metadata,
    Column('PROTEINID', BigInteger),
    Column('DISPLAYNAME', Text),
    Column('PROTEINNAME', Text),
    Column('ACCESSIONNUM', Text),
    Column('MASS', Float(53))
)


t_DIM_PROTEIN_QUANTITATION = Table(
    'DIM_PROTEIN_QUANTITATION', metadata,
    Column('QUANTRESULTS', Text),
    Column('PROTEINHITID', BigInteger)
)


t_DIM_PROTEIN_UDF = Table(
    'DIM_PROTEIN_UDF', metadata,
    Column('PROTEINHITID', BigInteger),
    Column('NAME', Text),
    Column('VALUE', Text),
    Column('UDFVALUEID', Text)
)


t_DIM_SOURCE = Table(
    'DIM_SOURCE', metadata,
    Column('ARTIFACTID', BigInteger),
    Column('ARTIFACTLUID', Text),
    Column('SAMPLELUID', Text),
    Column('SRFTYPE', Text)
)


t_PEPTIDE_FACT = Table(
    'PEPTIDE_FACT', metadata,
    Column('PEP_PEPTIDEHITID', BigInteger),
    Column('PRO_PROTEINHITID', BigInteger),
    Column('ID', Text),
    Column('PRO_ARTIFACTID', BigInteger),
    Column('PRO_SCORE', Float(53)),
    Column('PRO_CONFIDENCEINTERVAL', Float(53)),
    Column('PRO_QUANTRESULTS', Text),
    Column('PRO_MASS', Float(53)),
    Column('PRO_FLAG', Text),
    Column('PRO_SEQUENCECOVERAGE', Float(53)),
    Column('PEP_SOURCENAME', Text),
    Column('PEP_PEPTIDEMASS', Float(53)),
    Column('PEP_THEORETICALMASS', Float(53)),
    Column('PEP_CHARGESTATE', BigInteger),
    Column('PEP_DELTA', Float(53)),
    Column('PEP_MISSEDCLEAV', BigInteger),
    Column('PEP_IONSSCORE', Float(53)),
    Column('PEP_QUANTRESULTS', Text),
    Column('PEP_STARTING', BigInteger),
    Column('PEP_ENDING', BigInteger),
    Column('PEP_PARENTIONINTENSITY', Float(53)),
    Column('PEP_RETENTIONTIMESTART', Float(53)),
    Column('PEP_RETENTIONTIMEEND', Float(53)),
    Column('PEP_RETENTIONTIME', Text),
    Column('PEP_FLAG', Text),
    Column('PEP_NUMIONSMATCHED', BigInteger),
    Column('MODIFIEDSEQUENCE', Text),
    Column('PROTEINID', BigInteger)
)


class Activity(Base):
    __tablename__ = 'activity'

    activityid = Column(BigInteger, primary_key=True)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), nullable=False)
    typeid = Column(BigInteger, nullable=False)
    stateid = Column(String(20), nullable=False)
    attributes = Column(Text, nullable=False)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)

    principal = relationship('Principal')


class Addres(Base):
    __tablename__ = 'address'

    addressid = Column(BigInteger, primary_key=True)
    institution = Column(Text)
    department = Column(Text)
    street = Column(Text)
    city = Column(Text)
    province = Column(Text)
    country = Column(Text)
    postal = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Annotatedspot(Base):
    __tablename__ = 'annotatedspot'
    __table_args__ = (
        Index('ix_annotate_sourcear_sourcear', 'sourceartifactclassid', 'sourceartifactid'),
    )

    spotid = Column(BigInteger, primary_key=True)
    spotnumber = Column(BigInteger)
    subtype = Column(Text)
    intensity = Column(Float(53))
    ii = Column(Float(53))
    area = Column(Float(53))
    matchnumber = Column(BigInteger)
    volume = Column(Float(53))
    referencespotid = Column(BigInteger)
    normalizedvolume = Column(Float(53))
    name = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    outputartifactid = Column(ForeignKey('artifact.artifactid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'), index=True)
    sourceartifactclassid = Column(BigInteger)
    sourceartifactid = Column(BigInteger)

    artifact = relationship('Artifact')


class Artifact(Base):
    __tablename__ = 'artifact'

    artifactid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    luid = Column(Text, unique=True)
    volume = Column(Float(53))
    concentration = Column(Float(53))
    origvolume = Column(Float(53))
    origconcentration = Column(Float(53))
    datastoreid = Column(BigInteger)
    isworking = Column(Boolean)
    isoriginal = Column(Boolean)
    isglobal = Column(Boolean)
    isgenealogyartifact = Column(Boolean, nullable=False, index=True)
    ownerid = Column(BigInteger)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifacttypeid = Column(ForeignKey('artifacttype.typeid', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    processoutputtypeid = Column(ForeignKey('processoutputtype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    currentstateid = Column(ForeignKey('artifactstate.stateid', deferrable=True, initially='DEFERRED'), index=True)
    originalstateid = Column(ForeignKey('artifactstate.stateid', deferrable=True, initially='DEFERRED'), index=True)
    compoundartifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    outputindex = Column(BigInteger)

    artifacttype = relationship('Artifacttype')
    parent = relationship('Artifact', remote_side=[artifactid])
    artifactstate = relationship('Artifactstate', primaryjoin='Artifact.currentstateid == Artifactstate.stateid')
    artifactstate1 = relationship('Artifactstate', primaryjoin='Artifact.originalstateid == Artifactstate.stateid')
    processoutputtype = relationship('Processoutputtype')
    parents = relationship(
        'Artifact',
        secondary='artifact_ancestor_map',
        primaryjoin='Artifact.artifactid == artifact_ancestor_map.c.ancestorartifactid',
        secondaryjoin='Artifact.artifactid == artifact_ancestor_map.c.artifactid'
    )
    imagecoord = relationship('Imagecoord', secondary='list_coord')
    reagentlabel = relationship('Reagentlabel', secondary='artifact_label_map')
    externalprogramstatus = relationship('Externalprogramstatu', secondary='artifact_programstatus_map')
    sample = relationship('Sample', secondary='artifact_sample_map')


class Hybridizedsample(Artifact):
    __tablename__ = 'hybridizedsample'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    hybridizedsampleid = Column(BigInteger, nullable=False, unique=True)


class Gelspot(Artifact):
    __tablename__ = 'gelspot'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    spotid = Column(BigInteger, nullable=False, unique=True)


class Resultfile(Artifact):
    __tablename__ = 'resultfile'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    fileid = Column(BigInteger, nullable=False, unique=True)
    type = Column(Text)
    parsestatus = Column(Integer)
    status = Column(Integer)
    commandid = Column(Text)
    glsfileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)

    glsfile = relationship('Glsfile')


class Samplelane(Artifact):
    __tablename__ = 'samplelane'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    laneid = Column(BigInteger, nullable=False, unique=True)
    lanenumber = Column(BigInteger)


class Searchresultfile(Artifact):
    __tablename__ = 'searchresultfile'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    id = Column(BigInteger, nullable=False, unique=True)
    isparsed = Column(Boolean)
    hitcutoff = Column(BigInteger)
    scorecutoff = Column(Float(53))
    peptidescorecutoff = Column(Float(53))
    hitsimported = Column(BigInteger)
    dbrelease = Column(Text)
    type = Column(Text)
    status = Column(Integer)
    commandid = Column(Text)
    glsfileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)

    glsfile = relationship('Glsfile')


class Gel1d(Artifact):
    __tablename__ = 'gel1d'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    gelid = Column(BigInteger, nullable=False, unique=True)
    numlanes = Column(Integer)
    gelstainid = Column(ForeignKey('gelstain.gelstainid', deferrable=True, initially='DEFERRED'), index=True)

    gelstain = relationship('Gelstain')


class Spotlist(Artifact):
    __tablename__ = 'spotlist'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    listid = Column(BigInteger, nullable=False, unique=True)
    ismanual = Column(Boolean)
    fileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)

    glsfile = relationship('Glsfile')


class Analyte(Artifact):
    __tablename__ = 'analyte'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    analyteid = Column(BigInteger, nullable=False, unique=True)
    iscalibrant = Column(Boolean, nullable=False)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean, nullable=False)


class Genericsubartifact(Artifact):
    __tablename__ = 'genericsubartifact'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    subartifactid = Column(BigInteger, nullable=False, unique=True)


class Img(Artifact):
    __tablename__ = 'img'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    gelimageid = Column(BigInteger, nullable=False, unique=True)
    isinverted = Column(Boolean)
    fileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)

    glsfile = relationship('Glsfile')


class Gel2d(Artifact):
    __tablename__ = 'gel2d'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    gelid = Column(BigInteger, nullable=False, unique=True)
    gelstainid = Column(ForeignKey('gelstain.gelstainid', deferrable=True, initially='DEFERRED'), index=True)
    stripid = Column(ForeignKey('phstrip.stripid', deferrable=True, initially='DEFERRED'), index=True)

    gelstain = relationship('Gelstain')
    phstrip = relationship('Phstrip')


class Reagent(Artifact):
    __tablename__ = 'reagent'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    reagentid = Column(BigInteger, nullable=False, unique=True)
    originalreagentartifactid = Column(ForeignKey('reagent.artifactid', deferrable=True, initially='DEFERRED'), index=True)
    reagenttypeid = Column(ForeignKey('reagenttype.reagenttypeid', deferrable=True, initially='DEFERRED'), index=True)
    reagentlotid = Column(BigInteger, index=True)
    parentreagentartifactid = Column(ForeignKey('reagent.artifactid', deferrable=True, initially='DEFERRED'), index=True)

    parent = relationship('Reagent', remote_side=[artifactid], primaryjoin='Reagent.originalreagentartifactid == Reagent.artifactid')
    parent1 = relationship('Reagent', remote_side=[artifactid], primaryjoin='Reagent.parentreagentartifactid == Reagent.artifactid')
    reagenttype = relationship('Reagenttype')


t_artifact_ancestor_map = Table(
    'artifact_ancestor_map', metadata,
    Column('artifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('ancestorartifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


t_artifact_label_map = Table(
    'artifact_label_map', metadata,
    Column('artifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('labelid', ForeignKey('reagentlabel.labelid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


t_artifact_programstatus_map = Table(
    'artifact_programstatus_map', metadata,
    Column('externalprogramstatusid', ForeignKey('externalprogramstatus.externalprogramstatusid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('artifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


t_artifact_sample_map = Table(
    'artifact_sample_map', metadata,
    Column('artifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('processid', ForeignKey('sample.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


t_artifact_udf_view = Table(
    'artifact_udf_view', metadata,
    Column('artifactid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Artifactflag(Base):
    __tablename__ = 'artifactflag'

    artifactflagid = Column(BigInteger, primary_key=True)
    note = Column(Text)
    typeid = Column(BigInteger, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    artifact = relationship('Artifact')
    principals = relationship('Principal', secondary='artifactflag_principal_map')


t_artifactflag_principal_map = Table(
    'artifactflag_principal_map', metadata,
    Column('artifactflagid', ForeignKey('artifactflag.artifactflagid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('principalid', ForeignKey('principals.principalid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


class Artifactstate(Base):
    __tablename__ = 'artifactstate'

    stateid = Column(BigInteger, primary_key=True)
    qcflag = Column(Integer, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    artifact = relationship('Artifact', primaryjoin='Artifactstate.artifactid == Artifact.artifactid')


class Artifacttype(Base):
    __tablename__ = 'artifacttype'

    typeid = Column(BigInteger, primary_key=True)
    classname = Column(Text)
    displayname = Column(Text)
    ismasterartifact = Column(Boolean)
    issampleartifact = Column(Boolean)
    isaliquotable = Column(Boolean)
    isscannable = Column(Boolean)
    placementtype = Column(Integer, nullable=False)
    useforconfigurable = Column(Boolean)
    iscompoundedonly = Column(Boolean)
    entitynodename = Column(Text, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Artifactudfstorage(Base):
    __tablename__ = 'artifactudfstorage'
    __table_args__ = (
        UniqueConstraint('rowindex', 'artifactid'),
    )

    storageid = Column(BigInteger, primary_key=True)
    rowindex = Column(Integer, nullable=False)
    text0 = Column(Text)
    text1 = Column(Text)
    text2 = Column(Text)
    text3 = Column(Text)
    text4 = Column(Text)
    text5 = Column(Text)
    text6 = Column(Text)
    text7 = Column(Text)
    text8 = Column(Text)
    text9 = Column(Text)
    numeric0 = Column(Float(53))
    numeric1 = Column(Float(53))
    numeric2 = Column(Float(53))
    numeric3 = Column(Float(53))
    numeric4 = Column(Float(53))
    numeric5 = Column(Float(53))
    numeric6 = Column(Float(53))
    numeric7 = Column(Float(53))
    numeric8 = Column(Float(53))
    numeric9 = Column(Float(53))
    numeric10 = Column(Float(53))
    numeric11 = Column(Float(53))
    numeric12 = Column(Float(53))
    numeric13 = Column(Float(53))
    numeric14 = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)

    artifact = relationship('Artifact')
    udt = relationship('Udt')


class Assignedpermission(Base):
    __tablename__ = 'assignedpermission'
    __table_args__ = (
        UniqueConstraint('permissionid', 'roleid'),
    )

    assignedpermissionid = Column(BigInteger, primary_key=True)
    permissionid = Column(ForeignKey('permission.permissionid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    roleid = Column(BigInteger, nullable=False)

    permission = relationship('Permission')


class Auditchangelog(Base):
    __tablename__ = 'auditchangelog'
    __table_args__ = (
        Index('ix_auditchangelog_rowpk', 'tablename', 'rowpk'),
        Index('ix_auditchangelog_rowlimsid', 'tablename', 'rowlimsid')
    )

    changeid = Column(BigInteger, primary_key=True)
    eventid = Column(ForeignKey('auditeventlog.eventid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    transactionid = Column(String(100), index=True)
    databaseusername = Column(String(100))
    schemaname = Column(String(100), nullable=False)
    tablename = Column(String(100), nullable=False)
    rowpk = Column(Text, nullable=False)
    rowlimsid = Column(Text)
    applicationuserid = Column(BigInteger)
    applicationusername = Column(Text)
    applicationname = Column(Text)
    changetype = Column(String(1), nullable=False)
    rowdata = Column(Text, nullable=False)
    changedfields = Column(Text)
    changedate = Column(DateTime(True), nullable=False)

    auditeventlog = relationship('Auditeventlog')


class Auditeventlog(Base):
    __tablename__ = 'auditeventlog'

    eventid = Column(BigInteger, primary_key=True)
    applicationuserid = Column(BigInteger, nullable=False)
    applicationusername = Column(Text, nullable=False, index=True)
    applicationname = Column(Text, nullable=False)
    applicationversion = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    eventtype = Column(Text, nullable=False)
    eventdate = Column(DateTime(True), nullable=False)


class Basepermission(Base):
    __tablename__ = 'basepermission'

    basepermissionid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=False)


class Batchgelimageanalysismapping(Base):
    __tablename__ = 'batchgelimageanalysismapping'

    mappingid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    gelimageanalysisprocessid = Column(ForeignKey('gelimageanalysisrun.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    batchid = Column(ForeignKey('batchgelimageanalysisrun.batchid', deferrable=True, initially='DEFERRED'), index=True)

    batchgelimageanalysisrun = relationship('Batchgelimageanalysisrun')
    gelimageanalysisrun = relationship('Gelimageanalysisrun')


class Batchgelimageanalysisrun(Base):
    __tablename__ = 'batchgelimageanalysisrun'

    batchid = Column(BigInteger, primary_key=True)
    datecreated = Column(DateTime)
    name = Column(Text)
    luid = Column(Text)
    isparsed = Column(Boolean)
    analysistype = Column(Text)
    isprotocol = Column(Boolean)
    protocolnameused = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    fileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)
    installationid = Column(ForeignKey('installation.id', deferrable=True, initially='DEFERRED'), index=True)
    techid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)

    glsfile = relationship('Glsfile')
    installation = relationship('Installation')
    principal = relationship('Principal')


class Batchgelrun(Base):
    __tablename__ = 'batchgelrun'

    batchid = Column(BigInteger, primary_key=True)
    datecreated = Column(DateTime)
    isgel2d = Column(Boolean)
    name = Column(Text)
    luid = Column(Text)
    isprotocol = Column(Boolean)
    protocolnameused = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    techid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)

    principal = relationship('Principal')


class Batchgelrunmapping(Base):
    __tablename__ = 'batchgelrunmapping'

    mappingid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    batchid = Column(ForeignKey('batchgelrun.batchid', deferrable=True, initially='DEFERRED'), index=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    batchgelrun = relationship('Batchgelrun')
    proces = relationship('Proces')


class Bgiaidmaptospotlistid(Base):
    __tablename__ = 'bgiaidmaptospotlistid'
    __table_args__ = (
        Index('ix_bgiaidma_artifact_artifact', 'artifactclassid', 'artifactid'),
    )

    mappingid = Column(BigInteger, primary_key=True)
    imagename = Column(Text)
    artifactid = Column(BigInteger)
    artifactclassid = Column(BigInteger)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    batchid = Column(ForeignKey('batchgelimageanalysisrun.batchid', deferrable=True, initially='DEFERRED'), index=True)
    spotlistartifactid = Column(ForeignKey('spotlist.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    batchgelimageanalysisrun = relationship('Batchgelimageanalysisrun')
    spotlist = relationship('Spotlist')


class Biosource(Base):
    __tablename__ = 'biosource'

    biosourceid = Column(BigInteger, primary_key=True)
    description = Column(Text)
    ispreset = Column(Boolean)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Capturedfile(Base):
    __tablename__ = 'capturedfile'
    __table_args__ = (
        Index('ix_captured_fileenti_fileenti', 'fileentityclassid', 'fileentityid'),
    )

    fileid = Column(BigInteger, primary_key=True)
    luid = Column(Text)
    filename = Column(Text)
    filetype = Column(Text)
    filesize = Column(BigInteger)
    directory = Column(Text)
    lastmodifiedtime = Column(DateTime)
    transfertime = Column(DateTime)
    sourcehost = Column(Text)
    fileentityid = Column(BigInteger)
    fileentityclassid = Column(BigInteger)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    glsfileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), unique=True)

    glsfile = relationship('Glsfile', uselist=False)


t_cconstraint_input_conttype = Table(
    'cconstraint_input_conttype', metadata,
    Column('constraintid', ForeignKey('processcontainerconstraint.constraintid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('containertypeid', ForeignKey('containertype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


t_cconstraint_output_conttype = Table(
    'cconstraint_output_conttype', metadata,
    Column('constraintid', ForeignKey('processcontainerconstraint.constraintid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('containertypeid', ForeignKey('containertype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


class Classindex(Base):
    __tablename__ = 'classindex'

    classindexid = Column(BigInteger, primary_key=True)
    classname = Column(Text)
    tablename = Column(Text)
    anycolumn = Column(Text)


class Commonpkexpert(Base):
    __tablename__ = 'commonpkexpert'

    classname = Column(Text, primary_key=True)
    primarykey = Column(BigInteger)


class Container(Base):
    __tablename__ = 'container'
    __table_args__ = (
        Index('unique_cnt_name', 'name', 'datastoreid', unique=True),
    )

    containerid = Column(BigInteger, primary_key=True)
    subtype = Column(Text, nullable=False)
    luid = Column(Text, index=True)
    isvisible = Column(Boolean)
    name = Column(Text, index=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    stateid = Column(BigInteger, nullable=False)
    typeid = Column(ForeignKey('containertype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    lotnumber = Column(Text)
    expirydate = Column(DateTime)

    containertype = relationship('Containertype')


class Containerplacement(Base):
    __tablename__ = 'containerplacement'
    __table_args__ = (
        UniqueConstraint('containerid', 'wellxposition', 'wellyposition', 'reagentid'),
    )

    placementid = Column(BigInteger, primary_key=True)
    containerid = Column(ForeignKey('container.containerid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    wellxposition = Column(Integer)
    wellyposition = Column(Integer)
    dateplaced = Column(DateTime)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    reagentid = Column(BigInteger, nullable=False)
    processartifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    container = relationship('Container')
    artifact = relationship('Artifact')


class Containerselection(Base):
    __tablename__ = 'containerselection'
    __table_args__ = (
        UniqueConstraint('processid', 'containerid'),
    )

    selectionid = Column(BigInteger, primary_key=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    containerid = Column(ForeignKey('container.containerid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    onthefly = Column(Boolean, nullable=False, server_default=text("false"))
    rackrow = Column(BigInteger)
    rackcolumn = Column(BigInteger)
    rackindex = Column(BigInteger)

    container = relationship('Container')
    proces = relationship('Proces')


class Containertype(Base):
    __tablename__ = 'containertype'

    typeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    numxpositions = Column(Integer)
    isxalpha = Column(Boolean)
    numypositions = Column(Integer)
    isyalpha = Column(Boolean)
    xindexstartsat = Column(Integer, server_default=text("0"))
    yindexstartsat = Column(Integer, server_default=text("0"))
    iconsetconstant = Column(Integer, nullable=False, server_default=text("0"))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    subtype = Column(Text, nullable=False)
    vendoruniqueid = Column(Text)
    istube = Column(Boolean)

    protocol_steps = relationship('Protocolstep', secondary='protocolstep_containertype_map')


class Controltype(Base):
    __tablename__ = 'controltype'

    controltypeid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    supplier = Column(Text)
    cataloguenumber = Column(Text)
    website = Column(Text)
    ownerid = Column(BigInteger, nullable=False)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    lastmodifiedby = Column(BigInteger, nullable=False)
    archived = Column(Boolean, nullable=False, server_default=text("false"))
    singlestep = Column(Boolean, nullable=False, server_default=text("false"))
    concentration = Column(Text)

    protocolstep = relationship('Protocolstep', secondary='protocolstep_controltype_map')


class Datastore(Base):
    __tablename__ = 'datastore'

    datastoreid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    adminemail = Column(Text)
    ipaddress = Column(Text)


class Derivedpermassignment(Base):
    __tablename__ = 'derivedpermassignment'
    __table_args__ = (
        Index('ix_derivedpermassign_ppp0', 'permissionforid', 'permissionforclassid', 'principalid'),
        Index('ix_derivedp_permissi_permissi', 'permissionforclassid', 'permissionforid')
    )

    assignmentkey = Column(Text, primary_key=True)
    addperm = Column(Boolean)
    modifyperm = Column(Boolean)
    deleteperm = Column(Boolean)
    viewperm = Column(Boolean)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    permissionforclassid = Column(BigInteger)
    permissionforid = Column(BigInteger)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)

    principal = relationship('Principal')


class Digestenzyme(Base):
    __tablename__ = 'digestenzyme'

    enzymeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    sequencenumber = Column(Integer)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Disclaimer(Base):
    __tablename__ = 'disclaimer'

    disclaimerid = Column(BigInteger, primary_key=True)
    type = Column(Text)
    text = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Emailsignature(Base):
    __tablename__ = 'emailsignature'

    emailid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


t_entity_udf_view = Table(
    'entity_udf_view', metadata,
    Column('attachtoid', BigInteger),
    Column('attachtoclassid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Entityudfstorage(Base):
    __tablename__ = 'entityudfstorage'
    __table_args__ = (
        UniqueConstraint('attachtoid', 'rowindex', 'attachtoclassid'),
        Index('ix_entityud_attachto_attachto', 'attachtoclassid', 'attachtoid')
    )

    storageid = Column(BigInteger, primary_key=True)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)
    rowindex = Column(Integer, nullable=False)
    text0 = Column(Text)
    text1 = Column(Text)
    text2 = Column(Text)
    text3 = Column(Text)
    text4 = Column(Text)
    text5 = Column(Text)
    text6 = Column(Text)
    text7 = Column(Text)
    text8 = Column(Text)
    text9 = Column(Text)
    numeric0 = Column(Float(53))
    numeric1 = Column(Float(53))
    numeric2 = Column(Float(53))
    numeric3 = Column(Float(53))
    numeric4 = Column(Float(53))
    numeric5 = Column(Float(53))
    numeric6 = Column(Float(53))
    numeric7 = Column(Float(53))
    numeric8 = Column(Float(53))
    numeric9 = Column(Float(53))
    numeric10 = Column(Float(53))
    numeric11 = Column(Float(53))
    numeric12 = Column(Float(53))
    numeric13 = Column(Float(53))
    numeric14 = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)

    udt = relationship('Udt')


class Epptriggerconfiguration(Base):
    __tablename__ = 'epptriggerconfiguration'
    __table_args__ = (
        UniqueConstraint('parameterid', 'stepid'),
    )

    mapid = Column(BigInteger, primary_key=True)
    stepid = Column(ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    parameterid = Column(ForeignKey('processparameter.parameterid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    triggertype = Column(Text)
    triggerstatus = Column(Text)
    triggerpoint = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    processparameter = relationship('Processparameter')
    protocolstep = relationship('Protocolstep')


class Escalatedsample(Base):
    __tablename__ = 'escalatedsample'

    escalatedsampleid = Column(BigInteger, primary_key=True)
    escalationeventid = Column(ForeignKey('escalationevent.eventid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    artifact = relationship('Artifact')
    escalationevent = relationship('Escalationevent')


class Escalationevent(Base):
    __tablename__ = 'escalationevent'

    eventid = Column(BigInteger, primary_key=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    originatorid = Column(ForeignKey('principals.principalid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'))
    reviewerid = Column(ForeignKey('principals.principalid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'))
    escalationdate = Column(DateTime)
    reviewdate = Column(DateTime)
    escalationcomment = Column(Text)
    reviewcomment = Column(Text)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    ownerid = Column(BigInteger)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    principal = relationship('Principal', primaryjoin='Escalationevent.originatorid == Principal.principalid')
    proces = relationship('Proces')
    principal1 = relationship('Principal', primaryjoin='Escalationevent.reviewerid == Principal.principalid')


class ExpArtifactMap(Base):
    __tablename__ = 'exp_artifact_map'

    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
    experimentid = Column(ForeignKey('experiment.experimentid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
    dateadded = Column(DateTime, nullable=False, server_default=text("now()"))
    workflowrunid = Column(BigInteger)

    artifact = relationship('Artifact')
    experiment = relationship('Experiment')


class Experiment(Base):
    __tablename__ = 'experiment'

    experimentid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    datecreated = Column(DateTime)
    propagateartifacts = Column(Boolean, nullable=False, server_default=text("true"))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    workflowid = Column(ForeignKey('labworkflow.workflowid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'))

    labworkflow = relationship('Labworkflow')


class Experimentalcondition(Base):
    __tablename__ = 'experimentalcondition'

    conditionid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processid = Column(ForeignKey('sample.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    sample = relationship('Sample')


class Externalidentifier(Base):
    __tablename__ = 'externalidentifier'
    __table_args__ = (
        Index('ix_external_attachto_attachto', 'attachtoclassid', 'attachtoid'),
    )

    id = Column(BigInteger, primary_key=True)
    externalid = Column(Text, nullable=False, unique=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)


class Externalprograminputparameter(Base):
    __tablename__ = 'externalprograminputparameter'
    __table_args__ = (
        UniqueConstraint('externalprogramstatusid', 'token'),
    )

    inputparameterid = Column(BigInteger, primary_key=True)
    externalprogramstatusid = Column(ForeignKey('externalprogramstatus.externalprogramstatusid', deferrable=True, initially='DEFERRED'), nullable=False)
    token = Column(Text, nullable=False)
    value = Column(Text)

    externalprogramstatu = relationship('Externalprogramstatu')


class Externalprogramstatu(Base):
    __tablename__ = 'externalprogramstatus'

    externalprogramstatusid = Column(BigInteger, primary_key=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'))
    processparameterid = Column(ForeignKey('processparameter.parameterid', deferrable=True, initially='DEFERRED'), nullable=False)
    programuid = Column(String(50), nullable=False, unique=True)
    queuedtimestamp = Column(DateTime, nullable=False)
    statustimestamp = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)
    statusdetail = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    proces = relationship('Proces')
    processparameter = relationship('Processparameter')


class Filetype(Base):
    __tablename__ = 'filetype'

    filetypeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    parsername = Column(Text)
    isvisible = Column(Boolean)
    extension = Column(Text)
    issupported = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Gelstain(Base):
    __tablename__ = 'gelstain'

    gelstainid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    sequencenumber = Column(Integer)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class GlsDimension(Base):
    __tablename__ = 'gls_dimension'

    dimensionid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Glsfile(Base):
    __tablename__ = 'glsfile'
    __table_args__ = (
        Index('ix_glsfile_attachto_attachto', 'attachtoclassid', 'attachtoid'),
    )

    fileid = Column(BigInteger, primary_key=True)
    server = Column(Text)
    contenturi = Column(Text)
    luid = Column(Text)
    originallocation = Column(Text)
    ispublished = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)


t_group_principal_map = Table(
    'group_principal_map', metadata,
    Column('groupid', ForeignKey('usergroup.groupid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('principalid', ForeignKey('principals.principalid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


class Imagecoord(Base):
    __tablename__ = 'imagecoord'

    coordid = Column(BigInteger, primary_key=True)
    xcoordcenter = Column(Float)
    ycoordcenter = Column(Float)
    xcoordstart = Column(BigInteger)
    ycoordstart = Column(BigInteger)
    boundry = Column(Text)
    coordsize = Column(BigInteger)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    spotid = Column(ForeignKey('annotatedspot.spotid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    annotatedspot = relationship('Annotatedspot')


class Installation(Base):
    __tablename__ = 'installation'

    id = Column(BigInteger, primary_key=True)
    isvisible = Column(Boolean)
    isactive = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    instrumentid = Column(ForeignKey('instrument.instrumentid', deferrable=True, initially='DEFERRED'), index=True)
    softwareid = Column(ForeignKey('software.softwareid', deferrable=True, initially='DEFERRED'), index=True)

    instrument = relationship('Instrument')
    software = relationship('Software')


class Installhistory(Base):
    __tablename__ = 'installhistory'

    product = Column(Text, primary_key=True, nullable=False)
    version = Column(Text, nullable=False)
    installdate = Column(DateTime, primary_key=True, nullable=False)


class Instrument(Base):
    __tablename__ = 'instrument'

    instrumentid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    luid = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    typeid = Column(ForeignKey('itype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    itype = relationship('Itype')


class Itype(Base):
    __tablename__ = 'itype'

    typeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    vendorid = Column(ForeignKey('vendor.vendorid', deferrable=True, initially='DEFERRED'), index=True)

    vendor = relationship('Vendor')
    processtype = relationship('Processtype', secondary='proc_instrtype')
    software = relationship('Software', secondary='software_instrtype')


class Lab(Base):
    __tablename__ = 'lab'

    labid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    website = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    billingaddressid = Column(ForeignKey('address.addressid', deferrable=True, initially='DEFERRED'), index=True)
    shippingaddressid = Column(ForeignKey('address.addressid', deferrable=True, initially='DEFERRED'), index=True)

    addres = relationship('Addres', primaryjoin='Lab.billingaddressid == Addres.addressid')
    addres1 = relationship('Addres', primaryjoin='Lab.shippingaddressid == Addres.addressid')


class Labprotocol(Base):
    __tablename__ = 'labprotocol'

    protocolid = Column(BigInteger, primary_key=True)
    protocolname = Column(Text, nullable=False, unique=True)
    protocolindex = Column(BigInteger, nullable=False, server_default=text("(-1)"))
    ishidden = Column(Boolean, nullable=False, server_default=text("false"))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    qcprotocol = Column(Boolean, nullable=False, server_default=text("false"))
    displayablemodifieddate = Column(DateTime)
    displayablemodifiedby = Column(BigInteger)
    protocoltype = Column(Text, nullable=False)
    capacity = Column(Integer, nullable=False, server_default=text("0"))


class Labworkflow(Base):
    __tablename__ = 'labworkflow'

    workflowid = Column(BigInteger, primary_key=True)
    workflowname = Column(Text, nullable=False, unique=True)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    workflowstatus = Column(Text, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    lastmodifiedby = Column(BigInteger)


t_list_coord = Table(
    'list_coord', metadata,
    Column('coordid', ForeignKey('imagecoord.coordid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True),
    Column('artifactid', ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


class Loginaudit(Base):
    __tablename__ = 'loginaudit'

    loginauditid = Column(BigInteger, primary_key=True)
    principalid = Column(BigInteger)
    username = Column(Text)
    ipaddress = Column(Text)
    success = Column(Boolean, nullable=False)
    createddate = Column(DateTime, nullable=False, index=True)


class Loginrecord(Base):
    __tablename__ = 'loginrecords'

    loginrecordid = Column(BigInteger, primary_key=True)
    loginsuccess = Column(Boolean)
    createddate = Column(DateTime, nullable=False)
    principalid = Column(BigInteger, nullable=False)


class Migrationhistory(Base):
    __tablename__ = 'migrationhistory'

    identifier = Column(Text, primary_key=True)
    revision = Column(BigInteger)
    daterun = Column(DateTime)
    migratorversion = Column(Text)


class Note(Base):
    __tablename__ = 'notes'
    __table_args__ = (
        Index('ix_notes_attachto_attachto', 'attachtoclassid', 'attachtoid'),
    )

    noteid = Column(BigInteger, primary_key=True)
    note = Column(Text)
    ispublished = Column(Boolean)
    datecreated = Column(DateTime)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)


class Outputmapping(Base):
    __tablename__ = 'outputmapping'

    mappingid = Column(BigInteger, primary_key=True)
    outputvolume = Column(Float(53))
    outputconcentration = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    trackerid = Column(ForeignKey('processiotracker.trackerid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    outputartifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    artifact = relationship('Artifact')
    processiotracker = relationship('Processiotracker')


class Passwordreset(Base):
    __tablename__ = 'passwordreset'

    token = Column(String(32), primary_key=True)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), nullable=False)
    createddate = Column(DateTime, nullable=False)
    completeddate = Column(DateTime)

    principal = relationship('Principal')


class Pcrresult(Base):
    __tablename__ = 'pcrresult'

    resultid = Column(BigInteger, primary_key=True)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    ownerid = Column(BigInteger)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('resultfile.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    welllocation = Column(Integer)
    originalwell = Column(Text)
    samplename = Column(Text)
    detector = Column(Text)
    relativequantity = Column(Float(53))

    resultfile = relationship('Resultfile')


t_pephit_udf_view = Table(
    'pephit_udf_view', metadata,
    Column('peptidehitid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Peptidehit(Base):
    __tablename__ = 'peptidehit'

    id = Column(BigInteger, primary_key=True)
    peptidesequence = Column(Text)
    errortolmods = Column(Text)
    hitnum = Column(Float)
    homologypass = Column(Boolean)
    identitypass = Column(Boolean)
    ionseriesfound = Column(Text)
    ionsscore = Column(Float(53))
    missedcleav = Column(BigInteger)
    numionsmatched = Column(BigInteger)
    peaksfromions1 = Column(Text)
    varmodsstring = Column(Text)
    starting = Column(BigInteger)
    ending = Column(BigInteger)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    chargestate = Column(BigInteger)
    parentionintensity = Column(Float(53))
    detectedmodifications = Column(Text)
    retentiontimestart = Column(Float(53))
    retentiontimeend = Column(Float(53))
    quantresults = Column(Text)
    flag = Column(Integer, nullable=False)
    sourcename = Column(Text)
    proteinhit_id = Column(ForeignKey('proteinhit.id', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    theoreticalmass = Column(Float(53))
    peptidemass = Column(Float(53))
    delta = Column(Float(53))

    proteinhit = relationship('Proteinhit')


class Peptidehitudfstorage(Base):
    __tablename__ = 'peptidehitudfstorage'
    __table_args__ = (
        UniqueConstraint('peptidehitid', 'rowindex'),
    )

    storageid = Column(BigInteger, primary_key=True)
    rowindex = Column(Integer, nullable=False)
    text0 = Column(Text)
    text1 = Column(Text)
    text2 = Column(Text)
    text3 = Column(Text)
    text4 = Column(Text)
    text5 = Column(Text)
    text6 = Column(Text)
    text7 = Column(Text)
    text8 = Column(Text)
    text9 = Column(Text)
    numeric0 = Column(Float(53))
    numeric1 = Column(Float(53))
    numeric2 = Column(Float(53))
    numeric3 = Column(Float(53))
    numeric4 = Column(Float(53))
    numeric5 = Column(Float(53))
    numeric6 = Column(Float(53))
    numeric7 = Column(Float(53))
    numeric8 = Column(Float(53))
    numeric9 = Column(Float(53))
    numeric10 = Column(Float(53))
    numeric11 = Column(Float(53))
    numeric12 = Column(Float(53))
    numeric13 = Column(Float(53))
    numeric14 = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)
    peptidehitid = Column(ForeignKey('peptidehit.id', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    peptidehit = relationship('Peptidehit')
    udt = relationship('Udt')


class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = (
        UniqueConstraint('basepermissionid', 'actionname'),
    )

    permissionid = Column(BigInteger, primary_key=True)
    basepermissionid = Column(ForeignKey('basepermission.basepermissionid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    actionname = Column(Text, nullable=False)

    basepermission = relationship('Basepermission')


class Permissionassignment(Base):
    __tablename__ = 'permissionassignment'
    __table_args__ = (
        Index('ix_permissi_permissi_permissi', 'permissionforclassid', 'permissionforid'),
    )

    id = Column(BigInteger, primary_key=True)
    addperm = Column(Boolean)
    modifyperm = Column(Boolean)
    deleteperm = Column(Boolean)
    viewperm = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)
    groupid = Column(ForeignKey('usergroup.groupid', deferrable=True, initially='DEFERRED'), index=True)
    permissionforclassid = Column(BigInteger)
    permissionforid = Column(BigInteger)

    usergroup = relationship('Usergroup')
    principal = relationship('Principal')


class Phstrip(Base):
    __tablename__ = 'phstrip'

    stripid = Column(BigInteger, primary_key=True)
    lowerph = Column(Float)
    upperph = Column(Float)
    isnonlinear = Column(Boolean)
    length = Column(BigInteger)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Preference(Base):
    __tablename__ = 'preference'
    __table_args__ = (
        UniqueConstraint('researcherid', 'key'),
    )

    preferenceid = Column(BigInteger, primary_key=True)
    key = Column(String(255), nullable=False)
    value = Column(Text, nullable=False)
    researcherid = Column(ForeignKey('researcher.researcherid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)

    researcher = relationship('Researcher')


class Principal(Base):
    __tablename__ = 'principals'

    principalid = Column(BigInteger, primary_key=True)
    username = Column(Text)
    password = Column(Text)
    isvisible = Column(Boolean)
    isloggedin = Column(Boolean, nullable=False)
    datastoreid = Column(BigInteger)
    ownerid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    ldapdn = Column(Text)
    ldapuuid = Column(Text)
    accountlocked = Column(Boolean, nullable=False)
    researcherid = Column(ForeignKey('researcher.researcherid', deferrable=True, initially='DEFERRED'), index=True)
    locked = Column(Boolean, nullable=False, server_default=text("false"))

    researcher = relationship('Researcher')


t_proc_instrtype = Table(
    'proc_instrtype', metadata,
    Column('instrumenttypeid', ForeignKey('itype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('processtypeid', ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


class Proces(Base):
    __tablename__ = 'process'

    processid = Column(BigInteger, primary_key=True)
    daterun = Column(DateTime)
    luid = Column(Text, nullable=False, unique=True)
    isprotocol = Column(Boolean)
    protocolnameused = Column(Text)
    programstarted = Column(Boolean, nullable=False, server_default=text("false"))
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    ownerid = Column(BigInteger)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    installationid = Column(ForeignKey('installation.id', deferrable=True, initially='DEFERRED'), index=True)
    techid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)
    typeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    stringparameterid = Column(ForeignKey('processparameter.parameterid', deferrable=True, initially='DEFERRED'), index=True)
    fileparameterid = Column(ForeignKey('processparameter.parameterid', deferrable=True, initially='DEFERRED'), index=True)
    protocolstepid = Column(ForeignKey('protocolstep.stepid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'))
    workstatus = Column(Text, nullable=False, server_default=text("'COMPLETE'::text"))
    reagentcategoryid = Column(ForeignKey('reagentcategory.reagentcategoryid', deferrable=True, initially='DEFERRED'))
    signedbyid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'))
    signeddate = Column(DateTime(True))
    nextstepslocked = Column(Boolean, nullable=False, server_default=text("false"))

    processparameter = relationship('Processparameter', primaryjoin='Proces.fileparameterid == Processparameter.parameterid')
    installation = relationship('Installation')
    protocolstep = relationship('Protocolstep')
    reagentcategory = relationship('Reagentcategory')
    principal = relationship('Principal', primaryjoin='Proces.signedbyid == Principal.principalid')
    processparameter1 = relationship('Processparameter', primaryjoin='Proces.stringparameterid == Processparameter.parameterid')
    principal1 = relationship('Principal', primaryjoin='Proces.techid == Principal.principalid')
    processtype = relationship('Processtype')


class Gelimagingrun(Proces):
    __tablename__ = 'gelimagingrun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    imagingrunid = Column(BigInteger, nullable=False, unique=True)


class Taqmansnp(Proces):
    __tablename__ = 'taqmansnp'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    taqmansnpid = Column(BigInteger, nullable=False, unique=True)
    containerid = Column(ForeignKey('container.containerid', deferrable=True, initially='DEFERRED'), index=True)

    container = relationship('Container')


class Annotationprocessingrun(Proces):
    __tablename__ = 'annotationprocessingrun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    runid = Column(BigInteger, nullable=False, unique=True)


class Taqmanpcr(Proces):
    __tablename__ = 'taqmanpcr'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    taqmanpcrid = Column(BigInteger, nullable=False, unique=True)
    containerid = Column(ForeignKey('container.containerid', deferrable=True, initially='DEFERRED'), index=True)

    container = relationship('Container')


class Configuredproces(Proces):
    __tablename__ = 'configuredprocess'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    configuredprocessid = Column(BigInteger, nullable=False, unique=True)


class Transferproces(Proces):
    __tablename__ = 'transferprocess'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    transferprocessid = Column(BigInteger, nullable=False, unique=True)


class Toftofrun(Proces):
    __tablename__ = 'toftofrun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    searchid = Column(BigInteger, nullable=False, unique=True)
    url = Column(Text)
    dbid = Column(ForeignKey('searchdb.dbid', deferrable=True, initially='DEFERRED'), index=True)
    ratingid = Column(ForeignKey('srate.ratingid', deferrable=True, initially='DEFERRED'), index=True)

    searchdb = relationship('Searchdb')
    srate = relationship('Srate')


class Reagentaddition(Proces):
    __tablename__ = 'reagentaddition'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    reagentadditionid = Column(BigInteger, nullable=False, unique=True)
    volumeperwell = Column(Float(53))
    reagentcategoryid = Column(ForeignKey('reagentcategory.reagentcategoryid', deferrable=True, initially='DEFERRED'), index=True)
    reagenttypeid = Column(ForeignKey('reagenttype.reagenttypeid', deferrable=True, initially='DEFERRED'), index=True)
    containerid = Column(ForeignKey('container.containerid', deferrable=True, initially='DEFERRED'), index=True)

    container = relationship('Container')
    reagentcategory = relationship('Reagentcategory')
    reagenttype = relationship('Reagenttype')


class Prepstep(Proces):
    __tablename__ = 'prepstep'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    prepstepid = Column(BigInteger, nullable=False, unique=True)


class Gel1drun(Proces):
    __tablename__ = 'gel1drun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    gelrunid = Column(BigInteger, nullable=False, unique=True)


class Proteinsearch(Proces):
    __tablename__ = 'proteinsearch'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    searchid = Column(BigInteger, nullable=False, unique=True)
    dbid = Column(ForeignKey('searchdb.dbid', deferrable=True, initially='DEFERRED'), index=True)
    ratingid = Column(ForeignKey('srate.ratingid', deferrable=True, initially='DEFERRED'), index=True)

    searchdb = relationship('Searchdb')
    srate = relationship('Srate')


class Addmultiplereagent(Proces):
    __tablename__ = 'addmultiplereagents'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    addmultiplereagentsid = Column(BigInteger, nullable=False, unique=True)


class Gelimageanalysisrun(Proces):
    __tablename__ = 'gelimageanalysisrun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    analysisrunid = Column(BigInteger, nullable=False, unique=True)
    isreference = Column(Boolean)


class Sample(Proces):
    __tablename__ = 'sample'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    sampleid = Column(BigInteger, nullable=False, unique=True)
    name = Column(Text)
    datereceived = Column(DateTime)
    datecompleted = Column(DateTime)
    maximumanalyteid = Column(Integer)
    uniqueid = Column(BigInteger)
    bisourceid = Column(ForeignKey('biosource.biosourceid', deferrable=True, initially='DEFERRED'), index=True)
    projectid = Column(ForeignKey('project.projectid', deferrable=True, initially='DEFERRED'), index=True)
    controltypeid = Column(ForeignKey('controltype.controltypeid', deferrable=True, initially='DEFERRED'), index=True)

    biosource = relationship('Biosource')
    controltype = relationship('Controltype')
    project = relationship('Project')


class Gel2drun(Proces):
    __tablename__ = 'gel2drun'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    gelrunid = Column(BigInteger, nullable=False, unique=True)


class Ettanspothandling(Proces):
    __tablename__ = 'ettanspothandling'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    ettanspothandlingid = Column(BigInteger, nullable=False, unique=True)
    enzymeid = Column(ForeignKey('digestenzyme.enzymeid', deferrable=True, initially='DEFERRED'), index=True)

    digestenzyme = relationship('Digestenzyme')


class Digestion(Proces):
    __tablename__ = 'digestion'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    digestionid = Column(BigInteger, nullable=False, unique=True)
    enzymeid = Column(ForeignKey('digestenzyme.enzymeid', deferrable=True, initially='DEFERRED'), index=True)

    digestenzyme = relationship('Digestenzyme')


class Voladjust(Proces):
    __tablename__ = 'voladjust'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    voladjustid = Column(BigInteger, nullable=False, unique=True)


class Hybridization(Proces):
    __tablename__ = 'hybridization'

    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True)
    hybridizationid = Column(BigInteger, nullable=False, unique=True)
    containertypeid = Column(ForeignKey('containertype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    containertype = relationship('Containertype')


t_process_udf_view = Table(
    'process_udf_view', metadata,
    Column('processid', BigInteger),
    Column('typeid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Processcontainerconstraint(Base):
    __tablename__ = 'processcontainerconstraint'

    constraintid = Column(BigInteger, primary_key=True)
    numberofinputs = Column(Integer)
    inputdimensionx = Column(Integer)
    inputdimensiony = Column(Integer)
    inputexcludetubes = Column(Boolean)
    outputdimensionx = Column(Integer)
    outputdimensiony = Column(Integer)
    outputsameasinput = Column(Boolean)
    sameinputtype = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    processtype = relationship('Processtype')
    containertype = relationship('Containertype', secondary='cconstraint_output_conttype')
    containertype1 = relationship('Containertype', secondary='cconstraint_input_conttype')


class Processinputtype(Base):
    __tablename__ = 'processinputtype'

    typeid = Column(BigInteger, primary_key=True)
    displayname = Column(Text)
    isenabled = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    shoulddemote = Column(Boolean)
    transitionid = Column(Integer)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifacttypeid = Column(ForeignKey('artifacttype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    artifacttype = relationship('Artifacttype')
    processtype = relationship('Processtype')


class Processiotracker(Base):
    __tablename__ = 'processiotracker'

    trackerid = Column(BigInteger, primary_key=True)
    inputvolume = Column(Float(53))
    inputconcentration = Column(Float(53))
    inputstatepreid = Column(ForeignKey('artifactstate.stateid', deferrable=True, initially='DEFERRED'), index=True)
    inputstatepostid = Column(ForeignKey('artifactstate.stateid', deferrable=True, initially='DEFERRED'), index=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    inputartifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    artifact = relationship('Artifact')
    artifactstate = relationship('Artifactstate', primaryjoin='Processiotracker.inputstatepostid == Artifactstate.stateid')
    artifactstate1 = relationship('Artifactstate', primaryjoin='Processiotracker.inputstatepreid == Artifactstate.stateid')
    proces = relationship('Proces')


class Processoutputtype(Base):
    __tablename__ = 'processoutputtype'

    typeid = Column(BigInteger, primary_key=True)
    displayname = Column(Text)
    isenabled = Column(Boolean)
    typeofoutputgeneration = Column(Text, nullable=False)
    numoutputstogenerate = Column(Integer)
    variabilitytype = Column(Text, nullable=False)
    outputnamestring = Column(Text)
    shouldpromote = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifacttypeid = Column(ForeignKey('artifacttype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    artifacttype = relationship('Artifacttype')
    processtype = relationship('Processtype')


class ProcessoutputtypeUdfMap(Base):
    __tablename__ = 'processoutputtype_udf_map'

    mappingid = Column(BigInteger, primary_key=True)
    sequencenumber = Column(Integer, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processoutputtypeid = Column(ForeignKey('processoutputtype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    udfid = Column(ForeignKey('udf.udfid', deferrable=True, initially='DEFERRED'), index=True)

    processoutputtype = relationship('Processoutputtype')
    udf = relationship('Udf')


class Processoutputtypeinstance(Base):
    __tablename__ = 'processoutputtypeinstance'

    instanceid = Column(BigInteger, primary_key=True)
    numbergenerated = Column(Integer)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    typeid = Column(ForeignKey('processoutputtype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    proces = relationship('Proces')
    processoutputtype = relationship('Processoutputtype')


class Processparameter(Base):
    __tablename__ = 'processparameter'

    parameterid = Column(BigInteger, primary_key=True)
    parameterstring = Column(Text)
    invocationtype = Column(Text, nullable=False)
    channelname = Column(Text)
    datastoreid = Column(BigInteger, nullable=False)
    lastmodifiedby = Column(BigInteger, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    ownerid = Column(BigInteger, nullable=False)
    createddate = Column(DateTime, nullable=False)
    isvisible = Column(Boolean, nullable=False)
    isglobal = Column(Boolean, nullable=False)
    parametername = Column(Text, nullable=False)
    iscustom = Column(Boolean, nullable=False)
    runprogramperevent = Column(Boolean, nullable=False, server_default=text("false"))
    parameterfileid = Column(ForeignKey('glsfile.fileid', deferrable=True, initially='DEFERRED'), index=True)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    context = Column(Text, nullable=False, server_default=text("'STEP'::text"))

    glsfile = relationship('Glsfile')
    processtype = relationship('Processtype')


class Processtaskmapping(Base):
    __tablename__ = 'processtaskmapping'

    mappingid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    taskid = Column(ForeignKey('task.taskid', deferrable=True, initially='DEFERRED'), index=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    proces = relationship('Proces')
    task = relationship('Task')


class Processtype(Base):
    __tablename__ = 'processtype'

    typeid = Column(BigInteger, primary_key=True)
    displayname = Column(Text)
    typename = Column(Text)
    isenabled = Column(Boolean)
    contextcode = Column(Text)
    isvisible = Column(Boolean)
    style = Column(Integer)
    showinexplorer = Column(Boolean)
    showinbuttonbar = Column(Boolean)
    openpostprocess = Column(Boolean, nullable=False)
    iconconstant = Column(Text)
    outputcontextcode = Column(Text)
    useprotocol = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    behaviourname = Column(Text)
    metadata = Column(Text)
    canedit = Column(Boolean)
    modulename = Column(Text)
    expertname = Column(Text)

    software = relationship('Software', secondary='software_proctype')


class Processtypecalibrantmapping(Base):
    __tablename__ = 'processtypecalibrantmapping'

    mappingid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    analyteartifactid = Column(ForeignKey('analyte.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    analyte = relationship('Analyte')
    processtype = relationship('Processtype')


class Processudfstorage(Base):
    __tablename__ = 'processudfstorage'
    __table_args__ = (
        UniqueConstraint('rowindex', 'processid'),
    )

    storageid = Column(BigInteger, primary_key=True)
    rowindex = Column(Integer, nullable=False)
    text0 = Column(Text)
    text1 = Column(Text)
    text2 = Column(Text)
    text3 = Column(Text)
    text4 = Column(Text)
    text5 = Column(Text)
    text6 = Column(Text)
    text7 = Column(Text)
    text8 = Column(Text)
    text9 = Column(Text)
    numeric0 = Column(Float(53))
    numeric1 = Column(Float(53))
    numeric2 = Column(Float(53))
    numeric3 = Column(Float(53))
    numeric4 = Column(Float(53))
    numeric5 = Column(Float(53))
    numeric6 = Column(Float(53))
    numeric7 = Column(Float(53))
    numeric8 = Column(Float(53))
    numeric9 = Column(Float(53))
    numeric10 = Column(Float(53))
    numeric11 = Column(Float(53))
    numeric12 = Column(Float(53))
    numeric13 = Column(Float(53))
    numeric14 = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    proces = relationship('Proces')
    udt = relationship('Udt')


t_prohit_udf_view = Table(
    'prohit_udf_view', metadata,
    Column('proteinhitid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Project(Base):
    __tablename__ = 'project'

    projectid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    opendate = Column(DateTime)
    closedate = Column(DateTime)
    invoicedate = Column(DateTime)
    luid = Column(Text)
    priority = Column(BigInteger)
    maximumsampleid = Column(Text, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    researcherid = Column(ForeignKey('researcher.researcherid', deferrable=True, initially='DEFERRED'), index=True)

    researcher = relationship('Researcher')


class Property(Base):
    __tablename__ = 'property'
    __table_args__ = (
        UniqueConstraint('datastoreid', 'name'),
    )

    propertyid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    value = Column(Text)
    defaultvalue = Column(Text)
    description = Column(Text)
    iscustom = Column(Boolean, nullable=False)
    ispassword = Column(Boolean)
    showinapi = Column(Boolean, nullable=False)
    datastoreid = Column(BigInteger, nullable=False)
    isglobal = Column(Boolean, nullable=False)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)


class Protein(Base):
    __tablename__ = 'protein'

    id = Column(BigInteger, primary_key=True)
    accessionnum = Column(Text)
    proteinname = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    proteinsequence = Column(Text)
    searchdatabase_id = Column(ForeignKey('searchdb.dbid', deferrable=True, initially='DEFERRED'), index=True)
    mass = Column(Float(53))

    searchdatabase = relationship('Searchdb')


class Proteinhit(Base):
    __tablename__ = 'proteinhit'

    id = Column(BigInteger, primary_key=True)
    multiplicity = Column(BigInteger)
    score = Column(Float(53))
    flag = Column(Integer, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    sequencecoverage = Column(Float(53))
    quantresults = Column(Text)
    confidenceinterval = Column(Float(53))
    protein_id = Column(ForeignKey('protein.id', deferrable=True, initially='DEFERRED'), index=True)
    searchresultfileartifactid = Column(ForeignKey('searchresultfile.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    protein = relationship('Protein')
    searchresultfile = relationship('Searchresultfile')


class Proteinhitudfstorage(Base):
    __tablename__ = 'proteinhitudfstorage'
    __table_args__ = (
        UniqueConstraint('rowindex', 'proteinhitid'),
    )

    storageid = Column(BigInteger, primary_key=True)
    rowindex = Column(Integer, nullable=False)
    text0 = Column(Text)
    text1 = Column(Text)
    text2 = Column(Text)
    text3 = Column(Text)
    text4 = Column(Text)
    text5 = Column(Text)
    text6 = Column(Text)
    text7 = Column(Text)
    text8 = Column(Text)
    text9 = Column(Text)
    numeric0 = Column(Float(53))
    numeric1 = Column(Float(53))
    numeric2 = Column(Float(53))
    numeric3 = Column(Float(53))
    numeric4 = Column(Float(53))
    numeric5 = Column(Float(53))
    numeric6 = Column(Float(53))
    numeric7 = Column(Float(53))
    numeric8 = Column(Float(53))
    numeric9 = Column(Float(53))
    numeric10 = Column(Float(53))
    numeric11 = Column(Float(53))
    numeric12 = Column(Float(53))
    numeric13 = Column(Float(53))
    numeric14 = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)
    proteinhitid = Column(ForeignKey('proteinhit.id', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    proteinhit = relationship('Proteinhit')
    udt = relationship('Udt')


class Protocol(Base):
    __tablename__ = 'protocol'
    __table_args__ = (
        Index('ix_protocol_processc_processi', 'processclassid', 'processid'),
    )

    protocolid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    sequencenumber = Column(Integer)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)
    processclassid = Column(BigInteger)
    processid = Column(BigInteger)

    processtype = relationship('Processtype')


class Protocolstep(Base):
    __tablename__ = 'protocolstep'

    stepid = Column(BigInteger, primary_key=True)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'))
    protocolstepindex = Column(BigInteger, nullable=False)
    stepconfiguration = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    protocolid = Column(ForeignKey('labprotocol.protocolid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    filter = Column(Text)
    qcprotocolstep = Column(Boolean, nullable=False, server_default=text("false"))
    qcwithplacement = Column(Boolean, nullable=False, server_default=text("false"))
    qcmeasurementwithfile = Column(Boolean, nullable=False, server_default=text("false"))
    defaultprocesstemplate = Column(ForeignKey('protocol.protocolid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'))
    esignaturerequired = Column(Boolean, nullable=False, server_default=text("false"))
    epplocknextsteps = Column(Boolean, nullable=False, server_default=text("false"))

    protocol = relationship('Protocol')
    processtype = relationship('Processtype')
    labprotocol = relationship('Labprotocol')


t_protocolstep_containertype_map = Table(
    'protocolstep_containertype_map', metadata,
    Column('protocol_step_id', ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('container_type_id', ForeignKey('containertype.typeid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


t_protocolstep_controltype_map = Table(
    'protocolstep_controltype_map', metadata,
    Column('protocolstepid', ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('controltypeid', ForeignKey('controltype.controltypeid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


t_protocolstep_reagentctgry_map = Table(
    'protocolstep_reagentctgry_map', metadata,
    Column('stepid', ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('reagentcategoryid', ForeignKey('reagentcategory.reagentcategoryid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


t_protocolstep_reagentkit_map = Table(
    'protocolstep_reagentkit_map', metadata,
    Column('stepid', ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('reagentkitid', ForeignKey('reagentkit.reagentkitid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


class Reagentartifactmapping(Base):
    __tablename__ = 'reagentartifactmapping'

    mappingid = Column(BigInteger, primary_key=True)
    volume = Column(Float(53))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('analyte.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    reagentid = Column(ForeignKey('reagent.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    analyte = relationship('Analyte')
    reagent = relationship('Reagent')


class Reagentcategory(Base):
    __tablename__ = 'reagentcategory'
    __table_args__ = (
        UniqueConstraint('name', 'datastoreid'),
    )

    reagentcategoryid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    isvisible = Column(Boolean)

    protocolstep = relationship('Protocolstep', secondary='protocolstep_reagentctgry_map')


class Reagentkit(Base):
    __tablename__ = 'reagentkit'

    reagentkitid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    supplier = Column(Text)
    cataloguenumber = Column(Text)
    website = Column(Text)
    ownerid = Column(BigInteger, nullable=False)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    lastmodifiedby = Column(BigInteger, nullable=False)
    archived = Column(Boolean, nullable=False, server_default=text("false"))

    protocolstep = relationship('Protocolstep', secondary='protocolstep_reagentkit_map')


class Reagentlabel(Base):
    __tablename__ = 'reagentlabel'
    __table_args__ = (
        UniqueConstraint('name', 'datastoreid'),
    )

    labelid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Reagentlot(Base):
    __tablename__ = 'reagentlot'

    reagentlotid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False, index=True)
    luid = Column(Text, nullable=False, unique=True)
    status = Column(Text, nullable=False)
    lotnumber = Column(Text)
    expirydate = Column(DateTime)
    storagelocation = Column(Text)
    notes = Column(Text)
    ownerid = Column(BigInteger, nullable=False)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    lastmodifiedby = Column(BigInteger, nullable=False)
    reagentkitid = Column(ForeignKey('reagentkit.reagentkitid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    reagentkit = relationship('Reagentkit')


class Reagentlotselection(Base):
    __tablename__ = 'reagentlotselection'
    __table_args__ = (
        UniqueConstraint('processid', 'reagentlotid'),
    )

    selectionid = Column(BigInteger, primary_key=True)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    reagentlotid = Column(ForeignKey('reagentlot.reagentlotid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)

    proces = relationship('Proces')
    reagentlot = relationship('Reagentlot')


class Reagenttype(Base):
    __tablename__ = 'reagenttype'

    reagenttypeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    metadata = Column(Text)
    specialtype = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    isvisible = Column(Boolean)
    reagentcategoryid = Column(ForeignKey('reagentcategory.reagentcategoryid', deferrable=True, initially='DEFERRED'), index=True)

    reagentcategory = relationship('Reagentcategory')


class Researcher(Base):
    __tablename__ = 'researcher'

    researcherid = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger)
    firstname = Column(Text)
    lastname = Column(Text)
    title = Column(Text)
    initials = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    phone = Column(Text)
    email = Column(Text)
    fax = Column(Text)
    addressid = Column(ForeignKey('address.addressid', deferrable=True, initially='DEFERRED'), index=True)
    labid = Column(ForeignKey('lab.labid', deferrable=True, initially='DEFERRED'), index=True)
    supervisorid = Column(ForeignKey('researcher.researcherid', deferrable=True, initially='DEFERRED'), index=True)
    isapproved = Column(Boolean)
    requestedsupervisorfirstname = Column(Text)
    requestedsupervisorlastname = Column(Text)
    requestedusername = Column(Text)
    requestedpassword = Column(Text)
    requestedlabname = Column(Text)
    avatar = Column(LargeBinary)
    avatarcontenttype = Column(Text)

    addres = relationship('Addres')
    lab = relationship('Lab')
    parent = relationship('Researcher', remote_side=[researcherid])


class Rmap(Base):
    __tablename__ = 'rmap'

    rolemappingid = Column(BigInteger, primary_key=True)
    rolegroup = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger, nullable=False, server_default=text("10"))
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)
    roleid = Column(ForeignKey('securityrole.roleid', deferrable=True, initially='DEFERRED'), index=True)

    principal = relationship('Principal')
    securityrole = relationship('Securityrole')


class Routingaction(Base):
    __tablename__ = 'routingaction'

    routingactionid = Column(BigInteger, primary_key=True)
    actiontype = Column(String(20), nullable=False)
    actionstepid = Column(ForeignKey('protocolstep.stepid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'))
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    reworkedprocessid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'))
    reworkedartifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    protocolstep = relationship('Protocolstep')
    artifact = relationship('Artifact', primaryjoin='Routingaction.artifactid == Artifact.artifactid')
    proces = relationship('Proces', primaryjoin='Routingaction.processid == Proces.processid')
    artifact1 = relationship('Artifact', primaryjoin='Routingaction.reworkedartifactid == Artifact.artifactid')
    proces1 = relationship('Proces', primaryjoin='Routingaction.reworkedprocessid == Proces.processid')


t_sample_udf_view = Table(
    'sample_udf_view', metadata,
    Column('sampleid', BigInteger),
    Column('udtname', Text),
    Column('udfname', Text),
    Column('udftype', Text),
    Column('udfvalue', Text),
    Column('udfunitlabel', Text)
)


class Samplecheckout(Base):
    __tablename__ = 'samplecheckout'
    __table_args__ = (
        UniqueConstraint('artifactid', 'stepid'),
    )

    checkoutid = Column(BigInteger, primary_key=True)
    stepid = Column(ForeignKey('protocolstep.stepid', deferrable=True, initially='DEFERRED'), nullable=False)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    principalid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), nullable=False)
    checkouttime = Column(DateTime, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processid = Column(ForeignKey('process.processid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'))

    artifact = relationship('Artifact')
    principal = relationship('Principal')
    proces = relationship('Proces')
    protocolstep = relationship('Protocolstep')


class Searchdb(Base):
    __tablename__ = 'searchdb'

    dbid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    queryurl = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Searchparameter(Base):
    __tablename__ = 'searchparameters'

    id = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    name = Column(Text)
    value = Column(Text)
    searchresultfileartifactid = Column(ForeignKey('searchresultfile.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    searchresultfile = relationship('Searchresultfile')


class Securityrole(Base):
    __tablename__ = 'securityrole'

    roleid = Column(BigInteger, primary_key=True)
    role = Column(Text)
    displayname = Column(Text, nullable=False, unique=True)


class Snpresult(Base):
    __tablename__ = 'snpresult'

    resultid = Column(BigInteger, primary_key=True)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    ownerid = Column(BigInteger)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    artifactid = Column(ForeignKey('resultfile.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    welllocation = Column(Integer)
    originalwell = Column(Text)
    samplename = Column(Text)
    markername = Column(Text)
    allelexrn = Column(Float(53))
    alleleyrn = Column(Float(53))
    call = Column(Text)
    callmapped = Column(Text)
    qualityvalue = Column(Float(53))
    calltype = Column(Text)
    task = Column(Text)
    passiveref = Column(Float(53))

    resultfile = relationship('Resultfile')


class Software(Base):
    __tablename__ = 'software'

    softwareid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    version = Column(Text)
    issupported = Column(Boolean)
    resulturl = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    filetypedriverid = Column(ForeignKey('filetype.filetypeid', deferrable=True, initially='DEFERRED'), index=True)
    filetypeoutputid = Column(ForeignKey('filetype.filetypeid', deferrable=True, initially='DEFERRED'), index=True)
    vendorid = Column(ForeignKey('vendor.vendorid', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    filetype = relationship('Filetype', primaryjoin='Software.filetypedriverid == Filetype.filetypeid')
    filetype1 = relationship('Filetype', primaryjoin='Software.filetypeoutputid == Filetype.filetypeid')
    vendor = relationship('Vendor')


t_software_instrtype = Table(
    'software_instrtype', metadata,
    Column('instrumenttypeid', ForeignKey('itype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True),
    Column('softwareid', ForeignKey('software.softwareid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


t_software_proctype = Table(
    'software_proctype', metadata,
    Column('softwareid', ForeignKey('software.softwareid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False),
    Column('processtypeid', ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True)
)


class Specialwell(Base):
    __tablename__ = 'specialwell'

    wellid = Column(BigInteger, primary_key=True)
    wellxposition = Column(Integer)
    wellyposition = Column(Integer)
    specialcode = Column(Integer)
    wellname = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    typeid = Column(ForeignKey('containertype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    containertype = relationship('Containertype')


class Srate(Base):
    __tablename__ = 'srate'

    ratingid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Stage(Base):
    __tablename__ = 'stage'

    stageid = Column(BigInteger, primary_key=True)
    membershipid = Column(ForeignKey('workflowsection.sectionid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    stepid = Column(ForeignKey('protocolstep.stepid', deferrable=True, initially='DEFERRED'))
    stageindex = Column(BigInteger, nullable=False)

    workflowsection = relationship('Workflowsection')
    protocolstep = relationship('Protocolstep')


class Stagetransition(Base):
    __tablename__ = 'stagetransition'

    transitionid = Column(BigInteger, primary_key=True)
    stageid = Column(ForeignKey('stage.stageid', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    artifactid = Column(ForeignKey('artifact.artifactid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    workflowrunid = Column(BigInteger, nullable=False)
    generatedbyid = Column(ForeignKey('process.processid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'), index=True)
    ownerid = Column(BigInteger, nullable=False)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime, nullable=False)
    lastmodifieddate = Column(DateTime, nullable=False)
    lastmodifiedby = Column(BigInteger, nullable=False)
    actionid = Column(BigInteger, nullable=False, server_default=text("0"))
    completedbyid = Column(ForeignKey('process.processid', ondelete='SET NULL', deferrable=True, initially='DEFERRED'), index=True)
    actionstepid = Column(BigInteger)

    artifact = relationship('Artifact')
    proces = relationship('Proces', primaryjoin='Stagetransition.completedbyid == Proces.processid')
    proces1 = relationship('Proces', primaryjoin='Stagetransition.generatedbyid == Proces.processid')
    stage = relationship('Stage')


class Steptransition(Base):
    __tablename__ = 'steptransition'
    __table_args__ = (
        UniqueConstraint('previousstepid', 'nextstepid'),
    )

    transitionid = Column(BigInteger, primary_key=True)
    previousstepid = Column(ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    nextstepid = Column(ForeignKey('protocolstep.stepid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)

    protocolstep = relationship('Protocolstep', primaryjoin='Steptransition.nextstepid == Protocolstep.stepid')
    protocolstep1 = relationship('Protocolstep', primaryjoin='Steptransition.previousstepid == Protocolstep.stepid')


class Systemtag(Base):
    __tablename__ = 'systemtag'
    __table_args__ = (
        Index('ix_systemta_taggercl_taggerid', 'taggerclassid', 'taggerid'),
        Index('ix_systemta_attachto_attachto', 'attachtoclassid', 'attachtoid')
    )

    systemtagid = Column(BigInteger, primary_key=True)
    taggerclassid = Column(BigInteger)
    taggerid = Column(BigInteger)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)
    tagvalue = Column(Integer)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)


class TaqmanpcrReagenttype(Base):
    __tablename__ = 'taqmanpcr_reagenttype'

    taqmanpcrid = Column(BigInteger, primary_key=True, nullable=False)
    reagenttypeid = Column(BigInteger, primary_key=True, nullable=False)


class Task(Base):
    __tablename__ = 'task'

    taskid = Column(BigInteger, primary_key=True)
    assignmentdate = Column(DateTime)
    startdate = Column(DateTime)
    completiondate = Column(DateTime)
    details = Column(Text)
    priority = Column(Integer)
    intendedqty = Column(Float)
    actualqty = Column(Float)
    submissible = Column(Boolean)
    submissiondate = Column(DateTime)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    completedbyid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)
    techid = Column(ForeignKey('principals.principalid', deferrable=True, initially='DEFERRED'), index=True)
    groupid = Column(ForeignKey('usergroup.groupid', deferrable=True, initially='DEFERRED'), index=True)
    protocolid = Column(ForeignKey('protocol.protocolid', deferrable=True, initially='DEFERRED'), index=True)
    prereqtaskid = Column(ForeignKey('task.taskid', deferrable=True, initially='DEFERRED'), index=True)
    tasktypeid = Column(ForeignKey('tasktype.tasktypeid', deferrable=True, initially='DEFERRED'), index=True)

    principal = relationship('Principal', primaryjoin='Task.completedbyid == Principal.principalid')
    usergroup = relationship('Usergroup')
    parent = relationship('Task', remote_side=[taskid])
    protocol = relationship('Protocol')
    tasktype = relationship('Tasktype')
    principal1 = relationship('Principal', primaryjoin='Task.techid == Principal.principalid')


class Taskabletype(Base):
    __tablename__ = 'taskabletype'

    typeid = Column(BigInteger, primary_key=True)
    classname = Column(Text)
    displayname = Column(Text)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    tasktype = relationship('Tasktype', secondary='type_task')


class Taskmapping(Base):
    __tablename__ = 'taskmapping'
    __table_args__ = (
        Index('ix_taskmapp_attachto_attachto', 'attachtoclassid', 'attachtoid'),
    )

    mappingid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    taskid = Column(ForeignKey('task.taskid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)
    attachtoclassid = Column(BigInteger)
    attachtoid = Column(BigInteger)

    task = relationship('Task')


class Tasktype(Base):
    __tablename__ = 'tasktype'

    tasktypeid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    sequencenumber = Column(Integer)
    submissible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    processtypeid = Column(ForeignKey('processtype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    processtype = relationship('Processtype')


class Timing(Base):
    __tablename__ = 'timing'

    timingid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    executiontime = Column(Float(53), nullable=False)
    numberofresults = Column(Integer, nullable=False)
    attributes = Column(Text, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


t_type_task = Table(
    'type_task', metadata,
    Column('taskabletypeid', ForeignKey('taskabletype.typeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False, index=True),
    Column('tasktypeid', ForeignKey('tasktype.tasktypeid', deferrable=True, initially='DEFERRED'), primary_key=True, nullable=False)
)


class Udf(Base):
    __tablename__ = 'udf'
    __table_args__ = (
        UniqueConstraint('rowindex', 'storagefield', 'attachtoclassid', 'attachtosubtypeid', 'datastoreid'),
    )

    udfid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    rowindex = Column(Integer, nullable=False)
    storagefield = Column(Text, nullable=False)
    isvisible = Column(Boolean, nullable=False, server_default=text("true"))
    showinlablink = Column(Boolean, nullable=False, server_default=text("false"))
    allownonpresetvalues = Column(Boolean, nullable=False, server_default=text("false"))
    firstpresetisdefaultvalue = Column(Boolean, nullable=False, server_default=text("false"))
    attachtoclassid = Column(BigInteger, nullable=False)
    attachtosubtypeid = Column(BigInteger, nullable=False, server_default=text("(-1)"))
    showintables = Column(Boolean, nullable=False, server_default=text("false"))
    sequencenumber = Column(Integer, nullable=False)
    displayprecision = Column(Integer, nullable=False, server_default=text("0"))
    unitlabel = Column(Text)
    iseditable = Column(Boolean, server_default=text("false"))
    namespace = Column(Text, nullable=False, unique=True)
    udtid = Column(ForeignKey('udt.udtid', deferrable=True, initially='DEFERRED'), index=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    isdeviation = Column(Boolean, nullable=False, server_default=text("false"))
    parent = Column(ForeignKey('udf.udfid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), index=True)

    parent1 = relationship('Udf', remote_side=[udfid])
    udt = relationship('Udt')


class UdfUdtTargettype(Base):
    __tablename__ = 'udf_udt_targettype'
    __table_args__ = (
        UniqueConstraint('datastoreid', 'attachtosubtypeid', 'attachtoclassid'),
    )

    targettypeid = Column(BigInteger, primary_key=True)
    attachtoclassid = Column(BigInteger, nullable=False)
    attachtosubtypeid = Column(BigInteger, nullable=False, server_default=text("(-1)"))
    udtisrequired = Column(Boolean, nullable=False)
    datastoreid = Column(BigInteger)
    ownerid = Column(BigInteger)
    isglobal = Column(Boolean, nullable=False)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Udfpreset(Base):
    __tablename__ = 'udfpreset'

    presetid = Column(BigInteger, primary_key=True)
    value = Column(Text, nullable=False)
    sequencenumber = Column(Integer, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udfid = Column(ForeignKey('udf.udfid', deferrable=True, initially='DEFERRED'), index=True)

    udf = relationship('Udf')


class Udfvalidatorinstance(Base):
    __tablename__ = 'udfvalidatorinstance'

    validatorinstanceid = Column(BigInteger, primary_key=True)
    xmlvalidationdef = Column(Text, nullable=False)
    isvisible = Column(Boolean, nullable=False, server_default=text("true"))
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    udfid = Column(ForeignKey('udf.udfid', deferrable=True, initially='DEFERRED'), index=True)
    validatorid = Column(ForeignKey('validator.validatorid', deferrable=True, initially='DEFERRED'), index=True)

    udf = relationship('Udf')
    validator = relationship('Validator')


class Udt(Base):
    __tablename__ = 'udt'

    udtid = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    attachtoclassid = Column(BigInteger, nullable=False)
    attachtosubtypeid = Column(BigInteger, server_default=text("(-1)"))
    isvisible = Column(Boolean, nullable=False, server_default=text("true"))
    showinlablink = Column(Boolean, nullable=False, server_default=text("false"))
    sequencenumber = Column(Integer, nullable=False)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Unit(Base):
    __tablename__ = 'unit'

    unitid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    dimensionid = Column(ForeignKey('gls_dimension.dimensionid', deferrable=True, initially='DEFERRED'), index=True)

    gls_dimension = relationship('GlsDimension')


class Usergroup(Base):
    __tablename__ = 'usergroup'

    groupid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    datastoreid = Column(BigInteger)
    ownerid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)

    principals = relationship('Principal', secondary='group_principal_map')


class Validator(Base):
    __tablename__ = 'validator'

    validatorid = Column(BigInteger, primary_key=True)
    validatorclass = Column(Text)
    fieldclass = Column(Text)
    sequencenumber = Column(Integer)
    isdefault = Column(Boolean)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Vendor(Base):
    __tablename__ = 'vendor'

    vendorid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    isvisible = Column(Boolean)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)


class Workflow(Base):
    __tablename__ = 'workflow'

    workflowid = Column(BigInteger, primary_key=True)
    name = Column(Text)
    sequencenumber = Column(Integer)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    taskabletypeid = Column(ForeignKey('taskabletype.typeid', deferrable=True, initially='DEFERRED'), index=True)

    taskabletype = relationship('Taskabletype')


class Workflowitem(Base):
    __tablename__ = 'workflowitem'

    workflowitemid = Column(BigInteger, primary_key=True)
    ownerid = Column(BigInteger)
    datastoreid = Column(BigInteger)
    isglobal = Column(Boolean)
    createddate = Column(DateTime)
    lastmodifieddate = Column(DateTime)
    lastmodifiedby = Column(BigInteger)
    sequencenumber = Column(Integer)
    protocolid = Column(ForeignKey('protocol.protocolid', deferrable=True, initially='DEFERRED'), index=True)
    tasktypeid = Column(ForeignKey('tasktype.tasktypeid', deferrable=True, initially='DEFERRED'), index=True)
    workflowid = Column(ForeignKey('workflow.workflowid', deferrable=True, initially='DEFERRED'), index=True)
    prereqworkflowitemid = Column(ForeignKey('workflowitem.workflowitemid', deferrable=True, initially='DEFERRED'), index=True)

    parent = relationship('Workflowitem', remote_side=[workflowitemid])
    protocol = relationship('Protocol')
    tasktype = relationship('Tasktype')
    workflow = relationship('Workflow')


class Workflowsection(Base):
    __tablename__ = 'workflowsection'

    sectionid = Column(BigInteger, primary_key=True)
    workflowid = Column(ForeignKey('labworkflow.workflowid', ondelete='CASCADE', deferrable=True, initially='DEFERRED'), nullable=False)
    protocolid = Column(ForeignKey('labprotocol.protocolid', deferrable=True, initially='DEFERRED'), nullable=False)
    sectionindex = Column(BigInteger, nullable=False)

    labprotocol = relationship('Labprotocol')
    labworkflow = relationship('Labworkflow')
