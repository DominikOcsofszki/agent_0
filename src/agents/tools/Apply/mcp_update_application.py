import inspect
from mcp.server.fastmcp import FastMCP

from agents.tools.Apply.fake_db import FakeDB

mcp = FastMCP("APPLICATION")
fakeDB = FakeDB()


@mcp.tool()
def get_applicant_infos_that_needs_filling() -> str:
    """
    Here's a list of 10 useful items you could fill out after interviewing a candidate for a Computer Science (CS) position in consulting:
    """

    return """
    Interview Date – The date the interview took place.
    Candidate Full Name – First and last name of the interviewee.
    Educational Background – Degree(s), field of study, and relevant certifications.
    Technical Skills Assessment – Evaluation of relevant programming languages, frameworks, or tools.
    Problem-Solving & Algorithmic Thinking – How well the candidate approached and solved coding or logical problems.
    Communication Skills – Clarity, articulation, and ability to explain complex concepts.
    Consulting Mindset / Client Interaction Potential – Ability to communicate with clients, handle ambiguity, and present ideas.
    Cultural Fit & Team Collaboration – How well the candidate might fit into the team and company culture.
    Overall Interview Performance – General impression and effectiveness during the interview.
    Recommendation / Next Steps – Hire / No hire / Next round / Technical test, etc.
    Would you like this formatted as a checklist or form template?
    """


@mcp.tool()
def get_applicant_info_by_email(email: str) -> str:
    """
    Retrieve applicant information from the database using the provided email address as the key.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_interview_date(email: str, interview_date: str) -> str:
    """
    Update the interview date for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_candidate_full_name(email: str, full_name: str) -> str:
    """
    Update the full name of the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_educational_background(email: str, background: str) -> str:
    """
    Update the educational background of the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_technical_skills_assessment(email: str, assessment: str) -> str:
    """
    Update the technical skills assessment for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_problem_solving(email: str, assessment: str) -> str:
    """
    Update the problem-solving and algorithmic thinking evaluation for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_communication_skills(email: str, assessment: str) -> str:
    """
    Update the communication skills evaluation for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_consulting_mindset(email: str, assessment: str) -> str:
    """
    Update the consulting mindset and client interaction potential for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_cultural_fit(email: str, assessment: str) -> str:
    """
    Update the cultural fit and team collaboration notes for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_overall_performance(email: str, assessment: str) -> str:
    """
    Update the overall interview performance summary for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


@mcp.tool()
def update_recommendation(email: str, recommendation: str) -> str:
    """
    Update the final recommendation or next steps for the applicant identified by their email address.
    """
    return fakeDB.log_fake_db_args(inspect.currentframe())


if __name__ == "__main__":
    mcp.run()
