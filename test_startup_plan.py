"""
Simple tests for the startup_plan module
"""

from datetime import datetime, timedelta
from startup_plan import StartupPlan, create_example_plan


def test_create_startup_plan():
    """Test creating a basic startup plan"""
    plan = StartupPlan("TestCo", "Test Founder")
    assert plan.company_name == "TestCo"
    assert plan.founder == "Test Founder"
    assert len(plan.milestones) == 0
    assert len(plan.team) == 0
    print("✓ test_create_startup_plan passed")


def test_set_vision_mission():
    """Test setting vision and mission"""
    plan = StartupPlan("TestCo", "Test Founder")
    plan.set_vision("Test Vision")
    plan.set_mission("Test Mission")
    assert plan.vision == "Test Vision"
    assert plan.mission == "Test Mission"
    print("✓ test_set_vision_mission passed")


def test_add_milestone():
    """Test adding milestones"""
    plan = StartupPlan("TestCo", "Test Founder")
    target_date = datetime.now() + timedelta(days=30)
    plan.add_milestone("Test Milestone", "Description", target_date)
    assert len(plan.milestones) == 1
    assert plan.milestones[0]['title'] == "Test Milestone"
    assert plan.milestones[0]['completed'] is False
    print("✓ test_add_milestone passed")


def test_complete_milestone():
    """Test completing a milestone"""
    plan = StartupPlan("TestCo", "Test Founder")
    target_date = datetime.now() + timedelta(days=30)
    plan.add_milestone("Test Milestone", "Description", target_date)
    
    result = plan.complete_milestone("Test Milestone")
    assert result is True
    assert plan.milestones[0]['completed'] is True
    assert plan.milestones[0]['completed_date'] is not None
    
    # Try completing non-existent milestone
    result = plan.complete_milestone("Non-existent")
    assert result is False
    print("✓ test_complete_milestone passed")


def test_add_team_member():
    """Test adding team members"""
    plan = StartupPlan("TestCo", "Test Founder")
    plan.add_team_member("John Doe", "Developer", ["Python", "JavaScript"])
    assert len(plan.team) == 1
    assert plan.team[0]['name'] == "John Doe"
    assert plan.team[0]['role'] == "Developer"
    assert "Python" in plan.team[0]['skills']
    print("✓ test_add_team_member passed")


def test_get_summary():
    """Test getting summary"""
    plan = StartupPlan("TestCo", "Test Founder")
    plan.set_vision("Test Vision")
    plan.set_mission("Test Mission")
    summary = plan.get_summary()
    assert "TestCo" in summary
    assert "Test Founder" in summary
    assert "Test Vision" in summary
    assert "Test Mission" in summary
    print("✓ test_get_summary passed")


def test_get_next_milestone():
    """Test getting next milestone"""
    plan = StartupPlan("TestCo", "Test Founder")
    today = datetime.now()
    
    # Add milestones with different dates
    plan.add_milestone("First", "Description", today + timedelta(days=30))
    plan.add_milestone("Second", "Description", today + timedelta(days=15))
    plan.add_milestone("Third", "Description", today + timedelta(days=45))
    
    # Should return the closest one
    next_milestone = plan.get_next_milestone()
    assert next_milestone is not None
    assert next_milestone['title'] == "Second"
    
    # Complete the closest one
    plan.complete_milestone("Second")
    next_milestone = plan.get_next_milestone()
    assert next_milestone['title'] == "First"
    print("✓ test_get_next_milestone passed")


def test_example_plan():
    """Test the example plan creation"""
    plan = create_example_plan()
    assert plan.company_name == "TechVenture"
    assert plan.founder == "John Doe"
    assert len(plan.milestones) > 0
    assert len(plan.team) > 0
    assert plan.vision != ""
    assert plan.mission != ""
    print("✓ test_example_plan passed")


def run_all_tests():
    """Run all tests"""
    print("\nRunning startup_plan tests...\n")
    test_create_startup_plan()
    test_set_vision_mission()
    test_add_milestone()
    test_complete_milestone()
    test_add_team_member()
    test_get_summary()
    test_get_next_milestone()
    test_example_plan()
    print("\n✅ All tests passed!\n")


if __name__ == "__main__":
    run_all_tests()
