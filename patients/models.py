from django.db import models
from django.utils import timezone
from datetime import date


def get_current_date():
    return timezone.now().date()


class Patient(models.Model):
    patient_id = models.CharField(max_length=50, unique=True)  # Unique ID
    registration_date = models.DateField(default=get_current_date)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"


class Vitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vitals")
    visit_date = models.DateField(default=get_current_date)
    height_cm = models.FloatField()
    weight_kg = models.FloatField()
    bmi = models.FloatField(blank=True, null=True)  # auto-calculated

    def save(self, *args, **kwargs):
        # Auto-calculate BMI before saving
        if self.height_cm > 0:
            height_m = self.height_cm / 100
            self.bmi = self.weight_kg / (height_m ** 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vitals for {self.patient} on {self.visit_date}"


class VisitFormA(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="form_a_visits")
    visit_date = models.DateField(default=get_current_date)
    general_health = models.CharField(
        max_length=10,
        choices=[('Good', 'Good'), ('Poor', 'Poor')],
    )
    ever_been_on_diet = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Form A ({self.general_health}) for {self.patient}"


class VisitFormB(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="form_b_visits")
    visit_date = models.DateField(default=get_current_date)
    general_health = models.CharField(
        max_length=10,
        choices=[('Good', 'Good'), ('Poor', 'Poor')],
    )
    currently_using_drugs = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Form B ({self.general_health}) for {self.patient}"
