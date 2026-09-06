from django.shortcuts import render
from portfolio.models import (
    Profile,
    Skill,
    SkillSection,
    Achievement,
    AchievementSection,
    HeroSection,
    Stat,
    AboutSection,
    NavItem,
    AboutPrinciple,
    Language,
    LanguageSection,
    ProjectSection,
    Project,
    TeachingSection,
    TeachingStat,
    TeachingArea,
    EducationSection,
    EducationPrimary,
    EducationRecord,
    LearningTag,
    FocusSection,
    FocusCard,
    TimelineSection,
    TimelineItem,
    ContactSection,
    FooterSection,
)


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('order')
    achievements = Achievement.objects.all().order_by('order')
    stats = Stat.objects.all().order_by('order')

    skill_section = SkillSection.objects.first()
    achievement_section = AchievementSection.objects.first()
    hero_section = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    nav_items = NavItem.objects.all().order_by('order')
    about_principles = AboutPrinciple.objects.all().order_by('order')
    languages = Language.objects.all().order_by('order')
    language_section = LanguageSection.objects.first()
    projects = Project.objects.all().order_by('order')
    project_section = ProjectSection.objects.first()
    teaching_section = TeachingSection.objects.first()
    teaching_stats = TeachingStat.objects.all().order_by('order')
    teaching_areas = TeachingArea.objects.all().order_by('order')
    education_section = EducationSection.objects.first()
    education_primary = EducationPrimary.objects.first()
    education_records = EducationRecord.objects.all().order_by('order')
    learning_tags = LearningTag.objects.all().order_by('order')
    focus_section = FocusSection.objects.first()
    focus_cards = FocusCard.objects.all().order_by('order')
    timeline_section = TimelineSection.objects.first()
    timeline_items = TimelineItem.objects.all().order_by('order')
    contact_section = ContactSection.objects.first()
    footer_section = FooterSection.objects.first()

    return render(request, "home.html", {
        "profile": profile,
        "skills": skills,
        "achievements": achievements,
        "stats": stats,
        "skill_section": skill_section,
        "achievement_section": achievement_section,
        "hero_section": hero_section,
        "about_section": about_section,
        "nav_items": nav_items,
        "about_principles": about_principles,
        "languages": languages,
        "language_section": language_section,
        "projects": projects,
        "project_section": project_section,
        "teaching_section": teaching_section,
        "teaching_stats": teaching_stats,
        "teaching_areas": teaching_areas,
        "education_section": education_section,
        "education_primary": education_primary,
        "education_records": education_records,
        "learning_tags": learning_tags,
        "focus_section": focus_section,
        "focus_cards": focus_cards,
        "timeline_section": timeline_section,
        "timeline_items": timeline_items,
        "contact_section": contact_section,
        "footer_section": footer_section,
    })
