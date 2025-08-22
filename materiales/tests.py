from decimal import Decimal

from django.test import TestCase

from .models import Material, RegistroMaterial


class RegistroMaterialModelTest(TestCase):
    def test_crear_registro_material(self):
        material = Material.objects.create(
            nombre="Plástico", descripcion="PET", precio_kg=Decimal("1.50")
        )
        registro = RegistroMaterial.objects.create(
            material=material, cantidad_kg=Decimal("10")
        )

        self.assertEqual(registro.material, material)
        self.assertEqual(registro.cantidad_kg, Decimal("10"))
