"""
Startup Plan - A simple implementation of a startup business plan structure
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional


class StartupPlan:
    """
    Represents a comprehensive startup business plan.
    """

    @staticmethod
    def _is_valid_text(value: Optional[str]) -> bool:
        """Return True when a value is a non-empty string."""
        return isinstance(value, str) and value.strip() != ""

    def __init__(self, company_name: str, founder: str):
        self.company_name = company_name
        self.founder = founder
        self.vision = ""
        self.mission = ""
        self.milestones: List[Dict] = []
        self.team: List[Dict] = []
        self.created_at = datetime.now()

    def set_vision(self, vision: str) -> bool:
        """Set the company vision."""
        if not self._is_valid_text(vision):
            return False
        self.vision = vision.strip()
        return True

    def set_mission(self, mission: str) -> bool:
        """Set the company mission."""
        if not self._is_valid_text(mission):
            return False
        self.mission = mission.strip()
        return True

    def add_milestone(self, title: str, description: str, target_date: datetime) -> bool:
        """Add a milestone to the startup plan."""
        if not self._is_valid_text(title):
            return False
        if description is None:
            return False
        if not isinstance(target_date, datetime):
            return False

        milestone = {
            'title': title.strip(),
            'description': description,
            'target_date': target_date,
            'completed': False,
            'completed_date': None,
        }
        self.milestones.append(milestone)
        return True

    def complete_milestone(self, title: str) -> bool:
        """Mark a milestone as completed."""
        if not self._is_valid_text(title):
            return False

        normalized_title = title.strip().lower()
        for milestone in self.milestones:
            if milestone['title'].strip().lower() == normalized_title:
                milestone['completed'] = True
                milestone['completed_date'] = datetime.now()
                return True
        return False

    def add_team_member(self, name: str, role: str, skills: List[str]) -> bool:
        """Add a team member to the startup."""
        if not self._is_valid_text(name) or not self._is_valid_text(role):
            return False
        if skills is None:
            return False
        if isinstance(skills, str):
            skills = [skills]
        if not isinstance(skills, (list, tuple)):
            return False

        normalized_skills = []
        for skill in skills:
            if not isinstance(skill, str):
                return False
            cleaned_skill = skill.strip()
            if cleaned_skill:
                normalized_skills.append(cleaned_skill)

        team_member = {
            'name': name.strip(),
            'role': role.strip(),
            'skills': normalized_skills,
            'joined_date': datetime.now(),
        }
        self.team.append(team_member)
        return True

    def get_summary(self) -> str:
        """Get a summary of the startup plan."""
        summary = f"""
 Startup Plan Summary
 ====================
 Company: {self.company_name}
 Founder: {self.founder}
 Created: {self.created_at.strftime('%Y-%m-%d')}
 
 Vision: {self.vision}
 Mission: {self.mission}
 
 Team Members: {len(self.team)}
 Milestones: {len(self.milestones)} ({sum(1 for m in self.milestones if m['completed'])} completed)
 """
        return summary

    def get_next_milestone(self) -> Optional[Dict]:
        """Get the next uncompleted milestone."""
        uncompleted = [m for m in self.milestones if not m['completed']]
        valid_milestones = [
            m for m in uncompleted if isinstance(m.get('target_date'), datetime)
        ]
        if valid_milestones:
            return min(valid_milestones, key=lambda m: m['target_date'])
        return None


def create_example_plan() -> StartupPlan:
    """Create an example startup plan."""
    plan = StartupPlan("TechVenture", "John Doe")

    # Set vision and mission
    plan.set_vision("To revolutionize the way people interact with technology")
    plan.set_mission("Building innovative solutions that make technology accessible to everyone")

    # Add milestones
    today = datetime.now()
    plan.add_milestone(
        "Complete MVP",
        "Develop and test the minimum viable product",
        today + timedelta(days=90),
    )
    plan.add_milestone(
        "First Customer",
        "Acquire the first paying customer",
        today + timedelta(days=120),
    )
    plan.add_milestone(
        "Raise Seed Round",
        "Secure seed funding from investors",
        today + timedelta(days=180),
    )

    # Add team members
    plan.add_team_member("John Doe", "CEO & Founder", ["Leadership", "Product Strategy"])
    plan.add_team_member("Jane Smith", "CTO", ["Python", "Cloud Architecture", "DevOps"])
    plan.add_team_member("Bob Johnson", "Lead Developer", ["JavaScript", "React", "Node.js"])

    return plan


if __name__ == "__main__":
    # Create and display example plan
    plan = create_example_plan()
    print(plan.get_summary())

    # Show next milestone
    next_milestone = plan.get_next_milestone()
    if next_milestone:
        print(f"\nNext Milestone: {next_milestone['title']}")
        print(f"Target Date: {next_milestone['target_date'].strftime('%Y-%m-%d')}")
