from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name


class HeroSection(models.Model):
    label = models.CharField(max_length=100)

    primary_button_text = models.CharField(max_length=100)
    primary_button_link = models.CharField(max_length=200)

    secondary_button_text = models.CharField(max_length=100)
    secondary_button_link = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Stat(models.Model):
    number = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.number} - {self.label}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class SkillSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    focus_label = models.CharField(max_length=100)
    focus_title = models.CharField(max_length=200)
    focus_description = models.TextField()

    def __str__(self):
        return self.label

class Achievement(models.Model):
    year = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class AchievementSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.label


class AboutSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()

    def __str__(self):
        return self.label


class AboutPrinciple(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class NavItem(models.Model):
    label = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.label


class LanguageSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    journey_label = models.CharField(max_length=100)
    journey_text = models.TextField()

    def __str__(self):
        return self.label


class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ProjectSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    levels_label = models.CharField(max_length=100)
    focus_label = models.CharField(max_length=100)
    platform_label = models.CharField(max_length=100)
    technology_label = models.CharField(max_length=100)

    more_label = models.CharField(max_length=100)
    more_description = models.TextField()

    def __str__(self):
        return self.label

class Project(models.Model):
    number = models.CharField(max_length=10)
    project_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    tech_1 = models.CharField(max_length=50, blank=True)
    tech_2 = models.CharField(max_length=50, blank=True)
    tech_3 = models.CharField(max_length=50, blank=True)

    level = models.CharField(max_length=50, blank=True)
    focus = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=100, blank=True)
    technology = models.CharField(max_length=200, blank=True)

    detail_1 = models.TextField(blank=True)
    detail_2 = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class TeachingSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    philosophy_label = models.CharField(max_length=100)
    philosophy_quote = models.TextField()
    philosophy_description = models.TextField()

    def __str__(self):
        return self.label


class TeachingStat(models.Model):
    number = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.label


class TeachingArea(models.Model):
    number = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class EducationSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()
    learning_label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class EducationRecord(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.label


class LearningTag(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class EducationPrimary(models.Model):
    education_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class FocusSection(models.Model):
    label = models.CharField(max_length=100)
    eyebrow = models.CharField(max_length=100)
    title = models.TextField()

    intro_1 = models.TextField()
    intro_2 = models.TextField()

    statement_label = models.CharField(max_length=100)
    statement = models.TextField()

    def __str__(self):
        return self.label


class FocusCard(models.Model):
    number = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# =========================
# TIMELINE
# =========================

class TimelineSection(models.Model):
    label = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    end_label = models.CharField(max_length=100)
    end_text = models.TextField()
    current_label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class TimelineItem(models.Model):
    year = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    is_current = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# =========================
# CONTACT
# =========================

class ContactSection(models.Model):
    label = models.CharField(max_length=100)
    eyebrow = models.CharField(max_length=100)
    title = models.TextField()

    email_label = models.CharField(max_length=100)
    github_label = models.CharField(max_length=100)
    linkedin_label = models.CharField(max_length=100)
    instagram_label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class FooterSection(models.Model):
    tagline = models.TextField()
    copyright_text = models.TextField()
    built_with_text = models.TextField()

    def __str__(self):
        return "Footer"
# Create your models here.
