"""
Example usage of the startup_plan module
Demonstrates how to create and use a custom startup plan
"""

from datetime import datetime, timedelta
from startup_plan import StartupPlan


def main():
    """Create a custom startup plan"""
    
    # Initialize a new startup plan
    print("Creating a new startup plan...\n")
    plan = StartupPlan("MyTechStartup", "Jane Entrepreneur")
    
    # Define vision and mission
    plan.set_vision(
        "To empower small businesses with AI-powered automation tools"
    )
    plan.set_mission(
        "Making enterprise-grade automation accessible and affordable for everyone"
    )
    
    # Set up initial milestones
    today = datetime.now()
    print("Adding milestones...")
    
    plan.add_milestone(
        "Product Research",
        "Complete market research and user interviews",
        today + timedelta(days=30)
    )
    
    plan.add_milestone(
        "Build Prototype",
        "Develop working prototype with core features",
        today + timedelta(days=60)
    )
    
    plan.add_milestone(
        "Beta Launch",
        "Launch beta version to first 100 users",
        today + timedelta(days=90)
    )
    
    plan.add_milestone(
        "Raise Funding",
        "Close pre-seed round of $500K",
        today + timedelta(days=120)
    )
    
    # Build the team
    print("Adding team members...")
    
    plan.add_team_member(
        "Jane Entrepreneur",
        "CEO & Founder",
        ["Product Strategy", "Business Development", "Leadership"]
    )
    
    plan.add_team_member(
        "Alex Chen",
        "CTO",
        ["Python", "Machine Learning", "Cloud Architecture"]
    )
    
    plan.add_team_member(
        "Sarah Martinez",
        "Head of Design",
        ["UI/UX Design", "Figma", "User Research"]
    )
    
    # Display the plan
    print("\n" + "="*60)
    print(plan.get_summary())
    
    # Show next priority
    next_milestone = plan.get_next_milestone()
    if next_milestone:
        print("\n" + "="*60)
        print("NEXT PRIORITY")
        print("="*60)
        print(f"Milestone: {next_milestone['title']}")
        print(f"Description: {next_milestone['description']}")
        print(f"Due Date: {next_milestone['target_date'].strftime('%B %d, %Y')}")
        days_until = (next_milestone['target_date'] - datetime.now()).days
        print(f"Days Remaining: {days_until}")
    
    # Simulate completing first milestone
    print("\n" + "="*60)
    print("Simulating milestone completion...")
    print("="*60)
    
    success = plan.complete_milestone("Product Research")
    if success:
        print("✅ 'Product Research' milestone completed!")
        
        # Show updated next priority
        next_milestone = plan.get_next_milestone()
        if next_milestone:
            print(f"\n📋 Next up: {next_milestone['title']}")
            print(f"   Target: {next_milestone['target_date'].strftime('%B %d, %Y')}")


if __name__ == "__main__":
    main()
