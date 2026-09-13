from django.db import migrations


def add_project(apps, schema_editor):
    Project = apps.get_model("main", "Project")

    Project.objects.create(
        title="Suluh Djiwa Membangkitkan Setiap Jiwa❤️‍🩹",
        description=(
            "Project pengabdian masyarakat yang membahas keseimbangan "
            "kehidupan mahasiswa melalui podcast Heart to Heart, fun walk, "
            "dan aktivitas berbagi melalui Lentera Kata."
        ),
        date_completed="2026-06-01",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_project"),
    ]

    operations = [
        migrations.RunPython(add_project),
    ]