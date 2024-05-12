"""Source file for JiraRestRequestor Class.

"""

import requests

class JiraRestRequestor:
  """Interacts with the Jira Server.

  Attributes:
    api_link: A string uri link to Jira API.
    api_key: A string API key used for server authentication.
  """

  def __init__(self, api_link: str, api_key: str):
    """ Initializes a JiraRestRequestor instance.

    Args:
      api_link: Defines reference to the Jira API server.
      api_key: Defines authentication for server access.
    """
    self.api_link = api_link
    self.api_key = api_key

  def get_epics(self) -> list[str]:
    """The list of epic names."""
    return [""]

  def get_milestones(self) -> list[str]:
    """The list of milestone names."""
    return [""]

  def get_issues_from_epic(self, epic_name: str) -> list[str]:
    """The list of issues related to an epic."""
    return [""]

  def get_issues_from_milestone(self, milestone_name: str) -> list[str]:
    """The list of issues related to a milestone."""
    return [""]

  def get_all_issues(self) -> list[str]:
    """The list of all issues."""
    return [""]
