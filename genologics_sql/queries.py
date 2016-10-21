from genologics_sql.tables import *

from sqlalchemy import text
from sqlalchemy.sql import func

def get_last_modified_projects(session, interval="2 hours"):
    """gets the project objects last modified in the last <interval>

    :query: select * from project where age(lastmodifieddate)< '1 hour'::interval;

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records

    """
    txt="age(now(),lastmodifieddate)< '{int}'::interval".format(int=interval)
    return session.query(Project).filter(text(txt)).all()

def get_last_modified_project_udfs(session, interval="2 hours"):
    """gets the project objects that have a udf last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records

    """
    query="select pj.* from project pj \
           inner join entityudfstorage eus on pj.projectid = eus.attachtoid \
           where eus.attachtoclassid = 83 and age(now(), eus.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()


def get_last_modified_project_sample_udfs(session, interval="2 hours"):
    """gets the project objects that have sample udfs last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner  join processudfstorage pus on sa.processid=pus.processid \
            where age(now(), pus.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()

def get_last_modified_project_artifacts(session, interval="2 hours"):
    """gets the project objects that have artifacts last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner join artifact_sample_map asm on sa.processid=asm.processid \
            inner join artifact art on asm.artifactid=art.artifactid \
            where age(now(), art.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()

def get_last_modified_project_artifact_udfs(session, interval="2 hours"):
    """gets the project objects that have artifact udfs last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner join artifact_sample_map asm on sa.processid=asm.processid \
            inner join artifactudfstorage aus on asm.artifactid=aus.artifactid \
            where age(now(), aus.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()

def get_last_modified_project_containers(session, interval="2 hours"):
    """gets the project objects that have containers last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner join artifact_sample_map asm on sa.processid=asm.processid \
            inner join containerplacement cpl on asm.artifactid=cpl.processartifactid \
            inner join container ct on cpl.containerid=ct.containerid \
            where age(ct.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()

def get_last_modified_project_processes(session, interval="2 hours"):
    """gets the project objects that have containers last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner join artifact_sample_map asm on sa.processid=asm.processid \
            inner join processiotracker pit on asm.artifactid=pit.inputartifactid \
            inner join process pro on pit.processid=pro.processid \
            where age(now(), pro.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()

def get_last_modified_project_process_udfs(session, interval="2 hours"):
    """gets the project objects that have containers last modified in the last <interval>

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    query= "select distinct pj.* from project pj \
            inner join sample sa on sa.projectid=pj.projectid \
            inner join artifact_sample_map asm on sa.processid=asm.processid \
            inner join processiotracker pit on asm.artifactid=pit.inputartifactid \
            inner join process pro on pit.processid=pro.processid \
            inner join processudfstorage pus on pro.processid=pus.processid \
            where age(now(), pus.lastmodifieddate) < '{int}'::interval;".format(int=interval)
    return session.query(Project).from_statement(text(query)).all()


def get_last_modified_projectids(session, interval="2 hours"):
    """gets all the projectids for which any part has been modified in the last interval

    :param session: the current SQLAlchemy session to the database
    :param interval: str Postgres-compliant time string
    :returns: List of Project records
    """
    projectids=set()
    for project in get_last_modified_projects(session, interval):
        projectids.add(project.luid)

    for project in get_last_modified_project_udfs(session, interval):
        projectids.add(project.luid)

    for project in get_last_modified_project_sample_udfs(session, interval):
        projectids.add(project.luid)

    for project in get_last_modified_project_containers(session, interval):
        projectids.add(project.luid)

    for project in get_last_modified_project_processes(session, interval):
        projectids.add(project.luid)

    for project in get_last_modified_project_process_udfs(session, interval):
        projectids.add(project.luid)

    return projectids


def get_last_modified_processes(session, ptypes, interval="24 hours"):
    """gets all the processes of the given <type> that have been modified
    or have a udf modified in the last <interval>

    :param session: the current SQLAlchemy session to the db
    :param ptypes: the LIST of process type ids to be returned
    :param interval: the postgres compliant interval of time to search processes in.

    """
    query= "select distinct pro.* from process pro \
            inner join processudfstorage pus on pro.processid=pus.processid \
            where (pro.typeid in ({typelist}) \
            and age(now(), pus.lastmodifieddate) < '{int}'::interval) \
            or \
            (age(now(), pro.lastmodifieddate) < '{int}'::interval \
            and pro.typeid in ({typelist}));".format(int=interval, typelist=",".join([str(x) for x in ptypes]))
    return session.query(Process).from_statement(text(query)).all()

def get_processes_in_history(session, parent_process, ptypes):
    """returns wll the processes that are found in the history of parent_process 
    AND are of type ptypes

    :param session: the current SQLAlchemy session to the db
    :param parent_process: the id of the parent_process
    :param ptypes: the LIST of process type ids to be returned

    """

    query="select distinct pro.* from process pro \
            inner join processiotracker pio on pio.processid=pro.processid \
            inner join outputmapping om on om.trackerid=pio.trackerid \
            inner join artifact_ancestor_map aam on pio.inputartifactid=aam.ancestorartifactid\
            inner join processiotracker pio2 on pio2.inputartifactid=aam.artifactid \
            inner join process pro2 on pro2.processid=pio2.processid \
            where pro2.processid={parent} and pro.typeid in ({typelist});".format(parent=parent_process, typelist=",".join([str(x) for x in ptypes]))

    return session.query(Process).from_statement(text(query)).all()

def get_children_processes(session, parent_process, ptypes):
    """returns wll the processes that are found in the children of parent_process 
    AND are of type ptypes

    :param session: the current SQLAlchemy session to the db
    :param parent_process: the id of the parent_process
    :param ptypes: the LIST of process type ids to be returned

    """

    query="select distinct pro.* from process pro \
            inner join processiotracker pio on pio.processid=pro.processid \
            inner join outputmapping om on om.trackerid=pio.trackerid \
            inner join artifact_ancestor_map aam on om.outputartifactid=aam.artifactid\
            inner join processiotracker pio2 on pio2.inputartifactid=aam.ancestorartifactid \
            inner join process pro2 on pro2.processid=pio2.processid \
            where pro2.processid={parent} and pro.typeid in ({typelist});".format(parent=parent_process, typelist=",".join([str(x) for x in ptypes]))

    return session.query(Process).from_statement(text(query)).all()


def get_samples_and_processes(session, project_name=None, list_process=None, workstatus=None):
    """This method runs a query that return the sample name and the processeses they went through"""
    q = session.query(Project.name, Sample.name, ProcessType.displayname, Process.workstatus)\
           .distinct(Sample.name,Process.processid)\
           .join(Sample.project)\
           .join(Sample.artifacts)\
           .join(Artifact.processiotrackers)\
           .join(ProcessIOTracker.process)\
           .join(Process.type)
    if list_process:
        q = q.filter(ProcessType.displayname.in_(list_process))
    if project_name:
        q = q.filter(Project.name == project_name)
    if workstatus:
        q = q.filter(Process.workstatus == workstatus)
    return q.all()


def get_samples_container(session, project_name=None):
    '''Link sample to project and original container'''
    q = session.query(Project.name, Container.name, Sample.name)\
               .distinct(Project.name, Container.name, Sample.name)\
               .join(Sample.project)\
               .join(Sample.artifacts)\
               .join(Artifact.containerplacement)\
               .join(ContainerPlacement.container)
    if project_name:
        q = q.filter(Project.name == project_name)
    return q.all()


def get_samples_udf_containers(session, project_name=None):
    '''Link sample to project original container, and non null UDFs'''
    q = session.query(Project.name, Container.name, Sample.name, SampleUdfView.udfname,SampleUdfView.udfvalue)\
           .distinct(Sample.name, SampleUdfView.udfname)\
           .join(Sample.project)\
           .join(Sample.udfs)\
           .join(Sample.artifacts)\
           .join(Artifact.containerplacement)\
           .join(ContainerPlacement.container)\
           .filter(SampleUdfView.udfvalue!=None)
    if project_name:
        q = q.filter(Project.name == project_name)
    return q.all()


def all_samples_and_processes(session, project_name=None):
    from collections import defaultdict, Counter
    processes = defaultdict(dict)
    for result in get_samples_and_processes(session, project_name, workstatus='COMPLETE'):
        project_name, sample_name, process_name, process_status = result
        if not 'samples' in processes[process_name]:
            processes[process_name]['samples'] = set()
        processes[process_name]['samples'].add(sample_name)
        if not 'status' in processes[process_name]:
            processes[process_name]['status'] = Counter()
        processes[process_name]['status'][process_status]+=1
    for p in processes:
        print(p, len(processes[p]['samples']), ', '.join(['%s-%s'%(k, v) for k, v in processes[p]['status'].items()]))


def stage_transitions_action_ids(session, sample_name):
    '''See documentation: https://genologics.zendesk.com/hc/en-us/articles/213979583-Stage-transitions-and-Action-IDs'''
    q = session.query(Project.name, Sample.name, Artifact.artifactid, StageTransition.actionid,
                      ProcessType.displayname, StageTransition.workflowrunid) \
        .join(Sample.project) \
        .join(Sample.artifacts) \
        .join(Artifact.stage_transitions) \
        .join(StageTransition.stage) \
        .join(Stage.workflowsection) \
        .join(WorkflowSection.labworkflow) \
        .join(WorkflowSection.labprotocol) \
        .join(LabProtocol.protocolsteps) \
        .join(ProtocolStep.processtype)
    q = q.filter(Sample.name == sample_name)
    return q.all()

def stage_times_o(session, project_name=None, sample_name=None):
    q = session.query(
        Project.name,
        Sample.name,
        LabProtocol.protocolname,
        func.max(StageTransition.lastmodifieddate) - func.min(StageTransition.lastmodifieddate)
    )
    q = q.join(Sample.project) \
        .join(Sample.artifacts) \
        .join(Artifact.stage_transitions) \
        .join(StageTransition.stage) \
        .join(Stage.workflowsection) \
        .join(WorkflowSection.labprotocol)
    q = q.group_by(Project.name, Sample.name, LabProtocol.protocolname)
    q = q.order_by(Project.name, Sample.name, LabProtocol.protocolname)
    if project_name:
        q = q.filter(Project.name == project_name)
    if sample_name:
        q = q.filter(Sample.name == sample_name)

    return  q.all()

def stage_times(session, project_name=None, sample_name=None):
    q = session.query(
        Project.name,
        Sample.name,
        LabProtocol.protocolname,
        StageTransition.lastmodifieddate,
        StageTransition.generatedbyid,
        StageTransition.completedbyid
    )
    q = q.join(Sample.project) \
        .join(Sample.artifacts) \
        .join(Artifact.stage_transitions) \
        .join(StageTransition.stage) \
        .join(Stage.workflowsection) \
        .join(WorkflowSection.labprotocol)
    #q = q.group_by(Project.name, Sample.name, LabProtocol.protocolname)
    #q = q.order_by(Project.name, Sample.name, LabProtocol.protocolname)
    if project_name:
        q = q.filter(Project.name == project_name)
    if sample_name:
        q = q.filter(Sample.name == sample_name)

    return  q.all()

def format_tdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def non_QC_queues(session, project_name=None, sample_name=None, workflow_name=None, protocol_name=None, step_name=None):
    """
    This query gives all of the samples sitting in queue of a non aledgedly non-qc steps
    """
    q = session.query(
        Project.name, Sample.name, LabWorkflow.workflowname, LabProtocol.protocolname, LabProtocol.qcprotocol,
        ProcessType.displayname, WorkflowSection.sectionindex,
        ProtocolStep.protocolstepindex, StageTransition.workflowrunid, StageTransition.completedbyid
    )
    q = q.distinct(
        Project.name, Sample.name, LabWorkflow.workflowname, LabProtocol.protocolname, LabProtocol.qcprotocol,
        ProcessType.displayname
    )
    q = q.join(Sample.project) \
        .join(Sample.artifacts) \
        .join(Artifact.stage_transitions) \
        .join(StageTransition.stage) \
        .join(Stage.protocolstep) \
        .join(ProtocolStep.processtype) \
        .join(Stage.workflowsection) \
        .join(WorkflowSection.labprotocol) \
        .join(WorkflowSection.labworkflow)
    q = q.order_by(Project.name, Sample.name, LabProtocol.protocolname)
    if project_name:
        q = q.filter(Project.name == project_name)
    if sample_name:
        q = q.filter(Sample.name == sample_name)
    if workflow_name:
        q = q.filter(LabWorkflow.workflowname == workflow_name)
    if protocol_name:
        q = q.filter(LabProtocol.protocolname == protocol_name)
    if step_name:
        q = q.filter(ProcessType.displayname == step_name)

    # StageTransition.workflowrunid is positive when the transition in not complete and negative when the transition is completed
    q = q.filter(StageTransition.workflowrunid > 0)
    q = q.filter(StageTransition.completedbyid.is_(None))
    return q.all()


def test_show_queue(session, protocol_name, process_type):
    query1 = """
select queue.project, queue.sample, queue.createddate, queue.workflowrunid from
(
    Select
    CASE
    WHEN lp.qcprotocol = 't' then prqc.name
    ELSE pr.name
    END as project,

    CASE
    WHEN lp.qcprotocol = 't' then stqc.createddate
    ELSE st.createddate
    END as createddate,

    CASE
    WHEN lp.qcprotocol = 't' then aqc.name
    ELSE a.name
    END as sample,

    CASE
    WHEN lp.qcprotocol = 't' then stqc.workflowrunid
    ELSE st.workflowrunid
    END as workflowrunid

    from labprotocol lp
    INNER JOIN protocolstep ps ON ps.protocolid = lp.protocolid
    INNER JOIN processtype pt ON pt.typeid = ps.processtypeid
    INNER JOIN workflowsection ws ON ps.protocolid = ws.protocolid
    FULL OUTER JOIN stage sqc ON sqc.membershipid = ws.sectionid
    INNER JOIN stagetransition stqc ON stqc.stageid = sqc.stageid
    INNER JOIN artifact aqc ON aqc.artifactid = stqc.artifactid
    INNER JOIN artifact_sample_map asmqc ON asmqc.artifactid = aqc.artifactid
    INNER JOIN sample saqc ON saqc.processid = asmqc.processid
    INNER JOIN project prqc ON prqc.projectid = saqc.projectid

    FULL OUTER JOIN stage s ON s.stepid = ps.stepid
    FULL OUTER JOIN stagetransition st ON st.stageid = s.stageid
    FULL OUTER JOIN artifact a ON a.artifactid = st.artifactid
    FULL OUTER JOIN artifact_sample_map asm ON asm.artifactid = a.artifactid
    FULL OUTER JOIN sample sa ON sa.processid = asm.processid
    FULL OUTER JOIN project pr ON pr.projectid = sa.projectid

    WHERE lp.protocolname LIKE '{protocol_name}'
    AND pt.displayname LIKE '{process_type}'
    AND stqc.completedbyid IS NULL
    AND st.completedbyid IS NULL
) queue
where queue.workflowrunid > 0

"""
    query2 = """
    Select pr.name as project, a.name sample, st.createddate as createddate, st.workflowrunid as workflowrunid
    from labprotocol lp
    INNER JOIN protocolstep ps ON ps.protocolid = lp.protocolid
    INNER JOIN processtype pt ON pt.typeid = ps.processtypeid
    INNER JOIN stage s ON s.stepid = ps.stepid
    INNER JOIN stagetransition st ON st.stageid = s.stageid
    INNER JOIN artifact a ON a.artifactid = st.artifactid
    INNER JOIN artifact_sample_map asm ON asm.artifactid = a.artifactid
    INNER JOIN sample sa ON sa.processid = asm.processid
    INNER JOIN project pr ON pr.projectid = sa.projectid

    WHERE lp.protocolname LIKE '{protocol_name}'
    AND pt.displayname LIKE '{process_type}'
    AND st.completedbyid IS NULL
    AND st.workflowrunid > 0

    """
    query = query2.format(protocol_name=protocol_name, process_type=process_type)
    return session.query('project', 'sample', 'createddate', 'workflowrunid').from_statement(text(query)).all()


if __name__ == '__main__':
    import genologics_sql
    from collections import defaultdict
    session = genologics_sql.utils.get_session(echo=True)
    res = non_QC_workflows(session)
    print('\n'.join([str(r) for r in res]))
    print(len(res))
