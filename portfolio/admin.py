from django.contrib import admin

from .models import (
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
    LanguageSection,
    Language,
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


admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(SkillSection)
admin.site.register(Achievement)
admin.site.register(AchievementSection)
admin.site.register(HeroSection)
admin.site.register(Stat)
admin.site.register(AboutSection)
admin.site.register(NavItem)
admin.site.register(AboutPrinciple)
admin.site.register(LanguageSection)
admin.site.register(Language)
admin.site.register(ProjectSection)
admin.site.register(Project)
admin.site.register(TeachingSection)
admin.site.register(TeachingStat)
admin.site.register(TeachingArea)
admin.site.register(EducationSection)
admin.site.register(EducationPrimary)
admin.site.register(EducationRecord)
admin.site.register(LearningTag)
admin.site.register(FocusSection)
admin.site.register(FocusCard)
admin.site.register(TimelineSection)
admin.site.register(TimelineItem)
admin.site.register(ContactSection)
admin.site.register(FooterSection)


# Register your models here.
